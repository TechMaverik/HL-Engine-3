import sys
import pytest
sys.path.append('HL_Engine_2')
from HL_Engine_2.HL_Engine_Cipher import CipherEngine

@pytest.fixture
def Engine():
    Engine=CipherEngine()
    return Engine

def test_encrypt(Engine):    
    data=Engine.data_encryption("HL_Engine_2","HL_Engine_2\HL_Crypto\key.txt")
    assert "*.m'PIKPGmu" == data

def test_decryption(Engine):
    data=Engine.dataDecryption("*.m'PIKPGmu","HL_Engine_2\HL_Crypto\key.txt")
    assert "HL_Engine_2" == data