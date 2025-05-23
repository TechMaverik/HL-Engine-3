"""HLEngine3 Unitree Go2 Control System"""

from unitree_sdk2py.go2.sport.sport_client import SportClient


class HLEngineGo2RobotControlSystem:
    """HLEngine3 Go2 Robot Control System"""

    def __init__(self):
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

    def switch_gate_go2(self, param: bool):  # takes 0 or 1 as param
        self.go2_sports_client.SwitchGait(param)

    def balanced_stand_go2(self):
        self.go2_sports_client.BalanceStand()

    def recovery_stand_go2(self):
        self.go2_sports_client.RecoveryStand()
