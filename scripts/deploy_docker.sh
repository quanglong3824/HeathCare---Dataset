#!/bin/bash

# Docker Deployment Script
# This script builds and runs the Stroke Prediction application in Docker containers

echo "🐳 Docker Deployment for Stroke Prediction Project"

# Check if Docker is installed and running
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Create Dockerfile if it doesn't exist
if [ ! -f "Dockerfile" ]; then
    echo "📝 Creating Dockerfile..."
    cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p models results data/processed

# Expose ports
EXPOSE 8501 5000

# Default command (can be overridden)
CMD ["streamlit", "run", "src/streamlit_app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
EOF
fi

# Create docker-compose.yml if it doesn't exist
if [ ! -f "docker-compose.yml" ]; then
    echo "📝 Creating docker-compose.yml..."
    cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  streamlit-app:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./models:/app/models
      - ./results:/app/results
      - ./data:/app/data
    environment:
      - PYTHONPATH=/app/src
    command: streamlit run src/streamlit_app.py --server.port 8501 --server.address 0.0.0.0

  flask-api:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./models:/app/models
      - ./results:/app/results
      - ./data:/app/data
    environment:
      - FLASK_APP=src/flask_api.py
      - FLASK_ENV=production
      - PYTHONPATH=/app/src
    command: gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 60 src.flask_api:app
EOF
fi

# Build and run containers
echo "🔨 Building Docker images..."
docker-compose build

echo "🚀 Starting containers..."
docker-compose up -d

echo "✅ Deployment complete!"
echo ""
echo "🌐 Access your applications:"
echo "   - Streamlit App: http://localhost:8501"
echo "   - Flask API:     http://localhost:5000"
echo ""
echo "📋 Useful commands:"
echo "   - View logs:     docker-compose logs -f"
echo "   - Stop services: docker-compose down"
echo "   - Restart:       docker-compose restart"
echo ""
echo "🔍 Check container status:"
docker-compose ps