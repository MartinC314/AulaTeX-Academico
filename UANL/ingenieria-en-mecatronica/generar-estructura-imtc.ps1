param(
    [switch]$DownloadPrograms
)

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$script:SearchCache = @{}

$courses = @(
    'Cultura de paz y derechos humanos',
    'Igualdad de genero, diversidad sexual e inclusion',
    'Calculo diferencial',
    'Algebra para ingenieria',
    'Geometria analitica',
    'Quimica general',
    'Laboratorio de quimica general',
    'Mecanica clasica',
    'Laboratorio de mecanica clasica',
    'Liderazgo, emprendimiento e innovacion',
    'Responsabilidad social y desarrollo sustentable',
    'Etica, transparencia y cultura de la legalidad',
    'Calculo integral',
    'Ciencia de los materiales',
    'Probabilidad y estadistica',
    'Ondas y calor',
    'Laboratorio de ondas y calor',
    'Dibujo para ingenieria',
    'Ecuaciones diferenciales',
    'Programacion basica',
    'Mecanica vectorial',
    'Electricidad y magnetismo',
    'Laboratorio de electricidad y magnetismo',
    'Procesos de manufactura',
    'Laboratorio de procesos de manufactura',
    'Termodinamica basica',
    'Laboratorio de termodinamica basica',
    'Introduccion a la mecatronica',
    'Algebra lineal',
    'Series de Fourier y transformadas de Laplace',
    'Fisica moderna',
    'Laboratorio de fisica moderna',
    'Mecanica de materiales',
    'Laboratorio de mecanica de materiales',
    'Mecanica y potencia de fluidos',
    'Laboratorio de mecanica y potencia de fluidos',
    'Circuitos electricos',
    'Laboratorio de circuitos electricos',
    'Electronica digital',
    'Laboratorio de electronica digital',
    'Modelado y simulacion de sistemas mecatronicos',
    'Diseno de maquinas',
    'Laboratorio de diseno de maquinas',
    'Maquinas electricas',
    'Laboratorio de maquinas electricas',
    'Analisis de sistemas dinamicos',
    'Laboratorio de analisis de sistemas dinamicos',
    'Electronica analogica',
    'Laboratorio de electronica analogica',
    'Diseno e ingenieria por computadora',
    'Laboratorio de diseno e ingenieria por computadora',
    'Sensores y actuadores',
    'Laboratorio de sensores y actuadores',
    'Introduccion a la ciencia de datos',
    'Amplificadores operacionales',
    'Laboratorio de amplificadores operacionales',
    'Control de sistemas lineales',
    'Laboratorio de control de sistemas lineales',
    'Microcontroladores',
    'Laboratorio de microcontroladores',
    'Sistemas de control logico',
    'Laboratorio de sistemas de control logico',
    'Optativa I area curricular de formacion profesional fundamental',
    'Diseno de mecanismos de precision',
    'Laboratorio de diseno de mecanismos de precision',
    'Inteligencia artificial y redes neuronales',
    'Adquisicion de datos con sistemas embebidos',
    'Arquitectura de robots',
    'Laboratorio de arquitectura de robots',
    'Prototipados rapidos',
    'Laboratorio de prototipados rapidos',
    'Optativa II area curricular de formacion profesional fundamental',
    'Optativa III area curricular de formacion profesional fundamental',
    'Optativa IV area curricular de formacion profesional fundamental',
    'Optativa V area curricular de formacion profesional fundamental',
    'Diseno de sistemas mecatronicos',
    'Laboratorio de diseno de sistemas mecatronicos',
    'Robotica industrial',
    'Laboratorio de robotica industrial',
    'Servicio social',
    'Optativa I area curricular de formacion profesional integradora',
    'Optativa II area curricular de formacion profesional integradora',
    'Proyecto integrador de ingenieria mecatronica',
    'Practicas profesionales',
    'Optativa III area curricular de formacion profesional integradora',
    'Seminario para el desempeno profesional',
    'Optativa IV area curricular de formacion profesional integradora'
)

