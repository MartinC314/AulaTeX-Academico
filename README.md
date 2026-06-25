# AulaTeX-Academico

Entorno academico en LaTeX organizado por institucion, con una base comun de
plantillas Pizarror y puntos de entrada canonicos para reportes, actividades,
presentaciones y bibliografias.

## Flujo Principal

- Plantillas maestras y motor LaTeX: `base/`.
- Trabajos canonicos por institucion: `UnADM/`, `UCNL/`, `IIIEPE/`, `ITESCA/`.
- Material editorial y criterios de revision: `retroalimentacion-editorial/`.
- Automatizacion de compilacion y exportacion: `scripts/`.
- Residuales de compilacion: `.build/`.

Flujo editorial recomendado en AulaTeX:

1. Memoria editorial.
2. Investigación.
3. Extractor.
4. Generación y agente.
5. Compilación.

## Comandos Utiles

```powershell
.\scripts\latexmk-build.ps1 .\UnADM\reporte-unadm.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\reporte-temas-selectos-de-matematicas-I.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\ITESCA\ingenieria-en-sistemas-computacionales\primer-ingreso\reporte-primer-ingreso.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\base\Templates-Informe\main.tex
```

```powershell
.\scripts\aulatex.ps1
```

```powershell
.\scripts\aulatex.ps1 investigation --target .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde --query "historia del derecho en mexico unadm programa analitico"
```

El PDF final se copia en la misma carpeta del archivo `.tex`.

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
