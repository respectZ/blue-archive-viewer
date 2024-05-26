use std::{collections::HashMap, hash::Hash};

use anyhow::Result;
use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::mx::data::table_encryption_service::{convert_string, create_key, new_encrypt_string};
use base64::{engine::general_purpose, Engine};

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct GameMainConfig {
    pub server_info_data_url: String,
    pub default_connection_group: String,
    pub skip_tutorial: String,
    pub language: String,
}

impl GameMainConfig {
    pub fn from_bytes(bytes: &[u8]) -> Result<Self> {
        let key = create_key(b"GameMainConfig");
        let b64 = general_purpose::STANDARD.encode(bytes);
        let encrypted = convert_string(&b64, &key)?;
        let encrypted_map: HashMap<String, Value> = serde_json::from_str(&encrypted)?;
        // Loop GameMainConfig keys
        let keys = [
            "ServerInfoDataUrl",
            "DefaultConnectionGroup",
            "SkipTutorial",
            "Language",
        ];
        let keys: HashMap<String, &str> = keys
            .iter()
            .map(|key| {
                let k = create_key(key.as_bytes());
                let value = new_encrypt_string(*key, &k).unwrap();
                (value, *key)
            })
            .collect();
        let map = keys
            .iter()
            .map(|(encrypted_key, decrypted_key)| {
                let encrypted_value = encrypted_map.get(encrypted_key).unwrap();
                let key = create_key(decrypted_key.as_bytes());
                let decrypted_value =
                    convert_string(encrypted_value.as_str().unwrap(), &key).unwrap();
                (*decrypted_key, decrypted_value)
            })
            .collect::<HashMap<_, _>>();

        let json_s = serde_json::to_string_pretty(&map)?;
        let json: GameMainConfig = serde_json::from_str(&json_s)?;
        Ok(json)
    }
}
