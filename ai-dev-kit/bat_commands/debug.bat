@echo off
python check_status_autostart.py || echo Debug failed
call docker-compose ps
call docker-compose logs --tail=30
