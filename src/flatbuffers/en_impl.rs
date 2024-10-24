use super::en_generated::en::*;
use super::impl_serialize_for_enum_with_variant_name;
use super::DecryptAndDump;
use crate::mx::data::table_encryption_service::{
    convert_float, convert_int, convert_long, convert_string, convert_uint, create_key,
};
use serde::{
    ser::{SerializeSeq, SerializeStruct},
    Serialize,
};

impl_serialize_for_enum_with_variant_name!(ProductionStep);
impl_serialize_for_enum_with_variant_name!(DialogCategory);
impl_serialize_for_enum_with_variant_name!(DialogCondition);
impl_serialize_for_enum_with_variant_name!(Anniversary);
impl_serialize_for_enum_with_variant_name!(DialogType);
impl_serialize_for_enum_with_variant_name!(CVCollectionType);
impl_serialize_for_enum_with_variant_name!(ParcelType);
impl_serialize_for_enum_with_variant_name!(Rarity);
impl_serialize_for_enum_with_variant_name!(TacticEntityType);
impl_serialize_for_enum_with_variant_name!(TacticRole);
impl_serialize_for_enum_with_variant_name!(WeaponType);
impl_serialize_for_enum_with_variant_name!(TacticRange);
impl_serialize_for_enum_with_variant_name!(BulletType);
impl_serialize_for_enum_with_variant_name!(ArmorType);
impl_serialize_for_enum_with_variant_name!(AimIKType);
impl_serialize_for_enum_with_variant_name!(School);
impl_serialize_for_enum_with_variant_name!(Club);
impl_serialize_for_enum_with_variant_name!(StatLevelUpType);
impl_serialize_for_enum_with_variant_name!(SquadType);
impl_serialize_for_enum_with_variant_name!(EquipmentCategory);
impl_serialize_for_enum_with_variant_name!(Tag);
impl_serialize_for_enum_with_variant_name!(MemoryLobbyCategory);

impl<'a> Serialize for AcademyFavorScheduleExcel<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut state = serializer.serialize_struct("AcademyFavorScheduleExcel", 12)?;
        state.serialize_field("Id", &self.id())?;
        state.serialize_field("CharacterId", &self.character_id())?;
        state.serialize_field("ScheduleGroupId", &self.schedule_group_id())?;
        state.serialize_field("OrderInGroup", &self.order_in_group())?;
        state.serialize_field("Location", &self.location())?;
        state.serialize_field("LocalizeScenarioId", &self.localize_scenario_id())?;
        state.serialize_field("FavorRank", &self.favor_rank())?;
        state.serialize_field("SecretStoneAmount", &self.secret_stone_amount())?;
        state.serialize_field("ScenarioSriptGroupId", &self.scenario_sript_group_id())?;
        state.serialize_field("RewardParcelType", &self.reward_parcel_type())?;
        state.serialize_field("RewardParcelId", &self.reward_parcel_id())?;
        state.serialize_field("RewardAmount", &self.reward_amount())?;
        state.end()
    }
}

impl<'a> Serialize for CharacterDialogExcel<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut state = serializer.serialize_struct("CharacterDialogExcel", 29)?;
        state.serialize_field("CharacterId", &self.character_id())?;
        state.serialize_field("CostumeUniqueId", &self.costume_unique_id())?;
        state.serialize_field("DisplayOrder", &self.display_order())?;
        state.serialize_field("ProductionStep", &self.production_step())?;
        state.serialize_field("DialogCategory", &self.dialog_category())?;
        state.serialize_field("DialogCondition", &self.dialog_condition())?;
        state.serialize_field("Anniversary", &self.anniversary())?;
        state.serialize_field("StartDate", &self.start_date())?;
        state.serialize_field("EndDate", &self.end_date())?;
        state.serialize_field("GroupId", &self.group_id())?;
        state.serialize_field("DialogType", &self.dialog_type())?;
        state.serialize_field("ActionName", &self.action_name())?;
        state.serialize_field("Duration", &self.duration())?;
        state.serialize_field("AnimationName", &self.animation_name())?;
        state.serialize_field("LocalizeKR", &self.localize_kr())?;
        state.serialize_field("LocalizeJP", &self.localize_jp())?;
        state.serialize_field("LocalizeTH", &self.localize_th())?;
        state.serialize_field("LocalizeTW", &self.localize_tw())?;
        state.serialize_field("LocalizeEN", &self.localize_en())?;
        state.serialize_field("VoiceId", &self.voice_id())?;
        state.serialize_field("ApplyPosition", &self.apply_position())?;
        state.serialize_field("PosX", &self.pos_x())?;
        state.serialize_field("PosY", &self.pos_y())?;
        state.serialize_field("CollectionVisible", &self.collection_visible())?;
        state.serialize_field("CVCollectionType", &self.cv_collection_type())?;
        state.serialize_field("UnlockFavorRank", &self.unlock_favor_rank())?;
        state.serialize_field("UnlockEquipWeapon", &self.unlock_equip_weapon())?;
        state.serialize_field("LocalizeCVGroup", &self.localize_cv_group())?;
        state.serialize_field("TeenMode", &self.teen_mode())?;
        state.end()
    }
}

