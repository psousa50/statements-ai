FROM python:3.11-slim

WORKDIR /app

# Install Poetry and system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files and source code before poetry install
COPY pyproject.toml poetry.lock ./
COPY README.md ./
COPY bank_statements_api ./bank_statements_api
RUN poetry install --no-interaction --no-ansi

EXPOSE 10000
CMD ["uvicorn", "bank_statements_api.main:app", "--host", "0.0.0.0", "--port", "10000"]
