import fs from "fs";
import path from "path";

interface FileData {
  name: string;
  path: string;
  bytes: number;
  buffer: Buffer;
}

const resolvePath = (buf: Buffer) => {
  const html = buf.toString("utf-8");
  // Replaces "/_next..." with "./_next..."
  const r = html.replace(/\/_next/g, "./_next");
  return Buffer.from(r);
};

const fixDefaultModel = (buf: Buffer, characterId: string) => {
  // Dumb solution to replace default model.
  // selectedModel:"airi0_home" => selectedModel:{characterId}
  const script = buf.toString("utf-8");
  const r = script.replace(`selectedModel:"airi0_home"`, `selectedModel:"${characterId}"`);
  return Buffer.from(r);
};

/**
 * Get the data files for a character.
 * @param characterId - The character ID.
 * @returns The data files.
 * @example
 * const files = getDataFiles("airi_home");
 */
export const getDataFiles = (characterId: string): FileData[] => {
  const dataDir = path.join("data", "jp", "Android", characterId);
  const baseDir = path.join("public", dataDir);
  const dir = path.join(process.cwd(), baseDir);

  // Check if the directory exists
  if (!fs.existsSync(dir)) {
    return [];
  }

  const files = fs.readdirSync(dir).filter((file) => {
    return fs.lstatSync(path.join(dir, file)).isFile();
  });

  // Return
  const r = files.map((file) => {
    const stats = fs.statSync(path.join(dir, file));
    const buf = fs.readFileSync(path.join(dir, file));
    const name = path.basename(file);

    return {
      name,
      path: path.join(dataDir, file),
      bytes: stats.size,
      buffer: buf,
    };
  });

  // Add `info.json` to the files
  const infoPath = path.join("public", "data", "jp", "Android", "info.json");
  const infoBuf = fs.readFileSync(path.join(process.cwd(), infoPath));
  r.push({
    name: "info.json",
    path: "data/jp/Android/info.json",
    bytes: infoBuf.length,
    buffer: infoBuf,
  });

  return r;
};

/**
 * Get the table files for a character.
 */
export const getTableFiles = (): FileData[] => {
  const enDir = path.join("data", "en", "Preload", "TableBundles", "Excel");
  const jpDir = path.join("data", "jp", "TableBundles", "Excel");

  const dirs = [enDir, jpDir];
  const r: FileData[] = [];

  for (const dir of dirs) {
    const baseDir = path.join("public", dir);
    const dirPath = path.join(process.cwd(), baseDir);

    // Check if the directory exists
    if (!fs.existsSync(dirPath)) {
      continue;
    }

    const files = fs.readdirSync(dirPath).filter((file) => {
      return fs.lstatSync(path.join(dirPath, file)).isFile();
    });

    // Return
    const filesData: FileData[] = files.map((file) => {
      const stats = fs.statSync(path.join(dirPath, file));
      const buf = fs.readFileSync(path.join(dirPath, file));
      const name = path.basename(file);
      return {
        name,
        path: path.join(dir, file),
        bytes: stats.size,
        buffer: buf,
      };
    });

    r.push(...filesData);
  }

  return r;
};

/**
 * Get the static web files required for wallpaper engine.
 * @returns The web files.
 */
export const getWebFiles = (characterId: string): FileData[] => {
  const baseDir = path.join("wallpaper_engine");
  const dir = path.join(process.cwd(), "public", baseDir);

  //   Check if the directory exists
  if (!fs.existsSync(dir)) {
    return [];
  }

  const files = fs.readdirSync(dir, { recursive: true }).filter((file) => {
    // Skip directories
    if (typeof file !== "string") {
      return false;
    }
    return fs.lstatSync(path.join(dir, file)).isFile();
  });

  //   Return
  const r: FileData[] = files.map((file) => {
    if (typeof file !== "string") {
      return {
        name: "",
        path: "",
        bytes: 0,
        buffer: Buffer.from(""),
      };
    }
    const stats = fs.statSync(path.join(dir, file));
    let buf = fs.readFileSync(path.join(dir, file));
    const name = path.basename(file);

    // Check if the file is an HTML or js file
    if (name.endsWith(".html") || name.endsWith(".js")) {
      buf = resolvePath(buf);

      // Dummy solution to replace default model.
      if (name.endsWith(".js")) {
        buf = fixDefaultModel(buf, characterId);
      }
    }

    return {
      name,
      path: file,
      bytes: stats.size,
      buffer: buf,
    };
  }).filter((file) => {
    return file.name !== "";
  });

  return r;
};
