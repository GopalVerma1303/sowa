#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install or upgrade dependencies
pip install -r requirements.txt

# Check if GROQ_API_KEY is set
if [ -z "$GROQ_API_KEY" ]; then
    echo "GROQ_API_KEY is not set. Please set it before running the application."
    echo "You can set it by running: export GROQ_API_KEY=your_api_key_here"
    exit 1
fi

# Run the Streamlit app
streamlit run app.py

# Deactivate virtual environment
deactivate
