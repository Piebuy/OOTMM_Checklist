@echo off
cd /d "%~dp0"

call .venv\Scripts\activate.bat

start "Flask App" cmd /k python app.py
start "Main Program" cmd /k python main.py

