import { runOnClient } from "./util";

interface Character {
  Id: number;
  DevName: string;
  ScenarioCharacter: string;
  IsPlayable: boolean;
}

export const data: Character[] = [];

const initialize = async () => {
  const baseUrl = window.location.origin;
  const characters = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/CharacterExcelTable.json`).then((res) => res.json()) as Character[];
  data.push(...characters);
};

runOnClient(async () => await initialize());
