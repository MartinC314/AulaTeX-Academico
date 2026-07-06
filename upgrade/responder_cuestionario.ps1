param(
    [string]$EnvPath = "",
    [string]$OutputPath = "",
    [string]$ClipboardText = ""
)

$ErrorActionPreference = "Stop"

function Write-ProgressMarker {
    param(
        [int]$Percent,
        [string]$Message
    )

    $safePercent = [Math]::Max(0, [Math]::Min(100, $Percent))
    Write-Output "::progress::$safePercent::$Message"
    [Console]::Out.Flush()
}

function Write-ResultMarker {
    param(
        [string]$Status,
        [string]$Message
    )

    Write-Output "::result::$Status::$Message"
    [Console]::Out.Flush()
}

function Write-NoticeMarker {
    param([string]$Message)

    Write-Output "::notice::$Message"
    [Console]::Out.Flush()
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
                [Environment]::SetEnvironmentVariable($name, $value, 'Process')
            }
        }
    }
}

function Get-LlmMaxOutputTokens {
    $value = [Environment]::GetEnvironmentVariable('GIT_LLM_MAX_OUTPUT_TOKENS', 'Process')
    $parsed = 0
    if ([int]::TryParse($value, [ref]$parsed) -and $parsed -gt 0) {
        return $parsed
    }
    return 1200
}

function Get-LlmTimeoutSeconds {
    $value = [Environment]::GetEnvironmentVariable('GIT_LLM_TIMEOUT_SECONDS', 'Process')
    $parsed = 0
    if ([int]::TryParse($value, [ref]$parsed) -and $parsed -gt 0) {
        return $parsed
    }
    return 180
}

function Get-LlmRetryCount {
    $value = [Environment]::GetEnvironmentVariable('GIT_LLM_RETRY_COUNT', 'Process')
    $parsed = 0
    if ([int]::TryParse($value, [ref]$parsed) -and $parsed -gt 0) {
        return $parsed
    }
    return 3
}

function Invoke-LlmBackoffDelay {
    param([int]$Attempt)

    $baseDelay = 2000
    $maxDelay = 15000
    $delay = [Math]::Min($maxDelay, [int]($baseDelay * [Math]::Pow(2, [Math]::Max(0, $Attempt - 1))))
    $jitter = Get-Random -Minimum 150 -Maximum 900
    $totalDelay = [Math]::Min($maxDelay, $delay + $jitter)
    Write-NoticeMarker "Esperando $totalDelay ms antes del siguiente intento..."
    [System.Threading.Thread]::Sleep($totalDelay)
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

                throw 'La respuesta de Responses API no incluyó texto utilizable.'
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
                temperature = 0.1
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
            temperature = 0.1
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
            $exception = [System.Exception]::new('HTTP request failed')
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

    return @{
        StatusCode = $statusCode
        Detail = $detail
    }
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

    throw 'No se pudo convertir la respuesta del LLM a JSON válido.'
}

