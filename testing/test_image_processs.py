import pytest
import sys
sys.path.append('HL_Engine_2') # Adjust system path as per requirement
from HL_Engine_2.HL_Engine_Image_Processing import ImageProcessingEngine

@pytest.fixture
def Engine():
    Engine=ImageProcessingEngine()
    return (Engine)

def test_takePic(Engine):
    data=Engine.take_picture("Kooch.jpg","Kushum",0)
    assert data != False

def test_showImage(Engine):
    data=Engine.show_image("Kooch.jpg","Kushum")
    assert data != False

def test_object_from_video(Engine):
    data=Engine.track_object_from_video("HL_Engine_2\HL_Cascades\haarcascade_frontalface_default.xml",0,"Kushum_Video","")
    assert data != False

def test_stabilize_camera(Engine):
    data=Engine.stabilize_camera_input(0)
    assert data != False

def test_element_from_image(Engine):
    data=Engine.track_element_from_image("Kooch.jpg","bag.png","result.jpg")
    assert data != False