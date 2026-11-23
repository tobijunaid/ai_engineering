# Pinned to match the local dev interpreter (Python 3.13); -slim keeps the image small.
FROM python:3.13-slim

# Noise and buffering off: logs stream straight to `docker logs`.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install dependencies first so Docker caches this layer when only the app changes.
COPY requirements.txt .
RUN pip install -r requirements.txt

# App code last (changes most often).
COPY . .

EXPOSE 8000

# Run migrations on boot, then start the server.
# --host 0.0.0.0 so the container port is reachable from outside.
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
