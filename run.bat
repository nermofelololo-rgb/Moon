@echo off
chcp 65001 >nul
title New Dent Accounting
cd /d "%~dp0"

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed.
    echo Download from: https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during install
    pause
    exit /b
)

echo Starting New Dent...
python app.py
if errorlevel 1 (
    echo.
    echo Error occurred. Make sure Python is installed correctly.
    pause
)
