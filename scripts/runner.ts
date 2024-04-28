import { getDataFiles, getTableFiles, getWebFiles } from "./runner/data";
import { createProject, PropertyCombo } from "./runner/project";
import AdmZip from "adm-zip";
import fs from "fs";
import path from "path";

const createModelArchive = (characterId: string) => {
  // Get required assets with the character ID
  const assets = getDataFiles(characterId);
  if (assets.length === 0) {
    return;
  }

  // Get required webfiles for wallpaper engine
  const webFiles = getWebFiles(characterId);

  // Get required table files for subtitle, etc.
  const tableFiles = getTableFiles();

  // Create project.json for wallpaper engine
  const project = createProject();
  project.title = `Blue Archive Live2D | ${characterId}`;
  const model = project.general.properties.model as PropertyCombo;
  model.value = characterId;
  model.options = [
    {
      label: characterId,
      value: characterId,
    },
  ];

  // Create a zip file
  const zip = new AdmZip();
  assets.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  webFiles.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  tableFiles.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  const projectBuffer = Buffer.from(JSON.stringify(project, null, 2));
  zip.addFile("project.json", projectBuffer);

  const buffer = zip.toBuffer();
  return buffer;
};

const formatNumber = (num: number, total: number) => {
  const numStr = num.toString();
  const totalStr = total.toString();
  return `\x1b[96m[${numStr.padStart(totalStr.length, "0")}/${totalStr}]\x1b[0m`;
};

const formatCharacter = (character: string) => {
  return `\x1b[93m${character}\x1b[0m`;
};

const main = () => {
  const characters = fs.readdirSync(path.join(process.cwd(), "public", "data", "jp", "Android"))
    .filter((file) => {
      return fs.lstatSync(path.join(process.cwd(), "public", "data", "jp", "Android", file)).isDirectory();
    });

  // Create the directory if it doesn't exist
  if (!fs.existsSync(path.join(process.cwd(), "public", "model"))) {
    fs.mkdirSync(path.join(process.cwd(), "public", "model"));
  }

  let index = 1;
  for (const character of characters) {
    // Check if already exist
    const filePath = path.join(process.cwd(), "public", "model", `${character}.zip`);
    if (fs.existsSync(filePath)) {
      console.log(formatNumber(index, characters.length), `Skipping`, formatCharacter(character));
      index++;
      continue;
    }

    console.log(formatNumber(index, characters.length), `Creating`, formatCharacter(character));
    const buffer = createModelArchive(character);
    if (!buffer) {
      console.log(`Failed to create model archive for ${character}`);
      index++;
      continue;
    }

    // Write the buffer to a file
    fs.writeFileSync(filePath, buffer);
    index++;
  }
};

main();
