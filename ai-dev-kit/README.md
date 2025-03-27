# 🧠 AI DEV Kit

A fully modular, containerized development environment for working with AI tools, agents, and automations — powered by Docker Compose.

---

## 📋 Project Summary

This project is a DIY AI Developer Kit that brings together key AI and automation tools in a single, unified Docker environment.

### ✅ What We've Done So Far:
- Set up **Docker Compose** with isolated services and persistent volumes
- Successfully integrated and launched:
  - ✅ LM Studio (running separately on Windows)
  - ✅ n8n automation platform
  - ✅ FastAPI backend
  - ✅ Streamlit frontend UI
  - ✅ LangChain container placeholder (idle)
  - ✅ Qdrant vector DB
- Created reusable launch tools (`Makefile` + `launch.ps1`)

### 🔮 What's Still To Come:
- ⏳ Add **PostgreSQL** and **Redis** databases for long-term memory and queuing
- ⏳ Integrate **LangChain** more deeply with FastAPI and LM Studio
- ⏳ Add **Portainer** for visual container management
- ⏳ Optional proxy layer with **NGINX** or **Traefik**
- ⏳ Add **JupyterLab** for in-browser experimentation
- ⏳ Build example apps that use agents + memory + vector search

The goal is to provide an all-in-one development kit for AI apps, with full control over data, logic, and user interface.

---

# 🧠 AI DEV Kit

A fully modular, containerized development environment for working with AI tools, agents, and automations — powered by Docker Compose.

---

## 🚀 What's Included

| Service       | Description                              | URL                          |
|---------------|------------------------------------------|------------------------------|
| LM Studio     | Local LLM API Server (Windows app)       | `http://localhost:1234`      |
| n8n           | Automation workflows                     | `http://localhost:5678/setup`|
| LangChain     | AI orchestration agent                   | *(idle container)*           |
| FastAPI       | Custom API layer                         | `http://localhost:8001/`     |
| Streamlit     | Interactive UI testing                   | `http://localhost:8501/`     |
| Qdrant        | Vector database                          | `http://localhost:6333/`     |
| PostgreSQL    | Relational database                      | Internal only                |
| Redis         | Caching & queuing                        | Internal only                |

---

## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/aiforhumans/AI-DEV-Kit-Project-Overview.git
cd AI-DEV-Kit-Project-Overview/ai-dev-kit
```

### 2. Setup Environment Variables

```bash
cp .env.example .env
```

Edit `.env` if you want to change default ports or credentials.

---

### 3. Start Everything

#### On Linux/macOS/WSL:

```bash
make up
```

#### On Windows PowerShell:

```powershell
.\launch.ps1
```

---

## 🧱 Folder Structure

```
ai-dev-kit/
├── docker-compose.yml
├── .env / .env.example
├── Makefile / launch.ps1
├── fastapi-app/
│   ├── Dockerfile
│   └── main.py
├── streamlit-app/
│   ├── Dockerfile
│   └── app.py
├── langchain/
│   ├── Dockerfile
│   └── main.py (placeholder)
├── n8n/
│   └── config/
├── vector-db/
├── postgres/
├── redis/
└── proxy/
```

---

## 📦 Build Individual Services (Optional)

```bash
docker compose build fastapi
docker compose build streamlit
```

---

## 📌 Notes

- LM Studio is expected to be running on Windows separately
- Uses `host.docker.internal:1234` to connect from containers
- Built for local dev; not hardened for production

---

## 🧠 Credits

Created with ❤️ by [@aiforhumans](https://github.com/aiforhumans)

MIT License
