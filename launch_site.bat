@echo off
title URC Ground Station Launcher

:: 1. Activate the environment (using your Miniconda path ensures it works)
call C:\Users\sande\miniconda3\Scripts\activate.bat
call conda activate urc_ground_station

:: 2. Launch the Flask Server and open the browser
echo Launching Base Station...
start http://127.0.0.1:5000
python app.py

pause