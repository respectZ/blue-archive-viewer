import { runOnClient } from "./util";

interface LocalizeCharProfile {
  CharacterId: number;
  FullNameJp: string;
}

export const data: LocalizeCharProfile[] = [];

const initialize = async () => {
  const baseUrl = window.location.origin;
  const chars = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/LocalizeCharProfileExcelTable.json`).then((res) => res.json()) as LocalizeCharProfile[];
  data.push(...chars);
};

runOnClient(async () => await initialize());
