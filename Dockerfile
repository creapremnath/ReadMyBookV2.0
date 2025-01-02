# Use the Slim version of Python
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies (including Tesseract OCR)
RUN apt update && apt install -y --no-install-recommends \
    tesseract-ocr \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Set the FLASK_APP environment variable and run Flask
ENV FLASK_APP=app.py  
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
