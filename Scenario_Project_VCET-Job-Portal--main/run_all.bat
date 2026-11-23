@echo off
setlocal EnableDelayedExpansion
title VCET Job Portal - Master Launcher
cd /d "%~dp0"

:: Auto-detect Python binary
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

:MENU
cls
echo ===============================================================================
echo                            VCET JOB PORTAL
echo                      MASTER LAUNCHER MENU
echo ===============================================================================
echo.
echo   [1] Software Engineering (Open documentation and diagrams)
echo   [2] Database Management System (Run interactive SQLite DBMS)
echo   [3] Java Programming (Run interactive Java SE 17 system)
echo   [4] Foundation of Data Science (Run interactive EDA and trend analysis)
echo   [5] View Visuals and Diagrams Dashboard (Open in Web Browser)
echo   [6] Exit
echo.
echo ===============================================================================
set "CHOICE="
set /p "CHOICE=Enter your choice (1-6): "

if "%CHOICE%"=="1" goto SE_OPTION
if "%CHOICE%"=="2" goto DBMS_OPTION
if "%CHOICE%"=="3" goto JAVA_OPTION
if "%CHOICE%"=="4" goto DS_OPTION
if "%CHOICE%"=="5" goto DASHBOARD_OPTION
if "%CHOICE%"=="6" goto EXIT_OPTION

echo.
echo [ERROR] Invalid selection. Please enter a number between 1 and 6.
timeout /t 2 >nul
goto MENU

:SE_OPTION
cls
echo ===============================================================================
echo                    [1] SOFTWARE ENGINEERING (25ITT33)
echo ===============================================================================
echo.
echo Opening 1_Software_Engineering folder...
start "" "%~dp01_Software_Engineering"
if exist "%~dp01_Software_Engineering\Software_Engineering_Documentation.md" (
    echo Opening Software_Engineering_Documentation.md...
    start "" "%~dp01_Software_Engineering\Software_Engineering_Documentation.md"
)
echo.
echo Software Engineering folder and documentation opened successfully.
echo.
pause
goto MENU

:DBMS_OPTION
cls
echo ===============================================================================
echo             [2] DATABASE MANAGEMENT SYSTEM (25ITT31)
echo ===============================================================================
echo.
echo Switching working directory to 2_Database_Management_System...
pushd "%~dp02_Database_Management_System"
call run_dbms.bat
popd
cd /d "%~dp0"
echo.
echo Returned from Database Management System session.
pause
goto MENU

:JAVA_OPTION
cls
echo ===============================================================================
echo                    [3] JAVA PROGRAMMING (25ITT32)
echo ===============================================================================
echo.
echo Switching working directory to 3_Java_Programming...
pushd "%~dp03_Java_Programming"
call run_java.bat
popd
cd /d "%~dp0"
echo.
echo Returned from Java Programming session.
pause
goto MENU

:DS_OPTION
cls
echo ===============================================================================
echo              [4] FOUNDATION OF DATA SCIENCE (25ITC31)
echo ===============================================================================
echo.
echo Switching working directory to 4_Foundation_of_Data_Science...
pushd "%~dp04_Foundation_of_Data_Science"
call run_datascience.bat
popd
cd /d "%~dp0"
echo.
echo Returned from Foundation of Data Science session.
pause
goto MENU

:DASHBOARD_OPTION
cls
echo ===============================================================================
echo               [5] VISUALS AND DIAGRAMS WEB DASHBOARD
echo ===============================================================================
echo.
echo Scanning all visual assets (.png, .jpg, .jpeg, .webp) across subfolders...
%PY_CMD% "%~dp0generate_dashboard.py"
if %ERRORLEVEL% NEQ 0 (
    echo [WARN] Python scan encountered a warning, checking for existing dashboard...
)
if exist "%~dp0visuals_dashboard.html" (
    echo.
    echo [SUCCESS] Opening Visuals Dashboard in your default browser...
    start "" "%~dp0visuals_dashboard.html"
) else (
    echo [ERROR] visuals_dashboard.html could not be found or generated!
)
echo.
pause
goto MENU

:EXIT_OPTION
cls
echo ===============================================================================
echo Exiting VCET Job Portal Master Launcher. Goodbye!
echo ===============================================================================
timeout /t 1 >nul
exit /b 0
