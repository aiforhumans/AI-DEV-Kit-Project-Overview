FROM python:3.11-slim

WORKDIR /app

COPY ./main.py /app

RUN pip install --no-cache-dir fastapi uvicorn httpx

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
