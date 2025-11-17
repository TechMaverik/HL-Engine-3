"""
HL_Engine_Cipher.py
Author:Akhil P Jacob
HLDynamic-Integrations
"""
from HL_CommonDependency import *
import string


class CipherEngine:
    """Cipher Engine"""

    def data_encryption(self, data_to_encrypt, key_path):
        """Data Encryption"""
        if key_path == "":
            key_path = ENCRYPTION_PATH
        keyLoader = open(key_path, "r")
        key = keyLoader.read()
        dataModel = []
        ASCER = string.printable
        for i in ASCER:
            dataModel.append(i)
        keyModel = str(key)
        Position_Generator = []
        Data = str(data_to_encrypt)
        for i in Data:
            if i in Data:
                Position = dataModel.index(i)
                Position_Generator.append(Position)
        encrypt = []
        stringer = ""
        for i in Position_Generator:
            data = keyModel[i]
            encrypt.append(data)
        encrypted = stringer.join(encrypt)
        return encrypted

    def dataDecryption(self, data_to_decrypt, key_path):
        """Data Decryption"""
        if key_path == "":
            key_path = ENCRYPTION_PATH
        data = str(data_to_decrypt)
        dataModel = []
        ASCER = string.printable
        for i in ASCER:
            dataModel.append(i)
        keyLoader = open(key_path, "r")
        key = keyLoader.read()
        keyModel = str(key)
        decrypt = []
        decryption = []
        stringer = ""
        for i in data:
            if i in keyModel:
                position = keyModel.index(i)
                decrypt.append(position)
        for i in decrypt:
            decode = dataModel[i]
            decryption.append(decode)

        decrypted = stringer.join(decryption)
        return decrypted
