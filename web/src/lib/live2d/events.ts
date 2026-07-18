import { localizeCharFromDevName } from "./character";
import { getBGMByDevName } from "./bgm";
import { ADDRESSABLES_CATALOG_URL_ROOT } from "../urls";

export interface ModelOption {
  value: string;
  label: string;
  devName: string;
  model: string;
}

export const getLocalName = (s: string): [string, string] => {
  const devName = s.replace("_home", "");
  let dev = devName;
  let k = localizeCharFromDevName(devName);
  if (devName === k) {
    k = localizeCharFromDevName(`${devName}_default`);
    dev = `${devName}_default`;
    if (k === `${devName}_default`) {
      k = localizeCharFromDevName(`${devName.substring(0, devName.length - 1)}_default`);
      dev = `${devName.substring(0, devName.length - 1)}_default`;
      if (k === `${devName.substring(0, devName.length - 1)}_default`) {
        k = s;
        dev = s;
      }
    }
  }
  return [k, dev];
};

export const buildModelOptions = (
  models: Record<string, string[]>,
  sort: boolean = true,
): ModelOption[] => {
  let entries = Object.entries(models);
  if (sort) {
    entries.sort((a, b) => {
      const [aLocal] = getLocalName(a[0]);
      const [bLocal] = getLocalName(b[0]);
      return aLocal.localeCompare(bLocal);
    });
  }
  return entries.map(([model, files]) => {
    const [localName, devName] = getLocalName(model);
    return {
      value: JSON.stringify(files),
      label: `${localName} (${model})`,
      devName,
      model,
    };
  });
};

export const getModelBGMUrl = (devName: string): string | null => {
  const bgmId = getBGMByDevName(devName);
  if (bgmId === -1) return null;
  const bgmIdStr = bgmId.toString().padStart(2, "0");
  return `${ADDRESSABLES_CATALOG_URL_ROOT}/MediaResources/GameData/Audio/BGM/Theme_${bgmIdStr}.ogg`;
};

export const downloadAsWallpaperEngine = (model: string) => {
  const url = `/model/${model}.zip`;
  const a = document.createElement("a");
  a.href = url;
  a.target = "_blank";
  a.download = `ba_wpengine@${model}.zip`;
  a.click();
};