function Invoke-AzureOpenAIText {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$SystemPrompt,
        [string]$UserPrompt
    )

    $headers = @{
        'api-key' = $ApiKey
        'Content-Type' = 'application/json; charset=utf-8'
    }

    $attempts = [Math]::Max(1, (Get-LlmRetryCount))
    $lastErrorMessage = ''

    for ($attempt = 1; $attempt -le $attempts; $attempt++) {
        $request = Resolve-AzureOpenAIRequest -Endpoint $Endpoint -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $SystemPrompt -UserPrompt $UserPrompt
        Write-NoticeMarker "Consultando Azure OpenAI (intento $attempt/$attempts)..."

        try {
            $response = Invoke-JsonApiRequest -Uri $request.Uri -Headers $headers -Json $request.Body -TimeoutSeconds (Get-LlmTimeoutSeconds)
            return [string](& $request.ResponseExtractor $response)
        } catch {
            $errorInfo = Get-HttpErrorDetails $_
            $statusCode = if ($null -ne $errorInfo.StatusCode) { [string]$errorInfo.StatusCode } else { 'sin-status' }
            $lastErrorMessage = "Azure OpenAI devolvió ${statusCode}: $($errorInfo.Detail)"
            $isTransient = ($errorInfo.StatusCode -in 408,409,429,500,502,503,504)
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

    if (-not [string]::IsNullOrWhiteSpace($lastErrorMessage)) {
        throw $lastErrorMessage
    }

    throw 'Azure OpenAI no devolvió respuesta utilizable.'
}

function New-QuestionnaireItem {
    param(
        [int]$Number,
        [string]$Question,
        [object[]]$Options
    )

    return [pscustomobject]@{
        Number = $Number
        Question = $Question.Trim()
        Options = @($Options)
    }
}

function Normalize-QuestionnaireText {
    param([string]$QuestionText)

    $text = $QuestionText -replace '\r\n?', "`n"
    $builder = New-Object System.Text.StringBuilder

    for ($i = 0; $i -lt $text.Length; $i++) {
        $char = [string]$text[$i]
        $previousChar = if ($i -gt 0) { [string]$text[$i - 1] } else { '' }
        $shouldInsertLineBreak = $false

        if ($char -eq '¿' -and $i -gt 0 -and $previousChar -ne "`n") {
            $shouldInsertLineBreak = $true
        }

        if (($char -eq '◯' -or $char -eq '○' -or $char -eq '●' -or $char -eq '•') -and $i -gt 0 -and $previousChar -ne "`n") {
            $shouldInsertLineBreak = $true
        }

        if ($shouldInsertLineBreak -and $builder.Length -gt 0 -and [string]$builder[$builder.Length - 1] -ne "`n") {
            [void]$builder.Append("`n")
        }

        [void]$builder.Append($char)
    }

    $normalized = $builder.ToString()
    $normalized = [regex]::Replace($normalized, '(?<=[\?])\s+(?=(?:[A-Za-z0-9]+[\.)]\s+|[◯○●•]\s*[A-Za-z0-9]+[\.)]\s+))', "`n")
    return $normalized
}

function Get-QuestionnaireItems {
    param([string]$QuestionText)

    $normalizedText = Normalize-QuestionnaireText -QuestionText $QuestionText
    $questionMatches = [regex]::Matches($normalizedText, '¿[^?]+\?', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if ($questionMatches.Count -gt 0) {
        $regexItems = New-Object System.Collections.ArrayList

        for ($matchIndex = 0; $matchIndex -lt $questionMatches.Count; $matchIndex++) {
            $questionMatch = $questionMatches[$matchIndex]
            $blockStart = $questionMatch.Index
            $blockEnd = if ($matchIndex + 1 -lt $questionMatches.Count) { $questionMatches[$matchIndex + 1].Index } else { $normalizedText.Length }
            $blockText = $normalizedText.Substring($blockStart, $blockEnd - $blockStart).Trim()
            $question = $questionMatch.Value.Trim()
            $optionsText = $blockText.Substring($question.Length).Trim()
            $options = New-Object System.Collections.ArrayList

            $optionMatches = [regex]::Matches($optionsText, '(?:[◯○●•]\s*)?([A-Za-z0-9]+)[\.)]\s+(.+?)(?=(?:[◯○●•]\s*[A-Za-z0-9]+[\.)]\s+)|$)', [System.Text.RegularExpressions.RegexOptions]::Singleline)
            foreach ($optionMatch in $optionMatches) {
                [void]$options.Add([pscustomobject]@{
                    Label = $optionMatch.Groups[1].Value.Trim().ToLower()
                    Text = (($optionMatch.Groups[2].Value -replace '\s+', ' ').Trim())
                })
            }

            [void]$regexItems.Add((New-QuestionnaireItem -Number ($regexItems.Count + 1) -Question ($question -replace '\s+', ' ').Trim() -Options $options))
        }

        if ($regexItems.Count -gt 0) {
            return ,$regexItems
        }
    }

    $items = New-Object System.Collections.ArrayList
    $currentQuestion = ''
    $currentOptions = New-Object System.Collections.ArrayList

    foreach ($rawLine in ($normalizedText -split '\r?\n')) {
        $line = (($rawLine -replace '\t', ' ') -replace '\s{2,}', ' ').Trim()
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }

        if ($line -match '^[◯○●•\-\*\s]*([A-Za-z0-9]+)[\.)]\s+(.+)$') {
            if ([string]::IsNullOrWhiteSpace($currentQuestion)) {
                $currentQuestion = 'Pregunta sin encabezado claro'
            }

            [void]$currentOptions.Add([pscustomobject]@{
                Label = $matches[1].ToLower()
                Text = $matches[2].Trim()
            })
            continue
        }

        $normalizedQuestionLine = ($line -replace '^(?:\d+[\.)]\s*)', '').Trim()
        $isQuestionStart = ($normalizedQuestionLine -match '^¿.+\?$' -or $normalizedQuestionLine.EndsWith('?'))

        if ($isQuestionStart -and -not [string]::IsNullOrWhiteSpace($currentQuestion) -and ($currentOptions.Count -gt 0 -or $currentQuestion.EndsWith('?'))) {
            [void]$items.Add((New-QuestionnaireItem -Number ($items.Count + 1) -Question $currentQuestion -Options $currentOptions))
            $currentQuestion = $normalizedQuestionLine
            $currentOptions = New-Object System.Collections.ArrayList
            continue
        }

        if ($isQuestionStart -and [string]::IsNullOrWhiteSpace($currentQuestion)) {
            $currentQuestion = $normalizedQuestionLine
            continue
        }

        if ($currentOptions.Count -gt 0) {
            $lastIndex = $currentOptions.Count - 1
            $currentOptions[$lastIndex].Text = ($currentOptions[$lastIndex].Text + ' ' + $line).Trim()
            continue
        }

        if ([string]::IsNullOrWhiteSpace($currentQuestion)) {
            $currentQuestion = $normalizedQuestionLine
        } else {
            $currentQuestion = ($currentQuestion + ' ' + $normalizedQuestionLine).Trim()
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($currentQuestion)) {
        [void]$items.Add((New-QuestionnaireItem -Number ($items.Count + 1) -Question $currentQuestion -Options $currentOptions))
    }

    if ($items.Count -eq 0) {
        [void]$items.Add((New-QuestionnaireItem -Number 1 -Question $QuestionText.Trim() -Options @()))
    }

    return ,$items
}

function Format-QuestionnaireForDisplay {
    param([object[]]$Items)

    $lines = New-Object System.Collections.ArrayList
    foreach ($item in $Items) {
        [void]$lines.Add("$($item.Number). $($item.Question)")
        foreach ($option in @($item.Options)) {
            [void]$lines.Add("   $($option.Label). $($option.Text)")
        }
        [void]$lines.Add('')
    }

    return (($lines -join "`r`n").Trim())
}

function Format-QuestionnaireForLlm {
    param([object[]]$Items)

    $lines = New-Object System.Collections.ArrayList
    foreach ($item in $Items) {
        [void]$lines.Add("Pregunta $($item.Number): $($item.Question)")
        foreach ($option in @($item.Options)) {
            [void]$lines.Add("- $($option.Label)): $($option.Text)")
        }
        [void]$lines.Add('')
    }

    return (($lines -join "`n").Trim())
}

function Get-QuestionnairePrompt {
    param([string]$QuestionText)

    $system = @(
        'Eres un asistente que responde cuestionarios de opción múltiple.'
        'Debes detectar y responder una o varias preguntas numeradas a partir de texto crudo.'
        'Reglas:'
        '- Responde únicamente con JSON válido, sin markdown ni explicaciones adicionales.'
        '- Esquema exacto: {"items":[{"number":1,"question":"...","options":[{"label":"a","text":"..."}],"selected_option":"a","selected_text":"...","confidence":"alta","justification":"..."}]}'
        '- Debes devolver un item por cada pregunta detectada, en el mismo orden en que aparece.'
        '- question debe contener el texto limpio de la pregunta.'
        '- options debe contener todas las opciones detectadas en orden, con label y text.'
        '- selected_option debe contener solo la letra o etiqueta de la opción elegida; si no es claro, usa cadena vacía.'
        '- selected_text debe repetir brevemente el texto de la opción elegida; si no es claro, usa cadena vacía.'
        '- confidence debe ser alta, media o baja.'
        '- justification debe ser breve, máximo una oración.'
        '- No inventes fuentes externas.'
    ) -join "`n"

    $user = @(
        'Texto completo del cuestionario tomado del portapapeles:'
        $QuestionText
    ) -join "`n"

    return @{
        System = $system
        User = $user
    }
}

function Invoke-AzureOpenAIQuestionnaireAnswers {
    param(
        [string]$Endpoint,
        [string]$ApiKey,
        [string]$Deployment,
        [string]$ApiVersion,
        [string]$QuestionText
    )

    $prompt = Get-QuestionnairePrompt -QuestionText $QuestionText
    $rawAnswer = Invoke-AzureOpenAIText -Endpoint $Endpoint -ApiKey $ApiKey -Deployment $Deployment -ApiVersion $ApiVersion -SystemPrompt $prompt.System -UserPrompt $prompt.User
    $parsed = ConvertFrom-JsonLenient -Text $rawAnswer

    if ($null -eq $parsed.items -or $parsed.items.Count -eq 0) {
        throw 'El LLM no devolvió un cuestionario estructurado.'
    }

    $normalizedItems = New-Object System.Collections.ArrayList
    foreach ($item in @($parsed.items)) {
        $options = New-Object System.Collections.ArrayList
        foreach ($option in @($item.options)) {
            [void]$options.Add([pscustomobject]@{
                Label = ([string]$option.label).Trim().ToLower()
                Text = ([string]$option.text).Trim()
            })
        }

        [void]$normalizedItems.Add([pscustomobject]@{
            Number = [int]$item.number
            Question = ([string]$item.question).Trim()
            Options = @($options)
            SelectedOption = ([string]$item.selected_option).Trim()
            SelectedText = ([string]$item.selected_text).Trim()
            Confidence = ([string]$item.confidence).Trim().ToLower()
            Justification = ([string]$item.justification).Trim()
        })
    }

    if ($normalizedItems.Count -eq 0) {
        throw 'El LLM no devolvió reactivos utilizables.'
    }

    return @($normalizedItems | Sort-Object Number)
}

function Format-QuestionnaireAnswersForDisplay {
    param([object[]]$Answers)

    $lines = New-Object System.Collections.ArrayList
    foreach ($answer in $Answers) {
        $selectedOption = if ([string]::IsNullOrWhiteSpace($answer.SelectedOption)) { 'sin opción clara' } else { $answer.SelectedOption }
        $selectedText = if ([string]::IsNullOrWhiteSpace($answer.SelectedText)) { '' } else { '. ' + $answer.SelectedText }
        $confidence = if ([string]::IsNullOrWhiteSpace($answer.Confidence)) { 'media' } else { $answer.Confidence }
        $justification = if ([string]::IsNullOrWhiteSpace($answer.Justification)) { 'Sin justificación breve.' } else { $answer.Justification }

        [void]$lines.Add("$($answer.Number). Respuesta: $selectedOption$selectedText")
        [void]$lines.Add("   Confianza: $confidence")
        [void]$lines.Add("   Justificación: $justification")
        [void]$lines.Add('')
    }

    return (($lines -join "`r`n").Trim())
}

function Build-QuestionnaireOutputPayload {
    param(
        [string]$QuestionsText,
        [string]$AnswersText
    )

    return @(
        '::questions-begin::'
        $QuestionsText.Trim()
        '::questions-end::'
        '::answers-begin::'
        $AnswersText.Trim()
        '::answers-end::'
    ) -join "`r`n"
}

function Get-ClipboardQuestionText {
    param([string]$ClipboardOverride)

    if (-not [string]::IsNullOrWhiteSpace($ClipboardOverride)) {
        return $ClipboardOverride.Trim()
    }

    $clipboard = Get-Clipboard -Raw
    if ($null -eq $clipboard) {
        return ''
    }

    return ([string]$clipboard).Trim()
}

function Save-AnswerArtifacts {
    param(
        [string]$ClipboardAnswer,
        [string]$Payload,
        [string]$OutputPath
    )

    Set-Clipboard -Value $ClipboardAnswer

    if (-not [string]::IsNullOrWhiteSpace($OutputPath)) {
        $parent = Split-Path -Parent $OutputPath
        if (-not [string]::IsNullOrWhiteSpace($parent) -and -not (Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Path $parent -Force | Out-Null
        }

        Set-Content -LiteralPath $OutputPath -Value $Payload -Encoding UTF8
    }
}

try {
    Write-ProgressMarker -Percent 5 -Message 'Leyendo portapapeles...'
    $questionText = Get-ClipboardQuestionText -ClipboardOverride $ClipboardText
    if ([string]::IsNullOrWhiteSpace($questionText)) {
        throw 'El portapapeles está vacío. Copia primero la pregunta con sus opciones.'
    }

    if ($questionText.Length -lt 12) {
        throw 'El texto del portapapeles es demasiado corto para inferir un cuestionario.'
    }

    Write-ProgressMarker -Percent 12 -Message 'Analizando cuestionario...'

    Write-ProgressMarker -Percent 20 -Message 'Cargando credenciales del LLM...'
    if ([string]::IsNullOrWhiteSpace($EnvPath)) {
        $EnvPath = Join-Path $PSScriptRoot '..\notas.env'
    }
    Load-DotEnv -Path $EnvPath

    $endpoint = $env:AZURE_OPENAI_ENDPOINT
    $apiKey = $env:AZURE_OPENAI_API_KEY
    $deployment = if ($env:AZURE_OPENAI_CHAT_DEPLOYMENT) { $env:AZURE_OPENAI_CHAT_DEPLOYMENT } else { $env:AZURE_OPENAI_DEPLOYMENT_NAME }
    $apiVersion = if ($env:AZURE_OPENAI_API_VERSION) { $env:AZURE_OPENAI_API_VERSION } else { '2024-02-15-preview' }

    if ([string]::IsNullOrWhiteSpace($endpoint) -or [string]::IsNullOrWhiteSpace($apiKey) -or [string]::IsNullOrWhiteSpace($deployment)) {
        throw 'Faltan variables AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY o AZURE_OPENAI_CHAT_DEPLOYMENT/AZURE_OPENAI_DEPLOYMENT_NAME en notas.env.'
    }

    Write-ProgressMarker -Percent 35 -Message 'Preparando prompt del cuestionario...'

    Write-ProgressMarker -Percent 55 -Message 'Consultando el LLM...'
    $resolvedItems = Invoke-AzureOpenAIQuestionnaireAnswers -Endpoint $endpoint -ApiKey $apiKey -Deployment $deployment -ApiVersion $apiVersion -QuestionText $questionText
    $formattedQuestions = Format-QuestionnaireForDisplay -Items $resolvedItems
    $formattedAnswers = Format-QuestionnaireAnswersForDisplay -Answers $resolvedItems
    Write-NoticeMarker "Preguntas resueltas: $($resolvedItems.Count)"
    if ([string]::IsNullOrWhiteSpace($formattedAnswers)) {
        throw 'El LLM devolvió respuestas vacías.'
    }

    $payload = Build-QuestionnaireOutputPayload -QuestionsText $formattedQuestions -AnswersText $formattedAnswers

    Write-ProgressMarker -Percent 85 -Message 'Copiando respuesta al portapapeles...'
    Save-AnswerArtifacts -ClipboardAnswer $formattedAnswers -Payload $payload -OutputPath $OutputPath

    $preview = ($formattedAnswers -replace '\r?\n', ' ')
    if ($preview.Length -gt 180) {
        $preview = $preview.Substring(0, 180) + '...'
    }

    Write-NoticeMarker "Vista previa: $preview"
    Write-ProgressMarker -Percent 100 -Message 'Respuesta lista.'
    Write-ResultMarker -Status 'success' -Message 'Respuesta copiada al portapapeles.'
} catch {
    $message = $_.Exception.Message
    if ([string]::IsNullOrWhiteSpace($message)) {
        $message = 'Falló el flujo de Responder Cuestionario.'
    }

    Write-ResultMarker -Status 'error' -Message $message
    exit 1
}