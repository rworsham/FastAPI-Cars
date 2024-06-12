from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Cars(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cars/{car_id}")
def read_item(car_id: int, q: Union[str, None] = None):
    return {"car_id": car_id, "q": q}

@app.put("/cars/{car_id}")
def update_item(car_id: int, car: Cars):
    return {"car_name": car.name, "car_id": car_id}

@app.post("/cars/new/{car_id}")
def new_car(car_id: int, car: Cars):
