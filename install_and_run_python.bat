@echo off

:: Set Python version and script name
set PYTHON_VERSION=3.11.4
set SCRIPT_NAME=Recovery_Script.py

:: Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Downloading and installing Python %PYTHON_VERSION%...

    :: Download Python installer
    curl -o python-installer.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

    :: Install Python silently and add to PATH
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

    :: Verify installation
    python --version
    if %errorlevel% == 0 (
        echo Python installation was successful.
    ) else (
        echo Python installation failed.
        exit /b 1
    )
:: Clean up
del python-installer.exe

)

:: Run the Python script
echo Running the Python script: %SCRIPT_NAME%
python %SCRIPT_NAME%

pause
