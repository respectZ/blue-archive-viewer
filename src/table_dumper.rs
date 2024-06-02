use crate::info;
use crate::{
    api::jp::{table_catalog::TableCatalog, AddressableCatalog},
    flatbuffers::{
        jp::{
            AcademyFavorScheduleExcelTable, CharacterDialogExcel, CharacterExcelTable,
            LocalizeCharProfileExcelTable, MemoryLobbyExcel,
        },
        DecryptAndDump,
    },
    mx::data::table_encryption_service::xor,
    util::{save_file, save_json_pretty, table_service::TableZipFile},
};
use anyhow::Result;
use sqlite::{self, State};
use std::{fs, path::PathBuf};

pub async fn run_jp(catalog: AddressableCatalog) -> Result<()> {
    info!("Running table dumper");

    let table_catalog = catalog.get_table_catalog().await?;
    get_excel_db(table_catalog.clone()).await?;

    get_excel_zip(table_catalog.clone()).await?;
    extract_excel_zip().await?;

    let excel_path = PathBuf::from("./public/data/jp/TableBundles/Excel/");

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

pub fn get_character_dialog_table() -> Result<Vec<Vec<u8>>> {
    let conn = sqlite::open("./public/data/jp/TableBundles/ExcelDB.db")?;
    let mut stmt = conn.prepare("SELECT Bytes FROM CharacterDialogDBSchema")?;
    let mut data = Vec::new();
    while let Ok(State::Row) = stmt.next() {
        data.push(stmt.read::<Vec<u8>, _>(0)?);
    }

    Ok(data)
}

pub fn get_memory_lobby_excel_table() -> Result<Vec<Vec<u8>>> {
    let conn = sqlite::open("./public/data/jp/TableBundles/ExcelDB.db")?;
    let mut stmt = conn.prepare("SELECT Bytes FROM MemoryLobbyDBSchema")?;
    let mut data = Vec::new();
    while let Ok(State::Row) = stmt.next() {
        data.push(stmt.read::<Vec<u8>, _>(0)?);
    }

    Ok(data)
}

async fn get_excel_db(table_catalog: TableCatalog) -> Result<()> {
    let path = PathBuf::from("./public/data/jp/TableBundles/Excel/ExcelDB.db");
    // Get metadata
    let metadata = match fs::metadata(path.clone()) {
        Ok(metadata) => metadata.len(),
        Err(_) => 0,
    };
    // Compare excel db size
    let excel_db = table_catalog
        .get_tables()
        .await
        .into_iter()
        .find(|table| table.name == "ExcelDB.db")
        .unwrap();
    if metadata == excel_db.size as u64 {
        return Ok(());
    }

    info!("Downloading ExcelDB.db");
    table_catalog
        .save_tables(PathBuf::from("./public/data/jp/"), |table| {
            table.name == "ExcelDB.db"
        })
        .await?;
    Ok(())
}

async fn get_excel_zip(table_catalog: TableCatalog) -> Result<()> {
    let path = PathBuf::from("./temp/jp/");
    let metadata = match fs::metadata(path.clone().join("TableBundles/Excel.zip")) {
        Ok(metadata) => metadata.len(),
        Err(_) => 0,
    };
    // Compare excel zip size
    let excel_zip = table_catalog
        .get_tables()
        .await
        .into_iter()
        .find(|table| table.name == "Excel.zip")
        .unwrap();
    if metadata == excel_zip.size as u64 {
        return Ok(());
    }
    info!("Downloading Excel.zip");
    table_catalog
        .save_tables(path.clone(), |table| table.name == "Excel.zip")
        .await?;
    Ok(())
}
async fn extract_excel_zip() -> Result<()> {
    info!("Extracting Excel.zip");
    let path = PathBuf::from("./temp/jp/TableBundles/Excel.zip");
    let excel_path = PathBuf::from("./public/data/jp/TableBundles/Excel/");
    let buf = fs::read(path.clone())?;
    let filename = path
        .clone()
        .file_name()
        .unwrap()
        .to_str()
        .unwrap()
        .to_string();
    let mut zip = TableZipFile::new(buf, filename);

    info!("Decrypting and dumping AcademyFavorScheduleExcelTable");
    let data = zip.get_by_name("academyfavorscheduleexceltable.bytes");
    let data = xor("AcademyFavorScheduleExcelTable", &data);
    let mut academy_favor = flatbuffers::root::<AcademyFavorScheduleExcelTable>(&data)?;
    save_file(
        excel_path
            .clone()
            .join("AcademyFavorScheduleExcelTable.json"),
        academy_favor.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping CharacterExcelTable");
    let data = zip.get_by_name("characterexceltable.bytes");
    let data = xor("CharacterExcelTable", &data);
    save_file(excel_path.clone().join("CharacterExcelTable.bytes"), &data).await?;
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
