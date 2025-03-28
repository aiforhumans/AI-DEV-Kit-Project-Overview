FROM python:3.11-slim

WORKDIR /app
COPY ./app.py /app

COPY ./healthcheck.py /app/healthcheck.py
 

RUN pip install --no-cache-dir streamlit

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
