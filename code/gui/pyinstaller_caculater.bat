@echo on
@echo pyinstaller caculater.py
pyinstaller --noconsole   caculater.py -F --add-data="icons/pyCalc.ico"
@echo pyinstaller caculater.py done!!!

pause
@echo off
