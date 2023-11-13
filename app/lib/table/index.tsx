import { runOnClient } from "./util";
import * as AcademyFavorSchedule from "./academy_favor_schedule";
import * as CharacterDialog from "./character_dialog";
import * as Character from "./character";
import * as LocalizeCharProfile from "./localize_char_profile";
import * as MemoryLobby from "./memory_lobby";
import { Region } from "./types";

const imports = [
  AcademyFavorSchedule,
  CharacterDialog,
  Character,
  LocalizeCharProfile,
  MemoryLobby,
];

export const initialize = async (region: Region) => {
  let subdir = "";
  switch (region) {
    case "jp":
      subdir = `${region}`;
      break;
    case "en":
      subdir = `${region}/Preload`;
      break;
  }
  await new Promise((resolve) => {
    runOnClient(async () => {
      for (const i of imports) {
        if (i.data.length === 0) {
          await i.initialize(subdir);
        }
      }
      resolve(1);
    });
  });
};

export { AcademyFavorSchedule, Character, CharacterDialog, LocalizeCharProfile, MemoryLobby };
