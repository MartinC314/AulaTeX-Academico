param(
    [string]$ScriptBase = "",
    [string]$EnvPath = "",
    [switch]$NoPush,
    [switch]$NonInteractive
)

$ErrorActionPreference = "Stop"

$script:GitLlmRepoRoot = $null
$script:GitLlmCheckpoint = $null
$script:GitLlmPushStarted = $false

function Write-ProgressMarker {
    param(
        [int]$Percent,
        [string]$Message
    )

    $safePercent = [Math]::Max(0, [Math]::Min(100, $Percent))
    [Console]::WriteLine("::progress::$safePercent::$Message")
    [Console]::Out.Flush()
}

function Write-ResultMarker {
    param(
        [string]$Status,
        [string]$Message
    )

    [Console]::WriteLine("::result::$Status::$Message")
    [Console]::Out.Flush()
}

function Write-NoticeMarker {
    param([string]$Message)

    [Console]::WriteLine("::notice::$Message")
    [Console]::Out.Flush()
}

function Get-GitLlmLogPath {
    if ([string]::IsNullOrWhiteSpace($script:GitLlmRepoRoot)) {
        return $null
    }

    $logDir = Join-Path $script:GitLlmRepoRoot 'logs'
    if (-not (Test-Path -LiteralPath $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }

    return Join-Path $logDir 'git-llm-telemetry.log'
}

function Write-GitLlmLog {
    param(
        [string]$Event,
        [hashtable]$Data = @{}
    )

    try {
        $logPath = Get-GitLlmLogPath
        if ([string]::IsNullOrWhiteSpace($logPath)) {
            return
        }

        $payload = [ordered]@{
            timestamp = [DateTimeOffset]::Now.ToString('o')
            event = $Event
        }

        foreach ($key in ($Data.Keys | Sort-Object)) {
            $payload[$key] = $Data[$key]
        }

        Add-Content -LiteralPath $logPath -Value (($payload | ConvertTo-Json -Compress -Depth 8)) -Encoding UTF8
    } catch {
    }
}

function Get-EnvIntValue {
    param(
        [string]$Name,
        [int]$DefaultValue
    )

    $value = [Environment]::GetEnvironmentVariable($Name, 'Process')
    if ([string]::IsNullOrWhiteSpace($value)) {
        return $DefaultValue
    }

    $parsed = 0
    if ([int]::TryParse($value, [ref]$parsed) -and $parsed -gt 0) {
        return $parsed
    }

    return $DefaultValue
}

function Get-LlmMaxInputTokens {
    return Get-EnvIntValue -Name 'GIT_LLM_MAX_INPUT_TOKENS' -DefaultValue 200000
}

function Get-LlmMaxOutputTokens {
    return Get-EnvIntValue -Name 'GIT_LLM_MAX_OUTPUT_TOKENS' -DefaultValue 100000
}

function Get-LlmTimeoutSeconds {
    return Get-EnvIntValue -Name 'GIT_LLM_TIMEOUT_SECONDS' -DefaultValue 300
}

function Get-LlmRetryCount {
    return Get-EnvIntValue -Name 'GIT_LLM_RETRY_COUNT' -DefaultValue 3
}

function Get-LlmBackoffBaseMilliseconds {
    return Get-EnvIntValue -Name 'GIT_LLM_BACKOFF_BASE_MS' -DefaultValue 2000
}

function Get-LlmBackoffMaxMilliseconds {
    return Get-EnvIntValue -Name 'GIT_LLM_BACKOFF_MAX_MS' -DefaultValue 15000
}

function Get-LlmMaxCommitGroups {
    return Get-EnvIntValue -Name 'GIT_LLM_MAX_COMMIT_GROUPS' -DefaultValue 8
}

function Get-LlmRepairAttempts {
    return Get-EnvIntValue -Name 'GIT_LLM_REPAIR_ATTEMPTS' -DefaultValue 2
}
function Convert-LlmTokensToChars {
    param([int]$Tokens)

    return [Math]::Max(1000, $Tokens * 4)
}

function Load-DotEnv {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "No se encontró el archivo de credenciales: $Path"
    }

    Get-Content -LiteralPath $Path | ForEach-Object {
        $line = $_.Trim()
        if ($line -eq "" -or $line.StartsWith("#") -or $line -notmatch "=") {
            return
        }

        if ($line -match "^([^=]+?)\s*=\s*(.*)$") {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()

            if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
                $value = $value.Substring(1, $value.Length - 2)
            }

            if ($name -ne "") {
                [Environment]::SetEnvironmentVariable($name, $value, "Process")
            }
        }
    }
}

function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)

    $output = & git @Args 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Args -join ' ') falló:`n$output"
    }
    return $output
}

function Invoke-GitOptional {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)

    $output = & git @Args 2>$null
    if ($LASTEXITCODE -ne 0) {
        return $null
    }
    return $output
}

function Invoke-GitUtf8 {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)

    return (& git -c core.quotepath=false @Args 2>&1)
}

function Limit-Text {
    param(
        [string]$Text,
        [int]$MaxChars
    )

    if ($null -eq $Text) {
        return ""
    }

    if ($Text.Length -le $MaxChars) {
        return $Text
    }

    return $Text.Substring(0, $MaxChars) + "`n`n[...contenido truncado para no exceder el límite del LLM: $MaxChars caracteres aprox...]"
}

function Protect-SensitiveStagedFiles {
    $protectedPatterns = @(
        "(^|/)notas\.env$",
        "(^|/)config\.ini$",
        "(^|/)api_credentials\.local\.ini$",
        "(^|/)\.env($|\.)"
    )

    $stagedFiles = Invoke-GitUtf8 diff --cached --name-only --diff-filter=ACMRTUXB
    foreach ($file in $stagedFiles) {
        $normalized = ($file -replace "\\", "/")
        foreach ($pattern in $protectedPatterns) {
            if ($normalized -match $pattern) {
                & git reset -q -- $file | Out-Null
                break
            }
        }
    }
}

function Get-FallbackCommitMessage {
    param(
        [string]$ScriptBase,
        [string[]]$NameStatus
    )

    $subject = if ($ScriptBase -ne "") {
        "chore: compilar $ScriptBase y actualizar cambios"
    } else {
        "chore: actualizar cambios del repositorio"
    }

    $bodyLines = @("", "Cambios incluidos:")
    foreach ($line in ($NameStatus | Select-Object -First 12)) {
        if ($line.Trim() -ne "") {
            $bodyLines += "- $line"
        }
    }

    return ($subject + "`n" + ($bodyLines -join "`n")).TrimEnd()
}

function Normalize-CommitMessage {
    param([string]$Message)

    $message = ($Message -replace '```[a-zA-Z]*', '' -replace '```', '').Trim()
    $lines = @($message -split '\r?\n' | ForEach-Object { ([string]$_).TrimEnd() })

    while ($lines.Count -gt 0 -and ([string]$lines[0]).Trim() -eq "") {
        $lines = @($lines | Select-Object -Skip 1)
    }

    if ($lines.Count -eq 0) {
        return "chore: actualizar cambios del repositorio"
    }

    return ($lines -join "`n").Trim()
}

function Get-FirstCommitLine {
    param([string]$Message)

    if ([string]::IsNullOrWhiteSpace($Message)) {
        return "chore: actualizar cambios del repositorio"
    }

    return (($Message -split '\r?\n') | Select-Object -First 1).Trim()
}

