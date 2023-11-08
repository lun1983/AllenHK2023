@echo off

for /f "skip=1 tokens=2 delims=," %%A in ('wmic logicaldisk where "DeviceID='C:'" get Size /format:csv') do (
    echo 111
	echo 'a:' %%A
	set /a sizeMB=%%A/1000000
    echo Size: %sizeMB% MB
)