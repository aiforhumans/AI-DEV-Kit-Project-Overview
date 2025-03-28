up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

restart:
	docker compose down && docker compose up --build

open:
	start http://localhost:8501

check:
	python check_status_autostart.py
