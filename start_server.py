#!/usr/bin/env python3
"""
Simple script to start the FastAPI server and provide clear instructions
"""
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def main():
    print("🚀 FastAPI Server Starter")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("main.py").exists():
        print("❌ Error: main.py not found. Please run this script from the FastAPI project directory.")
        sys.exit(1)
    
    print("✅ Found main.py")
    
    # Check if virtual environment exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Error: Virtual environment not found. Please create it first.")
        sys.exit(1)
    
    print("✅ Found virtual environment")
    
    print("\n📋 Server Information:")
    print("   Host: http://127.0.0.1:8000")
    print("   Swagger Docs: http://127.0.0.1:8000/docs")
    print("   ReDoc: http://127.0.0.1:8000/redoc")
    print("   OpenAPI JSON: http://127.0.0.1:8000/openapi.json")
    
    print("\n🔧 Available Endpoints:")
    print("   • / - Home page")
    print("   • /health - Health check")
    print("   • /docs - Swagger documentation")
    print("   • /middleware-demo/ - Middleware demo")
    print("   • /templates/products/{id} - Product page")
    print("   • /blog/* - Blog endpoints")
    print("   • /user/* - User endpoints")
    
    print("\n🚀 Starting server...")
    print("   Press Ctrl+C to stop the server")
    print("   Open your browser to http://127.0.0.1:8000/docs")
    
    try:
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--reload", 
            "--host", "127.0.0.1", 
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 