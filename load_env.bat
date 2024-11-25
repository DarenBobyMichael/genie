@echo off
for /f "usebackq tokens=1,2 delims==" %%a in (`type .env`) do (
    set %%a=%%b
)