impl<'a> Serialize for CharacterExcel<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut state = serializer.serialize_struct("CharacterExcel", 62)?;
        state.serialize_field("Id", &self.id())?;
        state.serialize_field("DevName", &self.dev_name())?;
        state.serialize_field("CostumeGroupId", &self.costume_group_id())?;
        state.serialize_field("IsPlayable", &self.is_playable())?;
        state.serialize_field("ProductionStep", &self.production_step())?;
        state.serialize_field("CollectionVisible", &self.collection_visible())?;
        state.serialize_field("ReleaseDate", &self.release_date())?;
        state.serialize_field(
            "CollectionVisibleStartDate",
            &self.collection_visible_start_date(),
        )?;
        state.serialize_field(
            "CollectionVisibleEndDate",
            &self.collection_visible_end_date(),
        )?;
        state.serialize_field("IsPlayableCharacter", &self.is_playable_character())?;
        state.serialize_field("LocalizeEtcId", &self.localize_etc_id())?;
        state.serialize_field("Rarity", &self.rarity())?;
        state.serialize_field("IsNPC", &self.is_npc())?;
        state.serialize_field("TacticEntityType", &self.tactic_entity_type())?;
        state.serialize_field("CanSurvive", &self.can_survive())?;
        state.serialize_field("IsDummy", &self.is_dummy())?;
        state.serialize_field("SubPartsCount", &self.sub_parts_count())?;
        state.serialize_field("TacticRole", &self.tactic_role())?;
        state.serialize_field("WeaponType", &self.weapon_type())?;
        state.serialize_field("TacticRange", &self.tactic_range())?;
        state.serialize_field("BulletType", &self.bullet_type())?;
        state.serialize_field("ArmorType", &self.armor_type())?;
        state.serialize_field("AimIKType", &self.aim_ik_type())?;
        state.serialize_field("School", &self.school())?;
        state.serialize_field("Club", &self.club())?;
        state.serialize_field("DefaultStarGrade", &self.default_star_grade())?;
        state.serialize_field("MaxStarGrade", &self.max_star_grade())?;
        state.serialize_field("StatLevelUpType", &self.stat_level_up_type())?;
        state.serialize_field("SquadType", &self.squad_type())?;
        state.serialize_field("Jumpable", &self.jumpable())?;
        state.serialize_field("PersonalityId", &self.personality_id())?;
        state.serialize_field("CharacterAIId", &self.character_ai_id())?;
        state.serialize_field("ExternalBTId", &self.external_bt_id())?;
        state.serialize_field("ScenarioCharacter", &self.scenario_character())?;
        state.serialize_field("SpawnTemplateId", &self.spawn_template_id())?;
        state.serialize_field("FavorLevelupType", &self.favor_levelup_type())?;
        state.serialize_field("EquipmentSlot", &self.equipment_slot())?;
        state.serialize_field("WeaponLocalizeId", &self.weapon_localize_id())?;
        state.serialize_field("DisplayEnemyInfo", &self.display_enemy_info())?;
        state.serialize_field("BodyRadius", &self.body_radius())?;
        state.serialize_field("RandomEffectRadius", &self.random_effect_radius())?;
        state.serialize_field("HPBarHide", &self.hp_bar_hide())?;
        state.serialize_field("HpBarHeight", &self.hp_bar_height())?;
        state.serialize_field("HighlightFloaterHeight", &self.highlight_floater_height())?;
        state.serialize_field("EmojiOffsetX", &self.emoji_offset_x())?;
        state.serialize_field("EmojiOffsetY", &self.emoji_offset_y())?;
        state.serialize_field("MoveStartFrame", &self.move_start_frame())?;
        state.serialize_field("MoveEndFrame", &self.move_end_frame())?;
        state.serialize_field("JumpMotionFrame", &self.jump_motion_frame())?;
        state.serialize_field("AppearFrame", &self.appear_frame())?;
        state.serialize_field("CanMove", &self.can_move())?;
        state.serialize_field("CanFix", &self.can_fix())?;
        state.serialize_field("CanCrowdControl", &self.can_crowd_control())?;
        state.serialize_field("CanBattleItemMove", &self.can_battle_item_move())?;
        state.serialize_field("IsAirUnit", &self.is_air_unit())?;
        state.serialize_field("AirUnitHeight", &self.air_unit_height())?;
        state.serialize_field("Tags", &self.tags())?;
        state.serialize_field("SecretStoneItemId", &self.secret_stone_item_id())?;
        state.serialize_field("SecretStoneItemAmount", &self.secret_stone_item_amount())?;
        state.serialize_field("CharacterPieceItemId", &self.character_piece_item_id())?;
        state.serialize_field(
            "CharacterPieceItemAmount",
            &self.character_piece_item_amount(),
        )?;
        state.serialize_field("CombineRecipeId", &self.combine_recipe_id())?;
        state.end()
    }
}

