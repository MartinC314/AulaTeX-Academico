<#
.SYNOPSIS
    Reconstruye por completo el entorno virtual (.venv) de AulaTeX-Academico.

.DESCRIPTION
    El contenido de .venv NO se versiona (ver .venv/.gitignore); solo se
    conserva este script y el .gitignore. Ejecutalo para regenerar el
    entorno virtual desde cero e instalar todas las dependencias de Python
    declaradas en los archivos requirements-*.txt del proyecto.

    Pasos:
      1. Crea (o recrea con -Force) el entorno virtual .venv en la raiz.
      2. Actualiza pip, setuptools y wheel.
      3. Instala las dependencias de todos los requirements del proyecto.

.PARAMETER PythonExe
    Ruta al interprete de Python usado para crear el entorno.
    Por defecto usa "py -3.14" si esta disponible, o el "python" del PATH.

.PARAMETER Force
    Elimina un .venv existente antes de crearlo de nuevo.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .venv\install-venv.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .venv\install-venv.ps1 -Force
#>
[CmdletBinding()]
param(
    [string]$PythonExe = "",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

# --- Rutas base ---------------------------------------------------------------
# El script vive en <repo>/.venv/, la raiz del proyecto es su carpeta padre.
$VenvDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $VenvDir

Write-Host "==> Raiz del proyecto : $RepoRoot"
Write-Host "==> Entorno virtual   : $VenvDir"

# --- Seleccionar interprete de Python -----------------------------------------
function Resolve-Python {
    param([string]$Preferred)

    if ($Preferred) {
        if (Test-Path $Preferred) { return $Preferred }
        throw "No se encontro el interprete indicado: $Preferred"
    }

    # Intentar el Python Launcher con la version del proyecto (3.14).
    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) {
        try {
            & py -3.14 --version *> $null
            if ($LASTEXITCODE -eq 0) { return "py -3.14" }
        } catch { }
        return "py -3"
    }

    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) { return "python" }

    throw "No se encontro Python. Instala Python 3.14 o ajusta -PythonExe."
}

$pythonCmd = Resolve-Python -Preferred $PythonExe
Write-Host "==> Interprete base   : $pythonCmd"

# --- (Re)crear el entorno virtual ---------------------------------------------
$venvPython = Join-Path $VenvDir "Scripts\python.exe"

if ((Test-Path $venvPython) -and -not $Force) {
    Write-Host "==> El entorno ya existe. Usa -Force para recrearlo desde cero."
} else {
    if (Test-Path $venvPython) {
        Write-Host "==> Eliminando entorno existente (-Force)..."
        # Conservar este script y su .gitignore al recrear.
        Get-ChildItem -Path $VenvDir -Force |
            Where-Object { $_.Name -notin @("install-venv.ps1", ".gitignore") } |
            Remove-Item -Recurse -Force
    }

    Write-Host "==> Creando entorno virtual..."
    $createArgs = "-m venv `"$VenvDir`""
    Start-Process -FilePath "cmd.exe" `
        -ArgumentList "/c $pythonCmd $createArgs" `
        -NoNewWindow -Wait

    if (-not (Test-Path $venvPython)) {
        throw "Fallo la creacion del entorno virtual en $VenvDir"
    }
}

# --- Actualizar herramientas base ---------------------------------------------
Write-Host "==> Actualizando pip, setuptools y wheel..."
& $venvPython -m pip install --upgrade pip setuptools wheel

# --- Instalar dependencias del proyecto ---------------------------------------
$requirements = @(
    "scripts\requirements-aulatex-langchain.txt",
    "scripts\requirements-aulatex-deepagents.txt",
    "scripts\interfaz\requirements.txt",
    "scripts\extractor-conceptos-ideas\requirements.txt"
)

foreach ($rel in $requirements) {
    $reqPath = Join-Path $RepoRoot $rel
    if (Test-Path $reqPath) {
        Write-Host "==> Instalando dependencias: $rel"
        & $venvPython -m pip install -r $reqPath
    } else {
        Write-Warning "No se encontro el archivo de requisitos: $rel (se omite)"
    }
}

Write-Host ""
Write-Host "==> Entorno virtual reconstruido correctamente."
Write-Host "    Actívalo con:  .\.venv\Scripts\Activate.ps1"
