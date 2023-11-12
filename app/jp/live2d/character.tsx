import * as Character from "../table/character";
import * as LocalizeCharProfile from "../table/localize_char_profile";

/**
 * Localize character name from DevName to FullNameJp.
 * @param s - DevName
 * @returns FullNameJp
 * @example
 * localizeCharFromDevName("azusa_default") // => "白洲アズサ"
 */
export function localizeCharFromDevName(s: string): string {
  const id = findCharIdFromDevName(s);
  if (id !== -1) {
    return LocalizeCharProfile.data.find((v) => v.CharacterId === id)?.FullNameJp || s;
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
  const id = Character.data.find((v) => (v.DevName.toLowerCase() === s.toLowerCase() || v.ScenarioCharacter.toLowerCase() === s.toLowerCase()) && v.IsPlayable)?.Id;
  if (id) {
    return id;
  }
  return -1;
}
