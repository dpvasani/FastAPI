from fastapi import FastAPI, Query
from typing import Optional
from enum import Enum

app = FastAPI()

# 🧩 Predefined Path Parameter using Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# ✅ Basic GET Method with Path Parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# ✅ Path Parameter with Predefined Values
@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeNet is classic!"}
    return {"model_name": model_name, "message": "ResNet Rocks!"}

# ✅ With Query Parameters (Optional + Defaults)
@app.get("/products/")
def get_products(skip: int = 0, limit: int = 10, category: Optional[str] = Query(None, min_length=3)):
    return {
        "message": "Fetching products",
        "skip": skip,
        "limit": limit,
        "category": category or "all"
    }
