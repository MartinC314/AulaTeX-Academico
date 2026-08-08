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

.PARAMETER Full
    Instala tambien las dependencias pesadas de entrenamiento (SageMaker,
    transformers, TensorFlow Hub). Varios GB; omitidas por defecto.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .venv\install-venv.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .venv\install-venv.ps1 -Force
#>
[CmdletBinding()]
param(
    [string]$PythonExe = "",
    [switch]$Force,
    [switch]$Full
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

function Stop-VenvProcess {
    <#
    .SYNOPSIS
        Cierra procesos que bloquean el .venv (servidores de lenguaje de VS Code,
        REPLs abiertos). Sin esto, Remove-Item falla con "Acceso denegado".
    #>
    param([Parameter(Mandatory)][string]$Dir)

    $locking = @(Get-Process -ErrorAction SilentlyContinue |
        Where-Object { $_.Path -and $_.Path.StartsWith($Dir, [StringComparison]::OrdinalIgnoreCase) })
    if ($locking.Count -eq 0) { return }

    Write-Host "==> Cerrando $($locking.Count) proceso(s) que bloquean el entorno:"
    foreach ($p in $locking) {
        Write-Host "      PID $($p.Id)  $($p.ProcessName)"
        try { Stop-Process -Id $p.Id -Force -ErrorAction Stop } catch {
            Write-Warning "No se pudo cerrar PID $($p.Id): $($_.Exception.Message)"
        }
    }
    Start-Sleep -Milliseconds 800
}

if ((Test-Path $venvPython) -and -not $Force) {
    Write-Host "==> El entorno ya existe. Usa -Force para recrearlo desde cero."
} else {
    if (Test-Path $venvPython) {
        Write-Host "==> Eliminando entorno existente (-Force)..."
        # VS Code relanza sus servidores de lenguaje al instante, asi que se
        # reintenta el borrado en lugar de fallar al primer bloqueo.
        $removed = $false
        for ($attempt = 1; $attempt -le 5 -and -not $removed; $attempt++) {
            Stop-VenvProcess -Dir $VenvDir
            try {
                Get-ChildItem -Path $VenvDir -Force |
                    Where-Object { $_.Name -notin @("install-venv.ps1", ".gitignore") } |
                    Remove-Item -Recurse -Force -ErrorAction Stop
                $removed = $true
            }
            catch {
                Write-Host "    Intento $attempt bloqueado; reintentando..." -ForegroundColor DarkYellow
                Start-Sleep -Seconds 2
            }
        }
        if (-not $removed) {
            throw "No se pudo limpiar $VenvDir. Cierra VS Code o los procesos que usan el entorno y reintenta."
        }
    }

    Write-Host "==> Creando entorno virtual..."
    & cmd.exe /c "$pythonCmd -m venv `"$VenvDir`""

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
    "scripts\extractor-conceptos-ideas\requirements.txt",
    "scripts\extractor-conceptos-ideas\requirements-azure.txt",
    "scripts\extractor-conceptos-ideas\requirements-anthropic.txt"
)

# training y tfhub pesan varios GB y solo hacen falta para entrenar modelos.
if ($Full) {
    $requirements += "scripts\requirements-training.txt"
    $requirements += "scripts\extractor-conceptos-ideas\requirements-tfhub.txt"
}

foreach ($rel in $requirements) {
    $reqPath = Join-Path $RepoRoot $rel
    if (Test-Path $reqPath) {
        Write-Host "==> Instalando dependencias: $rel"
        & $venvPython -m pip install -r $reqPath
        if ($LASTEXITCODE -ne 0) { throw "Fallo la instalacion de $rel" }
    } else {
        Write-Warning "No se encontro el archivo de requisitos: $rel (se omite)"
    }
}

# cryptography solo llegaba como dependencia transitiva de deepagents, pero
# secrets_local.py la necesita para descifrar aulatex.env con AHK_MASTER_PIN.
Write-Host "==> Instalando dependencias directas del nucleo AulaTeX..."
& $venvPython -m pip install "cryptography>=42" "python-dotenv>=1.0.1" "requests>=2.31" "tiktoken>=0.7"
if ($LASTEXITCODE -ne 0) { throw "Fallo la instalacion de las dependencias del nucleo." }

# --- Verificacion --------------------------------------------------------------
Write-Host ""
Write-Host "==> Verificando modulos requeridos..."
$modules = @(
    'cryptography', 'dotenv', 'requests', 'openai', 'httpx', 'tiktoken',
    'langchain', 'langchain_core', 'langchain_openai', 'langchain_anthropic',
    'langgraph', 'anthropic', 'numpy', 'pandas', 'sklearn', 'openpyxl',
    'fitz', 'docx', 'pypdf', 'telegram', 'boto3'
)
$missing = @()
foreach ($m in $modules) {
    & $venvPython -c "import $m" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host ("    {0,-22} OK" -f $m) -ForegroundColor Green
    } else {
        Write-Host ("    {0,-22} FALTA" -f $m) -ForegroundColor Red
        $missing += $m
    }
}

Write-Host ""
if ($missing.Count -gt 0) {
    Write-Warning "Faltan $($missing.Count) modulo(s): $($missing -join ', ')"
    exit 1
}

Write-Host "==> Entorno virtual reconstruido correctamente." -ForegroundColor Green
Write-Host "    Activalo con:  .\.venv\Scripts\Activate.ps1"
Write-Host "    Valida LLMs:   `$env:AHK_MASTER_PIN='<pin>'; .\scripts\aulatex.ps1 llm-check"
