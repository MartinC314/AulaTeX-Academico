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
else {
    & $pythonCmd $entry @CommandArgs
}
