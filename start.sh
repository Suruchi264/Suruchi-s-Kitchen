#!/bin/bash

echo "========================================"
echo "  Nisarg's Kitchen - Starting Services"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo "Please copy .env.example to .env and add your credentials."
    exit 1
fi

echo "[1/3] Activating virtual environment..."
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
else
    echo "ERROR: Virtual environment not found!"
    echo "Please run: python -m venv venv"
    exit 1
fi

echo "[2/3] Starting Backend Server..."
echo "Backend will run on http://localhost:8000"
python server.py &
BACKEND_PID=$!

sleep 3

echo "[3/3] Starting Frontend Server..."
echo "Frontend will run on http://localhost:3000"
cd public
python -m http.server 3000 &
FRONTEND_PID=$!

cd ..

echo ""
echo "========================================"
echo "  Services Started Successfully!"
echo "========================================"
echo ""
echo "Backend:  http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo ""
echo "Backend PID:  $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Opening website in browser..."
sleep 2

# Try to open browser (works on macOS and many Linux distros)
if command -v open &> /dev/null; then
    open http://localhost:3000
elif command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:3000
else
    echo "Please open http://localhost:3000 in your browser"
fi

echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "All services stopped."
    exit 0
}

# Trap Ctrl+C
trap cleanup INT TERM

# Wait for processes
wait
