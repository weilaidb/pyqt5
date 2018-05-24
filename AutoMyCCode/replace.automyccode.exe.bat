@echo on
@echo pyinstaller db/main.py
pyinstaller --noconsole   -i akregator.ico  db/main.py -F
@echo pyinstaller db/main.py done!!!
@echo off

taskkill /im automyccode.exe /f 
copy E:\Qtexample\git\pyqt5\AutoMyCCode\dist\main.exe  E:\Dropbox\weidb\automyccode.exe
@echo copy done!!
explorer E:\Dropbox\weidb\automyccode.exe
pause