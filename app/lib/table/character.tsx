import { Region } from "./types";
import { get_origin } from "@/app/lib/get_origin";

interface Character {
  Id: number;
  DevName: string;
  ScenarioCharacter: string;
  IsPlayable?: boolean;
  IsPlayableCharacter?: boolean;
}

export const data: Character[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = get_origin();
  const characters = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/CharacterExcelTable.json`).then((res) => res.json()) as Character[];
  data.push(...characters);
};
