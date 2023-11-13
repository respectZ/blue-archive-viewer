export async function fetchModels(file: string): Promise<Record<string, string[]>> {
  const models = await fetch(file).then((res) => res.json()) as Record<string, string[]>;
  // Remap key to actual model name
  const remapped = Object.keys(models).reduce((obj, item) => {
    const k = item;
    const v = models[item];
    obj[k] = v;
    return obj;
  }, {} as Record<string, string[]>);
  return remapped;
}
