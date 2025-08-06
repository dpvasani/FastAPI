# FastAPI Server Starter Script
Write-Host "🚀 Starting FastAPI Server..." -ForegroundColor Green
Write-Host ""

# Activate virtual environment
& ".\venv\Scripts\Activate.ps1"

# Start the server
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000 