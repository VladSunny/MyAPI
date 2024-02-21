from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


@app.get("/hello/")
def read_name(name: str):
    return {"message": f"Hello {name}"}
