@echo off
REM Start ngrok tunnel for Jenkins webhook

echo =========================================
echo Starting ngrok tunnel for Jenkins
echo =========================================
echo.
echo Jenkins is running on: http://localhost:8090
echo Starting ngrok tunnel...
echo.

REM Start ngrok (adjust path if ngrok is not in PATH)
start "ngrok-tunnel" ngrok http 8090

echo.
echo =========================================
echo ngrok started!
echo =========================================
echo.
echo 1. Check your ngrok URL at: http://127.0.0.1:4040
echo 2. Copy the HTTPS URL (e.g., https://abc123.ngrok.io)
echo 3. Add to GitHub webhook: https://YOUR-URL.ngrok.io/github-webhook/
echo.
echo Keep this window open to maintain the tunnel!
echo =========================================
echo.

REM Wait a moment for ngrok to start
timeout /t 3 /nobreak >nul

REM Open ngrok dashboard in browser
start http://127.0.0.1:4040

pause
