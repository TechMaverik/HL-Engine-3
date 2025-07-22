import sys
import time
from dataclasses import dataclass
from configuration import *
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.g1.arm.g1_arm_action_client import G1ArmActionClient
from unitree_sdk2py.g1.arm.g1_arm_action_client import action_map


class HLEngineG1RobotControlSystem:
    """HL-Engine-3 G1 Robot Control System"""

    def __init__(self):
        try:
            ChannelFactoryInitialize(0, NETWORK_INTERFACE)
        except:
            pass
        self.g1_arm = G1ArmActionClient()
        self.g1_arm.SetTimeout(10.0)
        self.g1_arm.Init()

    def release_arm(self):
        self.g1_arm.ExecuteAction(action_map.get("release arm"))

    def shake_hand(self):
        self.g1_arm.ExecuteAction(action_map.get("shake hand"))
        time.sleep(2)
        self.release_arm()

    def high_five(self):
        self.g1_arm.ExecuteAction(action_map.get("high five"))
        time.sleep(2)
        self.release_arm()

    def hug(self):
        self.g1_arm.ExecuteAction(action_map.get("hug"))
        time.sleep(2)
        self.release_arm()

    def high_wave(self):
        self.g1_arm.ExecuteAction(action_map.get("high wave"))
        time.sleep(2)
        self.release_arm()

    def clap(self):
        self.g1_arm.ExecuteAction(action_map.get("clap"))
        time.sleep(2)
        self.release_arm()

    def face_wave(self):
        self.g1_arm.ExecuteAction(action_map.get("face wave"))
        time.sleep(2)
        self.release_arm()

    def left_kiss(self):
        self.g1_arm.ExecuteAction(action_map.get("left kiss"))
        time.sleep(2)
        self.release_arm()

    def heart(self):
        self.g1_arm.ExecuteAction(action_map.get("heart"))
        time.sleep(2)
        self.release_arm()

    def right_heart(self):
        self.g1_arm.ExecuteAction(action_map.get("right heart"))
        time.sleep(2)
        self.release_arm()

    def hands_up(self):
        self.g1_arm.ExecuteAction(action_map.get("hands up"))
        time.sleep(2)
        self.release_arm()

    def right_hand_up(self):
        self.g1_arm.ExecuteAction(action_map.get("right hand up"))
        time.sleep(2)
        self.release_arm()

    def reject(self):
        self.g1_arm.ExecuteAction(action_map.get("reject"))
        time.sleep(2)
        self.release_arm()

    def right_kiss(self):
        self.g1_arm.ExecuteAction(action_map.get("right kiss"))
        time.sleep(2)
        self.release_arm()

    def two_hand_kiss(self):
        self.g1_arm.ExecuteAction(action_map.get("two-hand kiss"))
        time.sleep(2)
        self.release_arm()
