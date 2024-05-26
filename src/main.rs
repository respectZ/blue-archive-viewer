mod api;
mod catalog;
mod cg;
mod util;

use clap::{Parser, Subcommand};

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
        name: Update,
    },
}

#[derive(clap::ValueEnum, Clone)]
enum Region {
    JP,
    EN,
}

#[derive(Subcommand)]
enum Update {
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

    let catalog_jp = match region {
        Region::JP => Some(api::jp::get_addressable_catalog().await.unwrap()),
        _ => None,
    };

    match cli.action {
        Action::Update { name } => match name {
            Update::All => {
                let c1 = catalog_jp.clone();
                let c2 = catalog_jp.clone();
                // CG
                if let Some(catalog) = c1 {
                    cg::run_jp(catalog).await.unwrap();
                } else {
                    cg::run_en().await.unwrap();
                }

                // Catalog
                if let Some(catalog) = c2 {
                    catalog::run_jp(catalog).await.unwrap();
                } else {
                    // catalog::run_en().await.unwrap();
                }

                // Live2D
                // Table
            }
            Update::CG => {
                if let Some(catalog) = catalog_jp {
                    cg::run_jp(catalog).await.unwrap();
                } else {
                    cg::run_en().await.unwrap();
                }
            }
            Update::Catalog => {
                if let Some(catalog) = catalog_jp {
                    catalog::run_jp(catalog).await.unwrap();
                }
            }
            Update::Live2D => {
                println!("TODO: Implement live2d")
            }
            Update::Table => {
                println!("TODO: Implement table")
            }
        },
    };
}
