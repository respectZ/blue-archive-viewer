import { runOnClient } from "@/app/lib/table/util";
import * as AcademyFavorSchedule from "@/app/lib/table/academy_favor_schedule";
import * as CharacterDialog from "@/app/lib/table/character_dialog";
import * as Character from "@/app/lib/table/character";
import * as LocalizeCharProfile from "@/app/lib/table/localize_char_profile";
import * as MemoryLobby from "@/app/lib/table/memory_lobby";
import { Region } from "@/app/lib/table/types";

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
        // Clear i.data
        i.data.length = 0;
        await i.initialize(subdir);
      }
      resolve(1);
    });
  });
};

export { AcademyFavorSchedule, Character, CharacterDialog, LocalizeCharProfile, MemoryLobby };
