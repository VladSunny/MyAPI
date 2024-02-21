from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


@app.get("/hello/")
def read_name(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)