---
id: "20260703131723"
title: "13:17 - Archivos generados y versionado"
key: "archivos_generados_y_versionado"
created_at: "2026-07-03T13:17:23.117834"
tags:
  - "data/"
  - "Versionado"
  - "Persistencia local"
  - "Archivos temporales"
  - "Notas generadas"
  - "Índices de notas"
  - "Audio TTS del bot"
  - "Acciones del bot"
  - "Monitoreo de PDF"
  - "notas.env"
related_terms:
  - ".gitignore"
  - "src/"
  - "tests/"
  - "README.md"
  - "docs/"
  - "requirements.txt"
  - "pytest.ini"
  - "data/notes/"
  - "index.json"
  - "Telegram"
  - "data/audio/"
  - "TTS"
  - "context.user_data"
  - "data/monitoring/"
  - "data/logs/"
  - ".env"
  - "credenciales.env"
  - "secretos locales"
---

# 13:17 - Archivos generados y versionado

## Nota limpia

El directorio data/ almacena artefactos de ejecución local y está excluido del versionado mediante .gitignore.

Se versionan únicamente el código fuente (src/), las pruebas (tests/) y la documentación o configuración no secreta (README.md, docs/, requirements.txt, pytest.ini).

No se versionan las notas generadas en data/notes/YYYY-MM-DD/*.md ni sus índices (data/notes/YYYY-MM-DD/index.md y data/notes/index.json), aunque sí permanecen localmente.

Los documentos recibidos por Telegram se descargan en data/audio/documents/ como copia temporal y se eliminan al finalizar. El audio recibido por Telegram se guarda en data/audio/* y actualmente se conserva.

El audio TTS del bot en data/audio/tts/ y las respuestas largas en Markdown en data/audio/responses/ son temporales: si el envío termina bien, se borran. Las acciones Explicar, Sugerencias, Investigar y Dialéctica, así como el botón Play, no dejan archivos permanentes locales; solo pueden generar temporalmente un .md largo o un MP3 TTS antes del envío, y su estado vive en Telegram y en memoria (context.user_data).

Los audios de la GUI en data/audio/gui/*_latest.mp3 se conservan durante la sesión local. El monitoreo de PDF guarda resultados en data/monitoring/pdf_pipeline_probe_*.json y puede crear PDFs sintéticos temporales en data/monitoring/notas_pdf_probe_*/. Los logs y el PID en data/logs/ y data/notas-bot.pid se mantienen mientras el proceso corre o para diagnóstico.

El entorno y los secretos locales (.venv/, .env, credenciales.env, notas.env) no deben versionarse. En particular, notas.env contiene credenciales locales y debe mantenerse fuera de Git; si aparece como archivo no rastreado, no debe agregarse al repositorio.

## Conceptos clave

- **data/**: Directorio de artefactos de ejecución local excluido del versionado por .gitignore.
- **Versionado**: Estado de los archivos que sí deben entrar al repositorio, limitado aquí a código, pruebas y documentación o configuración no secreta.
- **Persistencia local**: Condición de los archivos que se conservan en la máquina local, ya sea de forma continua o mientras dura una sesión o proceso.
- **Archivos temporales**: Archivos creados para procesamiento o envío y eliminados al finalizar correctamente, como copias descargadas, Markdown largos o MP3 TTS.
- **Notas generadas**: Archivos Markdown creados en data/notes/YYYY-MM-DD/ que se guardan localmente pero no se versionan.
- **Índices de notas**: Archivos index.md e index.json que organizan notas generadas y se mantienen localmente sin versionarse.
- **Audio TTS del bot**: Audio sintetizado en data/audio/tts/ que se usa para envío y se elimina si el proceso termina bien.
- **Acciones del bot**: Funciones como Explicar, Sugerencias, Investigar y Dialéctica, cuyo estado queda en Telegram y en context.user_data, sin archivo local permanente.
- **Monitoreo de PDF**: Salida de diagnóstico en data/monitoring/ que guarda probes JSON y puede generar PDFs sintéticos temporales.
- **notas.env**: Archivo con credenciales locales que debe mantenerse fuera de Git y no agregarse al repositorio.

## Terminos relacionados

- .gitignore
- src/
- tests/
- README.md
- docs/
- requirements.txt
- pytest.ini
- data/notes/
- index.json
- Telegram
- data/audio/
- TTS
- context.user_data
- data/monitoring/
- data/logs/
- .env
- credenciales.env
- secretos locales
