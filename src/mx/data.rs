pub mod table_encryption_service {
    use crate::mx::core::service::xxhash_service;
    use anyhow::Result;
    use base64::{engine::general_purpose, Engine};
    use rand_mt::{Mt, Mt19937GenRand32};

    fn gen_int31(rng: &mut Mt19937GenRand32) -> u32 {
        rng.next_u32() >> 1
    }
    fn next_bytes(rng: &mut Mt19937GenRand32, buf: &mut [u8]) {
        for i in 0..buf.len() / 4 {
            let num = gen_int31(rng);
            buf[i * 4] = (num & 0xFF) as u8;
            buf[i * 4 + 1] = ((num >> 8) & 0xFF) as u8;
            buf[i * 4 + 2] = ((num >> 16) & 0xFF) as u8;
            buf[i * 4 + 3] = ((num >> 24) & 0xFF) as u8;
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
