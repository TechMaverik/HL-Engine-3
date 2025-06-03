import uvicorn
from constants import *
from fastapi import FastAPI


engine = FastAPI()


@engine.get("/")
def version():
    return VERSION


if __name__ == "__main__":
    uvicorn.run(APPLICATION, host=IP_ADDRESS, port=PORT, reload=True)
