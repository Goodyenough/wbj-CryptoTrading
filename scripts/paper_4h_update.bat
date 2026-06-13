@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_logged_paper_task.ps1" -Mode paper_4h
exit /b %ERRORLEVEL%