impl<'a> Serialize for LocalizeCharProfileExcel<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut state = serializer.serialize_struct("LocalizeCharProfileExcel", 92)?;
        state.serialize_field("CharacterId", &self.character_id())?;
        state.serialize_field("StatusMessageKr", &self.status_message_kr())?;
        state.serialize_field("StatusMessageJp", &self.status_message_jp())?;
        state.serialize_field("StatusMessageTh", &self.status_message_th())?;
        state.serialize_field("StatusMessageTw", &self.status_message_tw())?;
        state.serialize_field("StatusMessageEn", &self.status_message_en())?;
        state.serialize_field("FullNameKr", &self.full_name_kr())?;
        state.serialize_field("FullNameJp", &self.full_name_jp())?;
        state.serialize_field("FullNameTh", &self.full_name_th())?;
        state.serialize_field("FullNameTw", &self.full_name_tw())?;
        state.serialize_field("FullNameEn", &self.full_name_en())?;
        state.serialize_field("FamilyNameKr", &self.family_name_kr())?;
        state.serialize_field("FamilyNameRubyKr", &self.family_name_ruby_kr())?;
        state.serialize_field("PersonalNameKr", &self.personal_name_kr())?;
        state.serialize_field("PersonalNameRubyKr", &self.personal_name_ruby_kr())?;
        state.serialize_field("FamilyNameJp", &self.family_name_jp())?;
        state.serialize_field("FamilyNameRubyJp", &self.family_name_ruby_jp())?;
        state.serialize_field("PersonalNameJp", &self.personal_name_jp())?;
        state.serialize_field("PersonalNameRubyJp", &self.personal_name_ruby_jp())?;
        state.serialize_field("FamilyNameTh", &self.family_name_th())?;
        state.serialize_field("FamilyNameRubyTh", &self.family_name_ruby_th())?;
        state.serialize_field("PersonalNameTh", &self.personal_name_th())?;
        state.serialize_field("PersonalNameRubyTh", &self.personal_name_ruby_th())?;
        state.serialize_field("FamilyNameTw", &self.family_name_tw())?;
        state.serialize_field("FamilyNameRubyTw", &self.family_name_ruby_tw())?;
        state.serialize_field("PersonalNameTw", &self.personal_name_tw())?;
        state.serialize_field("PersonalNameRubyTw", &self.personal_name_ruby_tw())?;
        state.serialize_field("FamilyNameEn", &self.family_name_en())?;
        state.serialize_field("FamilyNameRubyEn", &self.family_name_ruby_en())?;
        state.serialize_field("PersonalNameEn", &self.personal_name_en())?;
        state.serialize_field("PersonalNameRubyEn", &self.personal_name_ruby_en())?;
        state.serialize_field("SchoolYearKr", &self.school_year_kr())?;
        state.serialize_field("SchoolYearJp", &self.school_year_jp())?;
        state.serialize_field("SchoolYearTh", &self.school_year_th())?;
        state.serialize_field("SchoolYearTw", &self.school_year_tw())?;
        state.serialize_field("SchoolYearEn", &self.school_year_en())?;
        state.serialize_field("CharacterAgeKr", &self.character_age_kr())?;
        state.serialize_field("CharacterAgeJp", &self.character_age_jp())?;
        state.serialize_field("CharacterAgeTh", &self.character_age_th())?;
        state.serialize_field("CharacterAgeTw", &self.character_age_tw())?;
        state.serialize_field("CharacterAgeEn", &self.character_age_en())?;
        state.serialize_field("BirthDay", &self.birth_day())?;
        state.serialize_field("BirthdayKr", &self.birthday_kr())?;
        state.serialize_field("BirthdayJp", &self.birthday_jp())?;
        state.serialize_field("BirthdayTh", &self.birthday_th())?;
        state.serialize_field("BirthdayTw", &self.birthday_tw())?;
        state.serialize_field("BirthdayEn", &self.birthday_en())?;
        state.serialize_field("CharHeightKr", &self.char_height_kr())?;
        state.serialize_field("CharHeightJp", &self.char_height_jp())?;
        state.serialize_field("CharHeightTh", &self.char_height_th())?;
        state.serialize_field("CharHeightTw", &self.char_height_tw())?;
        state.serialize_field("CharHeightEn", &self.char_height_en())?;
        state.serialize_field("DesignerNameKr", &self.designer_name_kr())?;
        state.serialize_field("DesignerNameJp", &self.designer_name_jp())?;
        state.serialize_field("DesignerNameTh", &self.designer_name_th())?;
        state.serialize_field("DesignerNameTw", &self.designer_name_tw())?;
        state.serialize_field("DesignerNameEn", &self.designer_name_en())?;
        state.serialize_field("IllustratorNameKr", &self.illustrator_name_kr())?;
        state.serialize_field("IllustratorNameJp", &self.illustrator_name_jp())?;
        state.serialize_field("IllustratorNameTh", &self.illustrator_name_th())?;
        state.serialize_field("IllustratorNameTw", &self.illustrator_name_tw())?;
        state.serialize_field("IllustratorNameEn", &self.illustrator_name_en())?;
        state.serialize_field("CharacterVoiceKr", &self.character_voice_kr())?;
        state.serialize_field("CharacterVoiceJp", &self.character_voice_jp())?;
        state.serialize_field("CharacterVoiceTh", &self.character_voice_th())?;
        state.serialize_field("CharacterVoiceTw", &self.character_voice_tw())?;
        state.serialize_field("CharacterVoiceEn", &self.character_voice_en())?;
        state.serialize_field("HobbyKr", &self.hobby_kr())?;
        state.serialize_field("HobbyJp", &self.hobby_jp())?;
        state.serialize_field("HobbyTh", &self.hobby_th())?;
        state.serialize_field("HobbyTw", &self.hobby_tw())?;
        state.serialize_field("HobbyEn", &self.hobby_en())?;
        state.serialize_field("WeaponNameKr", &self.weapon_name_kr())?;
        state.serialize_field("WeaponDescKr", &self.weapon_desc_kr())?;
        state.serialize_field("WeaponNameJp", &self.weapon_name_jp())?;
        state.serialize_field("WeaponDescJp", &self.weapon_desc_jp())?;
        state.serialize_field("WeaponNameTh", &self.weapon_name_th())?;
        state.serialize_field("WeaponDescTh", &self.weapon_desc_th())?;
        state.serialize_field("WeaponNameTw", &self.weapon_name_tw())?;
        state.serialize_field("WeaponDescTw", &self.weapon_desc_tw())?;
        state.serialize_field("WeaponNameEn", &self.weapon_name_en())?;
        state.serialize_field("WeaponDescEn", &self.weapon_desc_en())?;
        state.serialize_field("ProfileIntroductionKr", &self.profile_introduction_kr())?;
        state.serialize_field("ProfileIntroductionJp", &self.profile_introduction_jp())?;
        state.serialize_field("ProfileIntroductionTh", &self.profile_introduction_th())?;
        state.serialize_field("ProfileIntroductionTw", &self.profile_introduction_tw())?;
        state.serialize_field("ProfileIntroductionEn", &self.profile_introduction_en())?;
        state.serialize_field("CharacterSSRNewKr", &self.character_ssr_new_kr())?;
        state.serialize_field("CharacterSSRNewJp", &self.character_ssr_new_jp())?;
        state.serialize_field("CharacterSSRNewTh", &self.character_ssr_new_th())?;
        state.serialize_field("CharacterSSRNewTw", &self.character_ssr_new_tw())?;
        state.serialize_field("CharacterSSRNewEn", &self.character_ssr_new_en())?;
        state.end()
    }
}

impl<'a> Serialize for MemoryLobbyExcel<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut state = serializer.serialize_struct("MemoryLobbyExcel", 14)?;
        state.serialize_field("Id", &self.id())?;
        state.serialize_field("ProductionStep", &self.production_step())?;
        state.serialize_field("LocalizeEtcId", &self.localize_etc_id())?;
        state.serialize_field("CharacterId", &self.character_id())?;
        state.serialize_field("PrefabName", &self.prefab_name())?;
        state.serialize_field("MemoryLobbyCategory", &self.memory_lobby_category())?;
        state.serialize_field("SlotTextureName", &self.slot_texture_name())?;
        state.serialize_field("RewardTextureName", &self.reward_texture_name())?;
        state.serialize_field("BGMId", &self.bgm_id())?;
        state.serialize_field("AudioClipJp", &self.audio_clip_jp())?;
        state.serialize_field("AudioClipKr", &self.audio_clip_kr())?;
        state.serialize_field("AudioClipTh", &self.audio_clip_th())?;
        state.serialize_field("AudioClipTw", &self.audio_clip_tw())?;
        state.serialize_field("AudioClipEn", &self.audio_clip_en())?;
        state.end()
    }
}

