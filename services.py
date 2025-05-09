"""Services.py"""

from unitree.hlengine_go2 import HLEngineGo2RobotControlSystem


class Services:

    def __init__(self):

        try:
            HLEngineGo2RobotControlSystem()
        except:
            return None
