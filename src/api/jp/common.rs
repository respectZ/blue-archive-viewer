use super::{bundle_packing_info, media_catalog, table_catalog};
use crate::util::save_json;
use anyhow::Result;
use serde::{Deserialize, Serialize};
use std::path::Path;

#[derive(Serialize, Deserialize, Clone, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct AddressableCatalog {
    connection_groups: Vec<ConnectionGroup>,
}

#[derive(Serialize, Deserialize, Clone, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct ConnectionGroup {
    name: String,
    management_data_url: String,
    is_production_addressables: bool,
    api_url: String,
    gateway_url: String,
    kibana_log_url: String,
    prohibited_word_black_list_uri: String,
    prohibited_word_white_list_uri: String,
    customer_service_url: String,
    override_connection_groups: Vec<OverrideConnectionGroup>,
    bundle_version: String,
}

#[derive(Serialize, Deserialize, Clone, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct OverrideConnectionGroup {
    name: String,
    addressables_catalog_url_root: String,
}

pub async fn get_addressable_catalog(url: &str) -> Result<AddressableCatalog> {
    // Request
    let resp = reqwest::get(url).await?;
    let body = resp.text().await?;
    let catalog: AddressableCatalog = serde_json::from_str(&body)?;
    Ok(catalog)
}

impl AddressableCatalog {
    pub fn get_addressable_catalog_url_root(&self) -> &String {
        &self.connection_groups[0].override_connection_groups[1].addressables_catalog_url_root
    }

    #[allow(dead_code)]
    pub async fn save<P: AsRef<Path>>(&self, path: P) -> Result<()> {
        save_json(path, self).await
    }
    pub async fn get_media_catalog(&self) -> Result<media_catalog::MediaCatalog> {
        let url = format!(
            "{}/MediaResources/Catalog/MediaCatalog.bytes",
            self.get_addressable_catalog_url_root()
        );
        let resp = reqwest::get(url).await?;
        let bytes = resp.bytes().await?;
        let media_catalog =
            media_catalog::deserialize(bytes.as_ref(), self.get_addressable_catalog_url_root())?;
        Ok(media_catalog)
    }
    pub async fn get_table_catalog(&self) -> Result<table_catalog::TableCatalog> {
        let url = format!(
            "{}/TableBundles/TableCatalog.bytes",
            self.get_addressable_catalog_url_root()
        );
        let resp = reqwest::get(url).await?;
        let bytes = resp.bytes().await?;
        let table_catalog =
            table_catalog::deserialize(bytes.as_ref(), self.get_addressable_catalog_url_root())?;
        Ok(table_catalog)
    }
    pub async fn get_bundle_packing_info(&self) -> Result<bundle_packing_info::BundlePackingInfo> {
        let url = format!(
            "{}/Android_PatchPack/BundlePackingInfo.json",
            self.get_addressable_catalog_url_root()
        );
        let resp = reqwest::get(url).await?;
        let body = resp.text().await?;
        let bundle_packing_info = bundle_packing_info::BundlePackingInfo::new(
            self.get_addressable_catalog_url_root().clone(),
            body,
        )?;
        Ok(bundle_packing_info)
    }
}
