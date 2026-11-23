@echo off
setlocal
title Online Job Portal - Data Science & Trend Analysis Console (25ITC31)
cd /d "%~dp0"

echo ===============================================================================
echo        ONLINE JOB PORTAL - FOUNDATIONS OF DATA SCIENCE (25ITC31)
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
echo Starting Interactive Data Science Console with Manual Keyboard Input...
echo You can test step-by-step: descriptive stats, z-scores, IQR outlier check,
echo pivot tables, filter candidates, and generate all Matplotlib/Seaborn plots!
echo.
%PY_CMD% interactive_ds.py

echo.
echo ===============================================================================
echo Data Science Session finished.
echo ===============================================================================
pause
