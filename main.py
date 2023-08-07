from typing import Union
import pydapper
from dataclasses import dataclass
from fastapi import FastAPI
import os

app = FastAPI()

postgres_cs = os.environ['PTA_DATABASE_URL']
print(postgres_cs)
@dataclass
class Actor:
    actor_id: int
    first_name: str
    last_name: str
    last_update: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/actors")
def get_actors():
    with pydapper.connect(postgres_cs) as commands:
        data = commands.query("select * from actor", model=Actor)
        return data
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}