@echo off
setlocal EnableExtensions

rem Lanzador de Windows para el entorno AulaTeX.
rem La instalacion y verificacion pertenecen a .venv\install-venv.ps1.

set "REPO_ROOT=%~dp0"
set "INSTALLER=%REPO_ROOT%.venv\install-venv.ps1"
set "ACTIVATE=%REPO_ROOT%.venv\Scripts\activate.bat"
set "PS_ARGS="
set "OPEN_SHELL=1"

:parse_args
if "%~1"=="" goto run_setup
if /I "%~1"=="--force" (
    set "PS_ARGS=%PS_ARGS% -Force"
    shift
    goto parse_args
)
if /I "%~1"=="--full" (
    set "PS_ARGS=%PS_ARGS% -Full"
    shift
    goto parse_args
)
if /I "%~1"=="--no-shell" (
    set "OPEN_SHELL=0"
    shift
    goto parse_args
)
if /I "%~1"=="--help" goto show_help
if /I "%~1"=="-h" goto show_help

echo [ERROR] Opcion no reconocida: %~1
echo.
goto show_help_error

:run_setup
if not exist "%INSTALLER%" (
    echo [ERROR] No se encontro el instalador: "%INSTALLER%"
    exit /b 1
)

pushd "%REPO_ROOT%" || exit /b 1
echo ==^> Configurando AulaTeX desde: %CD%
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%INSTALLER%" %PS_ARGS%
set "SETUP_EXIT=%ERRORLEVEL%"
if not "%SETUP_EXIT%"=="0" (
    echo.
    echo [ERROR] La configuracion fallo con codigo %SETUP_EXIT%.
    popd
    exit /b %SETUP_EXIT%
)

if not exist "%ACTIVATE%" (
    echo [ERROR] El instalador termino, pero no existe: "%ACTIVATE%"
    popd
    exit /b 1
)

if "%OPEN_SHELL%"=="0" (
    echo ==^> Entorno listo. Activalo con: .venv\Scripts\activate.bat
    popd
    exit /b 0
)

echo.
echo ==^> Abriendo CMD con el entorno AulaTeX activado.
call "%ACTIVATE%"
title AulaTeX - entorno virtual
set "AULATEX_REPO_ROOT=%REPO_ROOT:~0,-1%"
cmd.exe /K
set "SHELL_EXIT=%ERRORLEVEL%"
popd
exit /b %SHELL_EXIT%

:show_help
echo Uso: setup.bat [--force] [--full] [--no-shell]
echo.
echo   --force      Recrea por completo .venv.
echo   --full       Instala tambien dependencias pesadas de entrenamiento.
echo   --no-shell   Configura y valida, pero no abre una consola activada.
echo   --help, -h   Muestra esta ayuda.
exit /b 0

:show_help_error
echo Uso: setup.bat [--force] [--full] [--no-shell]
exit /b 2
