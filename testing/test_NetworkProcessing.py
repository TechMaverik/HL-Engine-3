import pytest
import sys
sys.path.append('HL_Engine_2') # Adjust system path as per requirement
from HL_Engine_2.HL_Engine_Network_Processing import NetworkProcessEngine

@pytest.fixture
def Engine():
    Engine=NetworkProcessEngine()
    return (Engine)

@pytest.mark.skip
def test_scanWifi():
    Engine=NetworkProcessEngine()
    data=Engine.scan_wifi("10.30.2.92")
    assert data != False

