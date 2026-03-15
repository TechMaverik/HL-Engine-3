import uvicorn
from configurations import *
from fastapi import FastAPI
from datamodel.go2 import Go2
from unitree.go2_movement_services import Go2MovementServices as go2
from unitree.hlengine_g1 import HLEngineG1RobotControlSystem as g1_arm

engine = FastAPI()

@engine.get("/")
def version():
    return VERSION

@engine.post("/go2_standup")
def go2_standup():
    go2().standup()

@engine.post("/go2_standdown")
def go2_standdown():
    go2().standdown()

@engine.post("/go2_forward")
def go2_forward():
    go2().movement(1, 0, 0)

@engine.post("/go2_backward")
def go2_backward():
    go2().movement(-1, 0, 0)

@engine.post("/go2_left")
def go2_left():
    go2().movement(0, 1, 0)

@engine.post("/go2_right")
def go2_right():
    go2().movement(0, -1, 0)

@engine.post("/go2_rotate_left")
def go2_rotate_left():
    go2().movement(0, 0, 1)

@engine.post("/go2_rotate_right")
def go2_rotate_right():
    go2().movement(0, 0, -1)

@engine.post("/stop")
def stop():
    go2().stop()

@engine.post("/g1_release_arm")
def g1_releasearm():
    g1_arm().release_arm()

@engine.post("/g1_shakehands")
def g1_shakehands():
    g1_arm().shake_hand()

@engine.post("/g1_highfive")
def g1_highfive():
    g1_arm().high_five()

@engine.post("/g1_hug")
def g1_hug():
    g1_arm().hug()

@engine.post("/g1_highwave")
def g1_highwave():
    g1_arm().high_wave()

@engine.post("/g1_claps")
def g1_claps():
    g1_arm().clap()

@engine.post("/g1_facewave")
def g1_facewave():
    g1_arm().face_wave()

@engine.post("/g1_leftkiss")
def g1_leftkiss():
    g1_arm().left_kiss()

@engine.post("/g1_rightkiss")
def g1_leftkiss():
    g1_arm().right_kiss()

@engine.post("/g1_heart")
def g1_heart():
    g1_arm().heart()

@engine.post("/g1_handsup")
def g1_handsup():
    g1_arm().hands_up()

@engine.post("/g1_reject")
def g1_reject():
    g1_arm().reject()

@engine.post("/g1_twokiss")
def g1_twokiss():
    g1_arm().two_hand_kiss()


if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
