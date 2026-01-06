# test_api.py

import pytest
import httpx
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app from main.py

# Create a test client using FastAPI's TestClient
client = TestClient(app)

def test_get_root_endpoint():
    """
    Test the GET '/' endpoint to verify it returns status code 200
    and the expected message 'Hello FastAPI!'
    """
    # Make a GET request to the root endpoint
    response = client.get("/")
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the response contains the expected message
    assert response.json() == {"message": "Hello FastAPI!"}

@pytest.mark.asyncio
async def test_get_root_endpoint_with_httpx():
    """
    Alternative test using httpx.AsyncClient for asynchronous testing
    """
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the response contains the expected message
    assert response.json() == {"message": "Hello FastAPI!"}

def test_response_content_type():
    """
    Test that the response content type is application/json
    """
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

# Example FastAPI app structure that should be in main.py:
"""
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI!"}
"""