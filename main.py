from fastapi import FastAPI
from routers import blog_post, blog_get, user
from db.database import engine
from db import models
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, FileResponse

app = FastAPI(
    title="FastAPI Blog API",
    description="A sample blog backend using FastAPI Routers",
    version="1.0.0"
)

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

@app.get("/download")
def download_file():
    # Using a sample PDF from Blogs directory
    return FileResponse("Blogs/1. GET Methods.pdf", media_type='application/pdf', filename="Sample.pdf")

# 🧾 3. Headers
@app.get("/headers/")
def read_headers(request: Request):
    headers = request.headers
    user_agent = headers.get("user-agent")
    return {"user_agent": user_agent}

@app.get("/custom-header")
def custom_header():
    content = {"message": "Hello with headers!"}
    headers = {"X-Powered-By": "FastAPI ⚡"}
    return JSONResponse(content=content, headers=headers)

# Include routers with prefix and tags
app.include_router(user.router)
app.include_router(blog_post.router, prefix="/blog", tags=["Blog - Post"])
app.include_router(blog_get.router, prefix="/blog", tags=["Blog - Get"])

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the FastAPI Blog API!"}

models.Base.metadata.create_all(engine)