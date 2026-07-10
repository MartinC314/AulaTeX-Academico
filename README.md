# AulaTeX-Academico

Entorno academico en LaTeX organizado por institucion, con una base comun de
plantillas Pizarror y puntos de entrada canonicos para reportes, actividades,
presentaciones y bibliografias.

## Flujo Principal

- Automatizacion de compilacion y exportacion: `scripts/`.- Entrada recomendada para trabajo editorial: `scripts/aulatex.ps1`.

## Arquitectura y compatibilidad de flujos agénticos AulaTeX

AulaTeX combina flujos especializados que pueden cooperar si intercambian productos duraderos del workspace. La regla general es no depender de logs temporales como fuente de verdad: los resultados reutilizables deben materializarse en TEX, BIB, referencias, `extractor-aulatex/` o `.memoria-aulatex/`.

```text
Intencion del usuario
  -> AulaTeX CLI/GUI
  -> Motor inteligente / Agente AulaTeX
  -> LangGraph cuando hay ruteo y ciclos
  -> LangChain adapter para llamadas LLM
  -> Herramientas locales: extractor, memoria, revision, bibliografia, compilacion
  -> Productos duraderos: TEX, BIB, referencias, extractor-aulatex, .memoria-aulatex
```

### Como elegir el flujo

| Necesidad | Comando recomendado | Internamente usa |
|---|---|---|
| Realizar o evaluar una actividad | `aulatex.ps1 agent --action realizar-actividad --activity N` | `AulaTeXAgent`, `EditorialContextProvider`, extractor opcional, LLMs |
| Bucle verificable de actividad | `aulatex.ps1 activity-monitor --activity N --workflow-backend langgraph` | `ActivityMonitor`, LangGraph, observer, revision, reparacion |
| Crear o reforzar nodos | `aulatex.ps1 generation ...` | `ConstructionBuilder`, memoria fundacional, contexto editorial |
| Reforzar memoria editorial | `aulatex.ps1 editorial-memory ...` | `EditorialMemoryBuilder`, `MemoryFusionEngine`, `.memoria-aulatex` |
| Campañas o lotes sobre el repo | `aulatex.ps1 intelligent-engine ...` | `IntelligentEngine`, contratos, ejecucion resumible |
| Extraer conceptos/referencias | `aulatex.ps1 extractor ...` | `ExtractorAdapter` |
| Comunicacion por bot | `bot-interfaz` con `/motor ...` | Planifica instruccion, muestra resumen, pide validacion y ejecuta `IntelligentEngine` solo tras confirmacion |

### Compatibilidad entre flujos

| Flujo | Productos duraderos que genera | Flujos que lo consumen |
|---|---|---|
| `extractor` | `extractor-aulatex/*.json`, conceptos, ideas, trazabilidad, planeacion | `agent`, `activity-monitor`, `editorial-memory`, `EditorialContextProvider` |
| `editorial-memory` | `.memoria-aulatex/*.json`, reglas, ADN editorial, conceptos reforzados | `agent`, `generation`, `intelligent-engine`, `activity-monitor` |
| `generation` | memoria fundacional, `plan.md`, `maqueta.tex`, estructura de nodo | `agent`, `editorial-memory`, `extractor`, `activity-monitor` |
| `agent` | TEX generado o revisado, reportes de ejecucion, compilacion opcional | `activity-monitor`, `editorial-memory`, compilacion, revision posterior |
| `activity-monitor` | observacion, evaluacion, parches, planes de reparacion | `agent`, `editorial-memory`, `intelligent-engine` |
| `intelligent-engine` | campañas, contratos, parches, reportes y ejecuciones por lote | todos, si materializa cambios en archivos o `.memoria-aulatex` |
| `bot-interfaz` | instrucciones validadas por el usuario hacia `IntelligentEngine` | `intelligent-engine`, auditoria humana previa a ejecucion |

Regla practica:

```text
Si un flujo produce algo util, debe materializarlo en TEX/BIB/referencias/extractor-aulatex/.memoria-aulatex.
Entonces los demas flujos pueden reutilizarlo.
```

Los logs en `.aulatex-temp/` son auditoria y depuracion; no son la memoria final.

### Mapa de integracion recomendado

