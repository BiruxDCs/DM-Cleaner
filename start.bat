@echo off
title DM Group Cleaner
cd /d "%~dp0"

echo.
echo [::] DM Group Cleaner - Launcher
echo [::] github.com/BiruxDCs/DM-Cleaner
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python no esta instalado.
    echo     Descargalo desde: https://python.org
    pause
    exit /b
)

echo [*] Verificando dependencias...
python -c "import discord" 2>nul
if %errorlevel% neq 0 (
    echo [~] Instalando discord.py-self...
    pip install discord.py-self
    if %errorlevel% neq 0 (
        echo [!] Error al instalar.
        pause
        exit /b
    )
    echo [OK] Instalado correctamente.
) else (
    echo [OK] Dependencias listas.
)

echo.
echo [*] Iniciando...
echo.
python "dm_cleaner.py"
if %errorlevel% neq 0 (
    echo.
    echo [!] El programa cerr con error.
    pause
)
