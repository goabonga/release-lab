# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from fastapi.testclient import TestClient

from hello.app import app


def test_read_root() -> None:
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI!"}
