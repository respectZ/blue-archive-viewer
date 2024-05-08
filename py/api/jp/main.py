import requests
import re
import os
from lib.downloader import Downloader
from .updater import App
from PIL import ImageOps
import UnityPy


URL = "https://yostar-serverinfo.bluearchiveyostar.com/r67_jjjg51ngucokd90cuk4l.json"

# TODO: Update tablebundles and mediaresources since they changed into .bytes instead of json response.


class MediaResource:
    def __init__(self, name="", mediaType=0, path="", fileName="", bytes=0, crc=0, isPrologue=False, isSplitDownload=False, baseUrl=""):
        self.name = name
        self.mediaType = mediaType
        self.path = path
        self.fileName = fileName
        self.bytes = bytes
        self.crc = crc
        self.isPrologue = isPrologue
        self.isSplitDownload = isSplitDownload
        self.baseUrl = baseUrl
        self.downloader = Downloader()

    def getDownloadUrl(self):
        return f"{self.baseUrl}/MediaResources/{self.path}"

    def download(self):
        self.downloader.download(self.getDownloadUrl(), self.fileName)

    def setOutPath(self, path):
        self.downloader.setOutPath(path)

    def setKeepSubDir(self, keepSubDir):
        self.downloader.setKeepSubDir(keepSubDir)


class Bundle:
    def __init__(self, name="", size=0, isPrologue=False, crc=1, isSplitDownload=False, baseUrl=""):
        self.name = name
        self.size = size
        self.isPrologue = isPrologue
        self.crc = crc
        self.isSplitDownload = isSplitDownload
        self.baseUrl = baseUrl

        self.downloader = Downloader()
        self.downloader.setOutPath("temp/")

    def getDownloadUrl(self):
        return f"{self.baseUrl}/Android/{self.name}"

    def download(self):
        self.downloader.download(self.getDownloadUrl())

    def setOutPath(self, path):
        self.downloader.setOutPath(path)

    @staticmethod
    def extract(src: str, dest: str):
        '''
        Extract bundle to dest.
        Src is the path to the bundle file.
        Dest is the path to the directory to extract to.

        Example:
        extractBundle("temp/bundle.bundle", "temp/extracted/")
        '''
        env = UnityPy.load(src)
        os.makedirs(dest, exist_ok=True)
        for obj in env.objects:
            # Texture2D
            if obj.type.name == "Texture2D":
                data = obj.read()
                img = data.image
                # img = ImageOps.flip(img) # We don't need to flip the image for JP.
                p = os.path.join(dest, data.name + ".png")
                img.save(p)
            # TextAsset, particularly for .skel and .atlas files
            elif obj.type.name == "TextAsset":
                data = obj.read()
                p = os.path.join(dest, data.name)
                with open(p, "wb") as f:
                    f.write(bytes(data.script))


class TableBundle:
    def __init__(self, name: str, size: int, crc: int, isInbuild: bool, isChanged: bool, isPrologue: bool, isSplitDownload: bool, baseUrl: str):
        self.name = name
        self.size = size
        self.crc = crc
        self.isInbuild = isInbuild
        self.isChanged = isChanged
        self.isPrologue = isPrologue
        self.isSplitDownload = isSplitDownload
        self.baseUrl = baseUrl

        self.downloader = Downloader()
        self.downloader.setOutPath("temp/")

    def getDownloadUrl(self):
        return f"{self.baseUrl}/TableBundles/{self.name}"

    def download(self):
        self.downloader.download(self.getDownloadUrl())

    def setOutPath(self, path):
        self.downloader.setOutPath(path)

    def setKeepSubDir(self, keepSubDir):
        self.downloader.setKeepSubDir(keepSubDir)


class Api:
    def __init__(self, url=URL):
        self.URL = URL

    def updateUrlFromCache(self):
        '''
        Update URL from cached temp.
        '''
        app = App()
        apkFile = os.path.join("temp", "BlueArchive.apk")
        if not os.path.exists(apkFile):
            return
        self.URL = app.get_gameconfig()

    def updateURL(self):
        app = App()
        app.download_app()
        app.extract_app()
        self.URL = app.get_gameconfig()

    def getBundleInfo(self):
        '''
        Returns a list of Bundle objects.
        '''
        s = requests.get(self.URL).json()

        baseUrl = s["ConnectionGroups"][0]["OverrideConnectionGroups"][1]["AddressablesCatalogUrlRoot"]
        address = f"{baseUrl}/Android/bundleDownloadInfo.json"

        data = requests.get(address).json()

        r = [Bundle(i["Name"], i["Size"], i["IsPrologue"], i["Crc"],
                    i["IsSplitDownload"], baseUrl) for i in data["BundleFiles"]]

        return r

    def getMediaResources(self) -> list[MediaResource]:
        '''
        Returns a list of MediaResource objects.
        '''
        s = requests.get(self.URL).json()

        baseUrl = s["ConnectionGroups"][0]["OverrideConnectionGroups"][1]["AddressablesCatalogUrlRoot"]
        address = f"{baseUrl}/MediaResources/MediaCatalog.json"

        data = requests.get(address).json()
        r = []

        tables = data["Table"]

        for k, v in tables.items():
            r.append(MediaResource(k, v["MediaType"], v["path"], v["FileName"],
                     v["Bytes"], v["Crc"], v["IsPrologue"], v["IsSplitDownload"], baseUrl))

        return r

    def getTableBundles(self) -> list[TableBundle]:
        '''
        Returns a list of TableBundle objects.
        '''
        s = requests.get(self.URL).json()

        baseUrl = s["ConnectionGroups"][0]["OverrideConnectionGroups"][1]["AddressablesCatalogUrlRoot"]
        address = f"{baseUrl}/TableBundles/TableCatalog.json"

        data = requests.get(address).json()
        r = []

        tables = data["Table"]

        for k, v in tables.items():
            r.append(TableBundle(k, v["Size"], v["Crc"], v["isInbuild"],
                                 v["isChanged"], v["IsPrologue"], v["IsSplitDownload"], baseUrl))

        return r

    def saveMediaCatalog(self, out="temp/"):
        '''
        Download MediaCatalog.json.
        '''
        s = requests.get(self.URL).json()

        baseUrl = s["ConnectionGroups"][0]["OverrideConnectionGroups"][1]["AddressablesCatalogUrlRoot"]
        address = f"{baseUrl}/MediaResources/MediaCatalog.json"

        data = requests.get(address).text

        with open(os.path.join(out, "MediaCatalog.json"), "w") as f:
            f.write(data)
