# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from fastapi import FastAPI

# Create FastAPI application instance
app = FastAPI(
    title="Minimal FastAPI Application",
    description="A simple FastAPI app with a welcome endpoint",
    version="1.0.0",
)


# Define GET route on root path
@app.get("/")
async def read_root():
    """
    Welcome endpoint that returns a greeting message

    Returns:
        dict: A dictionary containing the welcome message
    """
    return {"message": "Hello FastAPI!"}


# Run the application (for development)
if __name__ == "__main__":
    import uvicorn

    # Start the server on localhost:8000
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True,  # Enable auto-reload for development
    )
