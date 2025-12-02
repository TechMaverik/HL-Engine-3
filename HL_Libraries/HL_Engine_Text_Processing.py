"""
HL_Engine_Text_Processing.py
Author:Akhil P Jacob
HLDynamic-Integrations
"""
import pytesseract
import os
import wikipedia
import base64
import nltk
import speech_recognition as sr
from PyDictionary import PyDictionary
from PIL import Image, ImageEnhance, ImageFilter
from textblob import TextBlob


class TextProcessingEngine:
    """ Text Processing Engine"""
    
    def search_wikipedia(self,content_to_search):
        """search wikipedia for contents"""
        try:
            return(wikipedia.summary(content_to_search))
        except:
            return ("HLEngine:Error in executing search_wikipedia....")    
        
    def extract_text_from_image(self,image_path):
        """ extract text from image """
        try:
            img = Image.open(image_path)
            img = img.convert('RGBA')
            pix = img.load()
            text = pytesseract.image_to_string(Image.open(image_path))
            return(text)
        except:
            return ("HLEngine: Make sure tesseract ocr is installed for deb:'sudo apt install tesseract-ocr -y','sudo apt install tesseract-ocr-all -y'")

    def extract_words_from_sentence(self,sentence_param): #Tested OK
        """extract words from sentence"""
        try:
            sentence=str(sentence_param)
            first, middle, last = sentence_param.split()           
            return(first,middle,last)
        except:
            return ("HLEngine:Error in executing extract_words_from_sentence....")

    def extract_words_from_speech(self):
        """speech recognition"""
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
            try:
                print("HLEngine:You said: " + r.recognize_google(audio))
                content = r.recognize_google(audio)
                return(content)

            except sr.UnknownValueError:
                return ("HLEngine:Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                return ("HLEngine:Could not request results from Google Speech Recognition service; {0}".format(e))
        except:
            return ('HLEngine:microphone not connected')

    def sentimental_analysis(self,data_string): 
        """sentimental analysis"""
        try:
            score=TextBlob(data_string)
            return(score)
        except:
            return("HLEngine: Issue found")

    def dictionary(self,to_search):
        try:           
            meaning = PyDictionary().meaning(to_search)
            return (meaning)
        except:
            return ("HLEngine:Error in executing dict")