function To-Slug {
    param(
        [Parameter(Mandatory)]
        [string]$Name
    )

    $manualMap = @{
        'Igualdad de genero, diversidad sexual e inclusion' = 'igualdad-genero-div-sexual-incl-imtc'
        'Etica, transparencia y cultura de la legalidad' = 'etica-transp-cultura-legalidad-imtc'
        'Responsabilidad social y desarrollo sustentable' = 'resp-social-desarrollo-sust-imtc'
        'Modelado y simulacion de sistemas mecatronicos' = 'modelado-sim-sist-mecatronicos-imtc'
        'Proyecto integrador de ingenieria mecatronica' = 'proyecto-integrador-mecatronica-imtc'
        'Optativa I area curricular de formacion profesional fundamental' = 'optativa-i-fundamental-imtc'
        'Optativa II area curricular de formacion profesional fundamental' = 'optativa-ii-fundamental-imtc'
        'Optativa III area curricular de formacion profesional fundamental' = 'optativa-iii-fundamental-imtc'
        'Optativa IV area curricular de formacion profesional fundamental' = 'optativa-iv-fundamental-imtc'
        'Optativa V area curricular de formacion profesional fundamental' = 'optativa-v-fundamental-imtc'
        'Optativa I area curricular de formacion profesional integradora' = 'optativa-i-integradora-imtc'
        'Optativa II area curricular de formacion profesional integradora' = 'optativa-ii-integradora-imtc'
        'Optativa III area curricular de formacion profesional integradora' = 'optativa-iii-integradora-imtc'
        'Optativa IV area curricular de formacion profesional integradora' = 'optativa-iv-integradora-imtc'
    }

    if ($manualMap.ContainsKey($Name)) {
        return $manualMap[$Name]
    }

    $slug = (To-LegacySlug -Name $Name) -replace '-imtc$', ''
    if ($slug.Length -le 40) {
        return "$slug-imtc"
    }

    $slug = $slug -replace 'laboratorio', 'lab'
    $slug = $slug -replace 'responsabilidad', 'resp'
    $slug = $slug -replace 'diversidad', 'div'
    $slug = $slug -replace 'inclusion', 'incl'
    $slug = $slug -replace 'transparencia', 'transp'
    $slug = $slug -replace 'simulacion', 'sim'
    $slug = $slug -replace 'sistemas', 'sist'
    $slug = $slug -replace 'ingenieria', 'ing'
    $slug = $slug -replace 'sustentable', 'sust'
    $slug = $slug -replace 'potencia', 'pot'
    $slug = $slug -replace 'mecanismos', 'mecan'
    $slug = $slug -replace 'precision', 'prec'
    $slug = $slug -replace 'analisis', 'anal'
    $slug = $slug -replace 'mecatronicos', 'mecatron'
    $slug = $slug -replace 'mecatronica', 'mecatron'
    $slug = $slug -replace 'electricos', 'elec'
    $slug = $slug -replace 'operacionales', 'operac'
    $slug = $slug -replace 'adquisicion', 'adq'
    $slug = (($slug -split '-') | Where-Object {
        $_ -and $_ -notin @('de', 'del', 'la', 'el', 'los', 'las', 'y', 'e', 'para', 'por', 'con', 'area', 'curricular', 'formacion', 'profesional')
    }) -join '-'

    if ($slug.Length -gt 40) {
        $slug = $slug.Substring(0, 40).Trim('-')
    }

    return "$slug-imtc"
}

function To-LegacySlug {
    param(
        [Parameter(Mandatory)]
        [string]$Name
    )

    $slug = $Name.ToLowerInvariant()
    $slug = $slug -replace '&', ' y '
    $slug = $slug -replace '[^a-z0-9]+', '-'
    $slug = $slug.Trim('-')
    return "$slug-imtc"
}

