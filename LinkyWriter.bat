@echo off

rem Activate virtual environment
call .\venv\scripts\activate

rem Run Python script
python LinkyWriter.py

rem Deactivate virtual environment
call .\venv\scripts\deactivate

exit