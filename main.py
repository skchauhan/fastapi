from fastapi import FastAPI, Depends, Path, Form
from enum import Enum
from pydantic import BaseModel
import os
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/enum/{model_name}')
async def home(model_name: ModelName):
    print("all_model", list(ModelName))
    return {"message":"Hi, this is first api in fastapi", "model_name": model_name}

@app.get('/')
async def home():
    return {"message":"Hi, this is first api in fastapi"}

#Request Body
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

#set/get environment
@app.get('/env-variable')
async def get_enviornment_variable():
    my_name = os.getenv('path', 'Not Found')
    return {"env_variable": my_name}

def test():
    return {"name":"sunil", "address": "Noida"}

#annotated
@app.get('/annotated/')
def get_annoated_val(item: Annotated[str|int, "testing"]):
    return {"item": item}

#login user
@app.post('/login')
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password": password}

class FormData(BaseModel):
    username: str
    password: str

@app.post('/user-login')
def userLogin(data: Annotated[FormData, Form()]):
    return data