function Get-JsonPayloadFromText {
    param([string]$Text)

    $trimmed = $Text.Trim()
    if ($trimmed.StartsWith('```')) {
        $trimmed = $trimmed -replace '^```[a-zA-Z]*\s*', ''
        $trimmed = $trimmed -replace '\s*```$', ''
    }

    $startObject = $trimmed.IndexOf('{')
    $startArray = $trimmed.IndexOf('[')
    $starts = @($startObject, $startArray) | Where-Object { $_ -ge 0 } | Sort-Object
    if ($starts.Count -eq 0) {
        return $trimmed
    }

    $start = $starts[0]
    $stack = New-Object System.Collections.Stack
    $inString = $false
    $escaped = $false

    for ($i = $start; $i -lt $trimmed.Length; $i++) {
        $char = $trimmed[$i]

        if ($escaped) {
            $escaped = $false
            continue
        }

        if ($char -eq '\\') {
            if ($inString) {
                $escaped = $true
            }
            continue
        }

        if ($char -eq '"') {
            $inString = -not $inString
            continue
        }

        if ($inString) {
            continue
        }

        switch ($char) {
            '{' { [void]$stack.Push('}') }
            '[' { [void]$stack.Push(']') }
            '}' {
                if ($stack.Count -eq 0 -or $stack.Peek() -ne '}') {
                    break
                }
                [void]$stack.Pop()
            }
            ']' {
                if ($stack.Count -eq 0 -or $stack.Peek() -ne ']') {
                    break
                }
                [void]$stack.Pop()
            }
        }

        if ($stack.Count -eq 0) {
            return $trimmed.Substring($start, ($i - $start + 1)).Trim()
        }
    }

    return $trimmed.Substring($start).Trim()
}

function New-LlmPromptVariant {
    param(
        [string]$Name,
        [string]$UserPrompt
    )

    return [pscustomobject]@{
        Name = $Name
        UserPrompt = $UserPrompt
    }
}

function Get-DynamicLlmTimeoutSeconds {
    param(
        [string]$SystemPrompt,
        [string]$UserPrompt,
        [string]$VariantName,
        [int]$Attempt
    )

    $baseTimeout = Get-LlmTimeoutSeconds
    $totalChars = ([string]$SystemPrompt).Length + ([string]$UserPrompt).Length

    if ($totalChars -le 50000) {
        $timeout = [Math]::Max(120, [Math]::Min($baseTimeout, 180))
    } elseif ($totalChars -le 200000) {
        $timeout = [Math]::Max(240, $baseTimeout)
    } else {
        $timeout = [Math]::Max(600, $baseTimeout * 2)
    }

    if ($VariantName -eq 'minimal') {
        $timeout = [Math]::Max(120, [int]($timeout * 0.75))
    }

    if ($VariantName -eq 'compact') {
        $timeout = [Math]::Max(180, [int]($timeout * 0.85))
    }

    return ($timeout + (30 * [Math]::Max(0, $Attempt - 1)))
}

function Invoke-LlmBackoffDelay {
    param([int]$Attempt)

    $baseDelay = Get-LlmBackoffBaseMilliseconds
    $maxDelay = Get-LlmBackoffMaxMilliseconds
    $delay = [Math]::Min($maxDelay, [int]($baseDelay * [Math]::Pow(2, [Math]::Max(0, $Attempt - 1))))
    $jitter = Get-Random -Minimum 150 -Maximum 900
    $totalDelay = [Math]::Min($maxDelay, $delay + $jitter)

    Write-NoticeMarker "Esperando $totalDelay ms antes del siguiente intento con Azure OpenAI..."
    [System.Threading.Thread]::Sleep($totalDelay)
}

function ConvertFrom-JsonLenient {
    param([string]$Text)

    $candidates = New-Object System.Collections.ArrayList
    if (-not [string]::IsNullOrWhiteSpace($Text)) {
        [void]$candidates.Add($Text.Trim())
        $payload = Get-JsonPayloadFromText -Text $Text
        if (-not [string]::IsNullOrWhiteSpace($payload) -and $payload.Trim() -ne $Text.Trim()) {
            [void]$candidates.Add($payload.Trim())
        }
    }

    $seen = @{}
    foreach ($candidate in $candidates) {
        if ([string]::IsNullOrWhiteSpace($candidate) -or $seen.ContainsKey($candidate)) {
            continue
        }

        $seen[$candidate] = $true
        try {
            return ($candidate | ConvertFrom-Json -ErrorAction Stop)
        } catch {
        }
    }

    throw 'No se pudo convertir la respuesta del LLM a JSON valido.'
}

function Get-DatabaseChangeSummary {
    param([string[]]$Files)

    $dbFiles = @($Files | Where-Object { $_ -match '\.db$' })
    if ($dbFiles.Count -eq 0) {
        return ''
    }

    $python = Join-Path (Get-Location) '.venv\Scripts\python.exe'
    if (-not (Test-Path -LiteralPath $python)) {
        $python = 'python'
    }

    $summaryLines = New-Object System.Collections.ArrayList
    foreach ($file in $dbFiles) {
        $normalized = $file -replace '\\', '/'
        $currentPath = Join-Path (Get-Location) $file
        if (-not (Test-Path -LiteralPath $currentPath)) {
            [void]$summaryLines.Add("${normalized}: base eliminada o no disponible en working tree")
            continue
        }

        $oldPath = Join-Path $env:TEMP ("git-llm-old-db-" + [Guid]::NewGuid().ToString('N') + '.db')
        $hasOld = $false
        try {
            $oldSpec = "HEAD:$normalized"
            $cmdLine = 'git show ' + '"' + $oldSpec + '"' + ' > ' + '"' + $oldPath + '"'
            & cmd.exe /d /c $cmdLine 2>$null
            $hasOld = ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $oldPath) -and ((Get-Item -LiteralPath $oldPath).Length -gt 0))
        } catch {
            $hasOld = $false
        }

        $script = @'
import json
import os
import sqlite3
import sys

old_path, new_path, label = sys.argv[1], sys.argv[2], sys.argv[3]

def table_counts(path):
    if not path or not os.path.exists(path):
        return None
    conn = sqlite3.connect(path)
    try:
        tables = [row[0] for row in conn.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%' order by name")]
        counts = {}
        for table in tables:
            quoted = '"' + table.replace('"', '""') + '"'
            try:
                counts[table] = conn.execute(f"select count(*) from {quoted}").fetchone()[0]
            except Exception:
                counts[table] = None
        return counts
    finally:
        conn.close()

old_counts = table_counts(old_path)
new_counts = table_counts(new_path)
if old_counts is None:
    parts = []
    for table, count in (new_counts or {}).items():
        parts.append(f"{table}: nueva tabla con {count} fila(s)" if count is not None else f"{table}: nueva tabla")
    print(f"{label}: base nueva; " + ("; ".join(parts) if parts else "sin tablas de usuario detectadas"))
    sys.exit(0)

changes = []
for table in sorted(set(old_counts) | set(new_counts or {})):
    old = old_counts.get(table)
    new = (new_counts or {}).get(table)
    if old is None and new is not None:
        changes.append(f"{table}: nueva tabla con {new} fila(s)")
    elif old is not None and new is None:
        changes.append(f"{table}: tabla eliminada; antes {old} fila(s)")
    elif old != new:
        changes.append(f"{table}: {old} -> {new} fila(s) ({new - old:+d})")

print(f"{label}: " + ("; ".join(changes) if changes else "sin cambios en conteo de filas; posible cambio de contenido/esquema/binario"))
'@

        $scriptPath = Join-Path $env:TEMP ("git-llm-sqlite-summary-" + [Guid]::NewGuid().ToString('N') + '.py')
        try {
            Set-Content -LiteralPath $scriptPath -Value $script -Encoding UTF8
            $oldArg = if ($hasOld) { $oldPath } else { '' }
            $line = & $python $scriptPath $oldArg $currentPath $normalized 2>$null
            if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace(($line -join ' '))) {
                [void]$summaryLines.Add(($line -join ' '))
            } else {
                [void]$summaryLines.Add("${normalized}: base SQLite modificada")
            }
        } catch {
            [void]$summaryLines.Add("${normalized}: base SQLite modificada")
        } finally {
            if (Test-Path -LiteralPath $scriptPath) {
                Remove-Item -LiteralPath $scriptPath -Force -ErrorAction SilentlyContinue
            }
            if ($hasOld -and (Test-Path -LiteralPath $oldPath)) {
                Remove-Item -LiteralPath $oldPath -Force -ErrorAction SilentlyContinue
            }
        }
    }

    return ($summaryLines -join "`n")
}

function Limit-SubjectLine {
    param(
        [string]$Text,
        [int]$MaxLength = 72
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 'chore: actualiza archivos del repositorio'
    }

    $trimmed = $Text.Trim()
    if ($trimmed.Length -le $MaxLength) {
        return $trimmed
    }

    return ($trimmed.Substring(0, [Math]::Max(1, $MaxLength - 3)).TrimEnd() + '...')
}

