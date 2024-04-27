import { Region } from "./types";
import { get_origin } from "@/app/lib/get_origin";

interface CharacterDialog {
  CharacterId: number;
  GroupId: number;
  DialogCategory: string;
  DialogType: string;
  ActionName: string;
  AnimationName: string;
  LocalizeJP: string;
  LocalizeEN?: string;
}

export const data: CharacterDialog[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = get_origin();
  const characters = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/CharacterDialogExcelTable.json`).then((res) => res.json()) as CharacterDialog[];
  data.push(...characters);
};
