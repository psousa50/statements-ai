#!/bin/bash

curl -X POST http://localhost:8000/transactions/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-04-21",
    "description": "Coffee shop",
    "amount": 3.50
  }'