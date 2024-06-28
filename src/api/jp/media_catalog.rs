use crate::util;
use crate::util::save_json;
use anyhow::{Context, Result};
use reqwest::Url;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::io::Cursor;
use std::path::Path;
use trauma::download::Download;
use trauma::downloader::DownloaderBuilder;

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct Media {
    pub path: String,
    pub file_name: String,
    pub bytes: i64,
    pub crc: i64,
    pub is_prologue: bool,
    pub is_split_download: bool,
    pub media_type: i32,
}

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct MediaCatalog {
    table: HashMap<String, Media>,

    #[serde(skip)]
    base_url: String,
}

// Note: this is not an actual deserialization, just a mockup
pub fn deserialize(bytes: &[u8], base_url: &String) -> Result<MediaCatalog> {
    let mut cursor = Cursor::new(bytes);

    // Skip 1 byte
    let _ = util::memory_pack::read_i8(&mut cursor);

    // Table Size
    let table_size = util::memory_pack::read_i32(&mut cursor)?;
    let table = (0..table_size)
        .map(|_| read_media(&mut cursor))
        .collect::<Result<HashMap<String, Media>>>()
        .with_context(|| "Failed to read media")?;
    Ok(MediaCatalog {
        table,
        base_url: base_url.clone(),
    })
}

fn read_media(cursor: &mut Cursor<&[u8]>) -> Result<(String, Media)> {
    // Idk, skip 4 bytes
    let _ = util::memory_pack::read_i32(cursor);

    let key = util::memory_pack::read_string(cursor)?;

    // idk 1 byte
    let _ = util::memory_pack::read_i8(cursor);

    // idk 4 bytes
    let _ = util::memory_pack::read_i32(cursor);

    let path = util::memory_pack::read_string(cursor)?;

    // idk 4 bytes
    let _ = util::memory_pack::read_i32(cursor);

    let file_name = util::memory_pack::read_string(cursor)?;
    let bytes = util::memory_pack::read_i64(cursor)?;
    let crc = util::memory_pack::read_i64(cursor)?;
    let is_prologue = util::memory_pack::read_bool(cursor)?;
    let is_split_download = util::memory_pack::read_bool(cursor)?;
    let media_type = util::memory_pack::read_i32(cursor)?;

    Ok((
        key,
        Media {
            path,
            file_name,
            bytes,
            crc,
            is_prologue,
            is_split_download,
            media_type,
        },
    ))
}

impl MediaCatalog {
    /// Save the MediaCatalog to a file
    /// # Arguments
    /// * `path` - The root directory to save the MediaCatalog
    /// # Returns
    /// * `Result<()>` - Ok if successful, Err if an error occurred
    /// # Example
    /// ```
    /// let catalog = api::jp::get_addressable_catalog().await.unwrap();
    /// let media_catalog = catalog.get_media_catalog().await.unwrap();
    /// // ./test/MediaResources/MediaCatalog.json
    /// media_catalog.save(PathBuf::from("./test")).await.unwrap();
    /// ```
    pub async fn save<P: AsRef<Path>>(&self, path: P) -> Result<()> {
        save_json(path.as_ref().join("MediaResources/MediaCatalog.json"), self).await
    }
    pub async fn save_media<P: AsRef<Path>>(
        &self,
        path: P,
        filter: impl Fn(&Media) -> bool,
    ) -> Result<()> {
        let root_dir = path.as_ref().join("MediaResources");
        let downloader = DownloaderBuilder::new().directory(root_dir).build();
        let downloads = self
            .table
            .iter()
            .filter(|(_, v)| filter(v))
            .map(|(_, v)| Download {
                url: Url::parse(format!("{}/MediaResources/{}", self.base_url, v.path).as_str())
                    .unwrap(),
                filename: v.path.clone(),
            })
            .collect::<Vec<Download>>();
        downloader.download(&downloads).await;
        Ok(())
    }
}
