import { Character, LocalizeCharProfile } from "@/app/lib/table";

/**
 * Localize character name from DevName to EN (FamilyNameEn + PersonalNameEn) if available, otherwise FullNameJp.
 * @param s - DevName
 * @returns Localized character name
 * @example
 * localizeCharFromDevName("azusa_default") // => "Shirasu Azusa" | "白洲アズサ"
 */
export function localizeCharFromDevName(s: string): string {
  const id = findCharIdFromDevName(s);
  if (id !== -1) {
    const profile = LocalizeCharProfile.data.find((v) => v.CharacterId === id);
    if (!profile) return s;
    if (profile.FamilyNameEn === "" || profile.FamilyNameEn === undefined) return profile.FullNameJp;
    return `${[profile.FamilyNameEn, profile.PersonalNameEn].join(" ")}`;
  }
  return s;
}

/**
 * Find character id from DevName.
 * @param s - DevName
 * @returns CharacterId
 * @example
 * findCharIdFromDevName("azusa_default") // => 10019
 */
export function findCharIdFromDevName(s: string): number {
  const id = Character.data.find((v) => (v.DevName.toLowerCase() === s.toLowerCase() || v.ScenarioCharacter.toLowerCase() === s.toLowerCase()) && (v.IsPlayable || v.IsPlayableCharacter))?.Id;
  if (id) {
    return id;
  }
  return -1;
}
