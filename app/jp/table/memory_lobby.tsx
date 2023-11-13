interface MemoryLobby {
  CharacterId: number;
  BGMId: number;
}

export const data: MemoryLobby[] = [];

export const initialize = async () => {
  const baseUrl = window.location.origin;
  const memoryLobby = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/MemoryLobbyExcelTable.json`).then((res) => res.json()) as MemoryLobby[];
  data.push(...memoryLobby);
};
