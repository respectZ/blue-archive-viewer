use crate::util;
use crate::util::save_json;
use anyhow::{Context, Result};
use serde::{Deserialize, Serialize};
use std::{collections::HashMap, io::Cursor, path::PathBuf};
use trauma::download::Download;
use trauma::downloader::DownloaderBuilder;

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct Table {
    pub name: String,
    pub size: i64,
    pub crc: i64,
    pub is_in_build: bool,
    pub is_changed: bool,
    pub is_prologue: bool,
    pub is_split_download: bool,
    pub includes: Vec<String>,
}

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct TableCatalog {
    table: HashMap<String, Table>,

    #[serde(skip)]
    base_url: String,
}

pub fn deserialize(bytes: &[u8], base_url: &String) -> Result<TableCatalog> {
    let mut cursor = Cursor::new(bytes);

    // Skip 1 byte
    let _ = util::memory_pack::read_i8(&mut cursor);

    // Table Size
    let table_size = util::memory_pack::read_i32(&mut cursor)?;
    let table = (0..table_size)
        .map(|_| read_table(&mut cursor))
        .collect::<Result<HashMap<String, Table>>>()
        .with_context(|| "Failed to read table")?;
    Ok(TableCatalog {
        table,
        base_url: base_url.clone(),
    })
}

fn read_includes(cursor: &mut Cursor<&[u8]>) -> Result<Vec<String>> {
    let size = util::memory_pack::read_i32(cursor)?;
    // If size is 0xffffffff, return empty vector
    if size == -1 {
        return Ok(vec![]);
    }
    // Skip 4 bytes (C7 FF FF FF), array opening?
    let _ = util::memory_pack::read_i32(cursor);

    Ok((0..size)
        .map(|i| {
            let s = util::memory_pack::read_string(cursor).unwrap();
            // Skip 4 bytes if not last element
            if i != size - 1 {
                let _ = util::memory_pack::read_i32(cursor);
            }
            s
        })
        .collect())
}

fn read_table(cursor: &mut Cursor<&[u8]>) -> Result<(String, Table)> {
    // Idk, skip 4 bytes
    let _ = util::memory_pack::read_i32(cursor);

    // key
    let key = util::memory_pack::read_string(cursor)?;

    // Idk 1 byte
    let _ = util::memory_pack::read_i8(cursor);
    // Idk 4 bytes (F5 FF FF FF)
    let _ = util::memory_pack::read_i32(cursor);

    let name = util::memory_pack::read_string(cursor)?;
    let size = util::memory_pack::read_i64(cursor)?;
    let crc = util::memory_pack::read_i64(cursor)?;
    let is_in_build = util::memory_pack::read_bool(cursor)?;
    let is_changed = util::memory_pack::read_bool(cursor)?;
    let is_prologue = util::memory_pack::read_bool(cursor)?;
    let is_split_download = util::memory_pack::read_bool(cursor)?;

    let includes = read_includes(cursor)?;

    Ok((
        key,
        Table {
            name,
            size,
            crc,
            is_in_build,
            is_changed,
            is_prologue,
            is_split_download,
            includes,
        },
    ))
}

impl TableCatalog {
    /// Save the TableCatalog to a file
    /// # Arguments
    /// * `path` - The root directory to save the TableCatalog
    /// # Returns
    /// * `Result<()>` - Ok if successful, Err if an error occurred
    /// # Example
    /// ```
    /// let catalog = api::jp::get_addressable_catalog().await.unwrap();
    /// let table_catalog = catalog.get_table_catalog().await.unwrap();
    /// // ./test/TableBundles/TableCatalog.json
    /// table_catalog.save(PathBuf::from("./test")).await.unwrap();
    /// ```
    pub async fn save(&self, path: PathBuf) -> Result<()> {
        save_json(path.join("TableBundles/TableCatalog.json"), self).await
    }
    pub async fn save_tables(&self, path: PathBuf, filter: impl Fn(&Table) -> bool) -> Result<()> {
        let root_dir = path.join("TableBundles");
        let downloader = DownloaderBuilder::new().directory(root_dir).build();
        let downloads = self
            .table
            .iter()
            .filter(|(_, v)| filter(v))
            .map(|(key, _)| {
                Download::try_from(format!("{}/TableBundles/{}", self.base_url, key).as_str())
            })
            .collect::<Result<Vec<Download>, _>>()?;
        downloader.download(&downloads).await;
        Ok(())
    }
}
