export async function fetchModels(file: string): Promise<Record<string, string[]>> {
  const models = await fetch(file).then((res) => res.json()) as Record<string, string[]>;
  return models;
}
