pub mod xxhash_service {
    use xxhash_rust::xxh32::Xxh32;
    pub fn calculate_hash(bytes: &[u8]) -> u32 {
        let mut hasher = Xxh32::new(0);
        hasher.update(bytes);
        hasher.digest()
    }
}
