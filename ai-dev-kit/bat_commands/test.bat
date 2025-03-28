@echo off
curl -s http://localhost:8001/ping || echo FastAPI test failed
curl -s http://localhost:8501 || echo Streamlit test failed
