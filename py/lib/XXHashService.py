from typing import Union
from xxhash import xxh32_intdigest


def CalculateHash(name: Union[bytes, str]) -> int:
    if isinstance(name, str):
        name = name.encode("utf8")
    return xxh32_intdigest(name, 0)
