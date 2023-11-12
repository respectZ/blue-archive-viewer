import * as CharacterDialog from "../table/character_dialog";
import { findCharIdFromDevName } from "./character";

interface getSubtitleOptions {
  charId?: number;
  devName?: string;
}

export const getSubtitles = (animationName: string, opt: getSubtitleOptions): string[] => {
  if (!opt.charId && !opt.devName) {
    return [];
  }

  // Find character id from devName
  const id = opt.charId || findCharIdFromDevName(opt.devName!);
  if (id === -1) return [];

  // Find CharacterDialog that matches the character id, and DialogCategory is "UILobbySpecial"
  const dialogs = CharacterDialog.data.filter((x) => x.CharacterId === id && x.DialogCategory === "UILobbySpecial");
  if (dialogs.length === 0) return [];

  // Group them by AnimationName
  // Let's say we have AnimationName "Talk_03_M"
  // We group them until AnimationName changes, and AnimationName != "".
  const subtitles: string[] = [];
  let flag = false;
  for (let i = 0; i < dialogs.length; i++) {
    const dialog = dialogs[i];
    if (dialog.AnimationName === animationName) {
      flag = true;
    } else if (dialog.AnimationName !== animationName && dialog.AnimationName !== "" && flag) {
      break;
    }
    if (flag) {
      subtitles.push(dialog.LocalizeJP);
    }
  }
  return subtitles;
};
