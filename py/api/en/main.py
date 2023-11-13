import requests
import re
import os
from lib.downloader import Downloader
import UnityPy
from PIL import ImageOps


class Resource:
    def __init__(self, **kwargs):
        self.group = kwargs["group"]
        self.resource_path = kwargs["resource_path"]
        self.resource_size = kwargs["resource_size"]
        self.resource_hash = kwargs["resource_hash"]
        self.base_url = kwargs["baseUrl"]
        self.downloader = Downloader()
        self.downloader.setOutPath("temp/")

    def getDownloadUrl(self):
        return f"{self.base_url}/{self.resource_path}"

    def setOutPath(self, path):
        self.out_path = path

    def download(self):
        self.downloader.download(self.getDownloadUrl())

    def setKeepSubDir(self, keepSubDir):
        self.downloader.setKeepSubDir(keepSubDir)

    @staticmethod
    def extractBundle(src: str, dest: str):
        env = UnityPy.load(src)
        os.makedirs(dest, exist_ok=True)
        for obj in env.objects:
            # Texture2D
            if obj.type.name == "Texture2D":
                data = obj.read()
                img = data.image
                img = ImageOps.flip(img)
                p = os.path.join(dest, data.name + ".png")
                img.save(p)
            elif obj.type.name == "TextAsset":
                data = obj.read()
                p = os.path.join(dest, data.name)
                with open(p, "wb") as f:
                    f.write(bytes(data.script))


class Api:
    def __init__(self) -> None:
        ps = "https://play.google.com/store/apps/details?id=com.nexon.bluearchive&hl=in&gl=US"
        url = "https://api-pub.nexon.com/patch/v1.1/version-check"
        body = {
            "market_game_id": "com.nexon.bluearchive",
            "language": "en",
            "advertising_id": "636a7b75-5516-427b-b140-45318d3d51f0",
            "market_code": "playstore",
            "country": "US",
            "sdk_version": "187",
            "curr_build_version": "1.36.120365",
            "curr_build_number": 120365,
            "curr_patch_version": 0  # 156
        }
        regex_version = r"\d{1}\.\d{2}\.\d{6}"
        # Update version
        ps_src = requests.get(ps).text
        version = re.search(regex_version, ps_src).group(0)

        # Update body
        body["curr_build_version"] = version
        body["curr_build_number"] = int(version.split(".")[-1])

        # Get resource url
        src = requests.post(url, json=body).json()
        self.resource_url = src["patch"]["resource_path"]
        base_url = "/".join(src["patch"]["resource_path"].split("/")[:-1])

        # Fetch resources
        self.resources = []

        r = requests.get(self.resource_url).json()
        self.resources = [Resource(**x, baseUrl=base_url)
                          for x in r["resources"]]
