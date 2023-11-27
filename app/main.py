from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from model import generate


app = FastAPI()

class Item(BaseModel):
    text: str

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")

@app.post("/generate")
def read_root(item: Item):
    question = generate(item.text)
    return {"question": f"{question}"}
