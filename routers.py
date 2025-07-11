import uvicorn
from constants import *
from fastapi import FastAPI
from datamodel.go2 import Go2
from hlengine_services import Go2Services as go2

engine = FastAPI()


@engine.get("/")
def version():
    return VERSION

@engine.get("/go2_standup")
def go2_standup():
    go2().standup()

@engine.get("/go2_standdown")
def go2_standdown():
    go2().standdown()

@engine.get("/go2_forward")
def go2_forward():
    go2().movement(1, 0, 0)

@engine.get("/go2_left")
def go2_left():
    go2().movement(0, 1, 0)

@engine.get("/go2_rotate")
def go2_rotate():
    go2().movement(0, 0, 1)

@engine.get("/go2_move")
def go2_move(Go2: Go2):
    print(Go2.x, Go2.y, Go2.z)
    go2().movement(Go2.x, Go2.y, Go2.z)

@engine.get("/stop")
def stop():
    go2().stop()



if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
