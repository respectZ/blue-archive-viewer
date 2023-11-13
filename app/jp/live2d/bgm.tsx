import { MemoryLobby } from "@/app/lib/table";
import { findCharIdFromDevName } from "./character";

export const getBGM = (charId: number): number => {
  const bgm = MemoryLobby.data.find((v) => v.CharacterId === charId);
  if (bgm) {
    return bgm.BGMId;
  }
  return -1;
};

export const getBGMByDevName = (devName: string): number => {
  const id = findCharIdFromDevName(devName);
  if (id !== -1) {
    return getBGM(id);
  }
  return -1;
};
