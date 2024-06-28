use crate::api::en::catalog::Catalog;
use crate::flatbuffers::en::CharacterDialogExcelTable;
use crate::info;
use crate::util::compare_hash;
use crate::{
    flatbuffers::{
        en::{
            AcademyFavorScheduleExcelTable, CharacterExcelTable, LocalizeCharProfileExcelTable,
            MemoryLobbyExcelTable,
        },
        DecryptAndDump,
    },
    mx::data::table_encryption_service::xor,
    util::{save_file, table_service::TableZipFile},
};
use anyhow::Result;
use std::{fs, path::PathBuf};

static PUBLIC_EXCEL_PATH: &str = "./public/data/en/Preload/TableBundles/Excel/";
static TEMP_EXCEL_ZIP_PATH: &str = "./temp/en/Preload/TableBundles/Excel.zip";
static TEMP_PATH: &str = "./temp/en/";

pub async fn run(catalog: &Catalog) -> Result<()> {
    info!("Running table dumper");
    get_excel_zip(catalog).await?;
    extract_excel_zip().await?;
    Ok(())
}

async fn get_excel_zip(catalog: &Catalog) -> Result<()> {
    let base_url = catalog.get_base_url();
    // Compare Excel.zip hash
    let excel_zip = catalog
        .resources
        .clone()
        .into_iter()
        .find(|r| r.resource_path.ends_with("Excel.zip"))
        .unwrap();
    match compare_hash(TEMP_EXCEL_ZIP_PATH, &excel_zip.resource_hash).await {
        Ok(true) => return Ok(()),
        Ok(false) => {
            fs::remove_file(TEMP_EXCEL_ZIP_PATH)?;
        }
        _ => {}
    }

    info!("Downloading Excel.zip");
    excel_zip.save(TEMP_PATH, base_url).await?;
    Ok(())
}

async fn extract_excel_zip() -> Result<()> {
    info!("Extracting Excel.zip");
    let excel_path = PathBuf::from(PUBLIC_EXCEL_PATH);
    let buf = fs::read(TEMP_EXCEL_ZIP_PATH)?;
    let filename = PathBuf::from(TEMP_EXCEL_ZIP_PATH)
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
        excel_path.join("AcademyFavorScheduleExcelTable.json"),
        academy_favor.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping CharacterDialogExcelTable");
    let data = zip.get_by_name("characterdialogexceltable.bytes");
    let data = xor("CharacterDialogExcelTable", &data);
    let mut character_dialog = flatbuffers::root::<CharacterDialogExcelTable>(&data)?;
    save_file(
        excel_path.join("CharacterDialogExcelTable.json"),
        character_dialog.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping CharacterExcelTable");
    let data = zip.get_by_name("characterexceltable.bytes");
    let data = xor("CharacterExcelTable", &data);
    let mut character = flatbuffers::root::<CharacterExcelTable>(&data)?;
    save_file(
        excel_path.join("CharacterExcelTable.json"),
        character.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping LocalizeCharProfileExcelTable");
    let data = zip.get_by_name("localizecharprofileexceltable.bytes");
    let data = xor("LocalizeCharProfileExcelTable", &data);
    let mut localize_char_profile = flatbuffers::root::<LocalizeCharProfileExcelTable>(&data)?;
    save_file(
        excel_path.join("LocalizeCharProfileExcelTable.json"),
        localize_char_profile.decrypt_dump_json().as_bytes(),
    )
    .await?;

    info!("Decrypting and dumping MemoryLobbyExcelTable");
    let data = zip.get_by_name("memorylobbyexceltable.bytes");
    let data = xor("MemoryLobbyExcelTable", &data);
    let mut memory_lobby = flatbuffers::root::<MemoryLobbyExcelTable>(&data)?;
    save_file(
        excel_path.join("MemoryLobbyExcelTable.json"),
        memory_lobby.decrypt_dump_json().as_bytes(),
    )
    .await?;

    Ok(())
}
