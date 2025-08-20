---
sidebar_position: 6
title: User Flow
description: FastAPI User Creation Flow Documentation
---

# 📝 FastAPI User Creation Flow Documentation

## 📁 Project Structure (Relevant Files)
```
.
├── main.py
├── routers/
│   └── user.py
├── db/
│   ├── database.py
│   ├── models.py
│   ├── db_user.py
│   └── hash.py
├── schemas.py
└── fastapi_practice.db
```

## 1. **Pydantic Schemas** (`schemas.py`)

These define the structure and validation for request and response data.

```python
from pydantic import BaseModel

# Request model: what the client sends
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# Response model: what the API returns (no password for security)
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True  # Allows compatibility with ORM objects
```

Continue reading for complete user flow implementation...