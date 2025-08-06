#!/usr/bin/env python3
"""
Start FastAPI server in debug mode with relaxed CSP
"""
import os
import subprocess
import sys

def main():
    print("🐛 Starting FastAPI Server in Debug Mode")
    print("=" * 50)
    
    # Set debug environment variable
    os.environ["DEBUG"] = "true"
    
    print("✅ Debug mode enabled")
    print("✅ Relaxed CSP policy applied")
    print("✅ Swagger UI should work without CSP errors")
    
    print("\n🌐 Access URLs:")
    print("   • Swagger Docs: http://127.0.0.1:8000/docs")
    print("   • ReDoc: http://127.0.0.1:8000/redoc")
    print("   • Home: http://127.0.0.1:8000/")
    
    print("\n🚀 Starting server...")
    print("   Press Ctrl+C to stop")
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--reload", 
            "--host", "127.0.0.1", 
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

if __name__ == "__main__":
    main() 