```text
generation
  -> crea estructura base, memoria fundacional, plan y maqueta
  -> editorial-memory
      -> consolida .memoria-aulatex
      -> extractor
          -> produce conceptos, ideas, trazabilidad y planeacion
          -> agent
              -> realiza actividad o genera TEX con contexto editorial
              -> activity-monitor
                  -> observa, evalua, repara y reevalua
                  -> editorial-memory
                      -> absorbe lo aprendido en memoria distribuida
                      -> intelligent-engine
                          -> orquesta campañas o lotes sobre muchos nodos
                          -> bot-interfaz
                              -> recibe instrucciones, muestra plan y pide validacion humana
```

Este orden no es obligatorio, pero evita perdida de aprendizaje: primero se crean productos duraderos, luego se refuerza memoria, despues se ejecutan actividades y finalmente se reabsorbe lo aprendido.

### Pieza comun: `EditorialContextProvider`

La clase `scripts/aulatex/editorial_context.py` reune para cada nodo:

- memoria distribuida y heredada;
- artefactos del extractor (`conceptos`, `ideas`, `trazabilidad`, `planeacion`);
- bibliografia `.bib` local;
- referencias y planeaciones locales;
- señales TEX (`\\section`, `\\subsection`, `\\frametitle`);
- rutas de `.memoria-aulatex` disponibles.

El agente y la generacion descendente consumen este contexto antes de llamar a los LLMs. La prioridad operativa es:

```text
instrucciones locales > extractor > memoria distribuida > herencia > LLM
```

### Backends y responsabilidades

- `classic`: flujo Python directo con condicionales explicitos.
- `langgraph`: ruteo por grafo para ciclos de observacion, revision, reparacion y evaluacion.
- `langchain`: adaptador de llamada LLM; no sustituye al grafo ni al agente.
- `AulaTeXAgent`: ejecuta tareas concretas sobre un nodo.
- `IntelligentEngine`: orquesta campañas y lotes.
- `EditorialMemoryBuilder`: convierte productos duraderos en memoria distribuida.
- `bot-interfaz`: interfaz de comunicacion que pide confirmacion antes de ejecutar el motor inteligente.

Los artefactos temporales viven en `.aulatex-temp/`. La memoria persistente por nodo vive en carpetas `.memoria-aulatex/` distribuidas en el workspace.
```powershell
.\scripts\install-aulatex-deepagents.ps1
```

Para medir desempeño de forma explícita:

```powershell
.\scripts\aulatex.ps1 gui --diagnostics
```

```powershell
$env:AULATEX_ENABLE_DIAGNOSTIC_METRICS=1
.\scripts\aulatex.ps1 investigation --target .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde --query "historia del derecho en mexico unadm programa analitico"
Remove-Item Env:AULATEX_ENABLE_DIAGNOSTIC_METRICS
```

Cada carpeta de materia tiene un `COMPILACION.md` con el comando exacto, el
`.bib` esperado y el contrato de compilacion. Regla central: al script solo se
le pasa el `.tex`; `\input{template}` se resuelve con `TEXINPUTS` y
`\bibliography{...}` se resuelve con `BIBINPUTS`, ambos definidos en
`.latexmkrc`.

## Estructura Canonica

