use std::{fs, path::PathBuf};

use anyhow::Result;

use crate::{api::jp::AddressableCatalog, info, util::table_service::TableZipFile};

pub async fn run_jp(catalog: &AddressableCatalog) -> Result<()> {
    let media_catalog = catalog.get_media_catalog().await?;
    info!("Downloading JP voices...");
    media_catalog
        .save_media("./temp/jp/", |media| {
            media.file_name.starts_with("JP") && media.file_name.ends_with(".zip")
        })
        .await?;
    extract_jp_voices()?;
    Ok(())
}

fn extract_jp_voices() -> Result<()> {
    info!("Extracting JP voices...");
    let path = PathBuf::from("./temp/jp/MediaResources/GameData/Audio/VOC_JP/");
    for entry in path.read_dir()? {
        let entry = entry?;
        let path = entry.path();
        if path.extension().unwrap() != "zip" {
            continue;
        }
        let buf = fs::read(path.clone())?;
        let filename = path.file_name().unwrap().to_str().unwrap();
        let mut zip = TableZipFile::new(buf, filename.to_lowercase());
        for (name, buf) in zip.extract_all() {
            let dir = filename.trim_end_matches(".zip");
            let path = PathBuf::from(format!(
                "./public/data/jp/MediaResources/GameData/Audio/VOC_JP/{}/{}",
                dir, name
            ));
            fs::create_dir_all(path.parent().unwrap())?;
            fs::write(path, buf)?;
        }
    }
    Ok(())
}
