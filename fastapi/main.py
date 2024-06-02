from fastapi import FastAPI,HTTPException
import uvicorn

from pydantic import BaseModel

#Extend the BaseModel to create an Item class
class Item(BaseModel):
    text: str = None
    is_done: bool = False

# create new app
app = FastAPI()

items = []

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

#smart api is smart enough to convert string to int of limit value from request
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}" , response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404,detail=f"Item {item_id} not found")

# app decorator , it defines the path for the HTTP GET method
@app.get("/")
def root():
    return {"Hello": "World"}

if __name__ == "__main__":
   # run the app on localhost at port 8006
   uvicorn.run(app, host="localhost", port=8006)