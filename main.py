from fastapi import FastAPI
import uvicorn
from stock_search import search
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/stock_search/{query}")
def read_item(query: str):
    return search(query)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
