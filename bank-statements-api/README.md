# Bank Statements API (Steel Thread)

Minimal FastAPI backend for Steel Thread:
- PostgreSQL (Neon/Render)
- Endpoints: Create and list transactions
- Environment config via `.env`
- Tests: pytest

## Setup
- See `pyproject.toml` for dependencies
- Use `.env.development`, `.env.test`, `.env.production` for config

## Run
```bash
uvicorn src.main:app --reload
```

## Test
```bash
pytest
```
