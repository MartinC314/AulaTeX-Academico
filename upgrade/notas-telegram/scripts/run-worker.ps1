Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Resolve repo root (script may be in scripts/)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = if ((Split-Path -Leaf $scriptDir) -ieq 'scripts') { Split-Path -Parent $scriptDir } else { $scriptDir }
$workspaceRoot = Split-Path -Parent $repoRoot
$pythonCandidates = @(
    (Join-Path $workspaceRoot '.venv\Scripts\python.exe'),
    (Join-Path $repoRoot '.venv\Scripts\python.exe')
)
$pythonExe = $pythonCandidates | Where-Object { Test-Path -Path $_ -PathType Leaf } | Select-Object -First 1

if (-not $pythonExe) {
    $searchedPaths = $pythonCandidates -join ', '
    throw "No se encontró un intérprete virtual para notas-telegram. Rutas probadas: $searchedPaths"
}

Push-Location $repoRoot
& $pythonExe -c "from src.worker import run_loop; run_loop()"
Pop-Location
