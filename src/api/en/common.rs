use super::catalog::Catalog;
use anyhow::Result;
use regex::Regex;
use reqwest::Client;
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::{collections::HashMap, path::Path};

static PLAYSTORE_URL: &str =
    "https://play.google.com/store/apps/details?id=com.nexon.bluearchive&hl=in&gl=US";
static API_URL: &str = "https://api-pub.nexon.com/patch/v1.1/version-check";

#[derive(Deserialize, Serialize)]
pub struct ApiResponse {
    pub api_version: String,
    pub market_game_id: String,
    pub latest_build_version: String,
    pub latest_build_number: String,
    pub min_build_version: String,
    pub min_build_number: String,
    pub patch: Patch,
}

#[derive(Deserialize, Serialize)]
pub struct Patch {
    pub patch_version: i32,
    pub resource_path: String,
    pub bdiff_path: Vec<HashMap<String, String>>,
}

pub async fn get_addressable_catalog() -> Result<ApiResponse> {
    let version = get_game_version().await?;
    let build_number = version.split('.').last().unwrap();
    let client = Client::new();
    let api_response = client
        .post(API_URL)
        .json(&json!({
            "market_game_id": "com.nexon.bluearchive",
            "market_code": "playstore",
            "curr_build_version": version,
            "curr_build_number": build_number
        }))
        .send()
        .await?
        .json::<ApiResponse>()
        .await?;
    Ok(api_response)
}

async fn get_game_version() -> Result<String> {
    let regex_version = Regex::new(r"\d{1}\.\d{2}\.\d{6}")?;
    let client = Client::new();
    let res = client.get(PLAYSTORE_URL).send().await?.text().await?;
    let version = regex_version.find(&res).unwrap().as_str().to_string();
    Ok(version)
}

impl ApiResponse {
    pub async fn get_catalog(&self) -> Result<Catalog> {
        let catalog = reqwest::get(&self.patch.resource_path)
            .await?
            .text()
            .await?;
        let base_url = Path::new(&self.patch.resource_path)
            .parent()
            .unwrap()
            .to_str()
            .unwrap()
            .to_string();
        let catalog = Catalog::new(base_url, catalog);
        Ok(catalog)
    }
}
