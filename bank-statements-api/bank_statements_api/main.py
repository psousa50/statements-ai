from fastapi import FastAPI
from .api import transactions
from .cors import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(transactions.router)
