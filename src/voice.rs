use std::{collections::HashMap, path::PathBuf};

use anyhow::Result;
use tokio::fs;
use tokio::task;

use crate::{
    api::jp::{media_catalog::Media, AddressableCatalog},
    info,
    util::table_service::TableZipFile,
};

pub async fn run_jp(catalog: &AddressableCatalog) -> Result<()> {
    let media_catalog = catalog.get_media_catalog().await?;
    info!("Downloading JP voices...");
    let voices = media_catalog
        .table
        .iter()
        .filter(|(_, media)| media.file_name.starts_with("JP") && media.file_name.ends_with(".zip"))
        .map(|(key, media)| (key.clone(), media))
        .collect::<HashMap<String, &Media>>();

    media_catalog
        .save_medias("./temp/jp/", voices.values().cloned().collect())
        .await?;
    extract_jp_voices(voices).await?;
    Ok(())
}

async fn extract_jp_voices(medias: HashMap<String, &Media>) -> Result<()> {
    info!("Extracting JP voices...");
    let mut tasks = Vec::with_capacity(medias.len());
    for (key, media) in medias {
        let buf = fs::read(format!("./temp/jp/MediaResources/{}", media.path)).await?;
        let path_buf = PathBuf::from(&media.path);
        let filename = path_buf
            .file_name()
            .unwrap()
            .to_str()
            .unwrap()
            .to_string()
            .to_lowercase();
        let char_id = key.split('/').last().unwrap().to_string();

        tasks.push(task::spawn(async move {
            let mut zip = TableZipFile::new(buf, &filename);
            let dir = PathBuf::from("./public/data/jp/MediaResources/")
                .join(path_buf.parent().unwrap())
                .join(&char_id);
            fs::create_dir_all(&dir).await.unwrap();
            for (name, buf) in zip.extract_all() {
                fs::write(dir.join(name), buf).await.unwrap();
            }
        }));
    }
    for task in tasks {
        task.await?;
    }
    Ok(())
}
