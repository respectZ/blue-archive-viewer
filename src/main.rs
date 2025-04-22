mod api;
mod app;
mod catalog;
mod cg;
mod consts;
mod flatbuffers;
mod live2d;
mod mx;
mod table_dumper;
mod util;
mod voice;

#[macro_use]
mod logger;

use anyhow::Result;
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

            if let Err(e) = jp(cli.action).await {
                error!("An error occured: {}", e)
            }
        }
        _ => {
            info!("Using EN region");
            if let Err(e) = en(cli.action).await {
                error!("An error occured: {}", e)
            }
        }
    }
}

async fn jp(action: Action) -> Result<()> {
    app::jp::download().await?;
    app::jp::extract()?;

    info!("Finding GameMainConfig");
    let game_main_config = app::jp::get_game_main_config()?;

    info!("Parsing GameMainConfig");
    let game_main_config =
        api::jp::game_main_config::GameMainConfig::from_bytes(&game_main_config)?;

    // Save GameMainConfig
    info!("Saving GameMainConfig");
    save_json(
        PathBuf::from("public/data/jp/GameMainConfig.json"),
        &game_main_config,
    )
    .await?;

    info!("Requesting AddressableCatalog");
    let catalog = api::jp::get_addressable_catalog(&game_main_config.server_info_data_url).await?;
    save_json(
        PathBuf::from("public/data/jp/AddressableCatalog.json"),
        &catalog,
    )
    .await?;
    // Update url
    info!("Updating URL");

    let url_tsx_path = PathBuf::from("app/jp/url.tsx");
    let url = game_main_config.server_info_data_url;
    let addressable_catalog = catalog.get_addressable_catalog_url_root();
    let data = format!(
        "export const URL = \"{}\";\nexport const AddressablesCatalogUrlRoot = \"{}\";",
        url, addressable_catalog
    );
    save_file(url_tsx_path, data.as_bytes()).await?;

    match action {
        Action::Update { name } => match name {
            Update::All => {
                cg::run_jp(&catalog).await?;
                catalog::run_jp(&catalog).await?;
                live2d::run_jp(&catalog).await?;
                voice::run_jp(&catalog).await?;
                table_dumper::jp::run(&catalog).await?;
            }
            Update::CG => {
                cg::run_jp(&catalog).await?;
            }
            Update::Catalog => {
                catalog::run_jp(&catalog).await?;
            }
            Update::Live2D => {
                live2d::run_jp(&catalog).await?;
                voice::run_jp(&catalog).await?;
            }
            Update::Table => {
                table_dumper::jp::run(&catalog).await?;
            }
        },
    };
    Ok(())
}

async fn en(action: Action) -> Result<()> {
    info!("Requesting AddressableCatalog");
    let addressable_catalog = api::en::common::get_addressable_catalog().await?;
    save_json(
        "public/data/en/AddressableCatalog.json",
        &addressable_catalog,
    )
    .await?;
    info!("Version: {}", addressable_catalog.latest_build_version);
    // Save version as txt
    save_file(
        "public/data/en/version.txt",
        addressable_catalog.latest_build_version.as_bytes(),
    )
    .await?;
    info!("Requesting Catalog");
    let catalog = addressable_catalog.get_catalog().await?;
    catalog.save("public/data/en/").await?;
    match action {
        Action::Update { name } => match name {
            Update::All => {
                cg::run_en(&catalog).await?;
                catalog::run_en(&catalog).await?;
                table_dumper::en::run(&catalog).await?;
                live2d::run_en(catalog.clone()).await?;
            }
            Update::CG => {
                cg::run_en(&catalog).await?;
            }
            Update::Catalog => {
                catalog::run_en(&catalog).await?;
            }
            Update::Live2D => {
                live2d::run_en(catalog).await?;
            }
            Update::Table => {
                table_dumper::en::run(&catalog).await?;
            }
        },
    };
    Ok(())
}
