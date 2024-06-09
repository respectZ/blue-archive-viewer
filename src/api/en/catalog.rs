use crate::util::save_json;
use anyhow::Result;
use reqwest::Url;
use serde::{Deserialize, Serialize};
use std::path::Path;
use trauma::{download::Download, downloader::DownloaderBuilder};

#[derive(Serialize, Deserialize, Clone)]
pub struct Catalog {
    #[serde(skip)]
    #[allow(dead_code)]
    base_url: String,

    pub id: i32,
    pub market_game_id: String,
    pub build_id: Vec<i32>,
    pub patch_version: i32,
    pub name: String,
    pub patch_state: String,
    pub security_checked: bool,
    pub multi_language: bool,
    pub multi_texture_encode: bool,
    pub multi_texture_quality: bool,
    pub description: String,
    pub register: String,
    pub register_date: String,
    pub updater: String,
    pub update_date: String,
    pub compress: bool,
    pub size: i64,
    pub count: i32,
    pub use_multi_resource: bool,
    pub category: Category,
    pub category_mapping: Vec<CategoryMapping>,
    pub resources: Vec<Resource>,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct Category {
    pub lang: Option<String>,
    pub texture_encode_type: Option<String>,
    pub texture_quality_level: Option<String>,
    pub group: Vec<String>,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct CategoryMapping {
    pub group: String,
    pub paths: Vec<String>,
}

#[derive(Serialize, Deserialize, Clone)]
pub struct Resource {
    pub group: String,
    pub resource_path: String,
    pub resource_size: i64,
    pub resource_hash: String,
}

impl Catalog {
    pub fn new(base_url: String, str: String) -> Self {
        let mut catalog: Catalog = serde_json::from_str(&str).unwrap();
        catalog.base_url = base_url;
        catalog
    }
    pub async fn save<P: AsRef<Path>>(&self, path: P) -> Result<()> {
        save_json(path.as_ref().join("resource-data.json"), self).await
    }
    pub async fn save_resource<P: AsRef<Path>>(
        &self,
        path: P,
        filter: impl Fn(&Resource) -> bool,
    ) -> Result<Vec<String>> {
        let downloader = DownloaderBuilder::new()
            .directory(path.as_ref().to_path_buf())
            .build();
        let downloads = self
            .resources
            .iter()
            .filter(|v| filter(v))
            .map(|v| Download {
                url: Url::parse(format!("{}/{}", self.base_url, v.resource_path).as_str()).unwrap(),
                filename: v.resource_path.clone(),
            })
            .collect::<Vec<Download>>();
        downloader.download(&downloads).await;
        let files = downloads.iter().map(|v| v.filename.clone()).collect();
        Ok(files)
    }
    pub fn get_base_url(&self) -> String {
        self.base_url.clone()
    }
}

impl Resource {
    pub async fn save<P: AsRef<Path>>(&self, path: P, base_url: String) -> Result<()> {
        let downloader = DownloaderBuilder::new()
            .directory(path.as_ref().to_path_buf())
            .build();
        let download = Download {
            url: Url::parse(format!("{}/{}", base_url, self.resource_path).as_str()).unwrap(),
            filename: self.resource_path.clone(),
        };
        downloader.download(&[download]).await;
        Ok(())
    }
}
