import { runOnClient } from "./util";

interface AcademyFavorSchedule {
  Id: number;
  CharacterId: number;
  ScenarioSriptGroupId: number;
  RewardParcelType: string[];
}

export const data: AcademyFavorSchedule[] = [];

const initialize = async () => {
  const baseUrl = window.location.origin;
  const aca = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/AcademyFavorScheduleExcelTable.json`).then((res) => res.json()) as AcademyFavorSchedule[];
  data.push(...aca);
};

runOnClient(initialize);
