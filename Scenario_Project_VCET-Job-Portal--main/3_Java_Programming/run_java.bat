@echo off
setlocal
title Online Job Portal - Java Programming Console (25ITT32)
cd /d "%~dp0"

echo ===============================================================================
echo               ONLINE JOB PORTAL - JAVA PROGRAMMING SYSTEM (25ITT32)
echo ===============================================================================
echo.
echo Checking Java Development Kit (JDK)...

set "JAVAC_CMD=javac"
set "JAVA_CMD=java"

javac -version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\javac.exe" (
        set "JAVAC_CMD=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\javac.exe"
        set "JAVA_CMD=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe"
    )
)

echo Using Java Compiler: %JAVAC_CMD%
echo Using Java Runtime : %JAVA_CMD%
echo.

if not exist "bin" mkdir bin

echo Compiling Java source files...
"%JAVAC_CMD%" -d bin -sourcepath src src\com\jobportal\model\*.java src\com\jobportal\exception\*.java src\com\jobportal\service\*.java src\com\jobportal\thread\*.java src\com\jobportal\app\*.java

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Compilation failed!
    pause
    exit /b %ERRORLEVEL%
)

echo [SUCCESS] Compilation successful!
echo.
echo Starting Interactive Java Application with Manual Keyboard Input...
echo You can test step-by-step: register profiles, post jobs, test duplicate check,
echo run stream reports, and trigger multithreaded screening!
echo.

"%JAVA_CMD%" -cp bin com.jobportal.app.JobPortalApp

echo.
echo ===============================================================================
echo Java Application Session finished.
echo ===============================================================================
pause
