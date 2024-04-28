from table_dumper.jp.flat_data.CharacterDialogExcel import CharacterDialogExcel
from table_dumper.jp.flat_data.Enum import ProductionStep, DialogCategory, DialogCondition, Anniversary, DialogType, CVCollectionType
import sqlite3
import struct


def create_character_dialog_excel_table(path_to_excelDb: str):
    conn = sqlite3.connect(path_to_excelDb)
    cursor = conn.cursor()
    cursor.execute("SELECT Bytes FROM CharacterDialogDBSchema")
    data = cursor.fetchall()

    result = []
    for i in range(len(data)):
        b = data[i][0]

        # Offset is int8
        offset = struct.unpack("b", b[0:1])[0]

        c = CharacterDialogExcel()
        c.Init(b, offset)

        d = {
            "CharacterId": c.CharacterId(),
            "CostumeUniqueId": c.CostumeUniqueId(),
            "DisplayOrder": c.DisplayOrder(),
            "ProductionStep": ProductionStep(c.ProductionStep()).name,
            "DialogCategory": DialogCategory(c.DialogCategory()).name,
            "DialogCondition": DialogCondition(c.DialogCondition()).name,
            "Anniversary": Anniversary(c.Anniversary()).name,
            "StartDate": c.StartDate().decode("utf-8"),
            "EndDate": c.EndDate().decode("utf-8"),
            "GroupId": c.GroupId(),
            "DialogType": DialogType(c.DialogType()).name,
            "ActionName": c.ActionName().decode("utf-8"),
            "Duration": c.Duration(),
            "AnimationName": c.AnimationName().decode("utf-8"),
            "LocalizeKR": c.LocalizeKR().decode("utf-8"),
            "LocalizeJP": c.LocalizeJP().decode("utf-8"),
            "VoiceId": [c.VoiceId(j) for j in range(c.VoiceIdLength())],
            "ApplyPosition": c.ApplyPosition(),
            "PosX": c.PosX(),
            "PosY": c.PosY(),
            "CollectionVisible": c.CollectionVisible(),
            "CVCollectionType": CVCollectionType(c.CVCollectionType()).name,
            "UnlockFavorRank": c.UnlockFavorRank(),
            "UnlockEquipWeapon": c.UnlockEquipWeapon(),
            "LocalizeCVGroup": c.LocalizeCVGroup().decode("utf-8")
        }
        result.append(d)

    return result
