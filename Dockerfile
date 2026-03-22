# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* README.md ./
COPY src/ src/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi && \
    pip uninstall -y poetry

ENTRYPOINT ["hello"]
