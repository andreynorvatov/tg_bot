@echo off

call %~dp0\venv\Scripts\activate

set TOKEN=

python LoadTest_Bot.py

pause

