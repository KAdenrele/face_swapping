FROM ghcr.io/astral-sh/uv:latest AS uv_bin

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    libgl1 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv_bin /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

# --frozen: ensures uv doesn't try to update the lockfile
# --no-cache: keeps the image size small
RUN uv sync --frozen --no-cache

# Install dependencies for dataset downloading
RUN uv pip install datasets==2.19.0 Pillow==10.3.0 pyarrow==16.1.0
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

VOLUME /data

CMD ["python", "main.py"]

