use std::path::Path;

use anyhow::Result;
use reqwest::Url;
use serde::{Deserialize, Serialize};
use trauma::{download::Download, downloader::DownloaderBuilder};

use crate::util::save_json;

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct BundlePackingInfo {
    pub milestone: String,
    pub patch_version: u32,
    pub full_patch_packs: Vec<BundlePatchPack>,

    #[serde(skip)]
    _base_url: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct BundlePatchPack {
    pub pack_name: String,
    pub pack_size: i64,
    pub crc: i64,
    pub is_prologue: bool,
    pub is_split_download: bool,
    pub bundle_files: Vec<BundleFile>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct BundleFile {
    pub name: String,
    pub size: i64,
    pub is_prologue: bool,
    pub crc: i64,
    pub is_split_download: bool,
}

impl BundlePackingInfo {
    /// Save the bundle packing info to a file
    /// # Arguments
    /// * `path` - The path to save the bundle packing info to
    /// # Returns
    /// * `Result<()>` - The result of the operation
    /// # Errors
    /// * If the file cannot be saved
    /// # Example
    /// ```no_run
    /// let catalog = api::jp::get_addressable_catalog().await.unwrap();
    /// let bundle_packing_info = catalog.get_bundle_packing_info().await.unwrap();
    /// // ./test/MediaResources/MediaCatalog.json
    /// bundle_packing_info.save(std::path::PathBuf::from("./test"));
    /// ```
    pub fn new(base_url: String, str: String) -> Result<Self> {
        let mut bundle_packing_info: BundlePackingInfo = serde_json::from_str(&str)?;
        bundle_packing_info._base_url = base_url;
        Ok(bundle_packing_info)
    }
    pub async fn save<P: AsRef<Path>>(&self, path: P) -> Result<()> {
        save_json(path.as_ref().join("Android/bundlePackingInfo.json"), self).await
    }
    pub async fn save_bundle<P: AsRef<Path>>(
        &self,
        path: P,
        filter: impl Fn(&BundlePatchPack) -> bool,
    ) -> Result<Vec<String>> {
        let root_dir = path.as_ref().join("Android");
        let downloader = DownloaderBuilder::new().directory(root_dir).build();
        let downloads = self
            .full_patch_packs
            .iter()
            .filter(|v| filter(v))
            .map(|v| Download {
                url: Url::parse(
                    format!("{}/Android_PatchPack/{}", self._base_url, v.pack_name).as_str(),
                )
                .unwrap(),
                filename: v.pack_name.clone(),
            })
            .collect::<Vec<Download>>();
        downloader.download(&downloads).await;
        let files = downloads
            .iter()
            .map(|v| v.filename.clone())
            .collect::<Vec<String>>();
        Ok(files)
    }
}
