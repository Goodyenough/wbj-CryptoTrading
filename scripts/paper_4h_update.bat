@echo off
setlocal

set "PROJECT=%~dp0.."
set "PYTHON=C:\Users\10537\miniconda3\envs\ppt-master\python.exe"
set "LOG=%PROJECT%\logs\paper_4h_update.log"

cd /d "%PROJECT%"

echo [%DATE% %TIME%] === paper 4h update start === >> "%LOG%"

"%PYTHON%" main.py paper cycle --run-type paper_4h_update --account demo >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] === paper 4h update failed === >> "%LOG%"
    exit /b 1
)

echo [%DATE% %TIME%] paper update done >> "%LOG%"
echo [%DATE% %TIME%] paper report done >> "%LOG%"
echo [%DATE% %TIME%] observation-dashboard done >> "%LOG%"
echo [%DATE% %TIME%] === paper 4h update complete === >> "%LOG%"

endlocal
