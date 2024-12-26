@echo off

REM Check if virtual environment exists
if not exist venv (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install or upgrade dependencies
pip install -r requirements.txt

REM Check if GROQ_API_KEY is set
if "%GROQ_API_KEY%"=="" (
    echo GROQ_API_KEY is not set. Please set it before running the application.
    echo You can set it by running: set GROQ_API_KEY=your_api_key_here
    exit /b 1
)

REM Run the Streamlit app
streamlit run app.py

REM Deactivate virtual environment
deactivate
