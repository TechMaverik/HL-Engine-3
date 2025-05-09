import uvicorn
from constants import *
from fastapi import FastAPI
from services import Services

engine = FastAPI()


@engine.get("/")
def version():
    return VERSION


@engine.get("/check_connection")
def check_connection():
    status = Services()
    return status


if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
