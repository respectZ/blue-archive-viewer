import json
import os

path = {
    "en": os.path.join(
        os.getcwd(),
        "public",
        "data",
        "en",
        "Preload",
        "TableBundles",
        "Excel"
    ),
    "jp": os.path.join(
        os.getcwd(),
        "public",
        "data",
        "jp",
        "TableBundles",
        "Excel"
    )
}


class TableJP:
    def __init__(self, basepath="") -> None:
        if basepath == "":
            self.path = path["jp"]
        else:
            self.path = basepath

        with open(os.path.join(self.path, "CharacterExcelTable.json"), "r", encoding="utf-8") as f:
            self.character = json.load(f)

        with open(os.path.join(self.path, "LocalizeCharProfileExcelTable.json"), "r", encoding="utf-8") as f:
            self.localize_char_profile = json.load(f)

    def localize_char_from_dev_name(self, dev_name: str):
        id = self.find_char_id_from_dev_name(dev_name)
        if id is None:
            return None
        for char in self.localize_char_profile:
            if char["CharacterId"] == id:
                return char["FullNameJp"]

    def find_char_id_from_dev_name(self, dev_name: str):
        for char in self.character:
            # Case insensitive
            if (char["DevName"].lower() == dev_name.lower()) and (char["IsPlayableCharacter"]):
                return char["Id"]
            if (char["ScenarioCharacter"].lower() == dev_name.lower()) and (char["IsPlayableCharacter"]):
                return char["Id"]
        return None


class TableEN(TableJP):
    def __init__(self) -> None:
        super().__init__(basepath=path["en"])

    def localize_char_from_dev_name(self, dev_name: str):
        id = self.find_char_id_from_dev_name(dev_name)
        if id is None:
            return None
        for char in self.localize_char_profile:
            if char["CharacterId"] == id:
                return " ".join([char["FamilyNameEn"], char["PersonalNameEn"]])
