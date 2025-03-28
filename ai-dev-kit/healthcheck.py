import streamlit as st
import requests
import socket

st.set_page_config(page_title="Healthcheck Dashboard", layout="wide")
st.title("🩺 AI DEV KIT - Healthcheck Dashboard")

SERVICES = {
    "FastAPI": "http://fastapi:8001",
    "n8n": "http://n8n:5678",
    "Qdrant": "http://qdrant:6333",
    "Streamlit": "http://localhost:8501",
}

def check_http_service(name, url):
    try:
        response = requests.get(url, timeout=2)
        return "🟢 UP", f"{response.status_code} OK"
    except Exception as e:
        return "🔴 DOWN", str(e)

def check_socket_service(name, host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return "🟢 UP", "Connected"
    except Exception as e:
        return "🔴 DOWN", str(e)

st.subheader("📡 Web Services")

for name, url in SERVICES.items():
    status, message = check_http_service(name, url)
    st.markdown(f"**{name}**: {status} — {message}")

st.subheader("🗄️ Backend Services")

sockets = [
    ("Postgres", "postgres", 5432),
    ("Redis", "redis", 6379),
]

for name, host, port in sockets:
    status, message = check_socket_service(name, host, port)
    st.markdown(f"**{name}**: {status} — {message}")
