mod api;
mod util;
use clap::{Parser, Subcommand};
use std::path::PathBuf;
use tokio::runtime::Handle;

#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    action: Action,

    #[arg(short, long, value_enum, default_value_t=Region::JP)]
    region: Region,
}

#[derive(Subcommand)]
enum Action {
    Update {
        #[command(subcommand)]
        name: ActionUpdate,
    },
}

#[derive(clap::ValueEnum, Clone)]
enum Region {
    JP,
    EN,
}

#[derive(Subcommand)]
enum ActionUpdate {
    Catalog,
    CG,
    Table,
    Live2D,
    All,
}

#[tokio::main]
async fn main() {
    let cli = Cli::parse();
    let region = cli.region;

    let handle = Handle::current();

    let catalog_jp = match region {
        Region::JP => Some(api::jp::get_addressable_catalog().await.unwrap()),
        _ => None,
    };

    match cli.action {
        Action::Update { name } => match name {
            ActionUpdate::All => {
                println!("TODO: Implement all")
            }
            ActionUpdate::CG => {
                if let Some(catalog) = catalog_jp {
                    let media_catalog = catalog.get_media_catalog().await.unwrap();
                    media_catalog
                        .save_media(PathBuf::from("./public/data/jp"), |media| {
                            media.path.contains(".jpg")
                        })
                        .await
                        .unwrap();
                }
            }
            ActionUpdate::Catalog => {
                if let Some(catalog) = catalog_jp {
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
                }
            }
            ActionUpdate::Live2D => {
                println!("TODO: Implement live2d")
            }
            ActionUpdate::Table => {
                println!("TODO: Implement table")
            }
        },
    };
}
