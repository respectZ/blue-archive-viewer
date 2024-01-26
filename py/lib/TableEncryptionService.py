from typing import Union
from struct import Struct
from . import XXHashService
from .MersenneTwister import MersenneTwister
from base64 import b64decode, b64encode

# from itertools import cycle
from Crypto.Util.strxor import strxor, strxor_c

uint32 = Struct("<I")
uint64 = Struct("<Q")
int32 = Struct("<i")
int64 = Struct("<q")
float32 = Struct("<f")
float64 = Struct("<d")


def CreateKey(name: str) -> bytes:  # 0x02AAE200-0x02AAE288
    # v3 = XXHashService_CalculateHash(name, 0LL);
    seed = XXHashService.CalculateHash(name)
    # v4 = sub_1996DC4(MersenneTwister__TypeInfo);
    # MersenneTwister__ctor_1(v4, v3, 0LL);
    return MersenneTwister(seed).NextBytes(8)


def XOR(name: str, data: bytes) -> bytes:
    seed = XXHashService.CalculateHash(name)
    twister = MersenneTwister(seed)
    key = twister.NextBytes(len(data))

    if len(data) >= 1:
        data = _XOR(data, key)
    return data


def _XOR(value: bytes, key: bytes) -> bytes:
    # return bytes(x ^ y for x, y in zip(value, key))
    if len(value) == len(key):
        return strxor(value, key)
    elif len(value) < len(key):
        return strxor(value, key[: len(value)])
    else:
        return b"".join(
            strxor(value[i: i + len(key)], key) for i in range(0, len(value) - len(key) + 1, len(key))
        ) + strxor(
            value[(len(value) - (len(value) % len(key))):],
            key[: len(value) % len(key)],
        )


def _XOR_Struct(value: Union[int, float], key: bytes, struct: str) -> Union[int, float]:
    return struct.unpack(_XOR(struct.pack(value), key))[0]


def ConvertInt(value: int, key: bytes) -> int:
    return _XOR_Struct(value, key, int32) if value else 0


def ConvertLong(value: int, key: bytes) -> int:
    return _XOR_Struct(value, key, int64) if value else 0


def ConvertUInt(value: int, key: bytes) -> int:
    return _XOR_Struct(value, key, uint32) if value else 0


def ConvertULong(value: int, key: bytes) -> int:
    return _XOR_Struct(value, key, uint64) if value else 0


def ConvertFloat(value: float, key: bytes) -> float:
    return ConvertInt(int(value), key) * 0.00001 if value else 0.0


def ConvertDouble(value: float, key: bytes) -> float:
    return ConvertLong(int(value), key) * 0.00001 if value else 0.0


def EncryptFloat(value: float, key: bytes) -> float:
    return ConvertInt(int(value * 100000), key) if value else 0.0


def EncryptDouble(value: str, key: bytes) -> str:
    return ConvertLong(int(value * 100000), key) if value else 0.0


def ConvertString(value: str, key: bytes) -> str:
    if not value:
        return ""

    # the animator table contain strings that are not base64 encoded
    try:
        raw = b64decode(value)
        return _XOR(raw, key).decode("utf16")
    except:
        return value.decode("utf8")


def EncryptString(value: str, key: bytes) -> str:
    if not value or len(value) < 8:
        return value.encode() if value else b""
    raw = value.encode("utf16")
    return b64encode(_XOR(raw, key)).decode()
    # return b64encode(bytes(r ^ k for r, k in zip(raw, cycle(key))))