impl<'a> Serialize for AcademyFavorScheduleExcelTable<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.data_list().unwrap().len()))?;
        for element in self.data_list().unwrap() {
            seq.serialize_element(&element)?;
        }
        seq.end()
    }
}

impl<'a> Serialize for CharacterDialogExcelTable<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.data_list().unwrap().len()))?;
        for element in self.data_list().unwrap() {
            seq.serialize_element(&element)?;
        }
        seq.end()
    }
}

impl<'a> Serialize for CharacterExcelTable<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.data_list().unwrap().len()))?;
        for element in self.data_list().unwrap() {
            seq.serialize_element(&element)?;
        }
        seq.end()
    }
}

impl<'a> Serialize for LocalizeCharProfileExcelTable<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.data_list().unwrap().len()))?;
        for element in self.data_list().unwrap() {
            seq.serialize_element(&element)?;
        }
        seq.end()
    }
}

impl<'a> Serialize for MemoryLobbyExcelTable<'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.data_list().unwrap().len()))?;
        for element in self.data_list().unwrap() {
            seq.serialize_element(&element)?;
        }
        seq.end()
    }
}

macro_rules! create_string {
    ($fbb:expr, $func:expr, $key:expr) => {
        Some($fbb.create_string(&convert_string($func.unwrap(), $key).unwrap()))
    };
}

impl<'a> DecryptAndDump for AcademyFavorScheduleExcelTable<'a> {
    fn decrypt_dump_json(&mut self) -> String {
        let key = create_key(b"AcademyFavorSchedule");
        let data = self
            .data_list()
            .unwrap()
            .into_iter()
            .map(|a| {
                let fbb = &mut flatbuffers::FlatBufferBuilder::new();
                let location =
                    fbb.create_string(&convert_string(a.location().unwrap(), &key).unwrap());

                let reward_parcel_type = match a.reward_parcel_type() {
                    Some(reward_parcel_type) => reward_parcel_type
                        .iter()
                        .map(|j| {
                            let value = convert_int(j.0, &key);
                            ParcelType::ENUM_VALUES[value as usize]
                        })
                        .collect::<Vec<ParcelType>>(),
                    None => vec![], // empty vector
                };
                let reward_parcel_type = fbb.create_vector(&reward_parcel_type);

                let reward_parcel_id = match a.reward_parcel_id() {
                    Some(reward_parcel_id) => reward_parcel_id
                        .iter()
                        .map(|j| convert_long(j, &key))
                        .collect::<Vec<i64>>(),
                    None => vec![], // empty vector
                };
                let reward_parcel_id = fbb.create_vector(&reward_parcel_id);

                let reward_amount = match a.reward_amount() {
                    Some(reward_amount) => reward_amount
                        .iter()
                        .map(|j| convert_long(j, &key))
                        .collect::<Vec<i64>>(),
                    None => vec![], // empty vector
                };
                let reward_amount = fbb.create_vector(&reward_amount);

                let data = AcademyFavorScheduleExcel::create(
                    fbb,
                    &AcademyFavorScheduleExcelArgs {
                        id: convert_long(a.id(), &key),
                        character_id: convert_long(a.character_id(), &key),
                        schedule_group_id: convert_long(a.schedule_group_id(), &key),
                        order_in_group: convert_long(a.order_in_group(), &key),
                        location: Some(location),
                        localize_scenario_id: convert_uint(a.localize_scenario_id(), &key),
                        favor_rank: convert_long(a.favor_rank(), &key),
                        secret_stone_amount: convert_long(a.secret_stone_amount(), &key),
                        scenario_sript_group_id: convert_long(a.scenario_sript_group_id(), &key),
                        reward_parcel_type: Some(reward_parcel_type),
                        reward_parcel_id: Some(reward_parcel_id),
                        reward_amount: Some(reward_amount),
                    },
                );
                fbb.finish(data, None);
                let buf = fbb.finished_data().to_vec();
                buf
            })
            .collect::<Vec<Vec<u8>>>();
        let data = data
            .iter()
            .map(|a| flatbuffers::root::<AcademyFavorScheduleExcel>(&a).unwrap())
            .collect::<Vec<AcademyFavorScheduleExcel>>();
        let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
        let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
        data.serialize(&mut ser).unwrap();
        String::from_utf8(ser.into_inner()).unwrap()
    }
}

