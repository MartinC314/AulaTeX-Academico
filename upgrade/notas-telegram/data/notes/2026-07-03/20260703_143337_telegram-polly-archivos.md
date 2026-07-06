---
id: "20260703143337"
title: "14:33 - Telegram-polly-archivos"
key: "telegram-polly-archivos"
created_at: "2026-07-03T14:33:37.875626"
tags:
  - "Respuesta de audio en Telegram"
  - "Polly"
  - "Fallback a texto"
  - "data/notes"
  - "Archivos temporales de audio"
  - "notas.env"
  - "Monitoreo de PDF"
related_terms:
  - "Telegram"
  - "TTS"
  - "AWS"
  - "Polly"
  - "gitignore"
  - "data/notes"
---

# 14:33 - Telegram-polly-archivos

## Nota limpia

Configuración del bot para respuestas por audio en Telegram:
- `TELEGRAM_REPLY_AUDIO_ENABLED=true`
- AWS/Polly: `AWS_REGION=us-east-1`, `POLLY_VOICE_ID=Andres`, `POLLY_ENGINE=generative`, `POLLY_LANGUAGE_CODE=es-MX`, `POLLY_SAMPLE_RATE=24000`, `POLLY_MAX_CHARS=2500`.
- `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY` están vacíos en esta nota.

Comportamiento esperado:
1. El bot envía primero la respuesta en texto.
2. Después envía la misma salida en uno o varios audios cortos.
3. Si Polly falla, la respuesta en texto se conserva y el flujo no se interrumpe.

Manejo de archivos y versionado:
- `src/`, `tests/`, `README.md`, `docs/`, `requirements.txt` y `pytest.ini` se conservan localmente y sí se versionan.
- `data/notes/` ya no está ignorado por `.gitignore`; aquí se versionan la nota base, sus derivados (`*.explain.md`, `*.suggest.md`, `*.research.md`, `*.dialectic.md`) y los índices (`index.md`, `index.json`).
- El resto de `data/` sigue excluido del versionado.
- Archivos temporales de Telegram (`data/audio/documents/`, `data/audio/*`, `data/audio/tts/`, `data/audio/responses/`) se usan como copias locales durante el flujo y se eliminan al finalizar correctamente; no se versionan.
- Los audios de la GUI (`data/audio/gui/*.mp3`) existen durante la sesión local y no se versionan.
- El monitoreo de PDF guarda diagnósticos en `data/monitoring/pdf_pipeline_probe_*.json`; los artefactos sintéticos asociados tampoco se versionan.
- Logs y PID (`data/logs/`, `data/notas-bot.pid`) se mantienen localmente para ejecución o diagnóstico y no se versionan.
- `.venv`, `.env`, `credenciales.env` y `notas.env` son locales y no deben versionarse. En particular, `notas.env` contiene credenciales y no debe agregarse a Git.

Pruebas y diagnóstico:
- Ejecutar pruebas: `python -m pytest -q`
- Monitoreo de PDF con archivo real: `python scripts/monitor_pdf_pipeline.py --pdf RUTA\A\tu-archivo.pdf`
- Monitoreo sintético desde texto: `python scripts/monitor_pdf_pipeline.py --from-text data/monitoring/probe_roma_input.txt`
- El script de monitoreo genera un JSON de diagnóstico con tiempos de extracción, intento de PDF directo sobre Responses API, validez del JSON devuelto y resumen final.
- La lógica rescatada del prototipo quedó documentada en `docs/bedrock-prueba-migracion.md` y el pipeline funcional vive en `src/`.

## Conceptos clave

- **Respuesta de audio en Telegram**: Modo en el que el bot envía primero texto y luego la misma respuesta en audio, dividido en fragmentos cortos si hace falta.
- **Polly**: Servicio TTS configurado en esta nota para generar audios con voz Andres, motor generative, idioma es-MX y muestreo de 24000.
- **Fallback a texto**: Comportamiento por el cual, si falla la generación de audio con Polly, la respuesta en texto sigue entregándose sin romper el flujo.
- **data/notes**: Directorio donde se guardan y versionan las notas generadas, sus derivados en Markdown y los índices.
- **Archivos temporales de audio**: Copias locales de documentos, audios entrantes, TTS y respuestas largas usadas durante el flujo y eliminadas si termina correctamente.
- **notas.env**: Archivo de entorno local con credenciales que debe mantenerse fuera de Git.
- **Monitoreo de PDF**: Prueba controlada del pipeline de documentos que genera JSON de diagnóstico en `data/monitoring/`.

## Terminos relacionados

- Telegram
- TTS
- AWS
- Polly
- gitignore
- data/notes
