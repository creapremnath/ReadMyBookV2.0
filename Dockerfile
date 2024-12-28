# Use the Slim version of Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies (including Tesseract OCR)
RUN apt update && apt install -y --no-install-recommends \
    tesseract-ocr \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run FastAPI with uvicorn when the container starts
CMD ["uvicorn", "app:main", "--host", "0.0.0.0", "--port", "8000"]
