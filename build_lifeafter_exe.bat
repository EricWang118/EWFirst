@echo off
setlocal

set "PYTHON_EXE=%LocalAppData%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PYTHON_EXE%" (
    echo [ERROR] Python executable not found:
    echo %PYTHON_EXE%
    echo.
    echo Edit this file and update PYTHON_EXE to your real python.exe path.
    pause
    exit /b 1
)

echo [1/3] Checking PyInstaller...
"%PYTHON_EXE%" -m PyInstaller --version >nul 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    "%PYTHON_EXE%" -m pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller.
        pause
        exit /b 1
    )
)

echo [2/3] Building exe...
"%PYTHON_EXE%" -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "lifeafter_event_viewer" ^
    "lifeafter_event_app.py"

if errorlevel 1 (
    echo [ERROR] Build failed.
    pause
    exit /b 1
)

echo [3/3] Done.
echo Your exe is here:
echo %CD%\dist\lifeafter_event_viewer.exe
echo.
echo You can send that exe directly to users without Python.
pause
