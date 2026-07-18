import { CharacterDialog } from "../table";
import { findCharIdFromDevName } from "./character";

interface GetSubtitleOptions {
  charId?: number;
  devName?: string;
}

export const getSubtitles = (animationName: string, opt: GetSubtitleOptions): string[] => {
  if (!opt.charId && !opt.devName) return [];
  const id = opt.charId || findCharIdFromDevName(opt.devName!);
  if (id === -1) return [];
  const dialogs = CharacterDialog.data.filter(
    (x) => x.CharacterId === id && x.DialogCategory === "UILobbySpecial"
  );
  if (dialogs.length === 0) return [];
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
      subtitles.push(
        dialog.LocalizeEN !== "" && dialog.LocalizeEN !== undefined
          ? dialog.LocalizeEN
          : dialog.LocalizeJP
      );
    }
  }
  if (subtitles.length === 0 && animationName.includes("Talk_")) {
    const groupId = parseInt(
      animationName.replace("Talk_", "").replace("Dev_Talk_", "").split("_")[0]
    );
    for (let i = 0; i < dialogs.length; i++) {
      const dialog = dialogs[i];
      if (dialog.GroupId === groupId && dialog.DialogType === "Talk") {
        subtitles.push(
          dialog.LocalizeEN !== "" && dialog.LocalizeEN !== undefined
            ? dialog.LocalizeEN
            : dialog.LocalizeJP
        );
      }
    }
  }
  return subtitles;
};
