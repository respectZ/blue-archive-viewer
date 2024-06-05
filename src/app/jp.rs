use crate::info;
use anyhow::{Context, Result};
use reqwest::Url;
use reqwest::{redirect, Client};
use std::fs;
use std::fs::File;
use std::io::{self, Read};
use std::path::PathBuf;
use trauma::download::Download;
use trauma::downloader::DownloaderBuilder;
use walkdir::WalkDir;
use zip::ZipArchive;

async fn compare_app_size() -> Result<bool> {
    let url = "https://api.qoo-app.com/v6/apps/com.YostarJP.BlueArchive/download";
    let client = Client::builder()
        .redirect(redirect::Policy::none())
        .build()?;
    let resp = client.get(url).send().await?;

    let redirect_url = resp
        .headers()
        .get("location")
        .context("Failed to get location")?
        .to_str()
        .context("Failed to convert location to string")?;

    let resp = Client::new().head(redirect_url).send().await?;
    let size = resp
        .headers()
        .get("content-length")
        .context("Failed to get content-length")?
        .to_str()
        .context("Failed to convert content-length to string")?
        .parse::<u64>()
        .context("Failed to parse content-length")?;
    let path = PathBuf::from("./temp/app/com.YostarJP.BlueArchive.apk");
    let metadata = fs::metadata(path).context("Failed to get metadata")?;
    let app_size = metadata.len();

    Ok(size == app_size)
}

pub async fn download() -> Result<()> {
    match compare_app_size().await {
        Ok(true) => {
            info!("App is up to date");
            return Ok(());
        }
        _ => {
            // Remove old app
            let path = PathBuf::from("./temp/app/com.YostarJP.BlueArchive.apk");
            if path.exists() {
                fs::remove_file(path).with_context(|| "Failed to remove old app")?;
            }
            let url = "https://api.qoo-app.com/v6/apps/com.YostarJP.BlueArchive/download";
            let downloader = DownloaderBuilder::new()
                .directory(PathBuf::from("./temp/app"))
                .build();
            let downloads = vec![Download {
                url: Url::parse(url).unwrap(),
                filename: "com.YostarJP.BlueArchive.apk".to_string(),
            }];
            downloader.download(&downloads).await;
            info!("Finished downloading app");
            Ok(())
        }
    }
}

pub fn extract() -> Result<()> {
    info!("Extracting app");

    let mut archive = ZipArchive::new(
        File::open("./temp/app/com.YostarJP.BlueArchive.apk")
            .with_context(|| "./temp/app/com.YostarJP.BlueArchive.apk not found")?,
    )
    .with_context(|| "Failed to open archive")?;

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
