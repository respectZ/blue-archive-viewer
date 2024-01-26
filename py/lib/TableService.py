# from _typeshed import StrPath
from io import BytesIO
from typing import IO
from zipfile import ZipFile
import os
from .XXHashService import CalculateHash
from typing import Union
from .MersenneTwister import MersenneTwister
import base64


class TableZipFile(ZipFile):
    def __init__(self, file: Union[str, BytesIO], name: str = None) -> None:
        super().__init__(file)
        hash = CalculateHash(name if not isinstance(
            file, str) else os.path.basename(file))
        twister = MersenneTwister(hash)
        num = twister.NextBytes(15)
        self.password = base64.b64encode(num)

    def open(self, name: str, mode: str = "r", force_zip64=False):
        return super(self.__class__, self).open(
            name, mode, pwd=self.password, force_zip64=force_zip64
        )