```text
AulaTeX-Academico/
|-- README.md
|-- base/
|   |-- cwl-docs/
|   |-- Export-Subtemmplate/
|   |-- Plantilla-Informe/
|   |-- latex/
|   |-- Professional-CV/
|   |-- Template-Articulo/
|   |-- Template-Auxiliares/
|   |-- Template-Controles/
|   |-- Templates-Informe/
|   |-- Template-Informe-master/
|   |-- Template-latex.github.io/
|   |-- Template-Poster/
|   |-- Template-Presentacion/
|   |-- Template-Reporte/
|   `-- Template-Tesis/
|-- UnADM/
|   |-- bibliografia-unadm.bib
|   |-- reporte-unadm.tex
|   |-- presentacion-unadm.tex
|   |-- referencias-unadm/
|   |-- redaccion-en-contextos-virtuales/
|   |-- etica-y-moral-juridica/
|   `-- filosofia-del-derecho/
|-- UCNL/
|   |-- bibliografia-ucnl.bib
|   |-- reporte-ucnl.tex
|   |-- presentacion-ucnl.tex
|   |-- referencias-ucnl/
|   |-- administracion-I/
|   |-- contabilidad-I/
|   |-- curso-inductivo/
|   |-- desarrollo-sustentable/
|   |-- ingles-I/
|   |-- matematicas-I/
|   `-- microeconomia/
|-- IIIEPE/
|   |-- temas-selectos-de-matematicas-I/
|   `-- fundamentos-para-la-enseñanza-y-el-aprendizaje-I/
|-- ITESCA/
|   |-- ingenieria-en-sistemas-computacionales/
|   |   |-- bibliografia-itesca-isc.bib
|   |   |-- reporte-itesca-isc.tex
|   |   |-- presentacion-itesca-isc.tex
|   |   |-- referencias-itesca-isc/
|   |   `-- primer-ingreso/
|   `-- maestria-en-gestion-administrativa/
|       |-- bibliografia-itesca-mga.bib
|       |-- reporte-itesca-mga.tex
|       |-- presentacion-itesca-mga.tex
|       |-- referencias-itesca-mga/
|       `-- primer-ingreso/
|-- retroalimentacion-editorial/
`-- scripts/
```

## Convenciones

- Reporte general: `reporte-<materia>.tex`.
- Actividad: `reporte-<materia>-Actividad-N.tex`.
- Presentacion: `presentacion-<materia>.tex`.
- Bibliografia local: `<materia>.bib`.
- Cuando una institucion tiene mas de un programa educativo, el nivel canonico se mueve a `institucion/carrera/materia`.

## Base Original

El proyecto conserva el nucleo tecnico de `Template-Informe` de Pablo Pizarro R.
en `base/Plantilla-Informe/`, junto con copias originales y adaptaciones
institucionales. Licencia base: MIT.

## Environment

Use `scripts/aulatex.env` o variables de entorno locales para configurar
proveedores. No publiques llaves reales en este archivo.

