@echo off
REM Quick test runner for Windows
REM Run this to test locally before Jenkins

echo ========================================
echo Student Feedback Form - Local Test Run
echo ========================================
echo.

cd /d "%~dp0"
echo Current Directory: %CD%
echo.

echo Running Selenium tests...
python test/test_form.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo ALL TESTS PASSED!
    echo ========================================
) else (
    echo.
    echo ========================================
    echo TESTS FAILED!
    echo ========================================
)

pause
