use crate::consts::{APKPURE_DOWNLOAD_URL_REGEX, APKPURE_VERSION_REGEX, APKPURE_VERSION_URL};
use crate::info;
use crate::util::save_file;
use anyhow::{anyhow, Context, Result};
use regex::Regex;
use reqwest::header::{HeaderMap, HeaderValue};
use reqwest::Client;
use reqwest::Url;
use std::fs;
use std::fs::File;
use std::io::{self, Cursor, Read};
use std::path::PathBuf;
use trauma::download::Download;
use trauma::downloader::DownloaderBuilder;
use walkdir::WalkDir;
use zip::ZipArchive;

fn http_headers() -> HeaderMap {
    let mut headers = HeaderMap::new();
    headers.insert("x-cv", HeaderValue::from_static("3172501"));
    headers.insert("x-sv", HeaderValue::from_static("29"));
    headers.insert(
        "x-abis",
        HeaderValue::from_static("arm64-v8a,armeabi-v7a,armeabi"),
    );
    headers.insert("x-gp", HeaderValue::from_static("1"));
    headers
}

async fn get_version() -> Result<String> {
    let file = File::open("./public/data/jp/version.txt");
    if let Ok(mut file) = file {
        let mut version = String::new();
        file.read_to_string(&mut version)?;
        return Ok(version);
    }
    Ok("".to_string())
}

pub async fn download() -> Result<()> {
    info!("Checking for updates");
    let client = Client::builder().default_headers(http_headers()).build()?;
    let versions_response = client.get(APKPURE_VERSION_URL).send().await?;

    match versions_response.status() {
        reqwest::StatusCode::OK => {}
        _ => {
            return Err(anyhow!(
                "Failed to get versions: {}",
                versions_response.status()
            ));
        }
    }

    let body = versions_response.text().await?;
    let re_version = Regex::new(APKPURE_VERSION_REGEX).unwrap();
    let new_version = re_version.find(body.as_str()).unwrap().as_str();

    // Check version
    if new_version == get_version().await.unwrap() {
        info!("App is up to date");
        return Ok(());
    }

    // Remove old app
    let path = PathBuf::from("./temp/app/com.YostarJP.BlueArchive.apk");
    if path.exists() {
        fs::remove_file(path).with_context(|| "Failed to remove old app")?;
    }

    info!("Latest version: {}", new_version);

    let re_url = Regex::new(APKPURE_DOWNLOAD_URL_REGEX).unwrap();
    let download_url = match re_url.captures(body.as_str()) {
        Some(caps) if caps.len() >= 2 => caps.get(2).unwrap().as_str(),
        _ => {
            return Err(anyhow!("Failed to get download url"));
        }
    };

    info!("Downloading app");
    let downloader = DownloaderBuilder::new()
        .directory(PathBuf::from("./temp/app"))
        .build();
    let downloads = vec![Download {
        url: Url::parse(download_url).unwrap(),
        filename: "com.YostarJP.BlueArchive.apk".to_string(),
    }];
    downloader.download(&downloads).await;
    info!("Finished downloading app");
    save_file("./public/data/jp/version.txt", new_version.as_bytes()).await?;
    Ok(())
}

pub fn extract() -> Result<()> {
    info!("Extracting app");

    let mut archive = ZipArchive::new(
        File::open("./temp/app/com.YostarJP.BlueArchive.apk")
            .with_context(|| "./temp/app/com.YostarJP.BlueArchive.apk not found")?,
    )
    .with_context(|| "Failed to open archive")?;

    let mut unity_apk = match archive.by_name("UnityDataAssetPack.apk") {
        Ok(file) => file,
        Err(_) => {
            return Err(anyhow!("UnityDataAssetPack.apk not found"));
        }
    };

    let mut buf = Vec::new();
    unity_apk
        .read_to_end(&mut buf)
        .with_context(|| "Failed to read UnityDataAssetPack")?;
    let mut cursor = Cursor::new(buf);

    let mut archive =
        ZipArchive::new(&mut cursor).with_context(|| "Failed to open UnityDataAssetPack")?;

    for i in 0..archive.len() {
        let mut file = archive.by_index(i)?;
        // Extract that starts with "assets/bin/Data/"
        if !file.name().starts_with("assets/bin/Data/") {
            continue;
        }
        let outpath = match file.enclosed_name() {
            Some(path) => PathBuf::from("./temp/app/com.YostarJP.BlueArchive")
                .join(path)
                .to_owned(),
            None => continue,
        };
        if let Some(p) = outpath.parent() {
            if !p.exists() {
                fs::create_dir_all(p).with_context(|| "Failed to create directory")?;
            }
        }

        let mut outfile = File::create(outpath).with_context(|| "Failed to create file")?;
        io::copy(&mut file, &mut outfile).with_context(|| "Failed to copy file")?;
    }

    info!("Finished extracting app");
    Ok(())
}

// TODO: Implement actual reading of unity asset bundles
// This is not actual of reading unity asset bundles.
// This is an idiot way to read the game main config since the header isn't valid
// and I can't found any actual library.
// This may broke in the future.
pub fn get_game_main_config() -> Result<Vec<u8>> {
    let pattern = vec![
        0x47, 0x61, 0x6D, 0x65, 0x4D, 0x61, 0x69, 0x6E, 0x43, 0x6F, 0x6E, 0x66, 0x69, 0x67, 0x00,
        0x00, 0x92, 0x03, 0x00, 0x00,
    ];
    let path = PathBuf::from("./temp/app/com.YostarJP.BlueArchive/assets/bin/Data/");
    for entry in WalkDir::new(path) {
        let entry = entry?;
        if !entry.file_type().is_file() {
            continue;
        }
        let file = File::open(entry.path())?;
        let mut reader = io::BufReader::new(file);
        let mut buffer: Vec<u8> = Vec::new();
        reader.read_to_end(&mut buffer)?;
        // Find next bytes after the pattern
        for i in 0..buffer.len() {
            if buffer[i..].starts_with(&pattern) {
                let data = &buffer[i + pattern.len()..];
                // Strip last 0x00, 0x00
                let data = &data[..data.len() - 2];
                return Ok(data.to_vec());
            }
        }
    }
    Err(anyhow::anyhow!("GameMainConfig not found"))
}