impl<'a> DecryptAndDump for CharacterDialogExcelTable<'a> {
    fn decrypt_dump_json(&mut self) -> String {
        let key = create_key(b"CharacterDialog");

        let data = self
            .data_list()
            .unwrap()
            .into_iter()
            .map(|a| {
                let fbb = &mut flatbuffers::FlatBufferBuilder::new();

                let start_date = create_string!(fbb, a.start_date(), &key);
                let end_date = create_string!(fbb, a.end_date(), &key);
                let action_name = create_string!(fbb, a.action_name(), &key);
                let animation_name = create_string!(fbb, a.animation_name(), &key);
                let localize_kr = create_string!(fbb, a.localize_kr(), &key);
                let localize_jp = create_string!(fbb, a.localize_jp(), &key);
                let localize_th = create_string!(fbb, a.localize_th(), &key);
                let localize_tw = create_string!(fbb, a.localize_tw(), &key);
                let localize_en = create_string!(fbb, a.localize_en(), &key);
                let localize_cv_group = create_string!(fbb, a.localize_cv_group(), &key);

                let voice_id = match a.voice_id() {
                    Some(voice_id) => voice_id
                        .iter()
                        .map(|j| convert_uint(j, &key))
                        .collect::<Vec<u32>>(),
                    None => vec![], // empty vector
                };
                let voice_id = fbb.create_vector(&voice_id);

                let production_step = ProductionStep::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.production_step().0, &key))
                    .unwrap();
                let dialog_category = DialogCategory::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.dialog_category().0, &key))
                    .unwrap();
                let dialog_condition = DialogCondition::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.dialog_condition().0, &key))
                    .unwrap();
                let anniversary = Anniversary::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.anniversary().0, &key))
                    .unwrap();
                let dialog_type = DialogType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.dialog_type().0, &key))
                    .unwrap();
                let cv_collection_type = CVCollectionType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.cv_collection_type().0, &key))
                    .unwrap();

                let data = CharacterDialogExcel::create(
                    fbb,
                    &CharacterDialogExcelArgs {
                        character_id: convert_long(a.character_id(), &key),
                        costume_unique_id: convert_long(a.costume_unique_id(), &key),
                        display_order: convert_long(a.display_order(), &key),
                        production_step: production_step,
                        dialog_category: dialog_category,
                        dialog_condition: dialog_condition,
                        anniversary: anniversary,
                        start_date: start_date,
                        end_date: end_date,
                        group_id: convert_long(a.group_id(), &key),
                        dialog_type: dialog_type,
                        action_name: action_name,
                        duration: convert_long(a.duration(), &key),
                        duration_kr: convert_long(a.duration_kr(), &key),
                        animation_name: animation_name,
                        localize_kr: localize_kr,
                        localize_jp: localize_jp,
                        localize_th: localize_th,
                        localize_tw: localize_tw,
                        localize_en: localize_en,
                        voice_id: Some(voice_id),
                        apply_position: a.apply_position(),
                        pos_x: convert_float(a.pos_x(), &key),
                        pos_y: convert_float(a.pos_y(), &key),
                        collection_visible: a.collection_visible(),
                        cv_collection_type: cv_collection_type,
                        unlock_favor_rank: convert_long(a.unlock_favor_rank(), &key),
                        unlock_equip_weapon: a.unlock_equip_weapon(),
                        localize_cv_group: localize_cv_group,
                        teen_mode: a.teen_mode(),
                    },
                );
                fbb.finish(data, None);
                let buf = fbb.finished_data().to_vec();
                buf
            })
            .collect::<Vec<Vec<u8>>>();
        let data = data
            .iter()
            .map(|a| flatbuffers::root::<CharacterDialogExcel>(&a).unwrap())
            .collect::<Vec<CharacterDialogExcel>>();
        let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
        let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
        data.serialize(&mut ser).unwrap();
        String::from_utf8(ser.into_inner()).unwrap()
    }
}