function Get-NotasTelegramNotesFamilyKey {
    param([string]$FilePath)

    $normalized = ($FilePath -replace '\\', '/').Trim()
    if ($normalized.StartsWith('"') -and $normalized.EndsWith('"') -and $normalized.Length -ge 2) {
        $normalized = $normalized.Substring(1, $normalized.Length - 2)
    }
    if ($normalized -eq 'notas-telegram/data/notes/index.json') {
        return 'telegram-notes-index-root'
    }

    if ($normalized -notmatch '^notas-telegram/data/notes/([^/]+)/([^/]+)$') {
        return $null
    }

    $dateDir = $matches[1]
    $fileName = $matches[2]
    if ($fileName -ieq 'index.md') {
        return "telegram-notes-index:$dateDir"
    }

    if ($fileName -notmatch '\.md$') {
        return "telegram-notes-file:$dateDir/$fileName"
    }

    $stem = $fileName.Substring(0, $fileName.Length - 3)
    while ($stem -match '\.(explain|dialectic|research|suggest)$') {
        $stem = $stem -replace '\.(explain|dialectic|research|suggest)$', ''
    }

    return "telegram-note:$dateDir/$stem"
}

function Get-NotasTelegramBucketSubject {
    param([string]$Bucket)

    if ($Bucket -eq 'telegram-notes-index-root') {
        return 'docs(notas): actualiza indice global de notas'
    }

    if ($Bucket -match '^telegram-notes-index:(.+)$') {
        return (Limit-SubjectLine -Text ("docs(notas): actualiza indice diario " + $matches[1]))
    }

    if ($Bucket -match '^telegram-note:[^/]+/(.+)$') {
        $stem = $matches[1]
        if ($stem -match '^\d{8}_\d{6}_(.+)$') {
            $stem = $matches[1]
        }

        $label = ($stem -replace '^\d{8}_\d{6}_', '' -replace '[_-]+', ' ').Trim()
        if ([string]::IsNullOrWhiteSpace($label)) {
            $label = $stem
        }

        return (Limit-SubjectLine -Text ("docs(notas): actualiza nota " + $label))
    }

    if ($Bucket -match '^telegram-notes-file:') {
        return 'docs(notas): actualiza archivos auxiliares de notas'
    }

    return $null
}

function Get-ThemeBucketName {
    param([string]$FilePath)

    $normalized = ($FilePath -replace '\\', '/')

    $notesBucket = Get-NotasTelegramNotesFamilyKey -FilePath $normalized
    if (-not [string]::IsNullOrWhiteSpace($notesBucket)) {
        return $notesBucket
    }

    if ($normalized -match '\.db$') {
        return 'database'
    }

    if ($normalized -match '^(README\.md|docs/|.*\.md$)') {
        return 'documentacion'
    }

    if ($normalized -match '^(scripts/|.*\.ps1$)') {
        return 'scripts'
    }

    if ($normalized -match '^(src/|.*\.ahk$)') {
        return 'autohotkey'
    }

    $topLevel = ($normalized -split '/')[0]
    if ([string]::IsNullOrWhiteSpace($topLevel)) {
        return 'otros'
    }

    return $topLevel
}

function Get-FallbackCommitMessageForGroup {
    param(
        [string]$Bucket,
        [string[]]$Files,
        [string]$DatabaseSummary = ''
    )

    $notesSubject = Get-NotasTelegramBucketSubject -Bucket $Bucket
    if (-not [string]::IsNullOrWhiteSpace($notesSubject)) {
        $subject = $notesSubject
    } else {
        $subject = switch ($Bucket) {
        'database' { 'data(db): actualiza bases SQLite versionadas' }
        'documentacion' { 'docs: actualiza documentacion operativa' }
        'scripts' { 'fix(scripts): actualiza automatizaciones de soporte' }
        'autohotkey' { 'feat(ahk): ajusta automatizaciones del menu y atajos' }
        default {
            $scope = ($Bucket -replace '[^a-zA-Z0-9_-]', '-')
            if ([string]::IsNullOrWhiteSpace($scope)) {
                'chore: actualiza archivos del repositorio'
            } else {
                "chore($scope): actualiza archivos del grupo"
            }
        }
        }
    }

    $bodyLines = @('', 'Cambios incluidos:')
    foreach ($file in ($Files | Select-Object -First 12)) {
        $bodyLines += "- $file"
    }

    if ($Bucket -eq 'database' -and -not [string]::IsNullOrWhiteSpace($DatabaseSummary)) {
        $bodyLines += ''
        $bodyLines += 'Resumen SQLite:'
        foreach ($line in ($DatabaseSummary -split '\r?\n' | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
            $bodyLines += "- $line"
        }
    }

    return ($subject + "`n" + ($bodyLines -join "`n")).TrimEnd()
}

function Get-FallbackCommitGroups {
    param([string[]]$StagedFiles)

    $groupsByBucket = [ordered]@{}
    foreach ($file in $StagedFiles) {
        $bucket = Get-ThemeBucketName -FilePath $file
        if (-not $groupsByBucket.Contains($bucket)) {
            $groupsByBucket[$bucket] = New-Object System.Collections.ArrayList
        }
        [void]$groupsByBucket[$bucket].Add($file)
    }

    $databaseSummary = Get-DatabaseChangeSummary -Files $StagedFiles
    $result = New-Object System.Collections.ArrayList
    foreach ($bucket in $groupsByBucket.Keys) {
        $files = @($groupsByBucket[$bucket])
        [void]$result.Add([pscustomobject]@{
            Message = Get-FallbackCommitMessageForGroup -Bucket $bucket -Files $files -DatabaseSummary $databaseSummary
            Files = $files
            Reason = "Agrupacion local por bucket '$bucket'."
        })
    }

    return @($result)
}

function Test-CommitGroupsCoverAllFiles {
    param(
        [object[]]$Groups,
        [string[]]$StagedFiles
    )

    $expected = @{}
    foreach ($file in $StagedFiles) {
        $expected[$file] = 0
    }

    foreach ($group in $Groups) {
        if ($null -eq $group.Files -or $group.Files.Count -eq 0) {
            return $false
        }

        foreach ($file in $group.Files) {
            if (-not $expected.ContainsKey($file)) {
                return $false
            }
            $expected[$file] += 1
        }
    }

    foreach ($file in $expected.Keys) {
        if ($expected[$file] -ne 1) {
            return $false
        }
    }

    return $true
}

function Test-CommitGroupsAreReasonable {
    param([object[]]$Groups)

    if ($null -eq $Groups -or $Groups.Count -eq 0) {
        return $false
    }

    if ($Groups.Count -gt (Get-LlmMaxCommitGroups)) {
        return $false
    }

    foreach ($group in $Groups) {
        $files = @($group.Files)
        if ($files.Count -eq 0) {
            return $false
        }

        $subject = Get-FirstCommitLine -Message ([string]$group.Message)
        if ([string]::IsNullOrWhiteSpace($subject) -or $subject.Length -gt 72) {
            return $false
        }
    }

    return $true
}

function Test-CommitGroupsRespectSpecialFamilies {
    param(
        [object[]]$Groups,
        [string[]]$StagedFiles
    )

    $families = @{}
    foreach ($file in $StagedFiles) {
        $family = Get-NotasTelegramNotesFamilyKey -FilePath $file
        if ([string]::IsNullOrWhiteSpace($family) -or $family -notlike 'telegram-note:*') {
            continue
        }

        if (-not $families.ContainsKey($family)) {
            $families[$family] = New-Object System.Collections.ArrayList
        }

        [void]$families[$family].Add($file)
    }

    if ($families.Count -eq 0) {
        return $true
    }

    $fileToGroupIndex = @{}
    for ($index = 0; $index -lt $Groups.Count; $index++) {
        foreach ($file in @($Groups[$index].Files)) {
            $fileToGroupIndex[$file] = $index
        }
    }

    foreach ($family in $families.Keys) {
        $groupIndexes = @($families[$family] | ForEach-Object {
            if ($fileToGroupIndex.ContainsKey($_)) {
                $fileToGroupIndex[$_]
            }
        } | Sort-Object -Unique)

        if ($groupIndexes.Count -gt 1) {
            return $false
        }
    }

    return $true
}

function Invoke-AzureOpenAIText {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$SystemPrompt,
        [string]$UserPrompt,
        [string]$CompactUserPrompt,
        [object[]]$PromptVariants,
        [string]$OperationName = 'azure-openai'
    )

    $headers = @{
        'api-key' = $ApiKey
        'Content-Type' = 'application/json; charset=utf-8'
    }

    if ($null -eq $PromptVariants -or $PromptVariants.Count -eq 0) {
        $variants = New-Object System.Collections.ArrayList
        [void]$variants.Add((New-LlmPromptVariant -Name 'full' -UserPrompt $UserPrompt))
        if (-not [string]::IsNullOrWhiteSpace($CompactUserPrompt) -and $CompactUserPrompt.Trim() -ne $UserPrompt.Trim()) {
            [void]$variants.Add((New-LlmPromptVariant -Name 'compact' -UserPrompt $CompactUserPrompt))
        }

        $PromptVariants = @($variants)
    }

    $attempts = [Math]::Max(1, (Get-LlmRetryCount))
    $lastErrorMessage = ''
    $errors = New-Object System.Collections.ArrayList

    foreach ($variant in $PromptVariants) {
        if ($null -eq $variant -or [string]::IsNullOrWhiteSpace([string]$variant.UserPrompt)) {
            continue
        }

        $variantName = if ([string]::IsNullOrWhiteSpace([string]$variant.Name)) { 'default' } else { [string]$variant.Name }

        for ($attempt = 1; $attempt -le $attempts; $attempt++) {
            $request = Resolve-AzureOpenAIRequest -Endpoint $Endpoint -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $SystemPrompt -UserPrompt ([string]$variant.UserPrompt)
            $timeoutSeconds = Get-DynamicLlmTimeoutSeconds -SystemPrompt $SystemPrompt -UserPrompt ([string]$variant.UserPrompt) -VariantName $variantName -Attempt $attempt
            $startedAt = Get-Date
            Write-NoticeMarker "Consultando Azure OpenAI ($OperationName, perfil $variantName, intento $attempt/$attempts)..."

            try {
                $response = Invoke-JsonApiRequest -Uri $request.Uri -Headers $headers -Json $request.Body -TimeoutSeconds $timeoutSeconds
                $elapsedMs = [int]((Get-Date) - $startedAt).TotalMilliseconds
                Write-GitLlmLog -Event 'llm-call-success' -Data @{
                    attempt = $attempt
                    durationMs = $elapsedMs
                    operation = $OperationName
                    promptChars = ([string]$variant.UserPrompt).Length
                    timeoutSeconds = $timeoutSeconds
                    variant = $variantName
                }
                return [string](& $request.ResponseExtractor $response)
            } catch {
                $elapsedMs = [int]((Get-Date) - $startedAt).TotalMilliseconds
                $errorInfo = Get-HttpErrorDetails $_
                $statusCode = if ($null -ne $errorInfo.StatusCode) { [string]$errorInfo.StatusCode } else { 'sin-status' }
                $lastErrorMessage = "Azure OpenAI devolvio ${statusCode}: $($errorInfo.Detail)"
                [void]$errors.Add("$OperationName/$variantName#$attempt => $lastErrorMessage")
                Write-GitLlmLog -Event 'llm-call-failure' -Data @{
                    attempt = $attempt
                    detail = $errorInfo.Detail
                    durationMs = $elapsedMs
                    operation = $OperationName
                    promptChars = ([string]$variant.UserPrompt).Length
                    statusCode = $statusCode
                    timeoutSeconds = $timeoutSeconds
                    variant = $variantName
                }

                $isTransient = ($_.Exception.Message -match 'cancel|timed out|task|temporarily unavailable|timeout' -or $errorInfo.StatusCode -in 408,409,429,500,502,503,504)
                $isFatal = ($errorInfo.StatusCode -in 401,403,404)

                if ($isTransient -and $attempt -lt $attempts) {
                    Invoke-LlmBackoffDelay -Attempt $attempt
                    continue
                }

                if ($isFatal) {
                    throw $lastErrorMessage
                }

                break
            }
        }
    }

    if ($errors.Count -gt 0) {
        throw "Azure OpenAI no respondio correctamente tras varios perfiles/intentos. Ultimo error: $lastErrorMessage"
    }

    throw 'Azure OpenAI no devolvio respuesta utilizable.'
}

