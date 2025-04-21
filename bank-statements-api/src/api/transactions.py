from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date
from decimal import Decimal
from typing import List

# In-memory store for steel thread (replace with DB integration)
TRANSACTIONS = []

class TransactionCreate(BaseModel):
    date: date
    description: str
    amount: Decimal

class Transaction(TransactionCreate):
    id: UUID

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(tx: TransactionCreate) -> Transaction:
    new_tx = Transaction(id=uuid4(), **tx.dict())
    TRANSACTIONS.append(new_tx)
    return new_tx

@router.get("/", response_model=List[Transaction])
def list_transactions() -> List[Transaction]:
    return TRANSACTIONS
