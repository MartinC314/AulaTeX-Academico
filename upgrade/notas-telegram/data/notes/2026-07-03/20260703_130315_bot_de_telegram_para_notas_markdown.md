---
id: "20260703130315"
title: "13:03 - Bot de telegram para notas markdown"
key: "bot_de_telegram_para_notas_markdown"
created_at: "2026-07-03T13:03:15.615271"
tags:
  - "Pipeline de notas"
  - "Frontmatter mínimo"
  - "Proveedor de transcripción"
  - "GUI local"
  - "Acciones sobre notas"
  - "Síntesis de documentos"
  - "Audio de respuesta"
  - "Monitoreo del pipeline PDF"
related_terms:
  - "Telegram bot"
  - "Markdown"
  - "base de conocimiento"
  - "Azure Speech"
  - "Azure OpenAI"
  - "GPT Realtime"
  - "ffmpeg"
  - "AWS Polly"
  - "GUI local"
  - "transcripción de audio"
  - "resumen de documentos"
  - "index.md"
  - "index.json"
  - "pytest"
  - "logs"
  - "polling"
---

# 13:03 - Bot de telegram para notas markdown

## Nota limpia

Sistema para capturar texto, audios o documentos desde Telegram o una GUI local, transcribirlos si hace falta y convertirlos en notas Markdown limpias para una base de conocimiento.

Flujo principal:
1. Recibe texto, nota de voz, audio o documento.
2. Si la entrada es audio, lo guarda en data/audio/ y lo transcribe con Azure Speech o GPT Realtime, según la configuración.
3. Envía el contenido a Azure OpenAI para generar un título breve, una nota limpia o un resumen sintético, conceptos clave con definición y términos relacionados.
4. Guarda la nota en data/notes/YYYY-MM-DD/ y actualiza index.md e index.json.

La metadata de cada nota se mantiene mínima: id, title, key, created_at, tags y related_terms. Las definiciones de conceptos van en el cuerpo de la nota.

Configuración relevante:
- Variables para Telegram, directorios de notas y audio, y modo polling.
- Variables para Azure Speech.
- Variables para Azure OpenAI, incluyendo compatibilidad con distintos nombres de deployment y carga de credenciales desde .env, notas.env y credenciales.env.
- ffmpeg debe estar disponible para convertir audios antes de transcribirlos.

Proveedores de transcripción:
- speech: usa Azure Speech.
- realtime: usa GPT Realtime.
- auto: intenta Realtime y, si falla, vuelve a Azure Speech.

La GUI local permite capturar texto, audio o documentos y ejecutar el mismo pipeline. Muestra cinco resultados o acciones: Nota guardada, Explicar, Sugerencias, Investigar y Dialéctica. Incluye tarjetas con estado, vista previa, reproducción de audio, panel flotante, atajos de teclado y soporte para PDF, TXT, MD y DOCX. Cuando la entrada es un documento, la salida busca ser una síntesis útil y breve.

Después de guardar una nota, el sistema ofrece acciones rápidas para ampliar o analizar el contenido. La acción Investigar genera resumen ejecutivo, hallazgos clave, implicaciones prácticas, preguntas abiertas y acciones recomendadas; si hacen falta datos actuales o fuentes externas, lo indica.

Opcionalmente, el bot puede reenviar las respuestas como audio mediante AWS Polly. Primero envía el texto y luego uno o varios audios; si Polly falla, el flujo continúa con la respuesta textual.

Incluye pruebas con pytest, un script de monitoreo del pipeline de PDF y scripts para iniciar o detener el bot. También evita levantar dos instancias locales en modo polling, guarda el PID y escribe logs en data/logs/.

## Conceptos clave

- **Pipeline de notas**: Proceso que recibe una entrada, la transcribe si es audio, la transforma en nota Markdown con IA, la guarda y actualiza índices.
- **Frontmatter mínimo**: Conjunto corto de metadatos por nota: id, title, key, created_at, tags y related_terms.
- **Proveedor de transcripción**: Mecanismo configurable para transcribir audio: Azure Speech, GPT Realtime o modo automático con fallback.
- **GUI local**: Interfaz de escritorio para capturar texto, audio o documentos y ejecutar el mismo flujo del bot con resultados en tarjetas.
- **Acciones sobre notas**: Procesamientos posteriores a la nota guardada: Explicar, Sugerencias, Investigar y Dialéctica.
- **Síntesis de documentos**: Modo en el que documentos como PDF, TXT, MD o DOCX se convierten en una nota-resumen breve y útil.
- **Audio de respuesta**: Función opcional que convierte las respuestas del bot en audio con AWS Polly sin interrumpir el flujo si falla.
- **Monitoreo del pipeline PDF**: Prueba de diagnóstico que registra tiempos, validez del JSON devuelto y un resumen final del procesamiento de documentos.

## Terminos relacionados

- Telegram bot
- Markdown
- base de conocimiento
- Azure Speech
- Azure OpenAI
- GPT Realtime
- ffmpeg
- AWS Polly
- GUI local
- transcripción de audio
- resumen de documentos
- index.md
- index.json
- pytest
- logs
- polling