function Invoke-AzureOpenAICommitPlan {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$Status,
        [string]$DiffStat,
        [string]$NameStatus,
        [string]$Diff,
        [string[]]$StagedFiles,
        [string]$DatabaseSummary,
        [string]$ScriptBase,
        [string]$Branch
    )

    $system = @(
        'Eres un asistente experto en Git y refactorizacion de cambios.'
        'Debes decidir si conviene crear uno o varios commits por tema.'
        'Reglas:'
        '- Responde solo JSON valido, sin markdown ni explicaciones.'
        '- No dividas un mismo archivo en varios commits.'
        '- Todos los archivos deben quedar asignados exactamente una vez.'
        '- Usa Conventional Commits en espanol para cada mensaje.'
        '- Maximo 72 caracteres en la primera linea del mensaje.'
        '- Si hay archivos .db, incluyelos en algun commit y menciona que son bases SQLite/binarias versionadas.'
        '- Si se proporciona Resumen SQLite, incorpora sus tablas/conteos en el cuerpo del mensaje del commit de base de datos.'
        '- Para archivos bajo notas-telegram/data/notes, agrupa cada nota base con todos sus derivados (.explain, .dialectic, .research, .suggest y combinaciones) en un solo commit por nota.'
        '- No mezcles derivados de una nota con otra nota distinta; los indices diarios/globales pueden ir aparte.'
        '- Si los cambios estan fuertemente acoplados, devuelve un solo grupo.'
        '- Esquema exacto: {"groups":[{"message":"...","files":["ruta1","ruta2"],"reason":"..."}]}'
    ) -join "`n"

    $user = @(
        'Contexto:'
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        ''
        'Archivos staged:'
        ($StagedFiles -join "`n")
        ''
        'Git status:'
        $Status
        ''
        'Diff stat:'
        $DiffStat
        ''
        'Name status:'
        $NameStatus
        ''
        'Resumen SQLite:'
        $DatabaseSummary
        ''
        'Diff resumido:'
        $Diff
    ) -join "`n"

    $compactUser = @(
        'Contexto:'
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        ''
        'Archivos staged:'
        ($StagedFiles -join "`n")
        ''
        'Diff stat:'
        $DiffStat
        ''
        'Name status:'
        $NameStatus
        ''
        'Resumen SQLite:'
        $DatabaseSummary
    ) -join "`n"

    $minimalUser = @(
        'Contexto:'
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        ''
        'Archivos staged:'
        ($StagedFiles -join "`n")
        ''
        'Resumen SQLite:'
        $DatabaseSummary
    ) -join "`n"

    $rawPlan = Invoke-AzureOpenAIText -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $system -UserPrompt $user -CompactUserPrompt $compactUser -PromptVariants @(
        (New-LlmPromptVariant -Name 'full' -UserPrompt $user),
        (New-LlmPromptVariant -Name 'compact' -UserPrompt $compactUser),
        (New-LlmPromptVariant -Name 'minimal' -UserPrompt $minimalUser)
    ) -OperationName 'commit-plan-generation'

    $candidateTexts = New-Object System.Collections.ArrayList
    [void]$candidateTexts.Add($rawPlan)

    try {
        $validatedPlan = Invoke-AzureOpenAICommitPlanValidation -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -RawPlan $rawPlan -StagedFiles $StagedFiles -DatabaseSummary $DatabaseSummary -ScriptBase $ScriptBase -Branch $Branch
        if (-not [string]::IsNullOrWhiteSpace($validatedPlan)) {
            [void]$candidateTexts.Insert(0, $validatedPlan)
        }
    } catch {
        Write-NoticeMarker "No se pudo validar el plan con una llamada adicional al LLM. Se intentará parsear el plan bruto. Detalle: $($_.Exception.Message)"
    }

    $parsed = $null
    $repairError = $null
    foreach ($candidateText in $candidateTexts) {
        try {
            $parsed = ConvertFrom-JsonLenient -Text $candidateText
            break
        } catch {
            $repairError = $_
        }
    }

    if ($null -eq $parsed) {
        $repairAttempts = [Math]::Max(1, (Get-LlmRepairAttempts))
        for ($repairAttempt = 1; $repairAttempt -le $repairAttempts; $repairAttempt++) {
            $repairReason = if ($null -ne $repairError) { $repairError.Exception.Message } else { 'JSON invalido o incompleto.' }
            $repairedPlan = Invoke-AzureOpenAICommitPlanRepair -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -BrokenPlan $rawPlan -StagedFiles $StagedFiles -DatabaseSummary $DatabaseSummary -Reason "$repairReason (intento $repairAttempt/$repairAttempts)"
            try {
                $parsed = ConvertFrom-JsonLenient -Text $repairedPlan
                break
            } catch {
                $repairError = $_
            }
        }
    }

    if ($null -eq $parsed) {
        throw "No se pudo obtener JSON valido para el plan de commits. $($repairError.Exception.Message)"
    }

    if ($null -eq $parsed.groups -or $parsed.groups.Count -eq 0) {
        throw 'El LLM no devolvio grupos de commit.'
    }

    $groups = New-Object System.Collections.ArrayList
    foreach ($group in $parsed.groups) {
        $files = @($group.files | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | ForEach-Object { [string]$_ })
        $message = Normalize-CommitMessage ([string]$group.message)
        if ([string]::IsNullOrWhiteSpace($message)) {
            throw 'El LLM devolvio un grupo sin mensaje.'
        }

        [void]$groups.Add([pscustomobject]@{
            Message = $message
            Files = $files
            Reason = [string]$group.reason
        })
    }

    if (-not (Test-CommitGroupsCoverAllFiles -Groups @($groups) -StagedFiles $StagedFiles)) {
        throw 'El plan de commits no cubre todos los archivos staged exactamente una vez.'
    }

    if (-not (Test-CommitGroupsAreReasonable -Groups @($groups))) {
        throw 'El plan de commits no pasó las validaciones de sanidad (cantidad de grupos o mensajes).'
    }

    if (-not (Test-CommitGroupsRespectSpecialFamilies -Groups @($groups) -StagedFiles $StagedFiles)) {
        throw 'El plan separa una nota de notas-telegram y sus derivados en varios commits; debe ser un solo commit por nota.'
    }

    return @($groups)
}

