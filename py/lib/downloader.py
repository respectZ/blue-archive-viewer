import requests
import os


class Downloader:
    def __init__(self) -> None:
        self.outPath = ""
        self.keepSubDir = False

    def setOutPath(self, path: str) -> None:
        self.outPath = path

    def setKeepSubDir(self, keepSubDir: bool) -> None:
        self.keepSubDir = keepSubDir

    def download(self, url: str, filename="") -> None:
        '''
        Download file from url to path.

        Args:
        filename: If not specified, the filename will be the last part of the url.
        '''
        src = requests.get(url).content
        dest = self.outPath
        # Create directory if not exists
        if filename == "":
            filename = url.split("/")[-1]
        if self.keepSubDir:
            dest += "/".join(url.split("/")[-4:-1]) + "/"
        dest += filename
        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))
        # Write file
        with open(dest, "wb") as f:
            f.write(src)
