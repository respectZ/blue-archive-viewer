from Crypto.Cipher import AES

# Namespace: MX.Data AESEncryptionService
AESKey: bytes = "GameDevelopmentDepartment".encode("utf8")
AESIV: bytes = "TendouAris".encode("utf8")

def EncryptStringToBytes_Aes(plainText: str, Key: bytes, IV: bytes) -> bytes:
    # same as StringCipher?
    pass


def DecryptStringFromBytes_Aes(cipherText: bytes, Key: bytes, IV: bytes) -> str:
    # same as StringCipher?
    pass
