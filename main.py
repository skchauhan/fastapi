from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

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