impl<'a> DecryptAndDump for CharacterExcelTable<'a> {
    fn decrypt_dump_json(&mut self) -> String {
        let key = create_key(b"Character");

        let data = self
            .data_list()
            .unwrap()
            .into_iter()
            .map(|a| {
                let fbb = &mut flatbuffers::FlatBufferBuilder::new();

                let dev_name =
                    fbb.create_string(&convert_string(a.dev_name().unwrap(), &key).unwrap());
                let release_date =
                    fbb.create_string(&convert_string(a.release_date().unwrap(), &key).unwrap());
                let collection_visible_start_date = fbb.create_string(
                    &convert_string(a.collection_visible_start_date().unwrap(), &key).unwrap(),
                );
                let collection_visible_end_date = fbb.create_string(
                    &convert_string(a.collection_visible_end_date().unwrap(), &key).unwrap(),
                );
                let scenario_character = fbb
                    .create_string(&convert_string(a.scenario_character().unwrap(), &key).unwrap());

                let production_step = ProductionStep::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.production_step().0, &key))
                    .unwrap();
                let rarity = Rarity::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.rarity().0, &key))
                    .unwrap();
                let tactic_entity_type = TacticEntityType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.tactic_entity_type().0, &key))
                    .unwrap();
                let tactic_role = TacticRole::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.tactic_role().0, &key))
                    .unwrap();
                let weapon_type = WeaponType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.weapon_type().0, &key))
                    .unwrap();
                let tactic_range = TacticRange::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.tactic_range().0, &key))
                    .unwrap();
                let bullet_type = BulletType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.bullet_type().0, &key))
                    .unwrap();
                let armor_type = ArmorType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.armor_type().0, &key))
                    .unwrap();
                let aim_ik_type = AimIKType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.aim_ik_type().0, &key))
                    .unwrap();
                let school = School::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.school().0, &key))
                    .unwrap();
                let club = Club::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.club().0, &key))
                    .unwrap();
                let stat_level_up_type = StatLevelUpType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.stat_level_up_type().0, &key))
                    .unwrap();
                let squad_type = SquadType::ENUM_VALUES
                    .iter()
                    .cloned()
                    .find(|&x| x.0 == convert_int(a.squad_type().0, &key))
                    .unwrap();

                let equipment_slot = match a.equipment_slot() {
                    Some(equipment_slot) => equipment_slot
                        .iter()
                        .map(|j| {
                            let value = convert_int(j.0, &key);
                            EquipmentCategory::ENUM_VALUES[value as usize]
                        })
                        .collect::<Vec<EquipmentCategory>>(),
                    None => vec![], // empty vector
                };
                let equipment_slot = fbb.create_vector(&equipment_slot);
                let tags = match a.tags() {
                    Some(tags) => tags
                        .iter()
                        .map(|j| {
                            let value = convert_int(j.0, &key);
                            Tag::ENUM_VALUES[value as usize]
                        })
                        .collect::<Vec<Tag>>(),
                    None => vec![], // empty vector
                };
                let tags = fbb.create_vector(&tags);

                let data = CharacterExcel::create(
                    fbb,
                    &CharacterExcelArgs {
                        id: convert_long(a.id(), &key),
                        dev_name: Some(dev_name),
                        costume_group_id: convert_long(a.costume_group_id(), &key),
                        is_playable: a.is_playable(),
                        production_step: production_step,
                        collection_visible: a.collection_visible(),
                        release_date: Some(release_date),
                        collection_visible_start_date: Some(collection_visible_start_date),
                        collection_visible_end_date: Some(collection_visible_end_date),
                        is_playable_character: a.is_playable_character(),
                        localize_etc_id: convert_uint(a.localize_etc_id(), &key),
                        rarity: rarity,
                        is_npc: a.is_npc(),
                        tactic_entity_type,
                        can_survive: a.can_survive(),
                        is_dummy: a.is_dummy(),
                        sub_parts_count: convert_int(a.sub_parts_count(), &key),
                        tactic_role: tactic_role,
                        weapon_type: weapon_type,
                        tactic_range: tactic_range,
                        bullet_type: bullet_type,
                        armor_type: armor_type,
                        aim_ik_type: aim_ik_type,
                        school: school,
                        club: club,
                        default_star_grade: convert_int(a.default_star_grade(), &key),
                        max_star_grade: convert_int(a.max_star_grade(), &key),
                        stat_level_up_type: stat_level_up_type,
                        squad_type: squad_type,
                        jumpable: a.jumpable(),
                        personality_id: convert_long(a.personality_id(), &key),
                        character_ai_id: convert_long(a.character_ai_id(), &key),
                        external_bt_id: convert_long(a.external_bt_id(), &key),
                        main_combat_style_id: convert_long(a.main_combat_style_id(), &key),
                        combat_style_index: convert_int(a.combat_style_index(), &key),
                        scenario_character: Some(scenario_character),
                        spawn_template_id: convert_uint(a.spawn_template_id(), &key),
                        favor_levelup_type: convert_int(a.favor_levelup_type(), &key),
                        equipment_slot: Some(equipment_slot),
                        weapon_localize_id: convert_uint(a.weapon_localize_id(), &key),
                        display_enemy_info: a.display_enemy_info(),
                        body_radius: convert_long(a.body_radius(), &key),
                        random_effect_radius: convert_long(a.random_effect_radius(), &key),
                        hp_bar_hide: a.hp_bar_hide(),
                        hp_bar_height: convert_float(a.hp_bar_height(), &key),
                        highlight_floater_height: convert_float(a.highlight_floater_height(), &key),
                        emoji_offset_x: convert_float(a.emoji_offset_x(), &key),
                        emoji_offset_y: convert_float(a.emoji_offset_y(), &key),
                        move_start_frame: convert_int(a.move_start_frame(), &key),
                        move_end_frame: convert_int(a.move_end_frame(), &key),
                        jump_motion_frame: convert_int(a.jump_motion_frame(), &key),
                        appear_frame: convert_int(a.appear_frame(), &key),
                        can_move: a.can_move(),
                        can_fix: a.can_fix(),
                        can_crowd_control: a.can_crowd_control(),
                        can_battle_item_move: a.can_battle_item_move(),
                        is_air_unit: a.is_air_unit(),
                        air_unit_height: convert_long(a.air_unit_height(), &key),
                        tags: Some(tags),
                        secret_stone_item_id: convert_long(a.secret_stone_item_id(), &key),
                        secret_stone_item_amount: convert_int(a.secret_stone_item_amount(), &key),
                        character_piece_item_id: convert_long(a.character_piece_item_id(), &key),
                        character_piece_item_amount: convert_int(
                            a.character_piece_item_amount(),
                            &key,
                        ),
                        combine_recipe_id: convert_long(a.combine_recipe_id(), &key),
                    },
                );
                fbb.finish(data, None);
                let buf = fbb.finished_data().to_vec();
                buf
            })
            .collect::<Vec<Vec<u8>>>();
        let data = data
            .iter()
            .map(|a| flatbuffers::root::<CharacterExcel>(&a).unwrap())
            .collect::<Vec<CharacterExcel>>();
        let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
        let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
        data.serialize(&mut ser).unwrap();
        String::from_utf8(ser.into_inner()).unwrap()
    }
}

