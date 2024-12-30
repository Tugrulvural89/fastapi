from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def add_middleware(app : FastAPI):
    @app.middleware("http")
    async def log_request(request: Request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        return response
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"message": "Invalid Request"})
    