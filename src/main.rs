mod api;
mod app;
mod catalog;
mod cg;
mod mx;
mod util;

extern crate pretty_env_logger;
#[macro_use]
extern crate log;

use std::path::PathBuf;

use api::jp::{game_main_config, AddressableCatalog};
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

    pretty_env_logger::formatted_builder()
        .filter_level(log::LevelFilter::Info)
        .init();

    let region = cli.region;

    match region {
        Region::JP => {
            info!("Using JP region");
            if let Err(e) = app::jp::download().await {
                error!("{}", e);
            }
            if let Err(e) = app::jp::extract() {
                error!("{}", e);
            }

            info!("Finding GameMainConfig");
            let game_main_config = match app::jp::get_game_main_config() {
                Ok(bytes) => bytes,
                Err(e) => {
                    error!("Failed to get GameMainConfig: {}", e);
                    return;
                }
            };

            info!("Parsing GameMainConfig");
            let game_main_config =
                match api::jp::game_main_config::GameMainConfig::from_bytes(&game_main_config) {
                    Ok(game_main_config) => game_main_config,
                    Err(e) => {
                        error!("Failed to parse GameMainConfig: {}", e);
                        return;
                    }
                };

            // Save GameMainConfig
            info!("Saving GameMainConfig");
            util::save_json(
                PathBuf::from("public/data/jp/GameMainConfig.json"),
                &game_main_config,
            )
            .await
            .unwrap();

            info!("Requesting AddressableCatalog");
            let catalog = match api::jp::get_addressable_catalog(
                &game_main_config.server_info_data_url,
            )
            .await
            {
                Ok(catalog) => catalog,
                Err(e) => {
                    error!("Failed to get AddressableCatalog: {}", e);
                    return;
                }
            };
            jp(catalog, cli.action).await;
        }
        _ => {
            info!("Using EN region");
            en();
        }
    }
}

async fn jp(catalog: AddressableCatalog, action: Action) {
    match action {
        Action::Update { name } => match name {
            Update::All => {
                let c1 = catalog.clone();
                let c2 = catalog.clone();
                // CG
                cg::run_jp(c1).await.unwrap();

                // Catalog
                catalog::run_jp(c2).await.unwrap();

                // Live2D
                // Table
            }
            Update::CG => {
                cg::run_jp(catalog).await.unwrap();
            }
            Update::Catalog => {
                catalog::run_jp(catalog).await.unwrap();
            }
            Update::Live2D => {
                error!("TODO: Implement live2d")
            }
            Update::Table => {
                error!("TODO: Implement table")
            }
        },
    };
}

fn en() {
    error!("EN region not supported yet");
}
