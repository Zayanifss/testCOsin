# Use Python slim image
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Ensure group and user creation is safe
RUN getent group appgroup || groupadd -r appgroup && \
 id -u appuser &>/dev/null || useradd -r -g appgroup -u 1001 appuser

# Switch to the non-root user
USER appuser

COPY src/ ./src

# Ensure CMD uses JSON format to prevent OS signal issues
CMD ["python", "src/test1.py"]  
