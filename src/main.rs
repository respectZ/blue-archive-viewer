mod api;
mod app;
mod catalog;
mod cg;
mod flatbuffers;
mod live2d;
mod mx;
mod table_dumper;
mod util;

#[macro_use]
mod logger;

use clap::{Parser, Subcommand};
use std::path::PathBuf;
use util::{save_file, save_json};

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

    match region {
        Region::JP => {
            info!("Using JP region");

            jp(cli.action).await;
        }
        _ => {
            info!("Using EN region");
            en(cli.action).await;
        }
    }
}

async fn jp(action: Action) {
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
    save_json(
        PathBuf::from("public/data/jp/GameMainConfig.json"),
        &game_main_config,
    )
    .await
    .unwrap();

    info!("Requesting AddressableCatalog");
    let catalog =
        match api::jp::get_addressable_catalog(&game_main_config.server_info_data_url).await {
            Ok(catalog) => catalog,
            Err(e) => {
                error!("Failed to get AddressableCatalog: {}", e);
                return;
            }
        };
    save_json(
        PathBuf::from("public/data/jp/AddressableCatalog.json"),
        &catalog,
    )
    .await
    .unwrap();
    // Save version as txt
    save_file(
        PathBuf::from("public/data/jp/version.txt"),
        catalog.get_version().as_bytes(),
    )
    .await
    .unwrap();
    // Update url
    info!("Updating URL");

    let url_tsx_path = PathBuf::from("app/jp/url.tsx");
    let url = game_main_config.server_info_data_url;
    let addressable_catalog = catalog.get_addressable_catalog_url_root();
    let data = format!(
        "export const URL = \"{}\";\nexport const AddressablesCatalogUrlRoot = \"{}\";",
        url, addressable_catalog
    );
    save_file(url_tsx_path, data.as_bytes()).await.unwrap();

    match action {
        Action::Update { name } => match name {
            Update::All => {
                cg::run_jp(&catalog).await.unwrap();
                catalog::run_jp(&catalog).await.unwrap();
                live2d::run_jp(&catalog).await.unwrap();
                table_dumper::jp::run(&catalog).await.unwrap();
            }
            Update::CG => {
                cg::run_jp(&catalog).await.unwrap();
            }
            Update::Catalog => {
                catalog::run_jp(&catalog).await.unwrap();
            }
            Update::Live2D => {
                live2d::run_jp(&catalog).await.unwrap();
            }
            Update::Table => {
                table_dumper::jp::run(&catalog).await.unwrap();
            }
        },
    };
}

async fn en(action: Action) {
    info!("Requesting AddressableCatalog");
    let addressable_catalog = api::en::common::get_addressable_catalog().await.unwrap();
    save_json(
        "public/data/en/AddressableCatalog.json",
        &addressable_catalog,
    )
    .await
    .unwrap();
    info!("Version: {}", addressable_catalog.latest_build_version);
    // Save version as txt
    save_file(
        "public/data/en/version.txt",
        addressable_catalog.latest_build_version.as_bytes(),
    )
    .await
    .unwrap();
    info!("Requesting Catalog");
    let catalog = addressable_catalog.get_catalog().await.unwrap();
    catalog.save("public/data/en/").await.unwrap();
    match action {
        Action::Update { name } => match name {
            Update::All => {
                cg::run_en(&catalog).await.unwrap();
                catalog::run_en(&catalog).await.unwrap();
                table_dumper::en::run(&catalog).await.unwrap();
                live2d::run_en(catalog.clone()).await.unwrap();
            }
            Update::CG => {
                cg::run_en(&catalog).await.unwrap();
            }
            Update::Catalog => {
                catalog::run_en(&catalog).await.unwrap();
            }
            Update::Live2D => {
                live2d::run_en(catalog).await.unwrap();
            }
            Update::Table => {
                table_dumper::en::run(&catalog).await.unwrap();
            }
        },
    };
}
