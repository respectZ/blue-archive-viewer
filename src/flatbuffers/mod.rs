#[allow(dead_code, unused_imports)]
#[path = "./en_generated.rs"]
mod en_generated;
mod en_impl;
#[allow(dead_code, unused_imports)]
#[path = "./jp_generated.rs"]
mod jp_generated;
mod jp_impl;

pub trait DecryptAndDump {
    fn decrypt_dump_json(&mut self) -> String;
}

macro_rules! impl_serialize_for_enum_with_variant_name {
    ($enum_type:ty) => {
        impl Serialize for $enum_type {
            fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
            where
                S: serde::Serializer,
            {
                match self.variant_name() {
                    Some(variant_name) => variant_name.serialize(serializer),
                    None => {
                        println!("Failed to get variant name for {:?}", self);
                        // Return UNKNOWN
                        "UNKNOWN".serialize(serializer)
                    }
                }
            }
        }
    };
}

pub(super) use impl_serialize_for_enum_with_variant_name;

pub use en_generated::*;
pub use jp_generated::*;