function Remove-Diacritics {
    param(
        [string]$Text
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ''
    }

    $normalized = $Text.Normalize([Text.NormalizationForm]::FormD)
    $builder = New-Object System.Text.StringBuilder
    foreach ($char in $normalized.ToCharArray()) {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($char) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$builder.Append($char)
        }
    }

    return $builder.ToString().Normalize([Text.NormalizationForm]::FormC)
}

function Normalize-Text {
    param(
        [string]$Text
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ''
    }

    $value = [System.Net.WebUtility]::HtmlDecode($Text)
    $value = Remove-Diacritics -Text $value
    $value = $value.ToLowerInvariant()
    $value = $value -replace '<[^>]+>', ' '
    $value = $value -replace '[^a-z0-9]+', ' '
    $value = $value -replace '\s+', ' '
    return $value.Trim()
}

function Get-CourseAliases {
    param(
        [Parameter(Mandatory)]
        [string]$CourseName
    )

    $aliases = [System.Collections.Generic.List[string]]::new()
    $aliases.Add($CourseName)

    switch ($CourseName) {
        'Algebra para ingenieria' {
            $aliases.Add('Algebra')
        }
        'Programacion basica' {
            $aliases.Add('Metodologia de la programacion')
        }
        'Dibujo para ingenieria' {
            $aliases.Add('Dibujo tecnico')
            $aliases.Add('Dibujo')
        }
        'Introduccion a la mecatronica' {
            $aliases.Add('Mecatronica')
        }
        'Series de Fourier y transformadas de Laplace' {
            $aliases.Add('Transformadas de Laplace')
            $aliases.Add('Series de Fourier')
        }
        'Adquisicion de datos con sistemas embebidos' {
            $aliases.Add('Adquisicion de datos')
        }
        'Inteligencia artificial y redes neuronales' {
            $aliases.Add('Redes neuronales')
            $aliases.Add('Inteligencia artificial')
        }
    }

    return $aliases | Select-Object -Unique
}

function Get-MediaSearchResults {
    param(
        [Parameter(Mandatory)]
        [string]$Query
    )

    $normalizedQuery = Normalize-Text -Text $Query
    if ([string]::IsNullOrWhiteSpace($normalizedQuery)) {
        return @()
    }

    if ($script:SearchCache.ContainsKey($normalizedQuery)) {
        return $script:SearchCache[$normalizedQuery]
    }

    $apiUrl = 'https://www.uanl.mx/wp-json/wp/v2/media?search={0}&per_page=40' -f [uri]::EscapeDataString($normalizedQuery)
    try {
        $items = @(Invoke-RestMethod -Uri $apiUrl -TimeoutSec 45)
    } catch {
        $items = @()
    }

    [void]($script:SearchCache[$normalizedQuery] = $items)
    return $items
}

function Move-ExistingPath {
    param(
        [Parameter(Mandatory)]
        [string]$Source,
        [Parameter(Mandatory)]
        [string]$Destination
    )

    if (-not (Test-Path -LiteralPath $Source)) {
        return
    }

    if (-not (Test-Path -LiteralPath $Destination)) {
        Move-Item -LiteralPath $Source -Destination $Destination
        return
    }

    Get-ChildItem -LiteralPath $Source -Force | ForEach-Object {
        Move-Item -LiteralPath $_.FullName -Destination $Destination -Force
    }
    Remove-Item -LiteralPath $Source -Force -Recurse
}

