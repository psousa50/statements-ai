from fastapi import FastAPI
from .api import transactions

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(transactions.router)
