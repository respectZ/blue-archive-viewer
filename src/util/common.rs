use anyhow::Result;
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
