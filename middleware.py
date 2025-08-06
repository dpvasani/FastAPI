import time
import logging
from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import json
from typing import Callable
import uuid
from config import settings

# Configure logging
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log all requests and responses
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        
        # Log request
        start_time = time.time()
        logger.info(f"Request {request_id}: {request.method} {request.url.path} - Started")
        
        # Process request
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            
            # Log response
            logger.info(f"Request {request_id}: {request.method} {request.url.path} - Completed in {process_time:.4f}s - Status: {response.status_code}")
            
            # Add request ID to response headers
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(f"Request {request_id}: {request.method} {request.url.path} - Failed in {process_time:.4f}s - Error: {str(e)}")
            raise

class RateLimitingMiddleware(BaseHTTPMiddleware):
    """
    Simple rate limiting middleware
    """
    def __init__(self, app, requests_per_minute: int = None):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute or settings.RATE_LIMIT_REQUESTS_PER_MINUTE
        self.requests = {}
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Get client IP
        client_ip = request.client.host if request.client else "unknown"
        
        # Check rate limit
        current_time = time.time()
        if client_ip in self.requests:
            # Clean old requests
            self.requests[client_ip] = [req_time for req_time in self.requests[client_ip] 
                                       if current_time - req_time < 60]
            
            # Check if limit exceeded
            if len(self.requests[client_ip]) >= self.requests_per_minute:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Rate limit exceeded. Please try again later."}
                )
        
        # Add current request
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        self.requests[client_ip].append(current_time)
        
        return await call_next(request)

class SecurityMiddleware(BaseHTTPMiddleware):
    """
    Security middleware to add security headers
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        # Use CSP policy from settings
        response.headers["Content-Security-Policy"] = settings.CSP_POLICY
        
        return response

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Global error handling middleware
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(f"Unhandled error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Internal server error",
                    "error": str(e) if settings.DEBUG else "Something went wrong"
                }
            )

class RequestValidationMiddleware(BaseHTTPMiddleware):
    """
    Middleware to validate and sanitize requests
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Check content length
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > settings.MAX_CONTENT_LENGTH:
            return JSONResponse(
                status_code=413,
                content={"detail": "Request too large"}
            )
        
        # Check for suspicious headers
        suspicious_headers = ["x-forwarded-for", "x-real-ip"]
        for header in suspicious_headers:
            if header in request.headers:
                logger.warning(f"Suspicious header detected: {header}")
        
        return await call_next(request)

class PerformanceMiddleware(BaseHTTPMiddleware):
    """
    Middleware to monitor performance metrics
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        
        # Add performance headers
        response = await call_next(request)
        
        process_time = time.time() - start_time
        response.headers["X-Response-Time"] = f"{process_time:.4f}s"
        
        # Log slow requests
        if process_time > settings.SLOW_REQUEST_THRESHOLD:
            logger.warning(f"Slow request: {request.method} {request.url.path} took {process_time:.4f}s")
        
        return response

class AuthenticationMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle authentication checks
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Skip authentication for public paths
        if any(request.url.path.startswith(path) for path in settings.PUBLIC_PATHS):
            return await call_next(request)
        
        # Check for authentication token
        auth_header = request.headers.get("authorization")
        if not auth_header:
            # Allow the request to continue, let individual endpoints handle auth
            logger.info(f"No auth header for {request.method} {request.url.path}")
        
        return await call_next(request)

def setup_middleware(app):
    """
    Setup all middleware for the FastAPI application
    """
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Add trusted host middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )
    
    # Add GZip compression middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    
    # Add custom middleware (order matters - add from bottom to top)
    app.add_middleware(PerformanceMiddleware)
    app.add_middleware(RequestValidationMiddleware)
    app.add_middleware(SecurityMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(AuthenticationMiddleware)
    app.add_middleware(RateLimitingMiddleware, requests_per_minute=settings.RATE_LIMIT_REQUESTS_PER_MINUTE)
    app.add_middleware(LoggingMiddleware)
    
    logger.info("All middleware has been configured successfully!") 