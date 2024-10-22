@echo off
:: Set up the environment for running the MLflow server
:: Specify the backend store (SQLite in this case) and artifact root directory

set BACKEND_URI=sqlite:///mlflow.db
set ARTIFACT_ROOT=./mlruns
set HOST=127.0.0.1
set PORT=5000

:: Ensure artifacts directory exists
if not exist "%ARTIFACT_ROOT%" mkdir "%ARTIFACT_ROOT%"

:: Start the MLflow server
mlflow server --backend-store-uri %BACKEND_URI% --default-artifact-root %ARTIFACT_ROOT% --host %HOST% --port %PORT%

pause
