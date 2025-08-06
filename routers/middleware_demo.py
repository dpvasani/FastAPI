from fastapi import APIRouter, Request, HTTPException
import time
import random

router = APIRouter(
    prefix="/middleware-demo",
    tags=["Middleware Demo"]
)

@router.get("/")
async def middleware_demo_root():
    """
    Demo endpoint to showcase middleware functionality
    """
    return {
        "message": "Middleware Demo",
        "features": [
            "Request logging with unique IDs",
            "Rate limiting",
            "Security headers",
            "Performance monitoring",
            "Error handling",
            "Request validation"
        ]
    }

@router.get("/slow")
async def slow_endpoint():
    """
    Simulate a slow endpoint to test performance middleware
    """
    # Simulate processing time
    time.sleep(random.uniform(0.5, 2.0))
    return {
        "message": "This was a slow request",
        "processing_time": "1-2 seconds"
    }

@router.get("/error")
async def error_endpoint():
    """
    Simulate an error to test error handling middleware
    """
    raise HTTPException(status_code=500, detail="This is a simulated error")

@router.post("/large-request")
async def large_request_endpoint(request: Request):
    """
    Test request validation middleware with large content
    """
    body = await request.body()
    return {
        "message": "Large request processed",
        "content_length": len(body)
    }

@router.get("/rate-limit-test")
async def rate_limit_test():
    """
    Test rate limiting middleware
    """
    return {
        "message": "Rate limit test successful",
        "timestamp": time.time()
    }

@router.get("/headers")
async def headers_demo(request: Request):
    """
    Show request headers and middleware-added headers
    """
    return {
        "request_headers": dict(request.headers),
        "request_id": getattr(request.state, 'request_id', 'Not set'),
        "message": "Check response headers for X-Request-ID and X-Process-Time"
    } 