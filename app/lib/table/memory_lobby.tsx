import { Region } from "./types";
import { get_origin } from "@/app/lib/get_origin";

interface MemoryLobby {
  CharacterId: number;
  BGMId: number;
}

export const data: MemoryLobby[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = get_origin();
  const memoryLobby = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/MemoryLobbyExcelTable.json`).then((res) => res.json()) as MemoryLobby[];
  data.push(...memoryLobby);
};