```env
# Opcion compatible OpenAI/Azure v1 preferida por este repo:
OPENAI_BASE_URL=https://example-resource.openai.azure.com/openai/v1/
OPENAI_API_KEY=<your-openai-or-azure-openai-key>
OPENAI_VIDEO_MODEL=sora-2
OPENAI_AUDIO_MODEL=gpt-4o-mini-tts

# Opcion experimental de GPT Realtime para una futura integracion interactiva.
# No la usa el pipeline actual de narracion offline y no debe sobrescribir
# OPENAI_BASE_URL / OPENAI_API_KEY.
AZURE_OPENAI_REALTIME_ENDPOINT=https://example-resource.services.ai.azure.com
AZURE_OPENAI_REALTIME_DEPLOYMENT_NAME=gpt-realtime
AZURE_OPENAI_REALTIME_API_KEY=<your-realtime-key>

# Opcion Azure clasica:
AZURE_ENDPOINT=https://example-resource.services.ai.azure.com/api/projects/example-project
AZURE_API_KEY=<your-azure-ai-key>
AZURE_OPENAI_DEPLOYMENT_NAME=sora-2
AZURE_OPENAI_AUDIO_MODEL=gpt-4o-mini-tts

AZURE_ENV_NAME=example-env
AZURE_LOCATION=swedencentral
AZURE_SUBSCRIPTION_ID=00000000-0000-0000-0000-000000000000
AZURE_EXISTING_AIPROJECT_ENDPOINT=https://example-resource.openai.azure.com/openai/v1/
AZURE_EXISTING_AIPROJECT_RESOURCE_ID=/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.CognitiveServices/accounts/example-resource/projects/example-project
AZURE_EXISTING_RESOURCE_ID=/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.CognitiveServices/accounts/example-resource
AZD_ALLOW_NON_EMPTY_FOLDER=true

# GPT-Pro
GPT_PRO_BASE_URL=https://example-resource.services.ai.azure.com/openai/v1/responses
GPT_PRO_API_KEY=<your-gpt-pro-key>
GPT_PRO_CHAT_DEPLOYMENT=gpt-5.4-pro
GPT_PRO_API_VERSION=2026-03-05

# Claude Foundry
ANTHROPIC_FOUNDRY_BASE_URL=https://example-resource.services.ai.azure.com/anthropic
ANTHROPIC_FOUNDRY_API_KEY=<your-anthropic-foundry-key>
ANTHROPIC_FOUNDRY_CHAT_DEPLOYMENT=claude-opus-4-8
ANTHROPIC_FOUNDRY_API_VERSION=2023-06-01

# Configuracion para traduccion de libros y generacion de audio
AZURE_TRANSLATOR_KEY=<your-translator-key>
AZURE_TRANSLATOR_REGION=eastus
AZURE_TRANSLATOR_ENDPOINT=https://example-translator.cognitiveservices.azure.com/

# Glosario opcional
# TB_BOOKS_TERMINOLOGY_FILE=terminology/glossary.json

# Robustez / rendimiento
TB_BOOKS_TRANSLATION_WORKERS=12
TB_BOOKS_TRANSLATOR_MAX_RETRIES=6
TB_BOOKS_TRANSLATOR_BACKOFF=1
TB_BOOKS_TRANSLATOR_MAX_BACKOFF=30
TB_BOOKS_TRANSLATOR_TIMEOUT=90

# Amazon Polly / audio M4A
TTS_PROVIDER=polly
AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_REGION=us-east-1
POLLY_VOICE_ID=Andres
POLLY_ENGINE=generative
POLLY_LANGUAGE_CODE=es-MX
POLLY_SAMPLE_RATE=24000
VOICE_RATE=114%
VOICE_VOLUME=+1.14dB
MAX_CHARS=2500
POLLY_WORKERS=12
POLLY_MAX_TPS=6
POLLY_MAX_RETRIES=6
POLLY_RETRY_BASE_DELAY=1
POLLY_RETRY_MAX_DELAY=30
OUTPUT_BITRATE=128k
FFMPEG_PARALLEL_JOBS=4
FFMPEG_GROUP_SIZE=512

# Azure Speech / audio M4A (usado si TTS_PROVIDER=azure)
AZURE_SPEECH_KEY=<your-speech-key>
AZURE_SPEECH_REGION=eastus
AZURE_SPEECH_LANGUAGE=es-MX
AZURE_SPEECH_VOICE=es-MX-JorgeNeural
AZURE_SPEECH_STYLE=chat
AZURE_SPEECH_STYLE_DEGREE=0.9
AZURE_SPEECH_RATE=1.10
AZURE_SPEECH_PITCH=-1
AZURE_SPEECH_VOLUME=110

# FFMPEG_PATH=D:\ruta\a\ffmpeg.exe

# Motor LLM para semantic-safe, validacion y pruebas
TB_BOOKS_LLM_REVIEW_ENGINE=Codex
TB_BOOKS_LLM_VALIDATION_ENABLED=1
TB_BOOKS_LLM_VALIDATION_TIMEOUT=45
TB_BOOKS_LLM_VALIDATION_MAX_TOKENS=220
TB_BOOKS_LLM_VALIDATION_TEMPERATURE=0

# Auto (model-router)
MODEL_ROUTER_BASE_URL=https://example-resource.services.ai.azure.com/openai/v1/chat/completions
MODEL_ROUTER_API_KEY=<your-model-router-key>
MODEL_ROUTER_CHAT_DEPLOYMENT=model-router
MODEL_ROUTER_API_VERSION=2025-11-18

# Codex
CODEX_BASE_URL=https://example-resource.services.ai.azure.com/openai/v1/responses
CODEX_API_KEY=<your-codex-key>
CODEX_CHAT_DEPLOYMENT=gpt-5.3-codex
CODEX_API_VERSION=2026-02-24
```

## Deployments validados para límites

