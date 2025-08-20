---
sidebar_position: 1
title: GET Methods
description: Complete FastAPI Setup & GET Methods Guide
---

# 🚀 Complete FastAPI Setup & GET Methods Guide

## 🎯 Overview

This comprehensive guide covers everything from setting up a FastAPI project to implementing sophisticated GET methods with path parameters, query parameters, and validation. Whether you're a beginner or looking to enhance your FastAPI skills, this guide provides detailed explanations, code examples, and best practices.

## 🛠️ **Part 1: Environment Setup & Project Structure**

### 🧪 **1. Virtual Environment Setup (Cross-Platform)**

```bash
# 📦 Install virtualenv (if not already installed)
pip install virtualenv

# 🏗️ Create virtual environment
virtualenv venv

# ⚡ Activate virtual environment
# Windows 🪟
venv\Scripts\activate

# macOS/Linux 🐧🍎
source venv/bin/activate

# ✅ Verify activation (should show (venv) in prompt)
which python  # Should point to venv/bin/python
```

**💡 Pro Tips:**
- Always use virtual environments to avoid dependency conflicts
- Use descriptive names for project-specific environments
- Consider using `python -m venv venv` as an alternative to virtualenv

### 📦 **2. Install Core Dependencies**

```bash
# 🚀 Install FastAPI and Uvicorn
pip install fastapi uvicorn

# 🔧 Additional useful packages
pip install python-multipart  # For file uploads
pip install python-dotenv     # For environment variables
pip install pydantic[email]    # Enhanced Pydantic validation

# 💾 Save dependencies for team collaboration
pip freeze > requirements.txt
```

### 📁 **3. Professional Project Structure**

```
fastapi_project/
│
├── 📄 main.py                 # Main application entry point
├── 📄 requirements.txt        # Project dependencies
├── 📁 app/                    # Application package
│   ├── 📄 __init__.py
│   ├── 📁 routers/           # Route modules
│   │   ├── 📄 __init__.py
│   │   ├── 📄 items.py
│   │   └── 📄 users.py
│   ├── 📁 models/            # Pydantic models
│   │   ├── 📄 __init__.py
│   │   └── 📄 item.py
│   ├── 📁 core/              # Core functionality
│   │   ├── 📄 __init__.py
│   │   └── 📄 config.py
│   └── 📁 utils/             # Utility functions
│       ├── 📄 __init__.py
│       └── 📄 helpers.py
├── 📁 tests/                 # Test modules
│   ├── 📄 __init__.py
│   └── 📄 test_main.py
├── 📁 static/                # Static files
├── 📁 templates/             # HTML templates (if needed)
└── 📁 venv/                  # Virtual environment
```

## 🎯 **Part 2: Core FastAPI Implementation**

### 🔧 **4. Main Application with Advanced Configuration**

```python
# main.py
from fastapi import FastAPI, Query, Path, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional, List
from enum import Enum
import uvicorn

# 🎨 Create FastAPI instance with metadata
app = FastAPI(
    title="📚 Advanced FastAPI Guide",
    description="🚀 Comprehensive FastAPI implementation with best practices",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# 🌐 Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔧 Predefined values using Enum for type safety
class ModelName(str, Enum):
    """🤖 Machine Learning model names with descriptions"""
    alexnet = "alexnet"    # Image classification
    resnet = "resnet"      # Residual networks
    lenet = "lenet"        # Classic CNN architecture
    transformer = "transformer"  # Attention-based models

class Category(str, Enum):
    """📦 Product categories for filtering"""
    electronics = "electronics"
    clothing = "clothing"
    books = "books"
    home_garden = "home_garden"
    sports = "sports"

# 🏠 Root endpoint with API information
@app.get("/", tags=["🏠 Home"])
async def root():
    """
    🎯 API Welcome endpoint
    
    Returns:
        dict: Welcome message and API information
    """
    return {
        "message": "🚀 Welcome to Advanced FastAPI Guide!",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "features": [
            "📍 Path Parameters with validation",
            "🔍 Query Parameters with constraints", 
            "🎯 Predefined values with Enums",
            "📊 Automatic API documentation",
            "🛡️ Built-in data validation"
        ]
    }
```

Continue reading for complete implementation details...