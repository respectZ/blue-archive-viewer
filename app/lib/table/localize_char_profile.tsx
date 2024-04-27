import { Region } from "./types";
import { get_origin } from "@/app/lib/get_origin";

interface LocalizeCharProfile {
  CharacterId: number;
  FullNameJp: string;
  PersonalNameEn?: string;
  FamilyNameEn?: string;
}

export const data: LocalizeCharProfile[] = [];

export const initialize = async (subdir: string) => {
  const baseUrl = get_origin();
  const chars = await fetch(`${baseUrl}/data/${subdir}/TableBundles/Excel/LocalizeCharProfileExcelTable.json`).then((res) => res.json()) as LocalizeCharProfile[];
  data.push(...chars);
};
