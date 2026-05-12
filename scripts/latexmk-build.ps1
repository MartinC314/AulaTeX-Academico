param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$TexFile,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$LatexmkArgs
)

$ErrorActionPreference = 'Stop'

$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot '..')

function Resolve-TexFile {
    param([string]$Path)

    if ([System.IO.Path]::IsPathRooted($Path)) {
        return (Resolve-Path -LiteralPath $Path).Path
    }

    $fromCurrent = Join-Path (Get-Location) $Path
    if (Test-Path -LiteralPath $fromCurrent) {
        return (Resolve-Path -LiteralPath $fromCurrent).Path
    }

    $fromRoot = Join-Path $ProjectRoot $Path
    return (Resolve-Path -LiteralPath $fromRoot).Path
}

$ResolvedTex = Resolve-TexFile $TexFile
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot 'build/latex') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot 'build/latex/aux') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot 'salidas/pdf') | Out-Null

Push-Location $ProjectRoot
try {
    & latexmk -pdf -interaction=nonstopmode -file-line-error @LatexmkArgs $ResolvedTex
    $LatexmkExitCode = $LASTEXITCODE
    if ($LatexmkExitCode -ne 0) {
        exit $LatexmkExitCode
    }

    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($ResolvedTex)
    $GeneratedPdf = Join-Path $ProjectRoot ("build/latex/{0}.pdf" -f $BaseName)
    $FinalPdf = Join-Path $ProjectRoot ("salidas/pdf/{0}.pdf" -f $BaseName)

    if (-not (Test-Path -LiteralPath $GeneratedPdf -PathType Leaf)) {
        Write-Error "No se encontro el PDF generado: $GeneratedPdf"
        exit 1
    }

    Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Force
    Write-Host "PDF final: $FinalPdf"
    exit 0
}
finally {
    Pop-Location
}
