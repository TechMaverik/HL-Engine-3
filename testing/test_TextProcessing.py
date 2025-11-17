import pytest
import sys
sys.path.append('HL_Engine_2') # Adjust system path as per requirement
from HL_Engine_2.HL_Engine_Text_Processing import TextProcessingEngine

@pytest.fixture
def Engine():
    Engine=TextProcessingEngine()
    return (Engine)

def test_search_wiki(Engine):
    data=Engine.search_wikipedia('football')
    assert data[0]=="F"

def test_extract_text_from_img(Engine):
    data=Engine.extract_text_from_image("quotes.jpg")
    assert data=="DREAMS DO COME TRUE"

def test_extract_words_from_sentence(Engine):   
    data=Engine.extract_words_from_sentence("I am great")
    assert data[0]=="I"
    assert data[1]=="am"
    assert data[2]=="great"

@pytest.mark.skip
def test_speech_recognition(Engine):
    data="Cannot be tested"    

def test_sentimental(Engine):
    score=Engine.sentimental_analysis("I am cool")
    assert int(score)>=1
    
def test_dictionary(Engine):
    data=Engine.dictionary("success")
    assert(str(data)=="{'Noun': ['an event that accomplishes its intended purpose', 'an attainment that is successful', 'a state of prosperity or fame', 'a person with a record of successes']}")






