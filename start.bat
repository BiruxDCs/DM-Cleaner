@echo off
title DM Group Cleaner
cd /d "%~dp0"

echo.
echo [::] DM Group Cleaner - Launcher
echo [::] github.com/BiruxDCs/DM-Cleaner
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python is not installed.
    echo     Download it from: https://python.org
    pause
    exit /b
)

echo [*] Checking dependencies...
python -c "import discord" 2>nul
if %errorlevel% neq 0 (
    echo [~] Installing discord.py-self...
    pip install discord.py-self
    if %errorlevel% neq 0 (
        echo [!] Failed to install dependencies.
        pause
        exit /b
    )
    echo [OK] Installed successfully.
) else (
    echo [OK] All dependencies ready.
)

echo.
echo [*] Starting...
echo.
python "dm_cleaner.py"
if %errorlevel% neq 0 (
    echo.
    echo [!] The program exited with an error.
    pause
)
