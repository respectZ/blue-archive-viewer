import requests
import re
import os


class BlueArchiveResourceEN:
    def __init__(self, group: str, resource_path: str, resource_size: int, resource_hash: str, full_url="") -> None:
        self.group = group
        self.resource_path = resource_path
        self.resource_size = resource_size
        self.resource_hash = resource_hash
        self.full_url = full_url

    def download(self, rootDir: str) -> None:
        '''
        Download resource to path.
        '''
        src = requests.get(self.full_url).content
        path = rootDir + self.resource_path
        # Create directory if not exists
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        # Write file
        with open(path, "wb") as f:
            f.write(src)


class BlueArchiveAPIEN:
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


api = BlueArchiveAPIEN()

print(api.resource_url)
