import { CharacterDialog } from "./table";
import { findCharIdFromDevName } from "@/app/jp/live2d/character";

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
      if (dialog.LocalizeEN !== "" && dialog.LocalizeEN !== undefined) {
        subtitles.push(dialog.LocalizeEN);
      } else {
        subtitles.push(dialog.LocalizeJP);
      }
    }
  }
  // Another workaround, check by groupid, dialogtype = Talk, DialogCategory === UILobbySpecial
  if (subtitles.length === 0 && animationName.includes("Talk_")) {
    const groupId = parseInt(animationName.replace("Talk_", "").replace("Dev_Talk_", "").split("_")[0]);
    for (let i = 0; i < dialogs.length; i++) {
      const dialog = dialogs[i];
      if (dialog.GroupId === groupId && dialog.DialogType === "Talk") {
        if (dialog.LocalizeEN !== "" && dialog.LocalizeEN !== undefined) {
          subtitles.push(dialog.LocalizeEN);
        } else {
          subtitles.push(dialog.LocalizeJP);
        }
      }
    }
  }
  return subtitles;
};