impl<'a> DecryptAndDump for LocalizeCharProfileExcelTable<'a> {
    fn decrypt_dump_json(&mut self) -> String {
        let key = create_key(b"LocalizeCharProfile");

        let data = self
            .data_list()
            .unwrap()
            .into_iter()
            .map(|a| {
                let fbb = &mut flatbuffers::FlatBufferBuilder::new();

                let status_message_kr = create_string!(fbb, a.status_message_kr(), &key);
                let status_message_jp = create_string!(fbb, a.status_message_jp(), &key);
                let status_message_th = create_string!(fbb, a.status_message_th(), &key);
                let status_message_tw = create_string!(fbb, a.status_message_tw(), &key);
                let status_message_en = create_string!(fbb, a.status_message_en(), &key);
                let full_name_kr = create_string!(fbb, a.full_name_kr(), &key);
                let full_name_jp = create_string!(fbb, a.full_name_jp(), &key);
                let full_name_th = create_string!(fbb, a.full_name_th(), &key);
                let full_name_tw = create_string!(fbb, a.full_name_tw(), &key);
                let full_name_en = create_string!(fbb, a.full_name_en(), &key);
                let family_name_kr = create_string!(fbb, a.family_name_kr(), &key);
                let family_name_ruby_kr = create_string!(fbb, a.family_name_ruby_kr(), &key);
                let personal_name_kr = create_string!(fbb, a.personal_name_kr(), &key);
                let personal_name_ruby_kr = create_string!(fbb, a.personal_name_ruby_kr(), &key);
                let family_name_jp = create_string!(fbb, a.family_name_jp(), &key);
                let family_name_ruby_jp = create_string!(fbb, a.family_name_ruby_jp(), &key);
                let personal_name_jp = create_string!(fbb, a.personal_name_jp(), &key);
                let personal_name_ruby_jp = create_string!(fbb, a.personal_name_ruby_jp(), &key);
                let family_name_th = create_string!(fbb, a.family_name_th(), &key);
                let family_name_ruby_th = create_string!(fbb, a.family_name_ruby_th(), &key);
                let personal_name_th = create_string!(fbb, a.personal_name_th(), &key);
                let personal_name_ruby_th = create_string!(fbb, a.personal_name_ruby_th(), &key);
                let family_name_tw = create_string!(fbb, a.family_name_tw(), &key);
                let family_name_ruby_tw = create_string!(fbb, a.family_name_ruby_tw(), &key);
                let personal_name_tw = create_string!(fbb, a.personal_name_tw(), &key);
                let personal_name_ruby_tw = create_string!(fbb, a.personal_name_ruby_tw(), &key);
                let family_name_en = create_string!(fbb, a.family_name_en(), &key);
                let family_name_ruby_en = create_string!(fbb, a.family_name_ruby_en(), &key);
                let personal_name_en = create_string!(fbb, a.personal_name_en(), &key);
                let personal_name_ruby_en = create_string!(fbb, a.personal_name_ruby_en(), &key);
                let school_year_kr = create_string!(fbb, a.school_year_kr(), &key);
                let school_year_jp = create_string!(fbb, a.school_year_jp(), &key);
                let school_year_th = create_string!(fbb, a.school_year_th(), &key);
                let school_year_tw = create_string!(fbb, a.school_year_tw(), &key);
                let school_year_en = create_string!(fbb, a.school_year_en(), &key);
                let character_age_kr = create_string!(fbb, a.character_age_kr(), &key);
                let character_age_jp = create_string!(fbb, a.character_age_jp(), &key);
                let character_age_th = create_string!(fbb, a.character_age_th(), &key);
                let character_age_tw = create_string!(fbb, a.character_age_tw(), &key);
                let character_age_en = create_string!(fbb, a.character_age_en(), &key);
                let birth_day = create_string!(fbb, a.birth_day(), &key);
                let birthday_kr = create_string!(fbb, a.birthday_kr(), &key);
                let birthday_jp = create_string!(fbb, a.birthday_jp(), &key);
                let birthday_th = create_string!(fbb, a.birthday_th(), &key);
                let birthday_tw = create_string!(fbb, a.birthday_tw(), &key);
                let birthday_en = create_string!(fbb, a.birthday_en(), &key);
                let char_height_kr = create_string!(fbb, a.char_height_kr(), &key);
                let char_height_jp = create_string!(fbb, a.char_height_jp(), &key);
                let char_height_th = create_string!(fbb, a.char_height_th(), &key);
                let char_height_tw = create_string!(fbb, a.char_height_tw(), &key);
                let char_height_en = create_string!(fbb, a.char_height_en(), &key);
                let designer_name_kr = create_string!(fbb, a.designer_name_kr(), &key);
                let designer_name_jp = create_string!(fbb, a.designer_name_jp(), &key);
                let designer_name_th = create_string!(fbb, a.designer_name_th(), &key);
                let designer_name_tw = create_string!(fbb, a.designer_name_tw(), &key);
                let designer_name_en = create_string!(fbb, a.designer_name_en(), &key);
                let illustrator_name_kr = create_string!(fbb, a.illustrator_name_kr(), &key);
                let illustrator_name_jp = create_string!(fbb, a.illustrator_name_jp(), &key);
                let illustrator_name_th = create_string!(fbb, a.illustrator_name_th(), &key);
                let illustrator_name_tw = create_string!(fbb, a.illustrator_name_tw(), &key);
                let illustrator_name_en = create_string!(fbb, a.illustrator_name_en(), &key);
                let character_voice_kr = create_string!(fbb, a.character_voice_kr(), &key);
                let character_voice_jp = create_string!(fbb, a.character_voice_jp(), &key);
                let character_voice_th = create_string!(fbb, a.character_voice_th(), &key);
                let character_voice_tw = create_string!(fbb, a.character_voice_tw(), &key);
                let character_voice_en = create_string!(fbb, a.character_voice_en(), &key);
                let kr_character_voice_kr = create_string!(fbb, a.kr_character_voice_kr(), &key);
                let kr_character_voice_th = create_string!(fbb, a.kr_character_voice_th(), &key);
                let kr_character_voice_tw = create_string!(fbb, a.kr_character_voice_tw(), &key);
                let kr_character_voice_en = create_string!(fbb, a.kr_character_voice_en(), &key);
                let hobby_kr = create_string!(fbb, a.hobby_kr(), &key);
                let hobby_jp = create_string!(fbb, a.hobby_jp(), &key);
                let hobby_th = create_string!(fbb, a.hobby_th(), &key);
                let hobby_tw = create_string!(fbb, a.hobby_tw(), &key);
                let hobby_en = create_string!(fbb, a.hobby_en(), &key);
                let weapon_name_kr = create_string!(fbb, a.weapon_name_kr(), &key);
                let weapon_desc_kr = create_string!(fbb, a.weapon_desc_kr(), &key);
                let weapon_name_jp = create_string!(fbb, a.weapon_name_jp(), &key);
                let weapon_desc_jp = create_string!(fbb, a.weapon_desc_jp(), &key);
                let weapon_name_th = create_string!(fbb, a.weapon_name_th(), &key);
                let weapon_desc_th = create_string!(fbb, a.weapon_desc_th(), &key);
                let weapon_name_tw = create_string!(fbb, a.weapon_name_tw(), &key);
                let weapon_desc_tw = create_string!(fbb, a.weapon_desc_tw(), &key);
                let weapon_name_en = create_string!(fbb, a.weapon_name_en(), &key);
                let weapon_desc_en = create_string!(fbb, a.weapon_desc_en(), &key);
                let profile_introduction_kr =
                    create_string!(fbb, a.profile_introduction_kr(), &key);
                let profile_introduction_jp =
                    create_string!(fbb, a.profile_introduction_jp(), &key);
                let profile_introduction_th =
                    create_string!(fbb, a.profile_introduction_th(), &key);
                let profile_introduction_tw =
                    create_string!(fbb, a.profile_introduction_tw(), &key);
                let profile_introduction_en =
                    create_string!(fbb, a.profile_introduction_en(), &key);
                let character_ssr_new_kr = create_string!(fbb, a.character_ssr_new_kr(), &key);
                let character_ssr_new_jp = create_string!(fbb, a.character_ssr_new_jp(), &key);
                let character_ssr_new_th = create_string!(fbb, a.character_ssr_new_th(), &key);
                let character_ssr_new_tw = create_string!(fbb, a.character_ssr_new_tw(), &key);
                let character_ssr_new_en = create_string!(fbb, a.character_ssr_new_en(), &key);

                let data = LocalizeCharProfileExcel::create(
                    fbb,
                    &LocalizeCharProfileExcelArgs {
                        character_id: convert_long(a.character_id(), &key),
                        status_message_kr,
                        status_message_jp,
                        status_message_th,
                        status_message_tw,
                        status_message_en,
                        full_name_kr,
                        full_name_jp,
                        full_name_th,
                        full_name_tw,
                        full_name_en,
                        family_name_kr,
                        family_name_ruby_kr,
                        personal_name_kr,
                        personal_name_ruby_kr,
                        family_name_jp,
                        family_name_ruby_jp,
                        personal_name_jp,
                        personal_name_ruby_jp,
                        family_name_th,
                        family_name_ruby_th,
                        personal_name_th,
                        personal_name_ruby_th,
                        family_name_tw,
                        family_name_ruby_tw,
                        personal_name_tw,
                        personal_name_ruby_tw,
                        family_name_en,
                        family_name_ruby_en,
                        personal_name_en,
                        personal_name_ruby_en,
                        school_year_kr,
                        school_year_jp,
                        school_year_th,
                        school_year_tw,
                        school_year_en,
                        character_age_kr,
                        character_age_jp,
                        character_age_th,
                        character_age_tw,
                        character_age_en,
                        birth_day,
                        birthday_kr,
                        birthday_jp,
                        birthday_th,
                        birthday_tw,
                        birthday_en,
                        char_height_kr,
                        char_height_jp,
                        char_height_th,
                        char_height_tw,
                        char_height_en,
                        designer_name_kr,
                        designer_name_jp,
                        designer_name_th,
                        designer_name_tw,
                        designer_name_en,
                        illustrator_name_kr,
                        illustrator_name_jp,
                        illustrator_name_th,
                        illustrator_name_tw,
                        illustrator_name_en,
                        character_voice_kr,
                        character_voice_jp,
                        character_voice_th,
                        character_voice_tw,
                        character_voice_en,
                        kr_character_voice_kr,
                        kr_character_voice_th,
                        kr_character_voice_tw,
                        kr_character_voice_en,
                        hobby_kr,
                        hobby_jp,
                        hobby_th,
                        hobby_tw,
                        hobby_en,
                        weapon_name_kr,
                        weapon_desc_kr,
                        weapon_name_jp,
                        weapon_desc_jp,
                        weapon_name_th,
                        weapon_desc_th,
                        weapon_name_tw,
                        weapon_desc_tw,
                        weapon_name_en,
                        weapon_desc_en,
                        profile_introduction_kr,
                        profile_introduction_jp,
                        profile_introduction_th,
                        profile_introduction_tw,
                        profile_introduction_en,
                        character_ssr_new_kr,
                        character_ssr_new_jp,
                        character_ssr_new_th,
                        character_ssr_new_tw,
                        character_ssr_new_en,
                    },
                );
                fbb.finish(data, None);
                let buf = fbb.finished_data().to_vec();
                buf
            })
            .collect::<Vec<Vec<u8>>>();
        let data = data
            .iter()
            .map(|a| flatbuffers::root::<LocalizeCharProfileExcel>(&a).unwrap())
            .collect::<Vec<LocalizeCharProfileExcel>>();
        let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
        let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
        data.serialize(&mut ser).unwrap();
        String::from_utf8(ser.into_inner()).unwrap()
    }
}

