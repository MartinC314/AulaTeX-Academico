---
id: "20260703143120"
title: "14:31 - Bot de notas para telegram"
key: "bot_de_notas_para_telegram"
created_at: "2026-07-03T14:31:20.828367"
tags:
  - "Nota base"
  - "Procesamientos derivados"
  - "Transcripción"
  - "GUI local"
  - "Versionado en Git"
  - "Frontmatter corto"
related_terms:
  - "Telegram"
  - "Markdown"
  - "Azure Speech"
  - "Azure OpenAI"
  - "GPT Realtime"
  - "ffmpeg"
  - "data/notes"
  - "data/audio"
---

# 14:31 - Bot de notas para telegram

## Nota limpia

Sistema para capturar texto, audio o documentos desde Telegram o una GUI local y convertirlos en notas Markdown limpias para una base de conocimiento. Si la entrada es audio, se guarda en data/audio/ y se transcribe con Azure Speech o con GPT Realtime; en modo auto, Realtime se intenta primero y, si falla, se usa Azure Speech. Luego el texto crudo o el contenido del documento se envía a Azure OpenAI para generar un título breve, una redacción limpia o una síntesis si la entrada es extensa, conceptos clave con definición y términos relacionados.

Las notas se guardan en data/notes/YYYY-MM-DD/ y están pensadas para versionarse en Git junto con sus derivados Markdown. La nota base mantiene un frontmatter corto y una sección de Procesamientos derivados con enlaces a Explicar, Sugerencias, Investigar y Dialéctica. Cada derivado se guarda como archivo .md hermano de la nota base, y además se actualizan index.md del día e index.json global.

La GUI local usa el mismo pipeline y permite trabajar con texto, audio y documentos compatibles (.pdf, .txt, .md, .docx). Muestra cinco resultados en tarjetas compactas: Nota guardada, Explicar, Sugerencias, Investigar y Dialéctica. Cada tarjeta incluye estado, vista previa, reproducción de audio y acceso a un panel flotante con acciones como copiar, guardar como Markdown o enviar a Telegram. También incluye atajos de teclado y reproducción interna con pygame-ce, con fallback a reproductor externo si hace falta.

La instalación requiere pip install -r requirements.txt y ffmpeg en el PATH para convertir audios de Telegram antes de transcribirlos. La configuración depende de variables de entorno para Telegram, rutas locales, Azure Speech y Azure OpenAI; también se aceptan variantes para Azure AI Foundry y archivos .env, notas.env y credenciales.env, con prioridad final para credenciales.env. Los scripts evitan ejecutar dos instancias locales del bot con polling, guardan el PID en data/notas-bot.pid y escriben logs en data/logs/.

Como función adicional, el sistema puede reenviar respuestas textuales como audio mediante una integración opcional con AWS Polly.

## Conceptos clave

- **Nota base**: Archivo Markdown principal generado a partir de texto, audio o documento, con frontmatter corto, contenido limpio y enlaces a procesamientos derivados.
- **Procesamientos derivados**: Resultados adicionales asociados a una nota base: Explicar, Sugerencias, Investigar y Dialéctica, guardados como archivos Markdown hermanos.
- **Transcripción**: Conversión de audio a texto usando Azure Speech o GPT Realtime antes de generar la nota.
- **GUI local**: Interfaz de escritorio que permite capturar entradas, generar notas con el mismo pipeline del bot y gestionar resultados en tarjetas compactas.
- **Versionado en Git**: Criterio según el cual las notas y sus derivados dentro de data/notes/ están pensados para almacenarse y seguirse con Git.
- **Frontmatter corto**: Metadata mínima de cada nota, limitada a campos como id, title, key, created_at, tags y related_terms.

## Terminos relacionados

- Telegram
- Markdown
- Azure Speech
- Azure OpenAI
- GPT Realtime
- ffmpeg
- data/notes
- data/audio
