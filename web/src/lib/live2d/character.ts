import { Character, LocalizeCharProfile } from "../table";

export function localizeCharFromDevName(s: string): string {
  const id = findCharIdFromDevName(s);
  if (id !== -1) {
    const profile = LocalizeCharProfile.data.find((v) => v.CharacterId === id);
    if (!profile) return s;
    if (profile.FamilyNameEn === "" || profile.FamilyNameEn === undefined) return profile.FullNameJp;
    return `${profile.FamilyNameEn} ${profile.PersonalNameEn}`;
  }
  return s;
}

export function findCharIdFromDevName(s: string): number {
  const lower = s.toLowerCase();
  let id = Character.data.find(
    (v) =>
      (v.DevName.toLowerCase() === lower || v.ScenarioCharacter.toLowerCase() === lower) &&
      (v.IsPlayable || v.IsPlayableCharacter)
  )?.Id;
  if (id) return id;
  for (let i = 10; i >= 1; i--) {
    const suffix = `_${i.toString().padStart(2, "0")}`;
    id = Character.data.find(
      (v) =>
        (v.DevName.toLowerCase() === `${lower}${suffix}` || v.ScenarioCharacter.toLowerCase() === `${lower}${suffix}`) &&
        (v.IsPlayable || v.IsPlayableCharacter)
    )?.Id;
    if (id) return id;
  }
  return -1;
}
