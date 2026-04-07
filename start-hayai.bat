@echo off
title Hayai Launcher
color 0A

echo.
echo  =========================================
echo   速い HAYAI — Starting all services...
echo  =========================================
echo.

:: Kill any existing Ollama instances
echo [1/3] Stopping old Ollama instance...
taskkill /F /IM ollama.exe >nul 2>&1
timeout /t 2 /nobreak >nul

:: Start Ollama with CORS open in a new window
echo [2/3] Starting Ollama with CORS enabled...
start "Ollama" cmd /k "set OLLAMA_ORIGINS=* && ollama serve"
timeout /t 3 /nobreak >nul

:: Start Python proxy in a new window
echo [3/3] Starting Hayai proxy...
start "Hayai Proxy" cmd /k "python "%~dp0proxy.py""
timeout /t 2 /nobreak >nul

:: Start ngrok in a new window
echo [4/4] Starting ngrok tunnel...
start "ngrok" cmd /k "ngrok http 8080"

echo.
echo  =========================================
echo   All services started!
echo   - Check the ngrok window for your URL
echo   - Update the app if the URL changed
echo  =========================================
echo.
pause
