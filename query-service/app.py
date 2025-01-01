from fastapi import FastAPI
from elasticsearch import Elasticsearch
import uvicorn

app = FastAPI()
es = Elasticsearch("http://localhost:9200")

@app.get("/search")
def search(q: str):
    # A basic match query
    response = es.search(index="pages", query={"match": {"title": q}})
    return {
        "query": q,
        "results": response["hits"]["hits"]
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

