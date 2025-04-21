from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date
from decimal import Decimal
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from ..database import SessionLocal
from ..models import Transaction as TransactionModel

# In-memory store for steel thread (replace with DB integration)
# TRANSACTIONS = []

class TransactionCreate(BaseModel):
    date: date
    description: str
    amount: Decimal

    class Config:
        json_encoders = {
            Decimal: float
        }

class Transaction(TransactionCreate):
    id: UUID

router = APIRouter(prefix="/transactions", tags=["transactions"])

# Dependency for DB session
async def get_db():
    async with SessionLocal() as db:
        yield db

@router.post("/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(tx: TransactionCreate, db: AsyncSession = Depends(get_db)) -> Transaction:
    new_tx = TransactionModel(
        date=tx.date,
        description=tx.description,
        amount=tx.amount
    )
    db.add(new_tx)
    await db.commit()
    await db.refresh(new_tx)
    return Transaction(
        id=new_tx.id,
        date=new_tx.date,
        description=new_tx.description,
        amount=new_tx.amount
    )

@router.get("/", response_model=List[Transaction])
async def list_transactions(db: AsyncSession = Depends(get_db)) -> List[Transaction]:
    result = await db.execute(select(TransactionModel))
    txs = result.scalars().all()
    return [Transaction(
        id=tx.id,
        date=tx.date,
        description=tx.description,
        amount=tx.amount
    ) for tx in txs]
