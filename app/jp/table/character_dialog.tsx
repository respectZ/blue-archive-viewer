import { runOnClient } from "./util";

interface CharacterDialog {
  CharacterId: number;
  GroupId: number;
  DialogCategory: string;
  DialogType: string;
  ActionName: string;
  AnimationName: string;
  LocalizeJP: string;
}

export const data: CharacterDialog[] = [];

const initialize = async () => {
  const baseUrl = window.location.origin;
  const characters = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/CharacterDialogExcelTable.json`).then((res) => res.json()) as CharacterDialog[];
  data.push(...characters);
};

runOnClient(initialize);
