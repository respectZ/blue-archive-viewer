// "use server";

// import fs from "fs";
// import path from "path";

// export async function getModels(file: string): Promise<Record<string, string[]>> {
//   // TODO: use static instead with .json file
//   const rootDir = path.join(process.cwd(), "public", "data", "jp", "Android");
//   console.log(path.resolve(rootDir));
//   const models = fs.readdirSync(rootDir, { withFileTypes: true })
//     .filter((dirent) => dirent.isDirectory())
//     .map((dirent) => {
//       // Loop through each directory
//       const modelDir = path.join(rootDir, dirent.name);
//       const modelDirBase = dirent.name;
//       // List all files in modelDir
//       const files = fs.readdirSync(modelDir, { withFileTypes: true })
//         .filter((dirent) => dirent.name.endsWith(".skel"))
//         .map((dirent) => path.join("\\", "data", "jp", "Android", modelDirBase, dirent.name));
//       return [dirent.name, files];
//     }).reduce((obj, item) => {
//       const k = item[0] as string;
//       const v = item[1] as string[];
//       obj[k] = v;
//       return obj;
//     }, {} as Record<string, string[]>);
//   return models;
// }

export async function fetchModels(file: string): Promise<Record<string, string[]>> {
  const models = await fetch(file).then((res) => res.json()) as Record<string, string[]>;
  // Remap key to actual model name
  const remapped = Object.keys(models).reduce((obj, item) => {
    // const devName = item.split("_")[0];
    // let k = localizeCharFromDevName(devName);
    // if (devName === k) {
    //   k = localizeCharFromDevName(`${devName}_default`);
    //   // Still not found
    //   if (k === `${devName}_default`) {
    //     k = localizeCharFromDevName(`${devName.substring(0, devName.length - 1)}_default`);
    //     // Still not found
    //     if (k === `${devName.substring(0, devName.length - 1)}_default`) {
    //       k = item;
    //     }
    //   }
    // }
    const k = item;
    const v = models[item];
    obj[k] = v;
    return obj;
  }, {} as Record<string, string[]>);
  return remapped;
}