function Resolve-AzureOpenAIRequest {
    param(
        [string]$Endpoint,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$SystemPrompt,
        [string]$UserPrompt
    )

    $normalizedEndpoint = $Endpoint.Trim().TrimEnd('/')
    $uri = [Uri]$normalizedEndpoint
    $absolutePath = $uri.AbsolutePath.TrimEnd('/')

    if ($absolutePath -match '/openai/v1/responses$') {
        return @{
            Uri = $normalizedEndpoint
            Body = @{
                model = $Deployment
                instructions = $SystemPrompt
                input = $UserPrompt
                max_output_tokens = (Get-LlmMaxOutputTokens)
            } | ConvertTo-Json -Depth 8 -Compress
            ResponseExtractor = {
                param($Response)

                if ($null -ne $Response.output_text -and $Response.output_text -ne '') {
                    return [string]$Response.output_text
                }

                if ($null -ne $Response.output) {
                    foreach ($item in $Response.output) {
                        if ($null -eq $item.content) {
                            continue
                        }

                        foreach ($content in $item.content) {
                            if ($content.type -eq 'output_text' -and $content.text) {
                                return [string]$content.text
                            }

                            if ($content.text) {
                                return [string]$content.text
                            }
                        }
                    }
                }

                $diagnosticParts = @()
                if ($Response.status) { $diagnosticParts += "status=$($Response.status)" }
                if ($Response.error) { $diagnosticParts += "error=$($Response.error | ConvertTo-Json -Compress -Depth 5)" }
                if ($Response.incomplete_details) { $diagnosticParts += "incomplete=$($Response.incomplete_details | ConvertTo-Json -Compress -Depth 5)" }
                $diagnostic = if ($diagnosticParts.Count -gt 0) { $diagnosticParts -join '; ' } else { 'sin diagnostico adicional' }
                throw "La respuesta de Responses API no incluyo texto utilizable ($diagnostic)."
            }
        }
    }

    if ($absolutePath -match '/openai/v1/chat/completions$') {
        return @{
            Uri = $normalizedEndpoint
            Body = @{
                model = $Deployment
                messages = @(
                    @{ role = 'system'; content = $SystemPrompt },
                    @{ role = 'user'; content = $UserPrompt }
                )
                temperature = 0.2
                max_tokens = (Get-LlmMaxOutputTokens)
            } | ConvertTo-Json -Depth 8 -Compress
            ResponseExtractor = {
                param($Response)
                return [string]$Response.choices[0].message.content
            }
        }
    }

    return @{
        Uri = "$normalizedEndpoint/openai/deployments/$Deployment/chat/completions?api-version=$ApiVersion"
        Body = @{
            messages = @(
                @{ role = 'system'; content = $SystemPrompt },
                @{ role = 'user'; content = $UserPrompt }
            )
            temperature = 0.2
            max_tokens = (Get-LlmMaxOutputTokens)
        } | ConvertTo-Json -Depth 8 -Compress
        ResponseExtractor = {
            param($Response)
            return [string]$Response.choices[0].message.content
        }
    }
}

function Invoke-JsonApiRequest {
    param(
        [string]$Uri,
        [hashtable]$Headers,
        [string]$Json,
        [int]$TimeoutSeconds
    )

    Add-Type -AssemblyName System.Net.Http

    $client = [System.Net.Http.HttpClient]::new()
    try {
        $client.Timeout = [TimeSpan]::FromSeconds([Math]::Max(30, $TimeoutSeconds))
        foreach ($key in $Headers.Keys) {
            if ($key -eq 'Content-Type') {
                continue
            }

            [void]$client.DefaultRequestHeaders.Remove($key)
            [void]$client.DefaultRequestHeaders.Add($key, [string]$Headers[$key])
        }

        $content = [System.Net.Http.StringContent]::new($Json, [System.Text.Encoding]::UTF8, 'application/json')
        $response = $client.PostAsync($Uri, $content).GetAwaiter().GetResult()
        $responseBody = $response.Content.ReadAsStringAsync().GetAwaiter().GetResult()

        if (-not $response.IsSuccessStatusCode) {
            $exception = [System.Exception]::new("HTTP request failed")
            $exception.Data['StatusCode'] = [int]$response.StatusCode
            $exception.Data['Body'] = $responseBody
            throw $exception
        }

        if ([string]::IsNullOrWhiteSpace($responseBody)) {
            return $null
        }

        return $responseBody | ConvertFrom-Json -ErrorAction Stop
    } finally {
        $client.Dispose()
    }
}

function Get-HttpErrorDetails {
    param($ErrorRecord)

    $statusCode = $null
    $detail = $ErrorRecord.Exception.Message

    if ($null -ne $ErrorRecord.Exception.Data) {
        if ($ErrorRecord.Exception.Data.Contains('StatusCode')) {
            $statusCode = [int]$ErrorRecord.Exception.Data['StatusCode']
        }

        if ($ErrorRecord.Exception.Data.Contains('Body')) {
            $raw = [string]$ErrorRecord.Exception.Data['Body']
            if (-not [string]::IsNullOrWhiteSpace($raw)) {
                try {
                    $json = $raw | ConvertFrom-Json -ErrorAction Stop
                    if ($null -ne $json.error.message -and $json.error.message -ne '') {
                        $detail = [string]$json.error.message
                    } else {
                        $detail = $raw
                    }
                } catch {
                    $detail = $raw
                }
            }
        }
    }

    if ($null -ne $ErrorRecord.Exception.Response) {
        try {
            $statusCode = [int]$ErrorRecord.Exception.Response.StatusCode
        } catch {
            $statusCode = $null
        }

        try {
            $stream = $ErrorRecord.Exception.Response.GetResponseStream()
            if ($null -ne $stream) {
                $reader = New-Object System.IO.StreamReader($stream)
                $raw = $reader.ReadToEnd()
                if (-not [string]::IsNullOrWhiteSpace($raw)) {
                    try {
                        $json = $raw | ConvertFrom-Json -ErrorAction Stop
                        if ($null -ne $json.error.message -and $json.error.message -ne '') {
                            $detail = [string]$json.error.message
                        } else {
                            $detail = $raw
                        }
                    } catch {
                        $detail = $raw
                    }
                }
            }
        } catch {
        }
    }

    return @{
        StatusCode = $statusCode
        Detail = $detail
    }
}

