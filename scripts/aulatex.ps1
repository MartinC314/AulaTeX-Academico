param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CommandArgs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
$entry = Join-Path $PSScriptRoot 'aulatex_agent.py'

if (($null -eq $CommandArgs) -or ($CommandArgs.Count -eq 0)) {
    python $entry gui
}
else {
    python $entry @CommandArgs
}
