<#
.SYNOPSIS
    Monitor de avance visual para el Motor Inteligente de AulaTeX.

.DESCRIPTION
    Lanza `aulatex.ps1 intelligent-engine --execute --progress` y transmite en
    tiempo real su avance mediante los marcadores ::progress::, ::stage::,
    ::notice:: y ::result:: que el motor emite por stderr. El JSON de resultado
    (stdout) se conserva intacto y se muestra al final.

    Dos modos de presentación:
      * Consola enriquecida (por defecto): barra ANSI + líneas de estado en vivo.
      * Ventana gráfica (-Gui): barra de progreso + log en vivo (estilo Git+LLM),
        sin depender de una consola visible.

    Inspirado en el monitor Git+LLM de C:\ahk-Autohokey (scripts\git_llm_gui.ps1).

.PARAMETER Target
    Objetivo del motor (carpeta o .tex). Por defecto el repositorio completo.

.PARAMETER Activity
    Número de actividad a filtrar/ejecutar. 0 = todas.

.PARAMETER Actions
    Acciones a ejecutar por objetivo. Valores: 'realizar-actividad',
    'construir-memoria-editorial'. Repetible. Por defecto: ambas.

.PARAMETER MaxTargets
    Máximo de objetivos priorizados a procesar.

.PARAMETER Engines
    Motores LLM a usar (repetible). Por defecto GPT-5.6-Luna y GPT-5.6-Terra
    (los más confiables con prompts largos, ver memoria del repo).

.PARAMETER Plan
    Solo planificar (no ejecutar). Útil para inspeccionar la cola antes de correr.

.PARAMETER Gui
    Mostrar el monitor en una ventana gráfica en lugar de la consola.

.EXAMPLE
    .\scripts\motor-inteligente-monitor.ps1 -Target '.\UnADM\...\garantias-constitucionales-lde' -Activity 3

.EXAMPLE
    .\scripts\motor-inteligente-monitor.ps1 -Target '.\ITESCA' -MaxTargets 5 -Gui
#>
[CmdletBinding()]
param(
    [string]$Target = '.',
    [int]$Activity = 0,
    [ValidateSet('realizar-actividad', 'construir-memoria-editorial')]
    [string[]]$Actions = @('construir-memoria-editorial', 'realizar-actividad'),
    [int]$MaxTargets = 12,
    [string[]]$Engines = @('GPT-5.6-Luna', 'GPT-5.6-Terra'),
    [int]$MonitorMaxCycles = 100,
    [int]$OptimizeCycles = 3,
    [string]$Backend = 'langgraph',
    [string]$Output = '',
    [switch]$Plan,
    [switch]$Gui
)

$ErrorActionPreference = 'Stop'

