from fastapi import FastAPI
from routers import blog_post, blog_get, user, file as file_router, templates as templates_router, middleware_demo
from db.database import engine
from db import models
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, FileResponse
from fastapi import UploadFile, File, HTTPException, Depends
import os
from fastapi.staticfiles import StaticFiles
from auth.oauth import get_current_user
from fastapi.templating import Jinja2Templates
from middleware import setup_middleware

app = FastAPI(
    title="FastAPI Blog API",
    description="A sample blog backend using FastAPI Routers with comprehensive middleware",
    version="1.0.0"
)

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Setup all middleware
setup_middleware(app)

# 👾 Define a custom exception
class StoryException(Exception):
    def __init__(self, name: str):
        self.name = name

# 🔹 Add Exception Handler
@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,  # 🔥 Custom status code
        content={"detail": f"Oops! {exc.name} caused an issue ☠️"}
    )

# ✅ Usage Example for Custom Exception
@app.get("/story/")
def get_story(flag: bool = False):
    if not flag:
        raise StoryException(name="Missing Story Flag 🏳️")
    return {"message": "Here's your story! 📖"}

# 📦 2. Custom Response
@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Hello 🌍, this is raw HTML!</h1>"

@app.get("/text", response_class=PlainTextResponse)
def get_text():
    return "This is plain text ✉️"

# 5. Serve static files (e.g., images, frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers with prefix and tags
app.include_router(user.router)
app.include_router(file_router.router)
app.include_router(blog_post.router, prefix="/blog", tags=["Blog - Post"])
app.include_router(blog_get.router, prefix="/blog", tags=["Blog - Get"])
app.include_router(templates_router.router)
app.include_router(middleware_demo.router)

@app.get("/", response_class=HTMLResponse, tags=["Root"])
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "message": "FastAPI application is running with middleware",
        "version": "1.0.0"
    }

models.Base.metadata.create_all(engine)