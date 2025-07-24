from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# ✅ Create User
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# ✅ Read All Users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    users = db_user.get_all_users(db)
    return users

# ✅ Read One User
@router.get("/{user_id}", response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ✅ Update User
@router.put("/{user_id}", response_model=UserDisplay)
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db_user.update_user(db, user_id, request)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ✅ Delete User
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db_user.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}