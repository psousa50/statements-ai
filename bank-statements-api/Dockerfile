FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY src ./src

EXPOSE 10000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "10000"]
