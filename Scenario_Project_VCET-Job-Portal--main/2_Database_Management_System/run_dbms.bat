@echo off
setlocal
title Online Job Portal - DBMS Interactive Console (25ITT31)
cd /d "%~dp0"

echo ===============================================================================
echo            ONLINE JOB PORTAL - DATABASE MANAGEMENT SYSTEM (25ITT31)
echo ===============================================================================
echo.
echo Searching for Python environment...

set "PY_CMD=python"
python --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Users\sugirthan\AppData\Local\Programs\Python\Python313\python.exe" (
        set "PY_CMD=C:\Users\sugirthan\AppData\Local\Programs\Python\Python313\python.exe"
    ) else (
        where py >nul 2>nul
        if %ERRORLEVEL% EQU 0 (
            set "PY_CMD=py"
        )
    )
)

echo Using Python: %PY_CMD%
echo.
echo Starting Interactive DBMS Console with Manual Keyboard Input...
echo You can test step-by-step: add records, test duplicate checks, run queries!
echo.
%PY_CMD% dbms_interactive.py

echo.
echo ===============================================================================
echo DBMS Session finished.
echo ===============================================================================
pause
