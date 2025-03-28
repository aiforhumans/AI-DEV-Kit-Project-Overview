import socket
import requests
import subprocess
from datetime import datetime

LOG_FILE = "service_status.log"

services = [
    {"name": "FastAPI", "url": "http://localhost:8001", "compose_name": "fastapi"},
    {"name": "Streamlit", "url": "http://localhost:8501", "compose_name": "streamlit"},
    {"name": "n8n", "url": "http://localhost:5678", "compose_name": "n8n"},
    {"name": "Qdrant", "url": "http://localhost:6333", "compose_name": "qdrant"},
    {"name": "PostgreSQL", "host": "localhost", "port": 5432, "compose_name": "postgres"},
    {"name": "Redis", "host": "localhost", "port": 6379, "compose_name": "redis"},
    {"name": "LM Studio", "url": "http://localhost:1234", "compose_name": None}
]

def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except:
        return False

def check_url(url):
    try:
        r = requests.get(url, timeout=2)
        return r.status_code == 200 or r.status_code == 404
    except:
        return False

def status_icon(ok):
    return "🟢" if ok else "🔴"

def log_result(line):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} | {line}\n")

def auto_start_service(compose_name):
    if compose_name:
        subprocess.call(["docker", "compose", "start", compose_name])

print("\n🔍 Service Status Checker with Auto-Start\n")

for s in services:
    alive = False
    if "url" in s:
        alive = check_url(s["url"])
        display = f"{status_icon(alive)} {s['name']:<12} {s['url']}"
    elif "host" in s and "port" in s:
        alive = is_port_open(s["host"], s["port"])
        display = f"{status_icon(alive)} {s['name']:<12} {s['host']}:{s['port']}"

    print(display)
    log_result(display)

    if not alive and s.get("compose_name"):
        print(f"⏳ Trying to start {s['compose_name']} via Docker Compose...")
        auto_start_service(s["compose_name"])

print("\n✅ Done. Log saved to", LOG_FILE)
