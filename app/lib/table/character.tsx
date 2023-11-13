import { Region } from "./types";

interface Character {
  Id: number;
  DevName: string;
  ScenarioCharacter: string;
  IsPlayable?: boolean;
  IsPlayableCharacter?: boolean;
}

export const data: Character[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = window.location.origin;
  const characters = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/CharacterExcelTable.json`).then((res) => res.json()) as Character[];
  data.push(...characters);
};
