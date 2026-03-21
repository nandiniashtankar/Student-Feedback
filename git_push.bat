@echo off
REM Git push script for Windows

echo =========================================
echo Pushing Student Feedback to GitHub
echo =========================================
echo.

cd /d "%~dp0"

REM Initialize git if not already initialized
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

REM Add all files
echo Adding all files...
git add .
echo.

REM Commit
echo Creating commit...
git commit -m "Initial commit: Student Feedback Form with Selenium tests"
echo.

REM Rename branch to main
echo Setting branch to main...
git branch -M main
echo.

REM Add remote origin
echo Adding remote origin...
git remote add origin https://github.com/mrudangwanjari/student-feedback.git 2>nul || git remote set-url origin https://github.com/mrudangwanjari/student-feedback.git
echo.

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main
echo.

echo =========================================
echo Done! Check: https://github.com/mrudangwanjari/student-feedback
echo =========================================
pause
