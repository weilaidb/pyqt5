@echo on
@echo pyinstaller db/main.py
pyinstaller --noconsole  -i akregator.ico db/main.py
@echo pyinstaller db/main.py done!!!

pause
@echo off
