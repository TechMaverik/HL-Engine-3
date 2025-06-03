"""Services.py"""

from unitree.hlengine_go2 import HLEngineGo2RobotControlSystem


class Services:

    def emergency_shutdown(self):
        HLEngineGo2RobotControlSystem().damp_go2()

    def standup(self):
        HLEngineGo2RobotControlSystem().stand_up_go2()
