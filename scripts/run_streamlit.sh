#!/bin/bash

# Streamlit App Launcher Script
# This script launches the Stroke Prediction Streamlit application

echo "🚀 Starting Stroke Prediction Streamlit App..."

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed. Installing..."
    pip install streamlit
fi

# Check if the app file exists
if [ ! -f "src/streamlit_app.py" ]; then
    echo "❌ Streamlit app file not found at src/streamlit_app.py"
    echo "Please ensure the application file exists."
    exit 1
fi

# Set environment variables
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Launch Streamlit app
echo "🌐 Launching Streamlit app at http://localhost:8501"
echo "📊 Stroke Prediction Dashboard will open in your browser"
echo "⏹️  Press Ctrl+C to stop the application"

streamlit run src/streamlit_app.py --server.port 8501 --server.address localhost

echo "✅ Streamlit app stopped successfully"