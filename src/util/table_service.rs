use std::io::{Cursor, Read};

use base64::{engine::general_purpose, Engine};
use rand_mt::Mt;
use zip::ZipArchive;

use crate::mx::{core::service::xxhash_service::calculate_hash, data::table_encryption_service};

pub struct TableZipFile {
    archive: ZipArchive<Cursor<Vec<u8>>>,
    password: String,
}

impl TableZipFile {
    pub fn new<S: AsRef<str>>(buf: Vec<u8>, filename: S) -> Self {
        let hash = calculate_hash(filename.as_ref().as_bytes());
        let mut rng = Mt::new(hash);
        let mut next_buf = [0u8; 15];
        table_encryption_service::next_bytes(&mut rng, &mut next_buf);
        let password = general_purpose::STANDARD.encode(&next_buf);
        let archive = ZipArchive::new(Cursor::new(buf)).unwrap();
        Self { archive, password }
    }
    pub fn get_by_name<S: AsRef<str>>(&mut self, name: S) -> Vec<u8> {
        let mut file = self
            .archive
            .by_name_decrypt(name.as_ref(), self.password.as_bytes())
            .unwrap();
        let mut buf = Vec::new();
        file.read_to_end(&mut buf).unwrap();
        buf
    }
    #[allow(dead_code)]
    pub fn iter(&mut self) -> impl Iterator<Item = &str> {
        self.archive.file_names()
    }
}
