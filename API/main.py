from fastapi import FastAPI
import uvicorn

app = FastAPI()

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    ID: Optional[int]
    username: Optional[str]
    password: Optional[str]


@app.get("/")
async def api_con():
    con = {"Start": "Success"}
    return con


@app.get("/name")
async def name():
    name = "Panatda Phomngam"
    return name


@app.get("/how_are_you")
async def how_are_you():
    txt = "Good"
    return txt


@app.get("/plus")
async def plus():
    txt = 30 + 320
    return txt


@app.get("/area")
async def area(h, w):
    area = float(w) * float(h)
    return area


@app.get("/area_2")
async def area_2(r):
    area = 3.14 * float(r) * float(r)
    return area


@app.post("/login")
async def login(username, password):
    user = "admin"
    pas = "admin"
    if username == user and pas == password:
        txt = "login succeses"
        return txt
    else:
        txt = "login fail"
        return txt


@app.post("/login_2")
async def login_2(user: User):
    u = "admin"
    pas = "admin"
    if user.username == u and pas == user.password:
        txt = "login succeses"
        return txt
    else:
        txt = "login fail"
        return txt


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
