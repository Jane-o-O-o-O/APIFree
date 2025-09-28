 ```python
# app/main.py
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import events
import uvicorn
import os

# Create FastAPI app instance
app = FastAPI()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# CORS settings
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": exc.errors()},
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

# Start-up event
@app.on_event("startup")
async def startup_event():
    # Perform startup tasks here, e.g., database connection
    print("Application is starting up")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    # Perform shutdown tasks here, e.g., close database connection
    print("Application is shutting down")

# Example route
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

This file sets up a FastAPI application with the following features:
- Creates a FastAPI app instance.
- Registers a simple example route.
- Configures CORS settings.
- Adds exception handlers for validation errors and HTTP exceptions.
- Includes startup and shutdown events for application lifecycle management.
- Uses an in-memory SQLite database for demonstration purposes.
- Runs the app using Uvicorn server.