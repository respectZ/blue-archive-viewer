import { Region } from "./types";
import { get_origin } from "@/app/lib/get_origin";

interface AcademyFavorSchedule {
  Id: number;
  CharacterId: number;
  ScenarioSriptGroupId: number;
  RewardParcelType: string[];
}

export const data: AcademyFavorSchedule[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = get_origin();
  const aca = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/AcademyFavorScheduleExcelTable.json`).then((res) => res.json()) as AcademyFavorSchedule[];
  data.push(...aca);
};
