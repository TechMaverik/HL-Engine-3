"""HLEngine3 Unitree Go2 Control System"""

from configurations import *
from unitree_sdk2py.go2.sport.sport_client import SportClient
from unitree_sdk2py.core.channel import ChannelFactoryInitialize


class HLEngineGo2RobotControlSystem:
    """HL-Engine-3 Go2 Robot Control System"""

    def __init__(self):
        try:
            ChannelFactoryInitialize(0, NETWORK_INTERFACE)
        except:
            pass
        self.go2_sports_client = SportClient()
        self.go2_sports_client.SetTimeout(25.0)
        self.go2_sports_client.Init()

    def damp_go2(self):
        self.go2_sports_client.Damp()

    def stand_up_go2(self):
        self.go2_sports_client.StandUp()

    def stand_down_go2(self):
        self.go2_sports_client.StandDown()

    def custom_movement_go2(self, x: float, y: float, z: float):
        self.go2_sports_client.Move(x, y, z)

    def stop_movement_go2(self):
        self.go2_sports_client.StopMove()

    def switch_gate_go2(self, param: bool):
        self.go2_sports_client.SwitchGait(param)

    def balanced_stand_go2(self):
        self.go2_sports_client.BalanceStand()

    def recovery_stand_go2(self):
        self.go2_sports_client.RecoveryStand()

    def left_flip_go2(self):
        self.go2_sports_client.LeftFlip()

    def back_flip_go2(self):
        self.go2_sports_client.BackFlip()

    def free_walk_go2(self):
        self.go2_sports_client.FreeWalk(True)

    def walk_stair(self, status):
        self.go2_sports_client.WalkStair(status)

    def walk_upright(self, status):
        self.go2_sports_client.WalkUpright(status)

    def cross_step(self, status):
        self.go2_sports_client.CrossStep(status)

    def free_jump(self, status):
        self.go2_sports_client.FreeJump(status)
