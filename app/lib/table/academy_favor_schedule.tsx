import { Region } from "./types";

interface AcademyFavorSchedule {
  Id: number;
  CharacterId: number;
  ScenarioSriptGroupId: number;
  RewardParcelType: string[];
}

export const data: AcademyFavorSchedule[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = window.location.origin;
  const aca = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/AcademyFavorScheduleExcelTable.json`).then((res) => res.json()) as AcademyFavorSchedule[];
  data.push(...aca);
};
