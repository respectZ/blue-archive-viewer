use anyhow::Result;
use image::DynamicImage;
use serde::Serialize;
use std::path::PathBuf;
use tokio::fs::{create_dir_all, File};
use tokio::io::AsyncWriteExt;

pub async fn save_json<T: Serialize>(path: PathBuf, data: &T) -> Result<()> {
    let json = serde_json::to_string_pretty(data)?;
    // Create directory if not exists
    if let Some(parent) = path.parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(json.as_bytes()).await?;
    Ok(())
}

pub async fn save_json_pretty<T: Serialize>(path: PathBuf, data: &T) -> Result<()> {
    let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
    let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
    data.serialize(&mut ser)?;
    // Create directory if not exists
    if let Some(parent) = path.parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(&ser.into_inner()).await?;
    Ok(())
}

pub async fn save_image(path: PathBuf, image: DynamicImage) -> Result<()> {
    // Create directory if not exists
    if let Some(parent) = path.parent() {
        create_dir_all(parent).await?;
    }
    image.save(path)?;
    Ok(())
}

pub async fn save_file(path: PathBuf, data: &[u8]) -> Result<()> {
    // Create directory if not exists
    if let Some(parent) = path.parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(data).await?;
    Ok(())
}
