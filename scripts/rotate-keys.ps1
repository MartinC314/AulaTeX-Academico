<#
.SYNOPSIS
    Rota las claves del motor inteligente en Azure y AWS y las guarda cifradas
    en scripts/aulatex.env usando el PIN maestro $env:AHK_MASTER_PIN.

.DESCRIPTION
    Azure (az cli): regenera key1/key2 de una cuenta Microsoft.CognitiveServices
    y escribe la clave nueva cifrada en las variables indicadas por -AzureEnvName.

    AWS (aws cli): crea una nueva access key IAM, la escribe cifrada y opcionalmente
    desactiva o elimina la anterior.

    El cifrado lo realiza scripts/secrets_local.py (Fernet con clave derivada por
    PBKDF2-SHA256 del PIN maestro). Las claves en claro viajan solo por stdin:
    nunca aparecen en argv, en el historial de PowerShell ni en disco.

.EXAMPLE
    $env:AHK_MASTER_PIN = '6978'
    .\scripts\rotate-keys.ps1 -Provider Azure -AccountName jonathandelacruz-6234-resource -ResourceGroup rg-aulatex

.EXAMPLE
    $env:AHK_MASTER_PIN = '6978'
    .\scripts\rotate-keys.ps1 -Provider Aws -IamUserName aulatex-polly -DeactivateOld
#>

[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory)]
    [ValidateSet('Azure', 'Aws', 'All')]
    [string]$Provider,

    # --- Azure ---
    [string]$AccountName,
    [string]$ResourceGroup,
    [string]$SubscriptionId,
    [ValidateSet('key1', 'key2')]
    [string]$KeyName = 'key1',
    [string[]]$AzureEnvName = @('AZURE_API_KEY'),

    # --- AWS ---
    [string]$IamUserName,
    [string]$AwsProfile,
    [string]$AwsAccessKeyEnvName = 'AWS_ACCESS_KEY_ID',
    [string]$AwsSecretKeyEnvName = 'AWS_SECRET_ACCESS_KEY',
    [switch]$DeactivateOld,
    [switch]$DeleteOld,

    [string]$EnvFile = 'aulatex.env'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot    = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$secretsPy   = Join-Path $PSScriptRoot 'secrets_local.py'
$venvPython  = Join-Path $repoRoot '.venv\Scripts\python.exe'
$pythonCmd   = if (Test-Path $venvPython) { $venvPython } else { 'python' }

if ([string]::IsNullOrWhiteSpace($env:AHK_MASTER_PIN)) {
    throw "Define el PIN maestro antes de rotar: `$env:AHK_MASTER_PIN = '<pin>'"
}
if (-not (Test-Path $secretsPy)) {
    throw "No se encontro $secretsPy."
}

function Assert-Cli {
    param([Parameter(Mandatory)][string]$Name, [Parameter(Mandatory)][string]$Hint)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "No se encontro '$Name' en PATH. $Hint"
    }
}

function Invoke-CliJson {
    param(
        [Parameter(Mandatory)][string]$FilePath,
        [Parameter(Mandatory)][string[]]$Arguments
    )
    $stdout = & $FilePath @Arguments 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Fallo '$FilePath $($Arguments -join ' ')' (exit $LASTEXITCODE): $stdout"
    }
    $text = ($stdout | Out-String).Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return $text | ConvertFrom-Json
}

function Save-EncryptedSecret {
    <#
    .SYNOPSIS
        Cifra $Value y lo escribe en el .env. El valor viaja por stdin, no por argv.
    #>
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Value
    )
    $Value | & $pythonCmd $secretsPy set-value $EnvFile $Name
    if ($LASTEXITCODE -ne 0) { throw "No se pudo cifrar $Name en $EnvFile." }
}

function Format-Masked {
    param([Parameter(Mandatory)][AllowEmptyString()][string]$Value)
    if ([string]::IsNullOrEmpty($Value)) { return '(vacio)' }
    if ($Value.Length -le 4) { return '****' }
    return ('*' * 8) + $Value.Substring($Value.Length - 4)
}

