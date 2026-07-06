param(
    [switch]$Gui
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRoot = Split-Path -Parent $repoRoot
$pythonCandidates = @(
    (Join-Path $workspaceRoot '.venv\Scripts\python.exe'),
    (Join-Path $repoRoot '.venv\Scripts\python.exe')
)
$pythonExe = $pythonCandidates | Where-Object { Test-Path -Path $_ -PathType Leaf } | Select-Object -First 1
$pidFile = Join-Path $repoRoot 'data\notas-bot.pid'
$logDir = Join-Path $repoRoot 'data\logs'
$stdoutLog = Join-Path $logDir 'notas-bot.out.log'
$stderrLog = Join-Path $logDir 'notas-bot.err.log'
$lockPort = 58731
if ($env:BOT_INSTANCE_LOCK_PORT) {
    $lockPort = [int]$env:BOT_INSTANCE_LOCK_PORT
}

function Get-NotasBotProcess {
    Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" |
        Where-Object {
            $cmd = $_.CommandLine
            $cmd -and
            $cmd.IndexOf('-m src.bot', [StringComparison]::OrdinalIgnoreCase) -ge 0 -and
            $cmd.IndexOf($repoRoot, [StringComparison]::OrdinalIgnoreCase) -ge 0
        }
}

function Get-PreferredBotPid {
    param([object[]]$Processes)

    $lockOwner = $null
    try {
        $lockOwner = Get-NetTCPConnection -LocalPort $lockPort -State Listen -ErrorAction SilentlyContinue |
            Select-Object -First 1 -ExpandProperty OwningProcess
    } catch {
        $lockOwner = $null
    }

    if ($lockOwner) {
        foreach ($botProcess in $Processes) {
            if ([int]$botProcess.ProcessId -eq [int]$lockOwner) {
                return [int]$lockOwner
            }
        }
    }

    if ($Processes.Count -gt 0) {
        return [int]($Processes | Sort-Object CreationDate -Descending | Select-Object -First 1).ProcessId
    }

    return $null
}

if (-not $pythonExe) {
    $searchedPaths = $pythonCandidates -join ', '
    throw "No se encontro un interprete virtual para notas-telegram. Rutas probadas: $searchedPaths"
}

if ($Gui -or $env:NOTAS_GUI_MODE -eq '1') {
    Write-Host "Iniciando interfaz grafica local (GUI)..."
    & $pythonExe -m src.gui
    exit $LASTEXITCODE
}

New-Item -ItemType Directory -Path (Split-Path -Parent $pidFile) -Force | Out-Null
New-Item -ItemType Directory -Path $logDir -Force | Out-Null

$runningBotProcesses = @(Get-NotasBotProcess)
if ($runningBotProcesses.Count -gt 0) {
    $existingPid = Get-PreferredBotPid -Processes $runningBotProcesses
    Set-Content -Path $pidFile -Value $existingPid -Encoding ascii
    Write-Host "El bot ya esta en ejecucion con PID $existingPid"
    exit 0
}

if (Test-Path $pidFile) {
    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
}

$process = Start-Process `
    -FilePath $pythonExe `
    -ArgumentList '-m', 'src.bot' `
    -WorkingDirectory $repoRoot `
    -RedirectStandardOutput $stdoutLog `
    -RedirectStandardError $stderrLog `
    -WindowStyle Hidden `
    -PassThru

Start-Sleep -Seconds 1

$runningBotProcesses = @(Get-NotasBotProcess)
if ($runningBotProcesses.Count -eq 0) {
    throw "El bot no quedo en ejecucion. Revisa el log: $stderrLog"
}

$startedPid = Get-PreferredBotPid -Processes $runningBotProcesses
if (-not $startedPid) {
    $startedPid = $process.Id
}

Set-Content -Path $pidFile -Value $startedPid -Encoding ascii

Write-Host "Bot iniciado. PID: $startedPid"
Write-Host "PID file: $pidFile"
Write-Host "Logs: $stdoutLog y $stderrLog"
