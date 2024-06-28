use anyhow::Result;
use byteorder::{LittleEndian, ReadBytesExt};
use std::io::{Cursor, Read};

pub fn read_string(cursor: &mut Cursor<&[u8]>) -> Result<String> {
    let length = read_i32(cursor)? as usize;
    let mut buffer = vec![0; length];
    cursor.read_exact(&mut buffer).ok();
    Ok(String::from_utf8(buffer).expect("Invalid UTF-8 sequence"))
}

pub fn read_bool(cursor: &mut Cursor<&[u8]>) -> Result<bool> {
    Ok(cursor.read_u8()? == 1)
}

pub fn read_i8(cursor: &mut Cursor<&[u8]>) -> Result<i8> {
    Ok(cursor.read_i8()?)
}

#[allow(dead_code)]
pub fn read_i16(cursor: &mut Cursor<&[u8]>) -> Result<i16> {
    Ok(cursor.read_i16::<LittleEndian>()?)
}

pub fn read_i32(cursor: &mut Cursor<&[u8]>) -> Result<i32> {
    Ok(cursor.read_i32::<LittleEndian>()?)
}

pub fn read_i64(cursor: &mut Cursor<&[u8]>) -> Result<i64> {
    Ok(cursor.read_i64::<LittleEndian>()?)
}
