use anyhow::Result;
use astc_decode::{astc_decode, Footprint};
use image::{io::Reader as ImageReader, DynamicImage, ImageBuffer, ImageFormat};
use io_unity::unity_asset_view::UnityAssetViewer;
use std::{
    fs::{self, File, OpenOptions},
    io::BufReader,
    path::PathBuf,
};
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

pub fn read_file(path: PathBuf) -> Result<Env> {
    // Open file into bytes
    let bytes = fs::read(path)?;
    // Convert to &[u8]
    let bytes = bytes.as_slice();
    let mut env = Env::new();
    env.load_from_slice(bytes)?;
    Ok(env)
}

pub fn decode_astc_rgb(data: &[u8], w: u32, h: u32, footprint: Footprint) -> Result<DynamicImage> {
    let mut output = vec![0; (w * h * 4) as usize];
    astc_decode(&data[..], w, h, footprint, |x, y, color| {
        let offset = (y * w + x) as usize * 4;
        output[offset] = color[0];
        output[offset + 1] = color[1];
        output[offset + 2] = color[2];
        output[offset + 3] = color[3];
    })?;
    let image = DynamicImage::ImageRgba8(ImageBuffer::from_vec(w, h, output).unwrap());
    // Filp vertically
    let image = image.flipv();
    Ok(image)
}
