import { MemoryLobby } from "../table";
import { findCharIdFromDevName } from "./character";

export const getBGM = (charId: number): number => {
  const bgm = MemoryLobby.data.find((v) => v.CharacterId === charId);
  return bgm ? bgm.BGMId : -1;
};

export const getBGMByDevName = (devName: string): number => {
  const id = findCharIdFromDevName(devName);
  return id !== -1 ? getBGM(id) : -1;
};
