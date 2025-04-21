#!/bin/bash

API_URL=${1:-http://localhost:8000}

curl -X POST ${API_URL}/transactions/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-04-22",
    "description": "Pastelaria",
    "amount": 12.50
  }'