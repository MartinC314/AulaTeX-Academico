param(
    [string]$Compiler = 'g++',
    [string]$Standard = 'c++11'
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceDir = Join-Path $root 'programas-actividad-2'
$buildDir = Join-Path $root '.build-cpp'
$transcript = Join-Path $root 'resultados-ejecucion-actividad-2.txt'
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

$cases = @(
    @{ File='01_area_cuadrado.cpp'; Input="5" },
    @{ File='02_area_cuadrado_pow.cpp'; Input="5" },
    @{ File='03_area_circulo.cpp'; Input="2" },
    @{ File='04_area_triangulo.cpp'; Input="10`n6" },
    @{ File='05_hipotenusa.cpp'; Input="3`n4" },
    @{ File='06_nombre_semestre.cpp'; Input="Emilio Abraham Castillo Urdiales`n2" },
    @{ File='07_fahrenheit_centigrados.cpp'; Input="32" },
    @{ File='08_pies_metros.cpp'; Input="10" },
    @{ File='09_libras_kilogramos.cpp'; Input="10" },
    @{ File='10_acres_hectareas.cpp'; Input="1" },
    @{ File='11_fuerza.cpp'; Input="10`n2" },
    @{ File='12_velocidad_impacto.cpp'; Input="20" },
    @{ File='13_energia_potencial.cpp'; Input="10`n5" },
    @{ File='14_energia_cinetica.cpp'; Input="10`n3" },
    @{ File='15_hipotenusa_catetos.cpp'; Input="3`n4" },
    @{ File='16_volumen_esfera.cpp'; Input="3" },
    @{ File='17_recibo_luz.cpp'; Input="Emilio Castillo`n250`n0.85" },
    @{ File='18_pies_libras.cpp'; Input="10`n10" },
    @{ File='19_area_heron.cpp'; Input="3`n4`n5" }
)

$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add('EJECUCION AUTOMATIZADA DE LA ACTIVIDAD 2')
$lines.Add(('Fecha: {0:yyyy-MM-dd HH:mm:ss}' -f (Get-Date)))
$lines.Add('Compilador: GNU C++ / Dev-C++ compatible')
$lines.Add('')

foreach ($case in $cases) {
    $source = Join-Path $sourceDir $case.File
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($case.File)
    $executable = Join-Path $buildDir ($baseName + '.exe')
    & $Compiler "-std=$Standard" -Wall -Wextra -pedantic $source -o $executable
    if ($LASTEXITCODE -ne 0) { throw "No se pudo compilar $($case.File)" }

    $output = $case.Input | & $executable 2>&1
    if ($LASTEXITCODE -ne 0) { throw "La prueba fallo para $($case.File)" }

    $inputText = $case.Input -replace "`r?`n", ', '
    $consoleLines = [System.Collections.Generic.List[string]]::new()
    $consoleLines.Add(('> Entrada: {0}' -f $inputText))
    foreach ($line in $output) { $consoleLines.Add([string]$line) }
    $consoleLines.Add('> Proceso finalizado con codigo 0')
    $consolePath = Join-Path $sourceDir ($case.File + '.out')
    $consoleLines | Set-Content -Path $consolePath -Encoding UTF8

    $lines.Add(('===== {0} =====' -f $case.File))
    $lines.Add(('Entrada: {0}' -f $inputText))
    foreach ($line in $output) { $lines.Add([string]$line) }
    $lines.Add('Estado: COMPILACION Y EJECUCION CORRECTAS')
    $lines.Add('')
}

$lines.Add(('TOTAL: {0}/{0} PROGRAMAS CORRECTOS' -f $cases.Count))
$lines | Set-Content -Path $transcript -Encoding UTF8
$lines | ForEach-Object { Write-Host $_ }
Write-Host "Resultados guardados en: $transcript"
Write-Host "Salidas individuales guardadas en: $sourceDir\*.cpp.out"