function Invoke-AzureOpenAICommitPlanValidation {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$RawPlan,
        [string[]]$StagedFiles,
        [string]$DatabaseSummary,
        [string]$ScriptBase,
        [string]$Branch
    )

    $system = @(
        'Eres un validador estricto de planes de commit.'
        'Debes reparar, normalizar y devolver solo JSON valido.'
        'Reglas:'
        '- Usa exactamente el esquema {"groups":[{"message":"...","files":["..."],"reason":"..."}]}.'
        '- Todos los archivos staged deben aparecer exactamente una vez.'
        '- No inventes archivos.'
        '- Maximo ' + (Get-LlmMaxCommitGroups) + ' grupos.'
        '- Conventional Commits en espanol.'
        '- Primera linea maximo 72 caracteres.'
    ) -join "`n"

    $user = @(
        'Contexto:'
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        ''
        'Archivos staged obligatorios:'
        ($StagedFiles -join "`n")
        ''
        'Resumen SQLite:'
        $DatabaseSummary
        ''
        'Plan bruto a validar/reparar:'
        $RawPlan
    ) -join "`n"

    $compactUser = @(
        'Archivos staged obligatorios:'
        ($StagedFiles -join "`n")
        ''
        'Plan bruto:'
        $RawPlan
    ) -join "`n"

    $minimalUser = @(
        'Repara y normaliza este JSON de plan de commits.'
        'Archivos obligatorios:'
        ($StagedFiles -join ', ')
        ''
        'Contenido:'
        (Limit-Text $RawPlan 60000)
    ) -join "`n"

    return Invoke-AzureOpenAIText -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $system -UserPrompt $user -CompactUserPrompt $compactUser -PromptVariants @(
        (New-LlmPromptVariant -Name 'validation-full' -UserPrompt $user),
        (New-LlmPromptVariant -Name 'validation-compact' -UserPrompt $compactUser),
        (New-LlmPromptVariant -Name 'validation-minimal' -UserPrompt $minimalUser)
    ) -OperationName 'commit-plan-validation'
}

function Invoke-AzureOpenAICommitPlanRepair {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$BrokenPlan,
        [string[]]$StagedFiles,
        [string]$DatabaseSummary,
        [string]$Reason
    )

    $system = @(
        'Eres un reparador de planes de commit devueltos por LLM.'
        'Debes devolver solo JSON valido.'
        'Reglas:'
        '- Todos los archivos staged exactamente una vez.'
        '- No inventes archivos.'
        '- Maximo ' + (Get-LlmMaxCommitGroups) + ' grupos.'
        '- Primera linea de cada commit maximo 72 caracteres.'
        '- Si hay bases .db, reflejalas en un commit adecuado.'
    ) -join "`n"

    $user = @(
        "Motivo de reparacion: $Reason"
        ''
        'Archivos staged:'
        ($StagedFiles -join "`n")
        ''
        'Resumen SQLite:'
        $DatabaseSummary
        ''
        'Plan roto o inconsistente:'
        $BrokenPlan
    ) -join "`n"

    $compactUser = @(
        "Motivo: $Reason"
        'Archivos staged:'
        ($StagedFiles -join ', ')
        ''
        'Plan roto:'
        (Limit-Text $BrokenPlan 60000)
    ) -join "`n"

    return Invoke-AzureOpenAIText -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $system -UserPrompt $user -CompactUserPrompt $compactUser -PromptVariants @(
        (New-LlmPromptVariant -Name 'repair-full' -UserPrompt $user),
        (New-LlmPromptVariant -Name 'repair-compact' -UserPrompt $compactUser)
    ) -OperationName 'commit-plan-repair'
}

function Invoke-AzureOpenAICommitMessage {
    param(
        [string]$RepoTree,
        [string]$Status,
        [string]$DiffStat,
        [string]$NameStatus,
        [string]$Diff,
        [string]$ScriptBase,
        [string]$Branch,
        [string]$CandidateMessage = '',
        [string]$DatabaseSummary = ''
    )

    $endpoint = $env:AZURE_OPENAI_ENDPOINT
    $apiKey = $env:AZURE_OPENAI_API_KEY
    $deployment = if ($env:AZURE_OPENAI_CHAT_DEPLOYMENT) { $env:AZURE_OPENAI_CHAT_DEPLOYMENT } else { $env:AZURE_OPENAI_DEPLOYMENT_NAME }
    $apiVersion = if ($env:AZURE_OPENAI_API_VERSION) { $env:AZURE_OPENAI_API_VERSION } else { "2024-02-15-preview" }

    if ([string]::IsNullOrWhiteSpace($endpoint) -or [string]::IsNullOrWhiteSpace($apiKey) -or [string]::IsNullOrWhiteSpace($deployment)) {
        throw "Faltan variables AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY o AZURE_OPENAI_CHAT_DEPLOYMENT/AZURE_OPENAI_DEPLOYMENT_NAME en notas.env."
    }

    $endpoint = $endpoint.TrimEnd("/")

    $system = @(
        "Eres un asistente experto en Git. Genera mensajes de commit descriptivos, breves y seguros."
        "Reglas:"
        "- Responde únicamente con el mensaje de commit final."
        "- Usa Conventional Commits en español."
        "- Primera línea máximo 72 caracteres."
        "- Agrega cuerpo con viñetas si aporta claridad."
        "- No menciones secretos, tokens, claves, rutas locales sensibles ni valores de credenciales."
        "- No inventes cambios que no estén en el diff."
        "- Si recibes un mensaje candidato, mejóralo sin perder precisión."
    ) -join "`n"

    $user = @(
        "Contexto:"
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        "- Mensaje candidato: $CandidateMessage"
        ""
        "Árbol de archivos del repositorio:"
        $RepoTree
        ""
        "Git status:"
        $Status
        ""
        "Diff stat:"
        $DiffStat
        ""
        "Name status:"
        $NameStatus
        ""
        "Resumen SQLite:"
        $DatabaseSummary
        ""
        "Diff staged truncado:"
        $Diff
    ) -join "`n"

    $compactUser = @(
        "Contexto:"
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        "- Mensaje candidato: $CandidateMessage"
        ""
        "Git status:"
        $Status
        ""
        "Diff stat:"
        $DiffStat
        ""
        "Name status:"
        $NameStatus
        ""
        "Resumen SQLite:"
        $DatabaseSummary
        ""
        "Diff resumido:"
        (Limit-Text $Diff (Convert-LlmTokensToChars (Get-LlmMaxInputTokens)))
    ) -join "`n"

    $minimalUser = @(
        "Contexto:"
        "- Script compilado: $ScriptBase"
        "- Rama actual: $Branch"
        "- Mensaje candidato: $CandidateMessage"
        ""
        "Name status:"
        $NameStatus
        ""
        "Resumen SQLite:"
        $DatabaseSummary
    ) -join "`n"

    $message = Invoke-AzureOpenAIText -Endpoint $endpoint -ApiKey $apiKey -Deployment $deployment -ApiVersion $apiVersion -SystemPrompt $system -UserPrompt $user -CompactUserPrompt $compactUser -PromptVariants @(
        (New-LlmPromptVariant -Name 'message-full' -UserPrompt $user),
        (New-LlmPromptVariant -Name 'message-compact' -UserPrompt $compactUser),
        (New-LlmPromptVariant -Name 'message-minimal' -UserPrompt $minimalUser)
    ) -OperationName 'commit-message-refinement'
    return Normalize-CommitMessage $message
}

