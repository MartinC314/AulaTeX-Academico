<#
.SYNOPSIS
  Orquesta los 100 ciclos de realizar-actividad del motor-inteligente para la
  Actividad 2 de Derecho a la Seguridad Social en LOTES OBSERVABLES con watchdog.

.DESCRIPTION
  El flujo `agent --cycle-mode full --iterations 100` es vulnerable a cuelgues de
  red sin timeout (documentado en activity_contract.iterative_improvement_rules).
  Este orquestador lo divide en lotes pequeños, cada uno como un Job con timeout
  (watchdog). Si un lote se cuelga, se detiene y continúa con el siguiente, de
  modo que el avance es observable y resistente a cuelgues.

.NOTES
  Cada lote escribe su propio run en retroalimentacion-editorial/aulatex/runs.
  El progreso agregado se registra en el log de progreso.
#>
param(
    [int]$TotalCycles = 100,
    [int]$BatchSize = 10,
    [int]$LlmTimeoutSeconds = 120,
    [int]$BatchWatchdogSeconds = 1500,
    [string]$Target = '.\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\reporte-derecho-a-la-seguridad-social-Actividad-1.tex'
)

$ErrorActionPreference = 'Stop'
$root = 'C:\Users\delaCruz\Documents\AulaTeX-Academico'
Set-Location $root

$logDir = Join-Path $root '.aulatex-temp\act2-100ciclos'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$progressLog = Join-Path $logDir 'progreso-lotes.log'
$engines = @('GPT-5.6-SOL', 'GPT-5.6-Luna', 'GPT-5.6-Terra')

$batches = [math]::Ceiling($TotalCycles / $BatchSize)
$completedCycles = 0
$startedAt = Get-Date

function Write-Progress-Line([string]$msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $msg
    Write-Host $line
    Add-Content -Path $progressLog -Value $line -Encoding UTF8
}

Write-Progress-Line "INICIO: $TotalCycles ciclos en $batches lotes de $BatchSize (LLM timeout=$LlmTimeoutSeconds s, watchdog=$BatchWatchdogSeconds s)"

for ($b = 1; $b -le $batches; $b++) {
    $remaining = $TotalCycles - $completedCycles
    $thisBatch = [math]::Min($BatchSize, $remaining)
    if ($thisBatch -le 0) { break }

    Write-Progress-Line "LOTE $b/$batches -> ejecutando $thisBatch ciclos (acumulado previo: $completedCycles)"

    $job = Start-Job -ScriptBlock {
        param($r, $tgt, $iters, $llmTo, $eng)
        Set-Location $r
        $env:AULATEX_LLM_TIMEOUT_SECONDS = "$llmTo"
        $env:PYTHONUTF8 = '1'
        $engineArgs = @()
        foreach ($e in $eng) { $engineArgs += '--engine'; $engineArgs += $e }
        & '.\.venv\Scripts\python.exe' '.\scripts\aulatex_agent.py' agent `
            --action realizar-actividad --target $tgt --activity 2 `
            --iterations $iters --cycle-mode full --no-compile --no-detail-planner `
            @engineArgs 2>&1
    } -ArgumentList $root, $Target, $thisBatch, $LlmTimeoutSeconds, $engines

    $done = Wait-Job $job -Timeout $BatchWatchdogSeconds
    if ($done) {
        $out = Receive-Job $job
        $tail = ($out | Select-Object -Last 3) -join ' | '
        $completedCycles += $thisBatch
        Write-Progress-Line "LOTE $b OK. acumulado=$completedCycles/$TotalCycles. cola: $tail"
    }
    else {
        Stop-Job $job
        Write-Progress-Line "LOTE $b TIMEOUT (watchdog $BatchWatchdogSeconds s). Se detiene y continua siguiente lote."
        # Limpiar procesos python colgados del lote
        Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
            Where-Object { $_.CommandLine -like '*aulatex_agent.py*' } |
            ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    }
    Remove-Job $job -Force -ErrorAction SilentlyContinue
}

$elapsed = [math]::Round(((Get-Date) - $startedAt).TotalMinutes, 1)
Write-Progress-Line "FIN. ciclos completados=$completedCycles/$TotalCycles en $elapsed min."