function Get-BestProgramUrl {
    param(
        [Parameter(Mandatory)]
        [string]$CourseName
    )

    if ($CourseName -like 'Optativa *' -or $CourseName -in @('Servicio social', 'Practicas profesionales')) {
        return $null
    }

    $stopWords = @('de', 'del', 'la', 'las', 'los', 'el', 'y', 'e', 'para', 'por', 'con', 'area', 'curricular', 'formacion', 'profesional')
    $querySet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $candidateMap = @{}
    $normalizedNames = [System.Collections.Generic.List[string]]::new()

    foreach ($alias in @(Get-CourseAliases -CourseName $CourseName)) {
        $normalizedAlias = Normalize-Text -Text $alias
        if ([string]::IsNullOrWhiteSpace($normalizedAlias)) {
            continue
        }

        $normalizedNames.Add($normalizedAlias) | Out-Null
        [void]$querySet.Add($normalizedAlias)
        [void]$querySet.Add(($normalizedAlias -replace '\blaboratorio de\b', 'laboratorio'))

        $tokens = $normalizedAlias.Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries) |
            Where-Object { $_.Length -ge 4 -and $_ -notin $stopWords }

        if ($tokens.Count -ge 2) {
            [void]$querySet.Add(($tokens[0..([Math]::Min(1, $tokens.Count - 1))] -join ' '))
        }

        foreach ($token in ($tokens | Select-Object -First 3)) {
            [void]$querySet.Add($token)
        }

        if ($normalizedAlias -like 'laboratorio de *') {
            [void]$querySet.Add(($normalizedAlias -replace '^laboratorio de ', ''))
        }
    }

    foreach ($query in $querySet) {
        foreach ($item in @(Get-MediaSearchResults -Query $query)) {
            if ($item.mime_type -ne 'application/pdf') {
                continue
            }

            [void]($candidateMap[$item.id] = $item)
        }
    }

    $bestUrl = $null
    $bestScore = -1

    foreach ($item in $candidateMap.Values) {
        $blob = Normalize-Text -Text (@(
            $item.title.rendered,
            $item.description.rendered,
            $item.caption.rendered,
            $item.source_url
        ) -join ' ')

        $title = Normalize-Text -Text $item.title.rendered
        $url = Normalize-Text -Text $item.source_url

        $score = 0
        foreach ($name in $normalizedNames | Select-Object -Unique) {
            $nameTokens = $name.Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries) |
                Where-Object { $_.Length -ge 4 -and $_ -notin $stopWords }

            $tokenMatches = @($nameTokens | Where-Object { $blob -like "*$_*" }).Count
            if ($nameTokens.Count -gt 0) {
                $score += ($tokenMatches * 14)
            }

            if ($blob -like "*$name*") { $score += 100 }
            if ($title -like "*$name*") { $score += 120 }
            if ($url -like "*$name*") { $score += 90 }
        }

        if ($blob -like '*programa analitico modalidad escolarizada*') { $score += 110 }
        if ($blob -like '*programa analitico*') { $score += 60 }
        if ($blob -like '*plan analitico*') { $score += 30 }
        if ($blob -like '*plan sintetico y plan analitico*') { $score += 15 }
        if ($blob -like '*modalidad no escolarizada*') { $score -= 60 }
        if ($blob -like '*modalidad mixta*') { $score -= 40 }
        if ($blob -match '(^| )pa( |$)' -or $url -like '* pa *') { $score += 35 }
        if ($item.source_url -match '(^|[_/\-])pa([_/\-]|$)') { $score += 55 }
        if ($item.source_url -match '(^|[_/\-])ps([_/\-]|$)') { $score -= 15 }
        if ($item.source_url -match '(^|[_/\-])me([_/\-]|$)' -and $item.source_url -match '(^|[_/\-])pa([_/\-]|$)') { $score += 25 }
        if ($title -like '*topicos*' -and ($normalizedNames -notcontains 'topicos de algebra')) { $score -= 50 }

        if ($CourseName -like 'Laboratorio de *' -and $blob -notlike '*laboratorio*' -and $blob -notlike '*lab *') {
            $score -= 80
        }

        if ($CourseName -notlike 'Laboratorio de *' -and $blob -like '*laboratorio de *') {
            $score -= 20
        }

        if ($score -gt $bestScore) {
            [void]($bestScore = $score)
            [void]($bestUrl = $item.source_url)
        }
    }

    if ($bestScore -lt 95) {
        return $null
    }

    return $bestUrl
}

