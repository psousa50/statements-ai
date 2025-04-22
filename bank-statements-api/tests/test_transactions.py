import pytest
from fastapi.testclient import TestClient
from bank_statements_api.main import app

client = TestClient(app)

def test_create_and_list_transactions():
    # Create transaction
    payload = {
        "date": "2024-01-01",
        "description": "Test Transaction",
        "amount": 123.45
    }
    resp = client.post("/transactions/", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["description"] == "Test Transaction"
    assert data["amount"] == 123.45
    assert "id" in data

    # List transactions
    resp2 = client.get("/transactions/")
    assert resp2.status_code == 200
    txs = resp2.json()
    assert any(tx["id"] == data["id"] for tx in txs)
