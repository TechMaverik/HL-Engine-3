"""
HL_Engine_sR.py
Author:Akhil P Jacob
HLDynamic-Integrations
"""

import pygame
import pyttsx3
from gtts import gTTS
from playsound import playsound as play_music
import HL_CommonDependency


class AudioSpeechEngine:
    """SpeechEngine System"""

    def sound_player(self, sound_file_path):
        """Play sound"""
        try:
            play_music(sound_file_path)
        except:
            return False

    def save_audio(self, text_data, location):
        """Save to Audio"""
        try:
            language = "en"
            object = gTTS(text=text_data, lang=language, slow=False)
            object.save(location)
        except:
            return False

    def read_text(self, text_data):
        """Read text data"""
        try:
            engine = pyttsx3.init()
            engine.getProperty("rate")
            engine.setProperty("rate", HL_CommonDependency.RATE_OF_SPEECH)
            engine.say(text_data)
            engine.runAndWait()
        except:
            return False
