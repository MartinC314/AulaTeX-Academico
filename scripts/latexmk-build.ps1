param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$TexFile,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$LatexmkArgs
)

$ErrorActionPreference = 'Stop'

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

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
    if (Test-Path -LiteralPath $fromRoot) {
        return (Resolve-Path -LiteralPath $fromRoot).Path
    }

    if ([System.IO.Path]::GetFileName($Path) -eq $Path) {
        $matches = @(Get-ChildItem -LiteralPath $ProjectRoot -Recurse -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -ieq $Path } |
            Sort-Object FullName)

        if ($matches.Count -eq 1) {
            return $matches[0].FullName
        }

        if ($matches.Count -gt 1) {
            $matchList = ($matches | ForEach-Object { $_.FullName }) -join ', '
            throw "Se encontraron varios archivos con el nombre '$Path': $matchList. Usa una ruta mas especifica."
        }
    }

    throw "No se encontro el archivo TeX '$Path'. Se intento desde la carpeta actual y desde la raiz del proyecto."
}

$ResolvedTex = Resolve-TexFile $TexFile
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot '.build/latex') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot '.build/latex/aux') | Out-Null

Push-Location $ProjectRoot
try {
    & latexmk -pdf -interaction=nonstopmode -file-line-error @LatexmkArgs $ResolvedTex
    $LatexmkExitCode = $LASTEXITCODE
    if ($LatexmkExitCode -ne 0) {
        exit $LatexmkExitCode
    }

    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($ResolvedTex)
    $GeneratedPdfCandidates = @(
        (Join-Path $ProjectRoot (".build/latex/{0}.pdf" -f $BaseName)),
        (Join-Path $ProjectRoot (".build/latex/aux/{0}.pdf" -f $BaseName))
    )
    $GeneratedPdf = $GeneratedPdfCandidates | Where-Object {
        Test-Path -LiteralPath $_ -PathType Leaf
    } | Select-Object -First 1
    $FinalPdf = Join-Path (Split-Path -Parent $ResolvedTex) ("{0}.pdf" -f $BaseName)

    if (-not $GeneratedPdf) {
        Write-Error "No se encontro el PDF generado en las rutas esperadas: $($GeneratedPdfCandidates -join ', ')"
        exit 1
    }

    Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Force
    Write-Host "PDF final: $FinalPdf"
    exit 0
}
finally {
    Pop-Location
}
