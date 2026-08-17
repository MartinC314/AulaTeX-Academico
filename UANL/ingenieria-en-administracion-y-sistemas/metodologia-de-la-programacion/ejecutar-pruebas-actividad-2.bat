@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%ejecutar-pruebas-actividad-2.ps1"
if errorlevel 1 (
  echo ERROR: alguna compilacion o prueba fallo.
  exit /b 1
)
echo Todas las pruebas terminaron correctamente.
endlocal
