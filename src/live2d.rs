use super::api::jp::AddressableCatalog;
use crate::{
    error, info,
    util::{
        save_file, save_image, save_json,
        unityfs::{self, decode_astc_rgb, decode_astc_rgb_5x5},
    },
};
use anyhow::{Ok, Result};
use astc_decode::Footprint;
use num_enum::FromPrimitive;
use regex::Regex;
use std::{collections::BTreeMap, path::PathBuf};
use unity_rs::{
    classes::{TextAsset, Texture2D},
    Env,
};
use walkdir::WalkDir;

#[allow(non_camel_case_types, non_upper_case_globals)]
#[derive(Debug, Eq, PartialEq, FromPrimitive, Clone, Copy)]
#[repr(i32)]
enum TextureFormat {
    #[num_enum(default)]
    UnknownType = -1,
    ASTC_RGB_4x4 = 48,
    ASTC_RGB_5x5,
    ASTC_RGB_6x6,
    ASTC_RGB_8x8,
    ASTC_RGB_10x10,
    ASTC_RGB_12x12,
}

pub async fn run_jp(catalog: AddressableCatalog) -> Result<()> {
    // assets-_mx-spinelobbies-(.*?)-_
    let regex = Regex::new(r"assets-_mx-spinelobbies-(.*?)-_")?;
    let out_dir = PathBuf::from("./public/data/jp");
    info!("Requesting BundleCatalog");
    let bundle_catalog = catalog.get_bundle_catalog().await?;
    info!("Saving BundleCatalog");
    bundle_catalog.save(out_dir.clone()).await?;
    info!("Downloading Live2D bundles");
    let downloaded = bundle_catalog
        .save_bundle(PathBuf::from("./temp/jp/"), |bundle| {
            let char_id = match regex.captures(&bundle.name) {
                Some(captures) => {
                    // skip if it's "_mxcommon"
                    if captures[1].to_string() == "_mxcommon" {
                        return false;
                    }
                    captures[1].to_string()
                }
                None => return false,
            };
            // Check if folder exists
            let folder = out_dir.clone().join("Android").join(char_id);
            !folder.exists()
        })
        .await?;

    let mut handles = vec![];

    downloaded.iter().for_each(|filename| {
        info!("Extracting {}", filename);
        let char_id = regex.captures(filename).unwrap()[1].to_string();
        let env = unityfs::read_file(PathBuf::from("./temp/jp/Android").join(filename)).unwrap();
        handles.push(tokio::spawn(extract_live2d(char_id, env)));
    });

    for handle in handles {
        handle.await?.unwrap();
    }
    validate_atlas().await?;
    info!("Updating info.json");
    update_info().await?;
    Ok(())
}

async fn extract_live2d(char_id: String, env: Env) -> Result<()> {
    for obj in env.objects() {
        match obj.class() {
            unity_rs::ClassID::Texture2D => {
                let s: Texture2D = obj.read().unwrap();
                let format = TextureFormat::from(s.format as i32);
                let footprint = match format {
                    TextureFormat::ASTC_RGB_4x4 => Footprint::ASTC_4X4,
                    TextureFormat::ASTC_RGB_5x5 => Footprint::ASTC_5X5,
                    TextureFormat::ASTC_RGB_6x6 => Footprint::ASTC_6X6,
                    TextureFormat::ASTC_RGB_8x8 => Footprint::ASTC_8X8,
                    TextureFormat::ASTC_RGB_10x10 => Footprint::ASTC_10X10,
                    TextureFormat::ASTC_RGB_12x12 => Footprint::ASTC_12X12,
                    _ => {
                        error!("Unimplemented format: {:?}", s.format);
                        continue;
                    }
                };
                let image = decode_astc_rgb(&s.data, s.width as u32, s.height as u32, footprint)?;
                save_image(
                    PathBuf::from(format!(
                        "./public/data/jp/Android/{}/{}.png",
                        char_id, s.name
                    )),
                    image,
                )
                .await
                .unwrap();
            }
            unity_rs::ClassID::TextAsset => {
                let s: TextAsset = obj.read().unwrap();
                save_file(
                    PathBuf::from(format!("./public/data/jp/Android/{}/{}", char_id, s.name)),
                    &s.script,
                )
                .await
                .unwrap();
            }
            _ => {}
        }
    }
    Ok(())
}

async fn update_info() -> Result<()> {
    let dir = PathBuf::from("./public/data/jp/Android");
    let mut data: BTreeMap<String, Vec<String>> = BTreeMap::new();
    for entry in WalkDir::new(dir) {
        let entry = entry.unwrap();
        let filepath = entry.path();
        if filepath.is_dir() {
            continue;
        }
        if !filepath.to_str().unwrap().ends_with(".skel") {
            continue;
        }
        // Char id is the folder name
        let char_id = filepath
            .parent()
            .unwrap()
            .file_name()
            .unwrap()
            .to_str()
            .unwrap();
        // Push to data
        if !data.contains_key(char_id) {
            data.insert(char_id.to_string(), vec![]);
        }
        // push the path
        // Remove "./public/" from the filepath
        data.get_mut(char_id).unwrap().push(
            filepath
                .to_str()
                .unwrap()
                .replace("./public/", "")
                .replace("\\", "/"),
        );
    }
    save_json(PathBuf::from("./public/data/jp/Android/info.json"), &data).await?;
    Ok(())
}

async fn validate_atlas() -> Result<()> {
    error!("TODO: Implement validate_atlas");
    Ok(())
}
