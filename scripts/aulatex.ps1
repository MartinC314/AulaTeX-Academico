param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CommandArgs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
$entry = Join-Path $PSScriptRoot 'aulatex_agent.py'
$venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'

$pythonCmd = if (Test-Path $venvPython) {
    $venvPython
}
else {
    'python'
}

if (($null -eq $CommandArgs) -or ($CommandArgs.Count -eq 0)) {
    & $pythonCmd $entry gui
}
elseif ($CommandArgs[0] -in @('monitor-inteligente', 'motor-inteligente-monitor')) {
    # Atajo al monitor visual del motor inteligente (barra de avance en vivo).
    # El array splatting de PowerShell NO reconoce nombres de parámetro (trata
    # todo como posicional), así que convertimos "-Nombre valor" y "-Switch" en
    # un hashtable de splatting, que sí respeta los nombres del script destino.
    $monitor = Join-Path $PSScriptRoot 'motor-inteligente-monitor.ps1'
    $switchParams = @('Plan', 'Gui', 'Console')
    $params = @{}
    $i = 1
    while ($i -lt $CommandArgs.Count) {
        $token = [string]$CommandArgs[$i]
        if ($token -match '^-{1,2}(.+)$') {
            $name = $matches[1]
            $isSwitch = $switchParams -contains $name
            if ($isSwitch) {
                $params[$name] = $true
                $i++
            }
            elseif (($i + 1) -lt $CommandArgs.Count -and ([string]$CommandArgs[$i + 1]) -notmatch '^-{1,2}[A-Za-z]') {
                $params[$name] = [string]$CommandArgs[$i + 1]
                $i += 2
            }
            else {
                # Bandera sin valor explícito: se trata como switch/booleana.
                $params[$name] = $true
                $i++
            }
        }
        else {
            $i++
        }
    }
    & $monitor @params
    exit $LASTEXITCODE
}
else {
    & $pythonCmd $entry @CommandArgs
}
