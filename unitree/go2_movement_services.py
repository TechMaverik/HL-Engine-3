"""HL-Engine-Movement-Services"""

from unitree.hlengine_go2 import HLEngineGo2RobotControlSystem


class Go2MovementServices:

    def emergency_shutdown(self):
        HLEngineGo2RobotControlSystem().damp_go2()

    def standup(self):
        HLEngineGo2RobotControlSystem().stand_up_go2()

    def standdown(self):
        HLEngineGo2RobotControlSystem().stand_down_go2()

    def movement(self, x, y, z):
        HLEngineGo2RobotControlSystem().custom_movement_go2(x, y, z)

    def stop(self):
        HLEngineGo2RobotControlSystem().stop_movement_go2()

    def gate_mode(self, boolval):
        HLEngineGo2RobotControlSystem().switch_gate_go2(boolval)

    def balanced_stand(self):
        HLEngineGo2RobotControlSystem().balanced_stand_go2()

    def recovery_from_fall(self):
        HLEngineGo2RobotControlSystem().recovery_stand_go2()

    def left_flip_stunt(self):
        HLEngineGo2RobotControlSystem().left_flip_go2()

    def back_flip_stunt(self):
        HLEngineGo2RobotControlSystem().back_flip_go2()

    def free_walk(self):
        HLEngineGo2RobotControlSystem().free_walk_go2()

    def walk_stair(self):
        HLEngineGo2RobotControlSystem().walk_stair()

    def cross_step(self):
        HLEngineGo2RobotControlSystem().cross_step()

    def jump(self):
        HLEngineGo2RobotControlSystem().free_jump()


