@echo off
REM Shopify Product Translator - CLI Mode
REM Run this from Windows Terminal or Command Prompt

echo.
echo ============================================================
echo   SHOPIFY PRODUCT TRANSLATOR - CLI MODE
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if CSV file argument is provided
if "%~1"=="" (
    echo Usage: translate.bat your-file.csv
    echo.
    echo Example: translate.bat products.csv
    echo Example: translate.bat "C:\Users\Desktop\products.csv"
    echo.
    pause
    exit /b 1
)

REM Check if CSV file exists
if not exist "%~1" (
    echo ERROR: File not found: %~1
    echo.
    pause
    exit /b 1
)

REM Run the translator
echo Starting translation for: %~1
echo.
python shopify_translator.py "%~1"

REM Show result
if errorlevel 1 (
    echo.
    echo Translation failed! Check the errors above.
) else (
    echo.
    echo Translation completed successfully!
    echo Check the 'translated_outputs' folder for your file.
)

echo.
pause