function Invoke-AzureRotation {
    Assert-Cli -Name 'az' -Hint 'Instala Azure CLI: winget install Microsoft.AzureCLI'
    if ([string]::IsNullOrWhiteSpace($AccountName) -or [string]::IsNullOrWhiteSpace($ResourceGroup)) {
        throw 'Para -Provider Azure se requieren -AccountName y -ResourceGroup.'
    }

    $azArgs = @('cognitiveservices', 'account', 'keys', 'regenerate',
                '--key-name', $KeyName,
                '--name', $AccountName,
                '--resource-group', $ResourceGroup,
                '--output', 'json')
    if (-not [string]::IsNullOrWhiteSpace($SubscriptionId)) { $azArgs += @('--subscription', $SubscriptionId) }

    if (-not $PSCmdlet.ShouldProcess("$AccountName/$KeyName", 'Regenerar clave de Azure Cognitive Services')) {
        Write-Host "[WhatIf] az $($azArgs -join ' ')" -ForegroundColor Yellow
        return
    }

    Write-Host "Regenerando $KeyName de '$AccountName'..." -ForegroundColor Cyan
    $keys = Invoke-CliJson -FilePath 'az' -Arguments $azArgs
    $newKey = if ($KeyName -eq 'key1') { $keys.key1 } else { $keys.key2 }
    if ([string]::IsNullOrWhiteSpace($newKey)) { throw 'Azure no devolvio una clave nueva.' }

    foreach ($name in $AzureEnvName) {
        Save-EncryptedSecret -Name $name -Value $newKey
        Write-Host "  $name -> $(Format-Masked -Value $newKey) (cifrado)" -ForegroundColor Green
    }
}

function Invoke-AwsRotation {
    Assert-Cli -Name 'aws' -Hint 'Instala AWS CLI v2: winget install Amazon.AWSCLI'
    if ([string]::IsNullOrWhiteSpace($IamUserName)) {
        throw 'Para -Provider Aws se requiere -IamUserName.'
    }

    $profileArgs = @()
    if (-not [string]::IsNullOrWhiteSpace($AwsProfile)) { $profileArgs = @('--profile', $AwsProfile) }

    $existing = Invoke-CliJson -FilePath 'aws' -Arguments (@('iam', 'list-access-keys', '--user-name', $IamUserName, '--output', 'json') + $profileArgs)
    $oldKeys = @($existing.AccessKeyMetadata | Where-Object { $_.Status -eq 'Active' })

    # IAM admite un maximo de 2 access keys por usuario.
    if ($oldKeys.Count -ge 2) {
        throw "El usuario '$IamUserName' ya tiene 2 access keys activas. Elimina una antes de rotar."
    }

    if (-not $PSCmdlet.ShouldProcess($IamUserName, 'Crear nueva access key IAM y retirar la anterior')) {
        Write-Host "[WhatIf] aws iam create-access-key --user-name $IamUserName" -ForegroundColor Yellow
        return
    }

    Write-Host "Creando nueva access key para '$IamUserName'..." -ForegroundColor Cyan
    $created = Invoke-CliJson -FilePath 'aws' -Arguments (@('iam', 'create-access-key', '--user-name', $IamUserName, '--output', 'json') + $profileArgs)

    $newId     = $created.AccessKey.AccessKeyId
    $newSecret = $created.AccessKey.SecretAccessKey
    if ([string]::IsNullOrWhiteSpace($newId) -or [string]::IsNullOrWhiteSpace($newSecret)) {
        throw 'AWS no devolvio la nueva access key completa.'
    }

    Save-EncryptedSecret -Name $AwsAccessKeyEnvName -Value $newId
    Save-EncryptedSecret -Name $AwsSecretKeyEnvName -Value $newSecret
    Write-Host "  $AwsAccessKeyEnvName -> $(Format-Masked -Value $newId) (cifrado)" -ForegroundColor Green
    Write-Host "  $AwsSecretKeyEnvName -> $(Format-Masked -Value $newSecret) (cifrado)" -ForegroundColor Green

    foreach ($old in $oldKeys) {
        if ($old.AccessKeyId -eq $newId) { continue }
        if ($DeleteOld) {
            & aws iam delete-access-key --user-name $IamUserName --access-key-id $old.AccessKeyId @profileArgs
            if ($LASTEXITCODE -ne 0) { throw "No se pudo eliminar la access key $($old.AccessKeyId)." }
            Write-Host "  Eliminada clave anterior $($old.AccessKeyId)." -ForegroundColor Yellow
        }
        elseif ($DeactivateOld) {
            & aws iam update-access-key --user-name $IamUserName --access-key-id $old.AccessKeyId --status Inactive @profileArgs
            if ($LASTEXITCODE -ne 0) { throw "No se pudo desactivar la access key $($old.AccessKeyId)." }
            Write-Host "  Desactivada clave anterior $($old.AccessKeyId)." -ForegroundColor Yellow
        }
        else {
            Write-Host "  Clave anterior $($old.AccessKeyId) sigue ACTIVA. Usa -DeactivateOld o -DeleteOld tras validar." -ForegroundColor Yellow
        }
    }
}

switch ($Provider) {
    'Azure' { Invoke-AzureRotation }
    'Aws'   { Invoke-AwsRotation }
    'All'   { Invoke-AzureRotation; Invoke-AwsRotation }
}

Write-Host "`nRotacion completada. Verifica con: .\scripts\aulatex.ps1 llm-check" -ForegroundColor Cyan
