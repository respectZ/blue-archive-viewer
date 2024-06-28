use anyhow::{bail, Result};
use astc_decode::{astc_decode, Footprint};
use image::{DynamicImage, ImageBuffer};
use num_enum::FromPrimitive;
use std::{fs, path::Path};
use unity_rs::{classes::Texture2D, Env};

use super::{save_file, save_image};

#[allow(non_camel_case_types, non_upper_case_globals)]
#[derive(Debug, Eq, PartialEq, FromPrimitive, Clone, Copy)]
#[repr(i32)]
enum TextureFormat {
    #[num_enum(default)]
    UnknownType = -1,
    ASTC_RGB_4x4 = 48,
    ASTC_RGB_5x5,
    ASTC_RGB_6x6,
    ASTC_RGB_8x8,
    ASTC_RGB_10x10,
    ASTC_RGB_12x12,
}

pub fn read_file<P: AsRef<Path>>(path: P) -> Result<Env> {
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

pub async fn extract_images<P: AsRef<Path>>(env: &Env, path: P) -> Result<()> {
    for obj in env.objects() {
        match obj.class() {
            unity_rs::ClassID::Texture2D => {
                let s: Texture2D = obj.read().unwrap();
                let format = TextureFormat::from(s.format as i32);
                let footprint = match format {
                    TextureFormat::ASTC_RGB_4x4 => Some(Footprint::ASTC_4X4),
                    TextureFormat::ASTC_RGB_5x5 => Some(Footprint::ASTC_5X5),
                    TextureFormat::ASTC_RGB_6x6 => Some(Footprint::ASTC_6X6),
                    TextureFormat::ASTC_RGB_8x8 => Some(Footprint::ASTC_8X8),
                    TextureFormat::ASTC_RGB_10x10 => Some(Footprint::ASTC_10X10),
                    TextureFormat::ASTC_RGB_12x12 => Some(Footprint::ASTC_12X12),
                    _ => {
                        bail!("Unsupported texture format: {:?}", format);
                    }
                }
                .unwrap();
                let image = decode_astc_rgb(&s.data, s.width as u32, s.height as u32, footprint)?;
                let path = path.as_ref().join(format!("{}.png", s.name));
                save_image(path, image).await?;
            }
            _ => {}
        }
    }
    Ok(())
}

pub async fn extract_live2d<P: AsRef<Path>>(env: &Env, path: P) -> Result<()> {
    for obj in env.objects() {
        match obj.class() {
            unity_rs::ClassID::TextAsset => {
                let s: unity_rs::classes::TextAsset = obj.read().unwrap();
                save_file(path.as_ref().join(s.name), &s.script).await?;
            }
            _ => {}
        }
    }
    Ok(())
}