function New-GitLlmCheckpoint {
    param([string]$Branch)

    $head = (Invoke-Git rev-parse HEAD | Select-Object -First 1).Trim()
    $tag = "git-llm-backup-" + (Get-Date -Format 'yyyyMMdd-HHmmss')
    & git tag -f $tag $head 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo crear el punto de restauración $tag."
    }

    $checkpoint = [pscustomobject]@{
        Head = $head
        Tag = $tag
        Branch = $Branch
        Restored = $false
    }

    Write-GitLlmLog -Event 'checkpoint-created' -Data @{
        branch = $Branch
        head = $head
        tag = $tag
    }

    return $checkpoint
}

function Restore-GitLlmCheckpoint {
    param(
        [object]$Checkpoint,
        [string]$Reason
    )

    if ($null -eq $Checkpoint -or $Checkpoint.Restored) {
        return
    }

    $restoreOutput = & git reset --mixed $Checkpoint.Head 2>&1
    if ($LASTEXITCODE -eq 0) {
        $Checkpoint.Restored = $true
        Write-NoticeMarker "Se restauró el estado previo de Git+LLM tras el fallo. Tag de respaldo: $($Checkpoint.Tag)"
        Write-GitLlmLog -Event 'checkpoint-restored' -Data @{
            head = $Checkpoint.Head
            reason = $Reason
            tag = $Checkpoint.Tag
        }
        return
    }

    Write-NoticeMarker "No se pudo restaurar automáticamente el checkpoint $($Checkpoint.Tag). Revisa el repositorio manualmente."
    if ($restoreOutput) {
        Write-GitLlmLog -Event 'checkpoint-restore-failed' -Data @{
            output = ($restoreOutput -join "`n")
            reason = $Reason
            tag = $Checkpoint.Tag
        }
    }
}

function Remove-GitLlmCheckpoint {
    param([object]$Checkpoint)

    if ($null -eq $Checkpoint -or [string]::IsNullOrWhiteSpace([string]$Checkpoint.Tag)) {
        return
    }

    & git tag -d $Checkpoint.Tag 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-GitLlmLog -Event 'checkpoint-removed' -Data @{
            tag = $Checkpoint.Tag
        }
    }
}

function Test-GitRefExists {
    param([string]$RefName)

    & git show-ref --verify --quiet $RefName 2>$null
    return ($LASTEXITCODE -eq 0)
}

function Test-GitAncestor {
    param(
        [string]$Ancestor,
        [string]$Descendant
    )

    & git merge-base --is-ancestor $Ancestor $Descendant 2>$null
    return ($LASTEXITCODE -eq 0)
}

function Resolve-GitSyncTarget {
    param([string]$Branch)

    $upstream = Invoke-GitOptional rev-parse --abbrev-ref --symbolic-full-name '@{u}'
    if ($upstream) {
        $upstreamName = ($upstream | Select-Object -First 1).Trim()
        $remoteName = ($upstreamName -split '/')[0]
        return [pscustomobject]@{
            HasTracking = $true
            RemoteName = $remoteName
            Upstream = $upstreamName
        }
    }

    $originUrl = Invoke-GitOptional remote get-url origin
    if (-not $originUrl) {
        return $null
    }

    return [pscustomobject]@{
        HasTracking = $false
        RemoteName = 'origin'
        Upstream = "origin/$Branch"
    }
}

function Cleanup-GitPullState {
    & git rebase --abort 2>$null | Out-Null
    & git merge --abort 2>$null | Out-Null
    & git am --abort 2>$null | Out-Null
}

function Sync-LocalBranchWithRemote {
    param([string]$Branch)

    $syncTarget = Resolve-GitSyncTarget -Branch $Branch
    if ($null -eq $syncTarget) {
        Write-NoticeMarker 'No existe remoto configurado; se omite pull automático.'
        Write-GitLlmLog -Event 'remote-sync-skipped' -Data @{
            branch = $Branch
            reason = 'sin-remoto'
        }
        return
    }

    Write-NoticeMarker "Consultando cambios remotos en $($syncTarget.RemoteName)..."
    $fetchOutput = & git fetch --prune $syncTarget.RemoteName 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-GitLlmLog -Event 'remote-sync-fetch-failed' -Data @{
            branch = $Branch
            output = ($fetchOutput -join "`n")
            remote = $syncTarget.RemoteName
        }
        throw "git fetch falló al consultar cambios remotos en $($syncTarget.RemoteName)."
    }

    if (-not $syncTarget.HasTracking) {
        $remoteRefName = "refs/remotes/$($syncTarget.RemoteName)/$Branch"
        if (-not (Test-GitRefExists -RefName $remoteRefName)) {
            Write-NoticeMarker "No existe rama remota para $Branch; se omite pull automático."
            Write-GitLlmLog -Event 'remote-sync-skipped' -Data @{
                branch = $Branch
                reason = 'sin-rama-remota'
                remote = $syncTarget.RemoteName
            }
            return
        }
    }

    $localHead = (Invoke-Git rev-parse HEAD | Select-Object -First 1).Trim()
    $upstreamHead = (Invoke-Git rev-parse $syncTarget.Upstream | Select-Object -First 1).Trim()

    if ($localHead -eq $upstreamHead) {
        Write-NoticeMarker 'No hay cambios remotos pendientes; se omite pull automático.'
        Write-GitLlmLog -Event 'remote-sync-skipped' -Data @{
            branch = $Branch
            reason = 'sin-cambios-remotos'
            remote = $syncTarget.RemoteName
            upstream = $syncTarget.Upstream
        }
        return
    }

    $localBehind = Test-GitAncestor -Ancestor 'HEAD' -Descendant $syncTarget.Upstream
    $localAhead = Test-GitAncestor -Ancestor $syncTarget.Upstream -Descendant 'HEAD'

    if ($localAhead -and -not $localBehind) {
        Write-NoticeMarker 'La rama local ya contiene los cambios remotos; no se requiere pull.'
        Write-GitLlmLog -Event 'remote-sync-skipped' -Data @{
            branch = $Branch
            reason = 'local-ahead'
            remote = $syncTarget.RemoteName
            upstream = $syncTarget.Upstream
        }
        return
    }

    Write-NoticeMarker "Se detectaron cambios remotos en $($syncTarget.Upstream); se ejecutará pull automático con rebase."
    if ($syncTarget.HasTracking) {
        $pullOutput = & git pull --rebase --autostash --stat 2>&1
    } else {
        $pullOutput = & git pull --rebase --autostash $syncTarget.RemoteName $Branch 2>&1
    }

    if ($LASTEXITCODE -ne 0) {
        Cleanup-GitPullState
        Write-GitLlmLog -Event 'remote-sync-pull-failed' -Data @{
            branch = $Branch
            output = ($pullOutput -join "`n")
            remote = $syncTarget.RemoteName
            upstream = $syncTarget.Upstream
        }
        throw "git pull falló al sincronizar cambios remotos. Revisa conflictos o estado del remoto antes de ejecutar Git+LLM."
    }

    if (-not $syncTarget.HasTracking) {
        & git branch --set-upstream-to=$($syncTarget.Upstream) $Branch 2>$null | Out-Null
    }

    if ($pullOutput) {
        Write-Output ($pullOutput -join "`n")
    }

    Write-GitLlmLog -Event 'remote-sync-success' -Data @{
        branch = $Branch
        remote = $syncTarget.RemoteName
        upstream = $syncTarget.Upstream
    }
}

function New-CommitMessageFile {
    param([string]$Message)

    $tempFile = Join-Path $env:TEMP ("commit-message-" + [Guid]::NewGuid().ToString("N") + ".txt")
    Set-Content -LiteralPath $tempFile -Value $Message -Encoding UTF8
    return $tempFile
}

