from fastapi import FastAPI
from enum import Enum

app = FastAPI()

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