@echo off
set "PROJECT=%~dp0.."
set "PYTHON=C:\Users\10537\miniconda3\envs\ppt-master\python.exe"
set "LOG=%PROJECT%\logs\daily_paper_update.log"

cd /d "%PROJECT%"

echo [%DATE% %TIME%] === daily paper update start === >> "%LOG%"

"%PYTHON%" main.py daily --account demo >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] === daily paper update failed === >> "%LOG%"
    exit /b 1
)
echo [%DATE% %TIME%] scan done >> "%LOG%"
echo [%DATE% %TIME%] add-from-scan done >> "%LOG%"
echo [%DATE% %TIME%] paper update done >> "%LOG%"
echo [%DATE% %TIME%] paper report done >> "%LOG%"
echo [%DATE% %TIME%] observation-dashboard done >> "%LOG%"

echo [%DATE% %TIME%] === daily paper update complete === >> "%LOG%"
