from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Pydantic schema
class BlogPost(BaseModel):
    title: str
    content: str
    author: Optional[str] = "Anonymous"

@router.post(
    "/create",
    summary="Create a new blog post",
    description="This endpoint allows you to create a new blog post with a title, content, and optional author."
)
def create_blog(post: BlogPost = Body(...)):
    return {
        "message": "Blog created successfully!",
        "data": post
    }