$createdDirectories = 0
$downloadedPrograms = 0
$missingPrograms = [System.Collections.Generic.List[string]]::new()
$downloadErrors = [System.Collections.Generic.List[string]]::new()

foreach ($course in $courses) {
    $slug = To-Slug -Name $course
    $legacySlug = To-LegacySlug -Name $course
    $subjectRoot = Join-Path $root $slug
    $legacyRoot = Join-Path $root $legacySlug

    if ($legacySlug -ne $slug) {
        Move-ExistingPath -Source $legacyRoot -Destination $subjectRoot
        Move-ExistingPath -Source (Join-Path $subjectRoot "planeaciones-$legacySlug") -Destination (Join-Path $subjectRoot "planeaciones-$slug")
        Move-ExistingPath -Source (Join-Path $subjectRoot "referencias-$legacySlug") -Destination (Join-Path $subjectRoot "referencias-$slug")
        Move-ExistingPath -Source (Join-Path (Join-Path $subjectRoot "referencias-$slug") "notas-$legacySlug") -Destination (Join-Path (Join-Path $subjectRoot "referencias-$slug") "notas-$slug")
        Move-ExistingPath -Source (Join-Path (Join-Path $subjectRoot "referencias-$slug") "referencias-$legacySlug") -Destination (Join-Path (Join-Path $subjectRoot "referencias-$slug") "referencias-$slug")
    }

    $planningRoot = Join-Path $subjectRoot "planeaciones-$slug"
    $referencesRoot = Join-Path $subjectRoot "referencias-$slug"
    $paths = @(
        $subjectRoot,
        (Join-Path $subjectRoot '601_delaCruz _Martin_Act'),
        $planningRoot,
        $referencesRoot,
        (Join-Path $referencesRoot "notas-$slug"),
        (Join-Path $referencesRoot "referencias-$slug")
    )

    foreach ($path in $paths) {
        if (-not (Test-Path -LiteralPath $path)) {
            New-Item -ItemType Directory -Path $path -Force | Out-Null
            $createdDirectories++
        }
    }

    $targetPdf = Join-Path $planningRoot "p-analitico-$slug.pdf"
    if (-not (Test-Path -LiteralPath $targetPdf)) {
        $existingPdf = Get-ChildItem -LiteralPath $planningRoot -Filter 'p-analitico-*.pdf' -File -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if ($existingPdf) {
            Move-Item -LiteralPath $existingPdf.FullName -Destination $targetPdf -Force
        }
    }

    if (-not $DownloadPrograms) {
        continue
    }

    if (Test-Path -LiteralPath $targetPdf) {
        continue
    }

    $programUrl = Get-BestProgramUrl -CourseName $course
    if (-not $programUrl) {
        $missingPrograms.Add($course) | Out-Null
        continue
    }

    try {
        Invoke-WebRequest -Uri $programUrl -OutFile $targetPdf -TimeoutSec 90
        $downloadedPrograms++
    } catch {
        $downloadErrors.Add("$course => $programUrl") | Out-Null
    }
}

Write-Output ("Materias consideradas: {0}" -f $courses.Count)
Write-Output ("Directorios creados: {0}" -f $createdDirectories)

if ($DownloadPrograms) {
    Write-Output ("Programas descargados: {0}" -f $downloadedPrograms)
    Write-Output ("Materias sin programa localizado: {0}" -f $missingPrograms.Count)
    Write-Output ("Errores de descarga: {0}" -f $downloadErrors.Count)

    if ($missingPrograms.Count -gt 0) {
        Write-Output 'Primeras materias sin programa localizado:'
        $missingPrograms | Select-Object -First 20 | ForEach-Object { Write-Output $_ }
    }

    if ($downloadErrors.Count -gt 0) {
        Write-Output 'Primeros errores de descarga:'
        $downloadErrors | Select-Object -First 20 | ForEach-Object { Write-Output $_ }
    }
}