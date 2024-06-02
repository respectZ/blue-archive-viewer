pub mod table_encryption_service {
    use crate::mx::core::service::xxhash_service;
    use anyhow::Result;
    use base64::{engine::general_purpose, Engine};
    use byteorder::{ByteOrder, LittleEndian};
    use rand_mt::{Mt, Mt19937GenRand32};
    use std::convert::TryInto;

    fn gen_int31(rng: &mut Mt19937GenRand32) -> u32 {
        rng.next_u32() >> 1
    }
    pub fn next_bytes(rng: &mut Mt19937GenRand32, buf: &mut [u8]) {
        // // ceil make sure we fill the buf with 4 bytes
        // let len = (buf.len() + 3) / 4;
        // for i in 0..len {
        //     let num = gen_int31(rng);
        //     let offset = i * 4;
        //     buf[offset] = (num & 0xFF) as u8;
        //     if offset + 1 >= buf.len() {
        //         break;
        //     }
        //     buf[offset + 1] = ((num >> 8) & 0xFF) as u8;
        //     if offset + 2 >= buf.len() {
        //         break;
        //     }
        //     buf[offset + 2] = ((num >> 16) & 0xFF) as u8;
        //     if offset + 3 >= buf.len() {
        //         break;
        //     }
        //     buf[offset + 3] = ((num >> 24) & 0xFF) as u8;
        // }
        let len = (buf.len() + 3) / 4;
        for i in 0..len {
            let num = gen_int31(rng);
            let offset = i * 4;
            let end = (offset + 4).min(buf.len());
            let chunk = &mut buf[offset..end];
            for (j, x) in chunk.iter_mut().enumerate() {
                *x = ((num >> (j * 8)) & 0xFF) as u8;
            }
        }
    }
    fn strxor(value: &[u8], key: &[u8]) -> Vec<u8> {
        value.iter().zip(key.iter()).map(|(a, b)| a ^ b).collect()
    }
    fn _xor(value: &mut [u8], key: &[u8]) -> Vec<u8> {
        if value.len() == key.len() {
            strxor(value, key)
        } else if value.len() < key.len() {
            strxor(value, &key[..value.len()])
        } else {
            let mut result = Vec::new();
            for i in (0..value.len() - key.len() + 1).step_by(key.len()) {
                result.extend(strxor(&value[i..i + key.len()], key));
            }
            result.extend(strxor(
                &value[value.len() - (value.len() % key.len())..],
                &key[..value.len() % key.len()],
            ));
            result
        }
    }
    pub fn xor(name: &str, data: &[u8]) -> Vec<u8> {
        let seed = xxhash_service::calculate_hash(name.as_bytes());
        let mut rng = Mt::new(seed);
        let mut key = vec![0u8; data.len()];
        next_bytes(&mut rng, &mut key);
        _xor(&mut key, data)
    }

    pub fn xor_bytes(value: &[u8], key: &[u8]) -> Vec<u8> {
        value
            .iter()
            .zip(key.iter().cycle())
            .map(|(v, k)| v ^ k)
            .collect()
    }

    pub fn xor_int32(value: i32, key: &[u8]) -> i32 {
        let mut bytes = [0u8; 4];
        LittleEndian::write_i32(&mut bytes, value);
        let xored_bytes = xor_bytes(&bytes, key);
        LittleEndian::read_i32(&xored_bytes)
    }

    pub fn xor_int64(value: i64, key: &[u8]) -> i64 {
        let mut bytes = [0u8; 8];
        LittleEndian::write_i64(&mut bytes, value);
        let xored_bytes = xor_bytes(&bytes, key);
        LittleEndian::read_i64(&xored_bytes)
    }

    pub fn xor_uint32(value: u32, key: &[u8]) -> u32 {
        let mut bytes = [0u8; 4];
        LittleEndian::write_u32(&mut bytes, value);
        let xored_bytes = xor_bytes(&bytes, key);
        LittleEndian::read_u32(&xored_bytes)
    }

    pub fn xor_uint64(value: u64, key: &[u8]) -> u64 {
        let mut bytes = [0u8; 8];
        LittleEndian::write_u64(&mut bytes, value);
        let xored_bytes = xor_bytes(&bytes, key);
        LittleEndian::read_u64(&xored_bytes)
    }

    pub fn convert_int(value: i32, key: &[u8]) -> i32 {
        if value != 0 {
            xor_int32(value, key)
        } else {
            0
        }
    }

    pub fn convert_long(value: i64, key: &[u8]) -> i64 {
        if value != 0 {
            xor_int64(value, key)
        } else {
            0
        }
    }

    pub fn convert_uint(value: u32, key: &[u8]) -> u32 {
        if value != 0 {
            xor_uint32(value, key)
        } else {
            0
        }
    }

    pub fn convert_ulong(value: u64, key: &[u8]) -> u64 {
        if value != 0 {
            xor_uint64(value, key)
        } else {
            0
        }
    }

    pub fn convert_float(value: f32, key: &[u8]) -> f32 {
        if value != 0.0 {
            (convert_int(value as i32, key) as f32) * 0.00001
        } else {
            0.0
        }
    }

    pub fn convert_double(value: f64, key: &[u8]) -> f64 {
        if value != 0.0 {
            (convert_long(value as i64, key) as f64) * 0.00001
        } else {
            0.0
        }
    }

    pub fn create_key(bytes: &[u8]) -> [u8; 8] {
        let seed = xxhash_service::calculate_hash(bytes);
        let mut rng = Mt::new(seed);
        let mut buf = [0u8; 8];
        next_bytes(&mut rng, &mut buf);
        buf
    }
    pub fn convert_string(value: &str, key: &[u8]) -> Result<String> {
        let mut raw = general_purpose::STANDARD.decode(value.as_bytes())?;
        let bytes = self::_xor(&mut raw, key);
        let utf16_bytes = bytes
            .chunks_exact(2)
            .map(|x| u16::from_le_bytes([x[0], x[1]]))
            .collect::<Vec<u16>>();
        match String::from_utf16(&utf16_bytes) {
            Ok(s) => Ok(s),
            Err(_) => Ok(bytes.iter().map(|x| *x as char).collect::<String>()),
        }
    }
    pub fn new_encrypt_string(value: &str, key: &[u8]) -> Result<String> {
        if value.is_empty() || value.len() < 8 {
            return Ok(value.to_string());
        }
        let mut raw = value
            .encode_utf16()
            .flat_map(|x| x.to_le_bytes())
            .collect::<Vec<u8>>();
        let xor = self::_xor(&mut raw, key);
        Ok(general_purpose::STANDARD.encode(&xor))
    }
}