function Main {
    Write-ProgressMarker 5 "Preparando Git + LLM..."

    $repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
    $script:GitLlmRepoRoot = $repoRoot
    $script:GitLlmCheckpoint = $null
    $script:GitLlmPushStarted = $false
    Set-Location $repoRoot

    if ([string]::IsNullOrWhiteSpace($EnvPath)) {
        $EnvPath = Join-Path $repoRoot "notas.env"
    }

    Write-ProgressMarker 10 "Cargando credenciales desde notas.env..."
    Load-DotEnv -Path $EnvPath

    Write-ProgressMarker 15 "Verificando repositorio Git..."
    Invoke-Git rev-parse --is-inside-work-tree | Out-Null
    $branch = (Invoke-Git rev-parse --abbrev-ref HEAD | Select-Object -First 1).Trim()

    Write-ProgressMarker 20 "Sincronizando con cambios remotos si existen..."
    Sync-LocalBranchWithRemote -Branch $branch

    Write-ProgressMarker 25 "Preparando cambios seguros para commit..."
    & git add -A -- .
    if ($LASTEXITCODE -ne 0) {
        throw "No se pudieron preparar los cambios con git add."
    }
    Protect-SensitiveStagedFiles

    $stagedNames = @(Invoke-GitUtf8 diff --cached --name-only)
    if ($stagedNames.Count -eq 0) {
        Write-ResultMarker "cancelled" "Sin cambios seguros para commit."
        return
    }

    Write-ProgressMarker 35 "Analizando árbol, status y diff..."
    $llmInputCharBudget = Convert-LlmTokensToChars (Get-LlmMaxInputTokens)
    $status = Limit-Text ((Invoke-GitUtf8 status --short) -join "`n") $llmInputCharBudget
    $diffStat = Limit-Text ((Invoke-GitUtf8 diff --cached --stat) -join "`n") $llmInputCharBudget
    $nameStatusLines = @(Invoke-GitUtf8 diff --cached --name-status)
    $nameStatus = Limit-Text ($nameStatusLines -join "`n") $llmInputCharBudget
    $diff = Limit-Text ((& git diff --cached -- .) -join "`n") $llmInputCharBudget
    $databaseSummary = Limit-Text (Get-DatabaseChangeSummary -Files $stagedNames) $llmInputCharBudget
    Write-GitLlmLog -Event 'analysis-built' -Data @{
        diffChars = $diff.Length
        diffStatChars = $diffStat.Length
        stagedCount = $stagedNames.Count
        statusChars = $status.Length
    }

    Write-ProgressMarker 55 "Consultando LLM para agrupar commits por tema..."
    try {
        $commitGroups = Invoke-AzureOpenAICommitPlan -Endpoint $env:AZURE_OPENAI_ENDPOINT -ApiKey $env:AZURE_OPENAI_API_KEY -Deployment $(if ($env:AZURE_OPENAI_CHAT_DEPLOYMENT) { $env:AZURE_OPENAI_CHAT_DEPLOYMENT } else { $env:AZURE_OPENAI_DEPLOYMENT_NAME }) -ApiVersion $(if ($env:AZURE_OPENAI_API_VERSION) { $env:AZURE_OPENAI_API_VERSION } else { '2024-02-15-preview' }) -Status $status -DiffStat $diffStat -NameStatus $nameStatus -Diff $diff -StagedFiles $stagedNames -DatabaseSummary $databaseSummary -ScriptBase $ScriptBase -Branch $branch
    } catch {
        $commitGroups = Get-FallbackCommitGroups -StagedFiles $stagedNames
        Write-NoticeMarker "No se pudo agrupar con el LLM; se uso agrupacion local. Detalle: $($_.Exception.Message)"
    }

    if ($commitGroups.Count -eq 0) {
        Write-ResultMarker 'cancelled' 'No se pudo construir ningun grupo de commit.'
        return
    }

    Write-ProgressMarker 68 "Preparando $($commitGroups.Count) commit(s)..."
    & git reset -q
    if ($LASTEXITCODE -ne 0) {
        throw 'No se pudieron deshacer los staged temporales antes de crear commits por tema.'
    }

    $script:GitLlmCheckpoint = New-GitLlmCheckpoint -Branch $branch

    $createdCommitLines = New-Object System.Collections.ArrayList
    $groupIndex = 0
    foreach ($group in $commitGroups) {
        $groupIndex += 1
        $progress = [Math]::Min(90, 70 + [int](20 * ($groupIndex / [Math]::Max($commitGroups.Count, 1))))
        Write-ProgressMarker $progress "Creando commit $groupIndex de $($commitGroups.Count)..."

        $groupFiles = @($group.Files)
        if ($groupFiles.Count -eq 0) {
            continue
        }

        & git add -A -- @groupFiles
        if ($LASTEXITCODE -ne 0) {
            throw "No se pudieron preparar los archivos del grupo $groupIndex para commit."
        }

        $currentlyStaged = @(Invoke-GitUtf8 diff --cached --name-only)
        if ($currentlyStaged.Count -eq 0) {
            Write-NoticeMarker "El grupo $groupIndex no produjo archivos staged y se omitio."
            continue
        }

        try {
            $groupStatus = Limit-Text ((Invoke-GitUtf8 diff --cached --name-status -- @groupFiles) -join "`n") $llmInputCharBudget
            $groupDiffStat = Limit-Text ((Invoke-GitUtf8 diff --cached --stat -- @groupFiles) -join "`n") $llmInputCharBudget
            $groupDiff = Limit-Text ((& git diff --cached -- @groupFiles) -join "`n") $llmInputCharBudget
            $groupDatabaseSummary = Limit-Text (Get-DatabaseChangeSummary -Files $groupFiles) $llmInputCharBudget
            $groupMessage = Invoke-AzureOpenAICommitMessage -RepoTree ($groupFiles -join "`n") -Status $groupStatus -DiffStat $groupDiffStat -NameStatus $groupStatus -Diff $groupDiff -ScriptBase $ScriptBase -Branch $branch -CandidateMessage ([string]$group.Message) -DatabaseSummary $groupDatabaseSummary
            if (-not [string]::IsNullOrWhiteSpace($groupMessage)) {
                $group.Message = $groupMessage
            }
        } catch {
            Write-NoticeMarker "No se pudo refinar con el LLM el mensaje del grupo $groupIndex. Se usará el mensaje disponible. Detalle: $($_.Exception.Message)"
        }

        $commitFile = New-CommitMessageFile -Message $group.Message
        & git commit -F $commitFile
        if ($LASTEXITCODE -ne 0) {
            throw "git commit fallo al crear el grupo $groupIndex."
        }

        [void]$createdCommitLines.Add((Get-FirstCommitLine -Message $group.Message))
    }

    if ($createdCommitLines.Count -eq 0) {
        Remove-GitLlmCheckpoint -Checkpoint $script:GitLlmCheckpoint
        Write-ResultMarker 'cancelled' 'No se crearon commits despues de agrupar los cambios.'
        return
    }

    if ($NoPush) {
        Remove-GitLlmCheckpoint -Checkpoint $script:GitLlmCheckpoint
        $summary = "$($createdCommitLines.Count) commit(s) creados; push omitido.`n- " + (($createdCommitLines | ForEach-Object { $_ }) -join "`n- ")
        Write-ResultMarker 'success' $summary
        return
    }

    Write-ProgressMarker 92 "Ejecutando git push automáticamente..."
    $upstream = Invoke-GitOptional rev-parse --abbrev-ref --symbolic-full-name '@{u}'
    $script:GitLlmPushStarted = $true

    Write-ProgressMarker 95 "Ejecutando git push..."
    if ($upstream) {
        $pushOutput = & git push --porcelain 2>&1
    } else {
        $pushOutput = & git push --porcelain -u origin $branch 2>&1
    }
    $pushExitCode = $LASTEXITCODE
    if ($pushOutput) {
        Write-Output ($pushOutput -join "`n")
    }

    if ($pushExitCode -ne 0) {
        throw "git push falló. Revisa conectividad, permisos o estado remoto."
    }

    Write-ProgressMarker 100 "Commit y push completados."
    Remove-GitLlmCheckpoint -Checkpoint $script:GitLlmCheckpoint
    $summary = "$($createdCommitLines.Count) commit(s) creados y push completado.`n- " + (($createdCommitLines | ForEach-Object { $_ }) -join "`n- ")
    Write-ResultMarker 'success' $summary
}

try {
    Main
    exit 0
} catch {
    $message = $_.Exception.Message
    if ($null -ne $script:GitLlmCheckpoint -and -not $script:GitLlmPushStarted) {
        Restore-GitLlmCheckpoint -Checkpoint $script:GitLlmCheckpoint -Reason $message
    }
    Write-Error $message
    Write-ResultMarker "error" $message
    exit 1
}