impl<'a> DecryptAndDump for MemoryLobbyExcelTable<'a> {
    fn decrypt_dump_json(&mut self) -> String {
        let key = create_key(b"MemoryLobby");
        let data = self
            .data_list()
            .unwrap()
            .into_iter()
            .map(|a| {
                let fbb = &mut flatbuffers::FlatBufferBuilder::new();

                let production_step =
                    ProductionStep::ENUM_VALUES[convert_int(a.production_step().0, &key) as usize];
                let memory_lobby_category = MemoryLobbyCategory::ENUM_VALUES
                    [convert_int(a.memory_lobby_category().0, &key) as usize];

                let prefab_name = create_string!(fbb, a.prefab_name(), &key);
                let slot_texture_name = create_string!(fbb, a.slot_texture_name(), &key);
                let reward_texture_name = create_string!(fbb, a.reward_texture_name(), &key);
                let audio_clip_jp = create_string!(fbb, a.audio_clip_jp(), &key);
                let audio_clip_kr = create_string!(fbb, a.audio_clip_kr(), &key);
                let audio_clip_th = create_string!(fbb, a.audio_clip_th(), &key);
                let audio_clip_tw = create_string!(fbb, a.audio_clip_tw(), &key);
                let audio_clip_en = create_string!(fbb, a.audio_clip_en(), &key);

                let data = MemoryLobbyExcel::create(
                    fbb,
                    &MemoryLobbyExcelArgs {
                        id: convert_long(a.id(), &key),
                        production_step,
                        localize_etc_id: convert_uint(a.localize_etc_id(), &key),
                        character_id: convert_long(a.character_id(), &key),
                        prefab_name,
                        memory_lobby_category,
                        slot_texture_name,
                        reward_texture_name,
                        bgm_id: convert_long(a.bgm_id(), &key),
                        audio_clip_jp,
                        audio_clip_kr,
                        audio_clip_th,
                        audio_clip_tw,
                        audio_clip_en,
                    },
                );
                fbb.finish(data, None);
                let buf = fbb.finished_data().to_vec();
                buf
            })
            .collect::<Vec<Vec<u8>>>();
        let data = data
            .iter()
            .map(|a| flatbuffers::root::<MemoryLobbyExcel>(&a).unwrap())
            .collect::<Vec<MemoryLobbyExcel>>();
        let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
        let mut ser = serde_json::Serializer::with_formatter(Vec::new(), formatter);
        data.serialize(&mut ser).unwrap();
        String::from_utf8(ser.into_inner()).unwrap()
    }
}
