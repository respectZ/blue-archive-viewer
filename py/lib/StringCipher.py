from base64 import b64decode, b64encode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# String *__fastcall TextFileHelper_LoadEncryptedDataFile(String *fileName, String *decryptKey, MethodInfo *method)
# {
#   String *AllText; // x0

#   if ( (byte_70F27EB & 1) == 0 )
#   {
#     sub_1996CFC(78994LL, (__int64)decryptKey);
#     byte_70F27EB = 1;
#   }
#   AllText = File_ReadAllText(fileName, 0LL);
#   return StringCipher_Decrypt(AllText, decryptKey, 0LL);
# }

# // Namespace: MX.Core.Crypto.StringCipher
BlockSize: int = 128//8
Keysize: int = 128//8
DerivationIterations: int = 1000


def Encrypt(plainText: str, passPhrase: str) -> str:
    salt = get_random_bytes(0x10) # GenerateRandomEntropy
    iv = get_random_bytes(0x10) # GenerateRandomEntropy
    derived = PBKDF2(passPhrase, salt, 16, count=DerivationIterations)
    cipher = AES.new(key=derived[:16], iv=iv, mode=AES.MODE_CBC)
    data = pad(cipher.encrypt(plainText.encode("utf8")), BlockSize, style="pkcs7")
    return b64encode(salt + iv + data).decode("utf8")
    


def Decrypt(cipherText: str, passPhrase: str) -> str:
    rawCipherText = b64decode(cipherText)
    salt = rawCipherText[:16]
    iv = rawCipherText[16:32]
    rawCipherText = rawCipherText[32:]
    derived = PBKDF2(passPhrase, salt, 16, count=DerivationIterations)
    cipher = AES.new(key=derived[:16], iv=iv, mode=AES.MODE_CBC)
    return unpad(cipher.decrypt(rawCipherText), BlockSize, style="pkcs7").decode('utf-8')
    
# def GenerateRandomEntropy() -> bytes:
#     pass


def EncryptStringToBytes(plainText: str, Key: bytes, IV: bytes) -> bytes:
    # not sure about how the text is encoded, C# directly uses the charcode
    cipher = AES.new(key=Key, iv=IV, mode=AES.MODE_CBC)
    return pad(cipher.encrypt(plainText.encode("utf8")), BlockSize)


def DecryptStringFromBytes(cipherText: bytes, Key: bytes, IV: bytes) -> str:
    # not sure about how the text is encoded, C# directly uses the charcode
    cipher = AES.new(key=Key, iv=IV, mode=AES.MODE_CBC)
    return unpad(cipher.decrypt(cipherText), BlockSize).decode('utf-8')


def AESEncrypt256(Input: str, key: str) -> str:
    pass


def AESDecrypt256(Input: str, key: str) -> bytes:
    pass
