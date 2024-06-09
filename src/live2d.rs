use super::api::jp::AddressableCatalog;
use crate::{
    api::en::catalog::Catalog,
    error, info,
    util::{
        get_image_dimensions, save_json,
        unityfs::{self, extract_images, extract_live2d},
    },
};
use anyhow::{Ok, Result};
use regex::Regex;
use std::{collections::BTreeMap, path::PathBuf};
use unity_rs::Env;
use walkdir::WalkDir;

pub async fn run_jp(catalog: &AddressableCatalog) -> Result<()> {
    // assets-_mx-spinelobbies-(.*?)-_
    let regex = Regex::new(r"assets-_mx-spinelobbies-(.*?)-_")?;
    let out_dir = PathBuf::from("./public/data/jp");
    info!("Requesting BundleCatalog");
    let bundle_catalog = catalog.get_bundle_catalog().await?;
    info!("Saving BundleCatalog");
    bundle_catalog.save(out_dir.clone()).await?;
    info!("Downloading Live2D bundles");
    let downloaded = bundle_catalog
        .save_bundle("./temp/jp/", |bundle| {
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
            let folder = &out_dir.join("Android").join(&char_id);
            match folder.exists() {
                true => {
                    let is_empty = folder.read_dir().unwrap().next().is_none();
                    is_empty
                }
                false => true,
            }
        })
        .await?;

    let mut handles = vec![];

    downloaded.iter().for_each(|filename| {
        info!("Extracting {}", filename);
        let char_id = regex.captures(filename).unwrap()[1].to_string();
        let env = unityfs::read_file(PathBuf::from("./temp/jp/Android").join(filename)).unwrap();
        handles.push(tokio::spawn(jp_extract_assets(char_id.clone(), env)));
    });

    for handle in handles {
        match handle.await {
            Err(e) => {
                error!("Error: {}", e);
            }
            _ => {}
        }
    }
    validate_atlas().await?;
    info!("Updating info.json");
    jp_update_info().await?;
    Ok(())
}

async fn jp_extract_assets<S: AsRef<str>>(char_id: S, env: Env) -> Result<()> {
    extract_images(
        &env,
        format!("./public/data/jp/Android/{}", &char_id.as_ref()),
    )
    .await?;
    extract_live2d(
        &env,
        format!("./public/data/jp/Android/{}", &char_id.as_ref()),
    )
    .await?;
    Ok(())
}

async fn jp_update_info() -> Result<()> {
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
    save_json("./public/data/jp/Android/info.json", &data).await?;
    Ok(())
}

async fn validate_atlas() -> Result<()> {
    info!("Validating atlas");
    let directories = vec![
        "./public/data/jp/Android",
        "./public/data/en/GameData/Android",
    ];

    let mut handles = vec![];

    directories
        .iter()
        .flat_map(|dir| WalkDir::new(dir).into_iter().filter_map(|e| e.ok()))
        .filter(|e| e.path().extension().unwrap_or_default() == "atlas")
        .for_each(|entry| {
            handles.push(tokio::spawn(async move {
                info!("Checking {}", entry.path().display());
                let file = std::fs::read_to_string(entry.path()).unwrap();
                for i in 0..file.lines().count() {
                    let line = file.lines().nth(i).unwrap();
                    if !line.contains(".png") {
                        continue;
                    }
                    let filepath = entry.path().parent().unwrap().join(line);
                    if !filepath.exists() {
                        error!("Missing file: {}", filepath.display());
                        continue;
                    }
                    // Next line is size
                    let size_text = file.lines().nth(i + 1).unwrap();
                    let size: Vec<u32> = size_text
                        .split(": ")
                        .nth(1)
                        .unwrap()
                        .split(",")
                        .map(|s| s.parse().unwrap())
                        .collect();
                    let dimensions = get_image_dimensions(&filepath).await.unwrap();
                    if dimensions.0 != size[0] || dimensions.1 != size[1] {
                        error!(
                            "Size mismatch: {} ({}x{}) != {} ({}x{})",
                            &filepath.display(),
                            dimensions.0,
                            dimensions.1,
                            entry.path().display(),
                            size[0],
                            size[1]
                        );
                        // Resize
                        info!("Resizing {}", filepath.display());
                        let image = image::open(&filepath).unwrap();
                        let resized = image.resize_exact(
                            size[0],
                            size[1],
                            image::imageops::FilterType::Nearest,
                        );
                        resized.save(&filepath).unwrap();
                    }
                }
            }))
        });

    for handle in handles {
        match handle.await {
            Err(e) => {
                error!("Error: {}", e);
            }
            _ => {}
        }
    }

    Ok(())
}

pub async fn run_en(catalog: Catalog) -> Result<()> {
    info!("Running table dumper");
    let regex = Regex::new(r"assets-_mx-spinelobbies-(.*?)-_")?;
    let out_dir = PathBuf::from("./public/data/en");
    info!("Downloading Live2D bundles");
    let downloads = catalog
        .save_resource(PathBuf::from("./temp/en/"), |r| {
            let char_id = match regex.captures(&r.resource_path) {
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
            let folder = out_dir
                .clone()
                .join("GameData/Android")
                .join(char_id.clone());
            match folder.exists() {
                true => {
                    let is_empty = folder.read_dir().unwrap().next().is_none();
                    is_empty
                }
                false => {
                    // Check jp dir
                    let folder = PathBuf::from("./public/data/jp/Android").join(char_id.clone());
                    match folder.exists() {
                        true => {
                            let is_empty = folder.read_dir().unwrap().next().is_none();
                            is_empty
                        }
                        false => true,
                    }
                }
            }
        })
        .await?;

    let mut handles = vec![];

    downloads.iter().for_each(|filename| {
        info!("Extracting {}", filename);
        let char_id = regex.captures(filename).unwrap()[1].to_string();
        let env = unityfs::read_file(PathBuf::from("./temp/en").join(filename)).unwrap();
        handles.push(tokio::spawn(en_extract_assets(char_id.clone(), env)));
    });

    for handle in handles {
        match handle.await {
            Err(e) => {
                error!("Error: {}", e);
            }
            _ => {}
        }
    }
    validate_atlas().await?;
    info!("Updating info.json");
    en_update_info().await?;
    Ok(())
}

async fn en_extract_assets(char_id: String, env: Env) -> Result<()> {
    extract_images(
        &env,
        format!("./public/data/en/GameData/Android/{}", char_id),
    )
    .await?;
    extract_live2d(
        &env,
        format!("./public/data/en/GameData/Android/{}", char_id),
    )
    .await?;
    Ok(())
}

async fn en_update_info() -> Result<()> {
    let dir = PathBuf::from("./public/data/en/GameData/Android");
    let mut data = BTreeMap::new();
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
    // Add from jp too
    let jp_info: BTreeMap<String, Vec<String>> = serde_json::from_str(&std::fs::read_to_string(
        "./public/data/jp/Android/info.json",
    )?)?;
    for (key, value) in jp_info {
        if !data.contains_key(&key) {
            data.insert(key, value);
        }
    }
    save_json(
        PathBuf::from("./public/data/en/GameData/Android/info.json"),
        &data,
    )
    .await?;
    Ok(())
}