```json
      {
        "id": "gpt-5.4-pro",
        "name": "gpt-5.4-pro",
        "url": "https://jonathandelacruz-6234-resource.services.ai.azure.com/openai/v1/responses",
        "maxInputTokens": 922000,
        "maxOutputTokens": 128000,
      },
      {
        "id": "model-router",
        "name": "model-router",
        "url": "https://jonathandelacruz-6234-resource.services.ai.azure.com/openai/v1/chat/completions",
        "maxInputTokens": 1015808,
        "maxOutputTokens": 32768
      },
      {
        "id": "Mistral-Large-3",
        "name": "Mistral-Large-3",
        "url": "https://jonathandelacruz-6234-resource.services.ai.azure.com/openai/v1/chat/completions",
        "maxInputTokens": 126976,
        "maxOutputTokens": 4096
      },
      {
        "id": "gpt-chat-latest",
        "name": "gpt-chat-latest",
        "url": "https://jonathandelacruz-6234-resource.services.ai.azure.com/openai/v1/responses",
        "maxInputTokens": 72000,
        "maxOutputTokens": 128000,
      },
      {
        "id": "DeepSeek-V4-Pro",
        "name": "DeepSeek-V4-Pro",
        "url": "https://jonathandelacruz-2506-resource.services.ai.azure.com/openai/v1/chat/completions",
        "maxInputTokens": 872000,
        "maxOutputTokens": 128000
      },
      {
        "id": "gpt-5.3-codex",
        "name": "gpt-5.3-codex",
        "url": "https://jonathandelacruz-2506-resource.services.ai.azure.com/openai/v1/responses",
        "maxInputTokens": 272000,
        "maxOutputTokens": 128000,
      }
```

## Límites de tokens y tiempo de espera

Los valores siguientes distinguen tres capas: límites teóricos declarados/configurados, límites probados por llamadas reales y límites operativos que usa AulaTeX para estabilizar la ejecución local. Las pruebas se ejecutaron el 2026-07-08 con `scripts/validar-limites-deployments.ps1`. Los artefactos principales están en `.aulatex-temp/deployment-limit-probe/runs/20260708-133615/`, con refinamientos en `20260708-163927`, `20260708-164136` y `20260708-164637`.

### Deployments validados

| Deployment | Endpoint | Entrada teórica/configurada | Salida teórica/configurada |
| --- | --- | ---: | ---: |
| `gpt-5.4-pro` | `responses` | `922,000` | `128,000` |
| `model-router` | `chat/completions` | `1,015,808` | `32,768` |
| `Mistral-Large-3` | `chat/completions` | `126,976` | `4,096` |
| `gpt-chat-latest` | `responses` | `72,000` | `128,000` |
| `DeepSeek-V4-Pro` | `chat/completions` | `872,000` | `128,000` |
| `gpt-5.3-codex` | `responses` | `272,000` | `128,000` |

### Resultados probados y límites operativos

| Deployment | Entrada probada | Latencia entrada | Salida probada solicitada | Salida observada | Latencia salida | Límite operativo establecido |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `gpt-5.4-pro` | `138,300` | `41,378 ms` | no validada por `rate_limit` | `0` | `0 ms` | entrada `138,300`; salida `8,192` conservadora. |
| `model-router` | `253,951` | `13,258 ms` | `29,491` | `1,161` | `58,515 ms` | entrada `253,951`; salida `29,491`. |
| `Mistral-Large-3` | no validada por alta demanda | `0 ms` | `4,096` | `607` | `49,334 ms` | entrada deshabilitada para lotes largos; salida `4,096`. |
| `gpt-chat-latest` | `72,000` | `6,006 ms` | `128,000` | `443` | `3,987 ms` | entrada `72,000`; salida `128,000`. |
| `DeepSeek-V4-Pro` | no validada por alta demanda | `0 ms` | `128,000` | `8,815` | `114,011 ms` | entrada deshabilitada para lotes largos; salida `128,000`, con latencia alta. |
| `gpt-5.3-codex` | `265,200` | `2,660 ms` | `128,000` | `341` | `3,430 ms` | entrada `265,200`; salida `128,000`. |

### Configuración operativa del workspace

- `scripts/aulatex.env` fija `AULATEX_OPERATIVE_INPUT_TOKENS_*` y `AULATEX_MAX_OUTPUT_TOKENS_*` con los valores anteriores.
- `scripts/aulatex/llm_bridge.py` aplica `AULATEX_MAX_OUTPUT_TOKENS_<PREFIJO>` por motor antes de invocar el proveedor.
- `scripts/prueeba-lote-ejecucion-1.ps1` usa defaults actualizados para presupuestos DNA y salida de los motores principales.
- `0` o “no validada” en entrada probada significa que no se alcanzó éxito estable: la API falló por `rate_limit`, alta demanda o tamaño máximo permitido bajo carga antes de demostrar el límite duro del modelo.
- La salida probada indica que la API aceptó el valor de `max_output_tokens`; no implica que el modelo haya producido esa cantidad completa de tokens.
