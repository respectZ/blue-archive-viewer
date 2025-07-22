use crate::flatbuffers::en::AcademyFavorScheduleExcel;
use crate::info;
use crate::util::compare_crc;
use crate::{
    api::jp::{table_catalog::TableCatalog, AddressableCatalog},
    flatbuffers::{
        jp::{
            CharacterDialogExcel, CharacterExcelTable, LocalizeCharProfileExcelTable,
            MemoryLobbyExcel,
        },
        DecryptAndDump,
    },
    mx::data::table_encryption_service::xor,
    util::{save_file, save_json_pretty, table_service::TableZipFile},
};
use anyhow::Result;
use sqlite::{self, State};
use std::{fs, path::PathBuf};

static PUBLIC_PATH: &str = "./public/data/jp/";
static PUBLIC_EXCEL_PATH: &str = "./public/data/jp/TableBundles/Excel/";
// Removed from public because it is too large. ([JP] 1.59.359309)
static PUBLIC_EXCEL_DB_PATH: &str = "./temp/jp/TableBundles/ExcelDB.db";
static TEMP_EXCEL_ZIP_PATH: &str = "./temp/jp/TableBundles/Excel.zip";
static TEMP_PATH: &str = "./temp/jp/";

pub async fn run(catalog: &AddressableCatalog) -> Result<()> {
    info!("Running table dumper");

    let table_catalog = catalog.get_table_catalog().await?;
    get_excel_db(&table_catalog).await?;

    get_excel_zip(&table_catalog).await?;
    extract_excel_zip().await?;

    let excel_path = PathBuf::from(PUBLIC_EXCEL_PATH);

    info!("Dumping AcademyFavorScheduleExcelTable");
    let academy_favor_schedule_excel_table = get_academy_favor_schedule_excel_table()?;
    let academy_favor_schedule_excel_table = academy_favor_schedule_excel_table
        .iter()
        .map(|x| flatbuffers::root::<AcademyFavorScheduleExcel>(x).unwrap())
        .collect::<Vec<AcademyFavorScheduleExcel>>();
    save_json_pretty(
        excel_path
            .clone()
            .join("AcademyFavorScheduleExcelTable.json"),
        &academy_favor_schedule_excel_table,
    )
    .await?;

    info!("Dumping CharacterDialogExcelTable");
    let character_dialog_table = get_character_dialog_table()?;
    let character_dialog_table = character_dialog_table
        .iter()
        .map(|x| flatbuffers::root::<CharacterDialogExcel>(x).unwrap())
        .collect::<Vec<CharacterDialogExcel>>();
    save_json_pretty(
        excel_path.clone().join("CharacterDialogExcelTable.json"),
        &character_dialog_table,
    )
    .await?;

    info!("Dumping MemoryLobbyExcelTable");
    let memory_lobby_excel_table = get_memory_lobby_excel_table()?;
    let memory_lobby_excel_table = memory_lobby_excel_table
        .iter()
        .map(|x| flatbuffers::root::<MemoryLobbyExcel>(x).unwrap())
        .collect::<Vec<MemoryLobbyExcel>>();
    save_json_pretty(
        excel_path.clone().join("MemoryLobbyExcelTable.json"),
        &memory_lobby_excel_table,
    )
    .await?;

    Ok(())
}

fn get_character_dialog_table() -> Result<Vec<Vec<u8>>> {
    let conn = sqlite::open(PUBLIC_EXCEL_DB_PATH)?;
    let mut stmt = conn.prepare("SELECT Bytes FROM CharacterDialogDBSchema")?;
    let mut data = Vec::new();
    while let Ok(State::Row) = stmt.next() {
        data.push(stmt.read::<Vec<u8>, _>(0)?);
    }

    Ok(data)
}

fn get_memory_lobby_excel_table() -> Result<Vec<Vec<u8>>> {
    let conn = sqlite::open(PUBLIC_EXCEL_DB_PATH)?;
    let mut stmt = conn.prepare("SELECT Bytes FROM MemoryLobbyDBSchema")?;
    let mut data = Vec::new();
    while let Ok(State::Row) = stmt.next() {
        data.push(stmt.read::<Vec<u8>, _>(0)?);
    }

    Ok(data)
}

fn get_academy_favor_schedule_excel_table() -> Result<Vec<Vec<u8>>> {
    let conn = sqlite::open(PUBLIC_EXCEL_DB_PATH)?;
    let mut stmt = conn.prepare("SELECT Bytes FROM AcademyFavorScheduleDBSchema")?;
    let mut data = Vec::new();
    while let Ok(State::Row) = stmt.next() {
        data.push(stmt.read::<Vec<u8>, _>(0)?);
    }

    Ok(data)
}

async fn get_excel_db(table_catalog: &TableCatalog) -> Result<()> {
    // Compare excel db crc
    let excel_db = table_catalog
        .get_tables()
        .await
        .into_iter()
        .find(|table| table.name == "ExcelDB.db")
        .unwrap();

    match compare_crc(PUBLIC_EXCEL_DB_PATH, excel_db.crc as u32).await {
        Ok(true) => return Ok(()),
        Ok(false) => {
            fs::remove_file(PUBLIC_EXCEL_DB_PATH)?;
        }
        _ => {}
    }

    info!("Downloading ExcelDB.db");
    table_catalog
        .save_tables(PathBuf::from(PUBLIC_PATH), |table| {
            table.name == "ExcelDB.db"
        })
        .await?;
    Ok(())
}

async fn get_excel_zip(table_catalog: &TableCatalog) -> Result<()> {
    // Compare Excel.zip crc
    let excel_zip = table_catalog
        .get_tables()
        .await
        .into_iter()
        .find(|table| table.name == "Excel.zip")
        .unwrap();

    match compare_crc(TEMP_EXCEL_ZIP_PATH, excel_zip.crc as u32).await {
        Ok(true) => return Ok(()),
        Ok(false) => {
            fs::remove_file(TEMP_EXCEL_ZIP_PATH)?;
        }
        _ => {}
    }

    info!("Downloading Excel.zip");
    table_catalog
        .save_tables(TEMP_PATH, |table| table.name == "Excel.zip")
        .await?;
    Ok(())
}
async fn extract_excel_zip() -> Result<()> {
    info!("Extracting Excel.zip");
    let path = PathBuf::from(TEMP_EXCEL_ZIP_PATH);
    let excel_path = PathBuf::from(PUBLIC_EXCEL_PATH);
    let buf = fs::read(path.clone())?;
    let filename = path
        .clone()
        .file_name()
        .unwrap()
        .to_str()
        .unwrap()
        .to_string();
    let mut zip = TableZipFile::new(buf, filename);

    info!("Decrypting and dumping CharacterExcelTable");
    let data = zip.get_by_name("characterexceltable.bytes");
    let data = xor("CharacterExcelTable", &data);
    let mut character = flatbuffers::root::<CharacterExcelTable>(&data)?;
    save_file(
        excel_path.clone().join("CharacterExcelTable.json"),
        character.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping LocalizeCharProfileExcelTable");
    let data = zip.get_by_name("localizecharprofileexceltable.bytes");
    let data = xor("LocalizeCharProfileExcelTable", &data);
    let mut localize_char_profile = flatbuffers::root::<LocalizeCharProfileExcelTable>(&data)?;
    save_file(
        excel_path
            .clone()
            .join("LocalizeCharProfileExcelTable.json"),
        localize_char_profile.decrypt_dump_json().as_bytes(),
    )
    .await?;

    Ok(())
}
