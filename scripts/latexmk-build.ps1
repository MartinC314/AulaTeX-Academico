param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$TexFile,

    [ValidateSet('none', 'safe', 'full')]
    [string]$CleanMode = 'safe',

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

function Invoke-BuildCleanup {
    param(
        [string]$Mode,
        [string]$Root
    )

    if ($Mode -eq 'none') {
        return
    }

    $buildRoot = Join-Path $Root '.build/latex'
    if (-not (Test-Path -LiteralPath $buildRoot -PathType Container)) {
        return
    }

    if ($Mode -eq 'full') {
        Get-ChildItem -LiteralPath $buildRoot -Recurse -File -Force -ErrorAction SilentlyContinue |
            Remove-Item -Force -ErrorAction SilentlyContinue
        return
    }

    # Limpieza segura: elimina auxiliares temporales y conserva .log para diagnostico.
    $ephemeralExtensions = @(
        '.aux', '.bbl', '.blg', '.fdb_latexmk', '.fls',
        '.lof', '.lot', '.nav', '.out', '.run.xml', '.snm',
        '.synctex.gz', '.toc', '.vrb', '.xdv'
    )

    Get-ChildItem -LiteralPath $buildRoot -Recurse -File -Force -ErrorAction SilentlyContinue |
        Where-Object {
            $ext = $_.Extension.ToLowerInvariant()
            if ($ext -eq '.gz' -and $_.Name.ToLowerInvariant().EndsWith('.synctex.gz')) {
                return $true
            }
            return $ephemeralExtensions -contains $ext
        } |
        Remove-Item -Force -ErrorAction SilentlyContinue
}

$ResolvedTex = Resolve-TexFile $TexFile
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot '.build/latex') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot '.build/latex/aux') | Out-Null

Push-Location $ProjectRoot
try {
    # Force mode allows latexmk to complete bibliography passes even when
    # the first pdflatex run reports temporary undefined citations.
    & latexmk -f -pdf -interaction=nonstopmode -file-line-error @LatexmkArgs $ResolvedTex
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
    Invoke-BuildCleanup -Mode $CleanMode -Root $ProjectRoot
    Write-Host "PDF final: $FinalPdf"
    exit 0
}
finally {
    Pop-Location
}
