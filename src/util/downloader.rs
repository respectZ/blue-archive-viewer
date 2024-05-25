use std::path::PathBuf;
use trauma::{download::Download, downloader::DownloaderBuilder, Error};

pub fn create_downloader() -> DownloaderBuilder {
    DownloaderBuilder::new()
}

pub async fn download_files(root_dir: PathBuf, urls: Vec<&str>) -> Result<(), Error> {
    let downloader = DownloaderBuilder::new().directory(root_dir).build();
    // Convert urls to downloads
    let downloads = urls
        .iter()
        .map(|url| Download::try_from(*url))
        .collect::<Result<Vec<Download>, Error>>()?;
    downloader.download(&downloads).await;
    Ok(())
}
