import pytest
import sys
sys.path.append('HL_Engine_2') # Adjust system path as per requirement
from HL_Engine_2.HL_Engine_Audio_Processing import AudioSpeechEngine

@pytest.fixture
def Engine():
    Engine=AudioSpeechEngine()
    return (Engine)

def test_sound_player(Engine):
    data=Engine.sound_player("1pm.mp3")
    assert data != False

def test_save_audio(Engine):
    data=Engine.save_audio("I am Akhil","saved.mp3")
    assert data != False

def test_read_text(Engine):
    data=Engine.read_text("I am Akhil")
    assert data != False