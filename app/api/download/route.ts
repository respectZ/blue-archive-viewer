import { NextRequest, NextResponse } from "next/server";
import { getDataFiles, getTableFiles, getWebFiles } from "./data";
import AdmZip from "adm-zip";
import { createProject, PropertyCombo } from "./project";

export async function GET(req: NextRequest) {
  const characterId = req.nextUrl.searchParams.get("id");
  if (!characterId) {
    return new NextResponse("Missing character ID", { status: 400 });
  }

  // Get required assets with the character ID
  const assets = getDataFiles(characterId);
  if (assets.length === 0) {
    return new NextResponse(`${characterId} not found`, { status: 404 });
  }

  // Get required webfiles for wallpaper engine
  const webFiles = getWebFiles(characterId);

  // Get required table files for subtitle, etc.
  const tableFiles = getTableFiles();

  // Create project.json for wallpaper engine
  const project = createProject();
  project.title = `Blue Archive Live2D | ${characterId}`;
  const model = project.general.properties.model as PropertyCombo;
  model.value = characterId;
  model.options = [
    {
      label: characterId,
      value: characterId,
    },
  ];

  // Create a zip file
  const zip = new AdmZip();
  assets.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  webFiles.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  tableFiles.forEach((asset) => {
    zip.addFile(asset.path, asset.buffer);
  });
  const projectBuffer = Buffer.from(JSON.stringify(project, null, 2));
  zip.addFile("project.json", projectBuffer);

  const buffer = zip.toBuffer();

  // Return the zip file
  const res = new NextResponse(buffer);
  res.headers.set("Content-Type", "application/zip");
  res.headers.set("Content-Disposition", `attachment; filename=ba_wpengine@${characterId}.zip`);

  return res;
}
