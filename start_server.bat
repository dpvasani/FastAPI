@echo off
echo 🚀 Starting FastAPI Server...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the server
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

pause 