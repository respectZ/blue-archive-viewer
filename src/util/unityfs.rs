use std::{
    fs::{self, File, OpenOptions},
    io::BufReader,
    path::PathBuf,
};

use anyhow::Result;
use io_unity::unity_asset_view::UnityAssetViewer;
use unity_rs::Env;

pub fn read_dir(dir: PathBuf) -> Result<()> {
    let mut viewer = UnityAssetViewer::new();
    // viewer.read_bundle_dir(dir).unwrap_or_else(|e| {
    //     error!("{}", e);
    // });
    // Walk
    let file = OpenOptions::new().read(true).open(dir)?;
    let file = Box::new(BufReader::new(file));
    viewer.add_bundle_file(Box::new(file), Some(".".to_owned()))?;

    // viewer.add_serialized_file(Box::new(BufReader::new(file)), Some(".".to_owned()))?;

    println!("Len: {}", viewer.serialized_file_map.len());

    for (_, sf) in viewer.serialized_file_map {
        for (path_id, obj) in sf.get_object_map() {
            println!("{}: {:?}", path_id, obj);
        }
    }
    Ok(())
}

pub fn read_serialized_file(path: PathBuf) -> Result<()> {
    let mut viewer = UnityAssetViewer::new();
    let file = OpenOptions::new().read(true).open(path)?;

    viewer.add_serialized_file(Box::new(BufReader::new(file)), Some(".".to_owned()))?;
    println!("Len: {}", viewer.serialized_file_map.len());
    for (_, sf) in viewer.serialized_file_map {
        for (path_id, obj) in sf.get_object_map() {
            println!("{}: {:?}", path_id, obj);
        }
    }
    Ok(())
}

pub fn read_file(path: PathBuf) -> Result<()> {
    // Open file into bytes
    let bytes = fs::read(path)?;
    // Convert to &[u8]
    let bytes = bytes.as_slice();
    let mut env = Env::new();
    env.load_from_slice(bytes)?;
    for obj in env.objects() {
        println!("{:?}", obj.class());
    }
    Ok(())
}
