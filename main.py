from fastapi import FastAPI
from routers import blog_post, blog_get

app = FastAPI(
    title="FastAPI Blog API",
    description="A sample blog backend using FastAPI Routers",
    version="1.0.0"
)

# Include routers with prefix and tags
app.include_router(blog_post.router, prefix="/blog", tags=["Blog - Post"])
app.include_router(blog_get.router, prefix="/blog", tags=["Blog - Get"])

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the FastAPI Blog API!"}
