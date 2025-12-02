import uvicorn
from configurations import *
from fastapi import FastAPI
from datamodel.go2 import Go2
from go2_movement_services import Go2MovementServices as go2

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



if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
