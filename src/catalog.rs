use super::api::jp::AddressableCatalog;
use anyhow::Result;
use std::path::PathBuf;
use tokio::runtime::Handle;

pub async fn run_jp(catalog: AddressableCatalog) -> Result<()> {
    let handle = Handle::current();
    let c1 = catalog.clone();
    let c2 = catalog.clone();

    let task_1 = handle.spawn(async move {
        println!("[MediaCatalog] Saving");
        let media_catalog = c1.get_media_catalog().await.unwrap();
        media_catalog
            .save(PathBuf::from("./public/data/jp"))
            .await
            .unwrap();
        println!("[MediaCatalog] Saved");
    });
    let task_2 = handle.spawn(async move {
        println!("[TableCatalog] Saving");
        let table_catalog = c2.get_table_catalog().await.unwrap();
        table_catalog
            .save(PathBuf::from("./public/data/jp"))
            .await
            .unwrap();
        println!("[TableCatalog] Saved");
    });
    let _ = tokio::try_join!(task_1, task_2);
    Ok(())
}
