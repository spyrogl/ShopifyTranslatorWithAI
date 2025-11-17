@echo off
REM Setup OpenAI API Key for Shopify Translator

echo.
echo ============================================================
echo   SETUP OPENAI API KEY
echo ============================================================
echo.
echo This script will save your OpenAI API key to config.json
echo.
echo IMPORTANT: Get your API key from:
echo https://platform.openai.com/api-keys
echo.

set /p API_KEY="Enter your OpenAI API Key: "

if "%API_KEY%"=="" (
    echo ERROR: API Key cannot be empty
    pause
    exit /b 1
)

REM Create config.json
echo { > config.json
echo   "openai_api_key": "%API_KEY%" >> config.json
echo } >> config.json

echo.
echo SUCCESS! API Key saved to config.json
echo.
echo You can now run: translate.bat your-file.csv
echo.
pause
