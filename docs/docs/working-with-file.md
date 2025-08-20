---
sidebar_position: 10
title: Working With Files
description: FastAPI File Handling
---

# 📁 FastAPI File Handling 

## 🚀 Overview

FastAPI provides powerful and flexible file handling capabilities that allow developers to upload, download, and serve files efficiently. This documentation covers all aspects of file management with detailed code explanations, flow diagrams, and best practices.

## 📤 1. Uploading Files in FastAPI

FastAPI offers **two primary approaches** for handling file uploads, each suited for different use cases:

### ✅ **Option 1: Using `bytes`**

```python
from fastapi import FastAPI, File
from typing import List

app = FastAPI()

@app.post("/upload-bytes/")
def upload_bytes(file: bytes = File(...)):
    """
    📝 Handle file upload using bytes
    
    Args:
        file (bytes): Raw file content as bytes object
        
    Returns:
        dict: Processed file content split into lines
    """
    try:
        # 🔄 Decode bytes to UTF-8 string
        content = file.decode('utf-8')
        
        # ✂️ Split content into individual lines
        lines = content.split('\n')
        
        # 📊 Return processed data
        return {
            "status": "success",
            "total_lines": len(lines),
            "lines": lines,
            "file_size_bytes": len(file)
        }
    except UnicodeDecodeError:
        # ⚠️ Handle encoding errors gracefully
        return {
            "status": "error",
            "message": "File encoding not supported. Please upload UTF-8 encoded files."
        }
```

Continue reading for complete file handling implementation...