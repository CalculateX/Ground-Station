@echo off
title URC Clean Reinstall

:: 1. Initialize Conda
call C:\Users\sande\miniconda3\Scripts\activate.bat

:: 2. Remove the broken environment (Nuclear Option)
echo Deleting old environment to fix broken packages...
call conda remove --name urc_ground_station --all -y

:: 3. Create fresh from YAML
echo Creating new environment...
:: Note: This step might take 2-3 minutes, but it won't hang like before.
call conda env create -f environment.yml

echo.
echo Reinstall Complete. You can now run launch_site.bat
pause