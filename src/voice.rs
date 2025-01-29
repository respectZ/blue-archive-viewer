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
        let dir = PathBuf::from("./public/data/")
            .join(path.strip_prefix("./temp/")?.parent().unwrap())
            .join(filename.trim_end_matches(".zip"));
        info!("Extracting {} to {:?}", filename, dir);
        fs::create_dir_all(&dir)?;
        for (name, buf) in zip.extract_all() {
            fs::write(dir.join(name), buf)?;
        }
    }
    Ok(())
}
