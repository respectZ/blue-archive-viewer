import lib.TableEncryptionService as TableEncryptionService
from zipfile import ZipFile
import requests
import UnityPy
import base64
import json
import os


def NewEncryptString(value: str, key: bytes) -> str:
    if not value or len(value) < 8:
        return value.encode() if value else b""
    raw = value.encode("utf-16-le")
    return base64.b64encode(TableEncryptionService._XOR(raw, key)).decode()


class App:
    def __init__(self) -> None:
        self.URL = "https://d.apkpure.net/b/XAPK/com.YostarJP.BlueArchive?version=latest"

    def download_app(self, dest=os.path.join("temp")):
        '''
        Download the latest version of the app from apkpure.

        Dest is the path to the directory where the app will be downloaded.
        '''
        r = requests.get(self.URL, allow_redirects=True)
        self.filepath = os.path.join(dest, "BlueArchive.apk")
        open(self.filepath, 'wb').write(r.content)

    def extract_app(self):
        '''
        Extract the app.
        Extracts to "temp/" by default.

        Src is the filepath to the app file.
        Dest is the path to the directory to extract to.
        '''
        with ZipFile(self.filepath, 'r') as zipObj:
            zipObj.extractall(os.path.join("temp"))

    def extract_obb(self):
        src = ""
        for root, _, files in os.walk(os.path.join("temp", "Android")):
            for file in files:
                if file.endswith(".obb"):
                    src = os.path.join(root, file)
        with ZipFile(src, 'r') as zipObj:
            for file in zipObj.namelist():
                if file.startswith("assets/bin/Data/"):
                    zipObj.extract(file, os.path.join("temp"))

    def get_gameconfig(self):
        files = os.listdir(os.path.join("temp", "assets", "bin", "Data"))
        data = bytes()
        for a in files:
            file = os.path.join("temp", "assets", "bin", "Data", a)
            env = UnityPy.load(file)
            for obj in env.objects:
                if obj.type.name == "TextAsset":
                    d = obj.read()
                    if d.name == "GameMainConfig":
                        data = bytes(d.script)

        data = base64.b64encode(data)
        data = TableEncryptionService.ConvertString(
            data, TableEncryptionService.CreateKey("GameMainConfig")
        )
        data = json.loads(data)
        crypted_key = NewEncryptString(
            "ServerInfoDataUrl", TableEncryptionService.CreateKey(
                "ServerInfoDataUrl")
        )
        crypted_value = data[crypted_key]
        value = TableEncryptionService.ConvertString(
            crypted_value, TableEncryptionService.CreateKey(
                "ServerInfoDataUrl")
        )
        return value
