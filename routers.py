import uvicorn
from constants import *
from fastapi import FastAPI
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


if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
