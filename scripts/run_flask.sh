#!/bin/bash

# Flask API Launcher Script
# This script launches the Stroke Prediction Flask REST API

echo "🚀 Starting Stroke Prediction Flask API..."

# Check if flask is installed
if ! python -c "import flask" &> /dev/null; then
    echo "❌ Flask is not installed. Installing..."
    pip install flask
fi

# Check if the API file exists
if [ ! -f "src/flask_api.py" ]; then
    echo "❌ Flask API file not found at src/flask_api.py"
    echo "Please ensure the API file exists."
    exit 1
fi

# Set environment variables
export FLASK_APP=src/flask_api.py
export FLASK_ENV=development
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Launch Flask API
echo "🌐 Starting Flask API at http://localhost:5000"
echo "📋 API endpoints:"
echo "   - GET  /health          - Health check"
echo "   - POST /predict         - Stroke prediction"
echo "   - GET  /model/info      - Model information"
echo "⏹️  Press Ctrl+C to stop the API"

# Use gunicorn for production-like deployment
if command -v gunicorn &> /dev/null; then
    echo "🔧 Using Gunicorn WSGI server"
    gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 60 src.flask_api:app
else
    echo "🔧 Using Flask development server"
    python -m flask run --host=0.0.0.0 --port=5000
fi

echo "✅ Flask API stopped successfully"