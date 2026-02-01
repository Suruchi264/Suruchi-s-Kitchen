@echo off
echo ========================================
echo   Nisarg's Kitchen - Starting Services
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo ERROR: .env file not found!
    echo Please copy .env.example to .env and add your credentials.
    pause
    exit /b 1
)

echo [1/3] Activating virtual environment...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv venv
    pause
    exit /b 1
)

echo [2/3] Starting Backend Server...
echo Backend will run on http://localhost:8000
start "Nisarg's Kitchen - Backend" cmd /k python server.py

timeout /t 3 /nobreak > nul

echo [3/3] Starting Frontend Server...
echo Frontend will run on http://localhost:3000
cd public
start "Nisarg's Kitchen - Frontend" cmd /k python -m http.server 3000

echo.
echo ========================================
echo   Services Started Successfully!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to open the website...
pause > nul

start http://localhost:3000

echo.
echo Keep both terminal windows open!
echo Close them to stop the servers.
echo.
pause
