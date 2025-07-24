from fastapi import APIRouter
from schemas import UserBase


router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create User

@router.post('/')
def create_user(reqest:UserBase)

# Update User

# Delete User

# Read User

