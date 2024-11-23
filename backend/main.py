from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from httpx import AsyncClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.client_chuck = AsyncClient(base_url="https://api.chucknorris.io")
    app.client_kanye = AsyncClient(base_url="https://api.kanye.rest")
    yield
    await app.client_chuck.aclose()
    await app.client_kanye.aclose()


app = FastAPI(lifespan=lifespan, root_path="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chuck")
async def readJoke(request: Request):
    client = request.app.client_chuck
    res = await client.get("/jokes/random")
    data = res.json()
    return data


@app.get("/kanye")
async def readTweet(request: Request):
    client = request.app.client_kanye
    res = await client.get("/")
    data = res.json()
    return data
