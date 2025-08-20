---
sidebar_position: 5
title: Database
description: FastAPI Database Integration
---

# ⚙️ **Complete `create_user` Flow in FastAPI**

## ✅ 1. `schemas.py` — Request & Response Models

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # important to work with ORM objects
```

## ✅ 2. `models.py` — SQLAlchemy User Model

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)  # store hashed password
```

Continue reading for complete database implementation...