# UTF-8 para leer correctamente los marcadores con acentos.
try {
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [Console]::OutputEncoding = $utf8
    $OutputEncoding = $utf8
} catch {
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
$venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'
$entry = Join-Path $scriptDir 'aulatex_agent.py'
$pythonExe = if (Test-Path $venvPython) { $venvPython } else { 'python' }

if (-not (Test-Path -LiteralPath $entry)) {
    throw "No se encontró el punto de entrada: $entry"
}

# ---------------------------------------------------- construir argumentos ----
$engineArgs = @()
foreach ($engine in $Engines) { $engineArgs += @('--engine', $engine) }

$actionArgs = @()
if (-not $Plan) {
    foreach ($action in $Actions) { $actionArgs += @('--action', $action) }
}

$cliArgs = @(
    $entry,
    'intelligent-engine',
    '--target', $Target,
    '--max-targets', [string]$MaxTargets,
    '--backend', $Backend,
    '--progress'
)
if ($Activity -gt 0) { $cliArgs += @('--activity', [string]$Activity) }
if ($Output) { $cliArgs += @('--output', $Output) }
if (-not $Plan) {
    $cliArgs += '--execute'
    $cliArgs += @('--monitor-max-cycles', [string]$MonitorMaxCycles)
    $cliArgs += @('--optimize-cycles', [string]$OptimizeCycles)
    $cliArgs += $actionArgs
}
$cliArgs += $engineArgs

# ------------------------------------------------------- parser de marcadores -
# Devuelve un hashtable con la interpretación de una línea de stderr.
function ConvertFrom-ProgressLine {
    param([string]$Line)

    if ([string]::IsNullOrEmpty($Line)) { return $null }

    if ($Line -match '^::progress::(\d+)::(.*)$') {
        return @{ Type = 'progress'; Percent = [int]$matches[1]; Message = $matches[2] }
    }
    if ($Line -match '^::stage::([^:]*)::(.*)$') {
        return @{ Type = 'stage'; Id = $matches[1]; Title = $matches[2] }
    }
    if ($Line -match '^::notice::(.*)$') {
        return @{ Type = 'notice'; Message = $matches[1] }
    }
    if ($Line -match '^::result::([^:]+)::(.*)$') {
        return @{ Type = 'result'; Status = $matches[1]; Message = $matches[2] }
    }
    return @{ Type = 'raw'; Message = $Line }
}

function Get-ResultIcon {
    param([string]$Status)
    switch ($Status) {
        'success' { return '[OK]' }
        'warning' { return '[!!]' }
        'skipped' { return '[--]' }
        'cancelled' { return '[--]' }
        'error' { return '[XX]' }
        default { return '[..]' }
    }
}

# Windows PowerShell 5.1 no expone ProcessStartInfo.ArgumentList: construimos
# la cadena de argumentos citando los que contienen espacios.
function ConvertTo-ArgumentString {
    param([string[]]$Arguments)
    return (@($Arguments | ForEach-Object {
        if ($_ -match '[\s"]') { '"' + ($_ -replace '"', '\"') + '"' } else { $_ }
    }) -join ' ')
}

# ============================================================ MODO CONSOLA ====
function Invoke-ConsoleMonitor {
    param([string]$PythonExe, [string[]]$CliArgs, [string]$RepoRoot)

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $PythonExe
    $psi.WorkingDirectory = $RepoRoot
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
    $psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8
    $psi.EnvironmentVariables['PYTHONUTF8'] = '1'
    $psi.Arguments = ConvertTo-ArgumentString -Arguments $CliArgs

    $proc = New-Object System.Diagnostics.Process
    $proc.StartInfo = $psi

    Write-Host ''
    Write-Host '  Motor Inteligente AulaTeX - monitor de avance' -ForegroundColor Cyan
    Write-Host '  ---------------------------------------------' -ForegroundColor DarkCyan

    [void]$proc.Start()

    # stdout (JSON) se lee de forma asincrona a un StringBuilder para no bloquear
    # la lectura linea-a-linea de stderr (marcadores de progreso).
    $stdoutTask = $proc.StandardOutput.ReadToEndAsync()

    $barWidth = 40
    $lastPercent = -1
    while (-not $proc.StandardError.EndOfStream) {
        $line = $proc.StandardError.ReadLine()
        $evt = ConvertFrom-ProgressLine -Line $line
        if ($null -eq $evt) { continue }

        switch ($evt.Type) {
            'progress' {
                $lastPercent = $evt.Percent
                $filled = [int]([math]::Round($barWidth * $evt.Percent / 100))
                $bar = ('#' * $filled) + ('.' * ($barWidth - $filled))
                $status = $evt.Message
                if ($status.Length -gt 68) { $status = $status.Substring(0, 65) + '...' }
                $pad = ' ' * [math]::Max(0, 70 - $status.Length)
                Write-Host ("`r  [{0}] {1,3}%  {2}{3}" -f $bar, $evt.Percent, $status, $pad) -NoNewline -ForegroundColor Green
            }
            'stage' {
                Write-Host ''
                Write-Host ("  >> {0}" -f $evt.Title) -ForegroundColor Yellow
            }
            'notice' {
                Write-Host ''
                Write-Host ("       - {0}" -f $evt.Message) -ForegroundColor Gray
            }
            'result' {
                $icon = Get-ResultIcon -Status $evt.Status
                $color = switch ($evt.Status) {
                    'success' { 'Green' }
                    'warning' { 'Yellow' }
                    'error' { 'Red' }
                    default { 'DarkGray' }
                }
                Write-Host ''
                Write-Host ("     {0} {1}" -f $icon, $evt.Message) -ForegroundColor $color
            }
            'raw' {
                if (-not [string]::IsNullOrWhiteSpace($evt.Message)) {
                    Write-Host ''
                    Write-Host ("       {0}" -f $evt.Message.TrimEnd()) -ForegroundColor DarkGray
                }
            }
        }
    }

    $proc.WaitForExit()

    Write-Host ''
    Write-Host ''
    if ($proc.ExitCode -eq 0) {
        Write-Host '  Completado correctamente.' -ForegroundColor Green
    } else {
        Write-Host ("  Finalizado con errores (código {0})." -f $proc.ExitCode) -ForegroundColor Red
    }

    $json = ($stdoutTask.GetAwaiter().GetResult()).Trim()
    if ($json) {
        Write-Host ''
        Write-Host '  === Resultado (JSON) ===' -ForegroundColor DarkCyan
        try {
            $obj = $json | ConvertFrom-Json
            Write-Host ("  ok={0}  executed={1}  execution_ok={2}" -f $obj.ok, $obj.executed, $obj.execution_ok) -ForegroundColor Cyan
            Write-Host ("  run_dir: {0}" -f $obj.run_dir) -ForegroundColor DarkGray
            Write-Host ("  report : {0}" -f $obj.report) -ForegroundColor DarkGray
        } catch {
            Write-Host $json -ForegroundColor DarkGray
        }
    }
    return $proc.ExitCode
}

# =============================================================== MODO GUI =====
function Invoke-GuiMonitor {
    param([string]$PythonExe, [string[]]$CliArgs, [string]$RepoRoot)

    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing

    $form = New-Object System.Windows.Forms.Form
    $form.Text = 'Motor Inteligente AulaTeX · Progreso'
    $form.StartPosition = 'CenterScreen'
    $form.Size = New-Object System.Drawing.Size(760, 500)
    $form.MinimumSize = New-Object System.Drawing.Size(620, 400)
    $form.FormBorderStyle = 'Sizable'
    $form.BackColor = [System.Drawing.Color]::FromArgb(30, 30, 30)
    $form.KeyPreview = $true

    $lblStatus = New-Object System.Windows.Forms.Label
    $lblStatus.Text = 'Preparando motor inteligente...'
    $lblStatus.AutoSize = $false
    $lblStatus.Dock = 'Top'
    $lblStatus.Height = 32
    $lblStatus.TextAlign = 'MiddleLeft'
    $lblStatus.Padding = New-Object System.Windows.Forms.Padding(12, 0, 12, 0)
    $lblStatus.ForeColor = [System.Drawing.Color]::Gainsboro
    $lblStatus.Font = New-Object System.Drawing.Font('Segoe UI', 10, [System.Drawing.FontStyle]::Bold)

    $progressBar = New-Object System.Windows.Forms.ProgressBar
    $progressBar.Dock = 'Top'
    $progressBar.Height = 22
    $progressBar.Minimum = 0
    $progressBar.Maximum = 100
    $progressBar.Value = 0
    $progressBar.Style = 'Continuous'

    $spacer = New-Object System.Windows.Forms.Panel
    $spacer.Dock = 'Top'
    $spacer.Height = 8
    $spacer.BackColor = $form.BackColor

    $txtLog = New-Object System.Windows.Forms.TextBox
    $txtLog.Multiline = $true
    $txtLog.ReadOnly = $true
    $txtLog.ScrollBars = 'Vertical'
    $txtLog.Dock = 'Fill'
    $txtLog.BackColor = [System.Drawing.Color]::FromArgb(20, 20, 20)
    $txtLog.ForeColor = [System.Drawing.Color]::Gainsboro
    $txtLog.Font = New-Object System.Drawing.Font('Consolas', 9)
    $txtLog.BorderStyle = 'None'

    $panelBottom = New-Object System.Windows.Forms.Panel
    $panelBottom.Dock = 'Bottom'
    $panelBottom.Height = 48
    $panelBottom.BackColor = $form.BackColor

    $btnClose = New-Object System.Windows.Forms.Button
    $btnClose.Text = 'Cerrar'
    $btnClose.Size = New-Object System.Drawing.Size(120, 30)
    $btnClose.Anchor = 'Right'
    $btnClose.Location = New-Object System.Drawing.Point(($panelBottom.Width - 132), 9)
    $btnClose.FlatStyle = 'Flat'
    $btnClose.ForeColor = [System.Drawing.Color]::White
    $btnClose.BackColor = [System.Drawing.Color]::FromArgb(60, 60, 60)
    $btnClose.Enabled = $false
    $btnClose.Add_Click({ $form.Close() })

    $panelBottom.Controls.Add($btnClose)
    $panelBottom.Add_Resize({
        $btnClose.Location = New-Object System.Drawing.Point(($panelBottom.Width - 132), 9)
    })

    $form.Controls.Add($txtLog)
    $form.Controls.Add($spacer)
    $form.Controls.Add($progressBar)
    $form.Controls.Add($lblStatus)
    $form.Controls.Add($panelBottom)

    # Estado compartido entre el worker (runspace) y el timer de UI.
    $sync = [hashtable]::Synchronized(@{
        Lines    = New-Object System.Collections.ArrayList
        Percent  = 0
        Status   = 'Preparando motor inteligente...'
        Done     = $false
        ExitCode = $null
        Stdout   = New-Object System.Text.StringBuilder
        Raw      = [System.Collections.Concurrent.ConcurrentQueue[string]]::new()
    })

    # La cadena de argumentos se compone fuera del runspace (el helper no viaja).
    $argString = ConvertTo-ArgumentString -Arguments $CliArgs

    # Worker: ejecuta python y encola stderr; stdout (JSON) se acumula aparte.
    $workerScript = {
        param($pythonExe, $argString, $repoRoot, $sync)

        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $pythonExe
        $psi.WorkingDirectory = $repoRoot
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
        $psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8
        $psi.EnvironmentVariables['PYTHONUTF8'] = '1'
        $psi.Arguments = $argString

        $proc = New-Object System.Diagnostics.Process
        $proc.StartInfo = $psi

        $stderrHandler = {
            if ($null -ne $EventArgs.Data) {
                [void]$Event.MessageData.Enqueue([string]$EventArgs.Data)
            }
        }
        $stderrEvent = Register-ObjectEvent -InputObject $proc -EventName ErrorDataReceived -Action $stderrHandler -MessageData $sync.Raw

        $stdoutHandler = {
            if ($null -ne $EventArgs.Data) {
                [void]$Event.MessageData.AppendLine([string]$EventArgs.Data)
            }
        }
        $stdoutEvent = Register-ObjectEvent -InputObject $proc -EventName OutputDataReceived -Action $stdoutHandler -MessageData $sync.Stdout

        [void]$proc.Start()
        $proc.BeginOutputReadLine()
        $proc.BeginErrorReadLine()
        $proc.WaitForExit()

        Start-Sleep -Milliseconds 200
        Unregister-Event -SourceIdentifier $stderrEvent.Name -ErrorAction SilentlyContinue
        Unregister-Event -SourceIdentifier $stdoutEvent.Name -ErrorAction SilentlyContinue

        $sync.ExitCode = $proc.ExitCode
        $sync.Done = $true
    }

    $runspace = [runspacefactory]::CreateRunspace()
    $runspace.ApartmentState = 'MTA'
    $runspace.ThreadOptions = 'ReuseThread'
    $runspace.Open()
    $ps = [powershell]::Create()
    $ps.Runspace = $runspace
    [void]$ps.AddScript($workerScript).AddArgument($PythonExe).AddArgument($argString).AddArgument($RepoRoot).AddArgument($sync)
    $asyncHandle = $ps.BeginInvoke()

    # Parser: traduce una línea de stderr a entradas de log / porcentaje.
    $parseLine = {
        param($rawLine)
        $line = [string]$rawLine
        if ([string]::IsNullOrEmpty($line)) { return }

        if ($line -match '^::progress::(\d+)::(.*)$') {
            $sync.Percent = [int]$matches[1]
            $sync.Status = $matches[2]
            return
        }
        if ($line -match '^::stage::([^:]*)::(.*)$') {
            [void]$sync.Lines.Add('')
            [void]$sync.Lines.Add(">> $($matches[2])")
            return
        }
        if ($line -match '^::notice::(.*)$') {
            [void]$sync.Lines.Add("     - $($matches[1])")
            return
        }
        if ($line -match '^::result::([^:]+)::(.*)$') {
            $status = $matches[1]
            $icon = switch ($status) {
                'success' { '[OK]' }
                'warning' { '[!!]' }
                'error' { '[XX]' }
                'skipped' { '[--]' }
                default { '[..]' }
            }
            [void]$sync.Lines.Add("   $icon [$status] $($matches[2])")
            return
        }
        [void]$sync.Lines.Add("  $($line.TrimEnd())")
    }

    $lastLineCount = 0
    $timer = New-Object System.Windows.Forms.Timer
    $timer.Interval = 150
    $timer.Add_Tick({
        $item = ''
        while ($sync.Raw.TryDequeue([ref]$item)) { & $parseLine $item }

        if ($progressBar.Value -ne $sync.Percent) {
            $progressBar.Value = [Math]::Max(0, [Math]::Min(100, [int]$sync.Percent))
        }
        if ($lblStatus.Text -ne $sync.Status) {
            $lblStatus.Text = [string]$sync.Status
        }
        if ($sync.Lines.Count -gt $lastLineCount) {
            $nuevas = @()
            for ($i = $lastLineCount; $i -lt $sync.Lines.Count; $i++) { $nuevas += [string]$sync.Lines[$i] }
            $lastLineCount = $sync.Lines.Count
            if ($nuevas.Count -gt 0) { $txtLog.AppendText(($nuevas -join "`r`n") + "`r`n") }
        }

        if ($sync.Done) {
            $timer.Stop()
            $item2 = ''
            while ($sync.Raw.TryDequeue([ref]$item2)) { & $parseLine $item2 }
            if ($sync.Lines.Count -gt $lastLineCount) {
                $nuevas2 = @()
                for ($i = $lastLineCount; $i -lt $sync.Lines.Count; $i++) { $nuevas2 += [string]$sync.Lines[$i] }
                $lastLineCount = $sync.Lines.Count
                $txtLog.AppendText(($nuevas2 -join "`r`n") + "`r`n")
            }

            $ok = ($sync.ExitCode -eq 0)
            $progressBar.Value = 100
            if ($ok) {
                $lblStatus.Text = 'Completado correctamente.'
                $lblStatus.ForeColor = [System.Drawing.Color]::LightGreen
            } else {
                $lblStatus.Text = "Finalizado con errores (código $($sync.ExitCode))."
                $lblStatus.ForeColor = [System.Drawing.Color]::Salmon
            }

            $json = $sync.Stdout.ToString().Trim()
            if ($json) {
                try {
                    $obj = $json | ConvertFrom-Json
                    $txtLog.AppendText("`r`n=== Resultado ===`r`n")
                    $txtLog.AppendText("ok=$($obj.ok)  executed=$($obj.executed)  execution_ok=$($obj.execution_ok)`r`n")
                    $txtLog.AppendText("run_dir: $($obj.run_dir)`r`n")
                    $txtLog.AppendText("report : $($obj.report)`r`n")
                } catch {
                    $txtLog.AppendText("`r`n$json`r`n")
                }
            }

            $btnClose.Enabled = $true
            $form.AcceptButton = $btnClose
            $form.TopMost = $true
            [void]$form.Activate(); $form.BringToFront(); $form.TopMost = $false
            $btnClose.Focus()

            try { $ps.EndInvoke($asyncHandle) } catch {}
            try { $ps.Dispose() } catch {}
            try { $runspace.Close(); $runspace.Dispose() } catch {}
        }
    })

    $form.Add_Shown({ $timer.Start() })
    $form.Add_FormClosing({
        if (-not $sync.Done) {
            # Permitir cerrar aunque siga corriendo; el proceso hijo terminará solo.
        }
    })
    [void][System.Windows.Forms.Application]::Run($form)
    if ($null -ne $sync.ExitCode) { return [int]$sync.ExitCode }
    return 0
}

# ==================================================================== MAIN ====
if ($Gui) {
    $code = Invoke-GuiMonitor -PythonExe $pythonExe -CliArgs $cliArgs -RepoRoot $repoRoot
} else {
    $code = Invoke-ConsoleMonitor -PythonExe $pythonExe -CliArgs $cliArgs -RepoRoot $repoRoot
}
exit $code
