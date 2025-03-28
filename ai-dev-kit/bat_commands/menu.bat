@echo off
:menu
cls
echo ================================
echo       AI DEV KIT MENU
echo ================================
echo 1. Start all services (launch)
echo 2. Check service status
echo 3. Show logs
echo 4. Restart everything
echo 5. Open docs
echo 6. Run tests
echo 7. Deploy
echo 8. Exit
echo.

set /p choice=Select an option: 

if "%choice%"=="1" call launch.bat
if "%choice%"=="2" call check.bat
if "%choice%"=="3" call logs.bat
if "%choice%"=="4" call restart.bat
if "%choice%"=="5" call docs.bat
if "%choice%"=="6" call test.bat
if "%choice%"=="7" call deploy.bat
if "%choice%"=="8" exit

pause
goto menu
