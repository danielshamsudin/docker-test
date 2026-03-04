from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample data model
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }