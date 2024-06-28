use anyhow::{anyhow, Result};
use image::DynamicImage;
use serde::Serialize;
use std::path::Path;
use tokio::fs::{create_dir_all, File};
use tokio::io::{AsyncReadExt, AsyncWriteExt};

pub async fn save_json<T: Serialize, P: AsRef<Path>>(path: P, data: &T) -> Result<()> {
    let json = serde_json::to_string_pretty(data)?;
    // Create directory if not exists
    if let Some(parent) = path.as_ref().parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(json.as_bytes()).await?;
    Ok(())
}

pub async fn save_json_pretty<T: Serialize, P: AsRef<Path>>(path: P, data: &T) -> Result<()> {
    let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
    let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
    data.serialize(&mut ser)?;
    // Create directory if not exists
    if let Some(parent) = path.as_ref().parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(&ser.into_inner()).await?;
    Ok(())
}

pub async fn save_image<P: AsRef<Path>>(path: P, image: DynamicImage) -> Result<()> {
    // Create directory if not exists
    if let Some(parent) = path.as_ref().parent() {
        create_dir_all(parent).await?;
    }
    image.save(path)?;
    Ok(())
}

pub async fn save_file<P: AsRef<Path>>(path: P, data: &[u8]) -> Result<()> {
    // Create directory if not exists
    if let Some(parent) = path.as_ref().parent() {
        create_dir_all(parent).await?;
    }
    let mut file = File::create(path).await?;
    file.write_all(data).await?;
    Ok(())
}

pub async fn get_image_dimensions<P: AsRef<Path>>(path: P) -> Result<(u32, u32)> {
    let file = std::fs::File::open(path)?;
    let reader = std::io::BufReader::new(file);
    let dimensions = image::io::Reader::new(reader)
        .with_guessed_format()?
        .into_dimensions()?;
    Ok(dimensions)
}

pub async fn compare_crc<P: AsRef<Path>>(path: P, crc: u32) -> Result<bool> {
    let file = match File::open(&path).await {
        Ok(file) => file,
        Err(_) => {
            return Err(anyhow!("File not found: {:?}", path.as_ref()));
        }
    };
    // Compare crc
    let mut buf = Vec::new();
    let mut reader = tokio::io::BufReader::new(file);
    tokio::io::copy(&mut reader, &mut buf).await?;
    let mut hasher = crc32fast::Hasher::new();
    hasher.update(&buf);
    let checksum = hasher.finalize();
    Ok(crc == checksum)
}

async fn calculate_hash<P: AsRef<Path>>(path: P) -> Result<String> {
    let mut file = File::open(&path).await?;
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer).await?;
    let digest = md5::compute(buffer);
    let hash_hex = format!("{:x}", digest);
    Ok(hash_hex)
}

pub async fn compare_hash<P: AsRef<Path>, S: AsRef<str>>(path: P, hash: S) -> Result<bool> {
    match path.as_ref().exists() {
        true => {}
        false => {
            return Err(anyhow!("File not found: {:?}", path.as_ref()));
        }
    }
    // Compare hash
    let file_hash = calculate_hash(&path).await?;
    Ok(hash.as_ref().to_string() == file_hash)
}
