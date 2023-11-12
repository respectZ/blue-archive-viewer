import { runOnClient } from "./util";

interface ScenarioScriptFavor {
  GroupId: number;
  BGMId: number;
  BGName: number;
  TextJp: string;
}

export const data: ScenarioScriptFavor[] = [];

const initialize = async () => {
  const baseUrl = window.location.origin;
  let i = 1;
  while (true) {
    const res = await fetch(`${baseUrl}/data/jp/TableBundles/Excel/ScenarioScriptFavor${i}ExcelTable.json`);
    // Check if success
    if (res.status !== 200) {
      break;
    }
    const sc = await res.json() as ScenarioScriptFavor[];
    data.push(...sc);
    i++;
  }
};

runOnClient(initialize);
