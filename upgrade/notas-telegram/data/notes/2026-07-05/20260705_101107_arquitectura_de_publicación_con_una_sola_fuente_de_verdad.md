---
id: "20260705101107"
title: "10:11 - Arquitectura de publicación con una sola fuente de verdad"
key: "arquitectura_de_publicación_con_una_sola_fuente_de_verdad"
created_at: "2026-07-05T10:11:07.690241"
text_type: "informativo"
tags:
  - "Una sola fuente de verdad"
  - "Varias salidas"
  - "Prioridad de lectura humana"
  - "Estrategia dual de nombres de archivo"
  - "Idempotencia"
  - "Automatismo final"
related_terms:
  - "publicación"
  - "Markdown"
  - "audio"
  - "cuestionario"
  - "saltos de línea"
  - "nombres de archivo"
  - "dependencias"
  - "automatización"
  - "Play"
  - "formato literal"
---

# 10:11 - Arquitectura de publicación con una sola fuente de verdad

## Nota limpia

Conviene adoptar una arquitectura de una sola fuente de verdad con varias salidas, sin perder la prioridad de lectura humana en la entrega. El contenido se modela una sola vez y, desde ahí, se generan el texto con acciones, el Markdown y el audio para evitar divergencias entre representaciones.

La publicación debería comenzar con la pieza más accionable, conservar los saltos de línea cuando expresen la estructura de un cuestionario y resolver los nombres de archivo con una estrategia dual: un nombre visible completo para las personas y un nombre técnico normalizado para los sistemas.

Los derivados pueden ejecutarse automáticamente con validaciones de dependencia e idempotencia. En cambio, Play debería dispararse solo cuando el estado sea inequívoco o cuando la política de uso justifique la automatización.

Sigue abierta una decisión central: cuánto valor aporta el automatismo final frente al riesgo de errores silenciosos y en qué punto la preservación literal del formato deja de aclarar y empieza a fragilizar el flujo.

## Conceptos clave

- **Una sola fuente de verdad**: Modelo en el que el contenido se define una sola vez y desde ahí se generan todas las representaciones.
- **Varias salidas**: Derivaciones del mismo contenido hacia formatos como texto con acciones, Markdown y audio.
- **Prioridad de lectura humana**: Criterio de entrega que favorece la claridad para las personas por encima de otras consideraciones técnicas.
- **Estrategia dual de nombres de archivo**: Uso de un nombre visible completo para personas y un nombre técnico normalizado para sistemas.
- **Idempotencia**: Propiedad deseable en la ejecución automática de derivados para evitar efectos inconsistentes al repetir procesos.
- **Automatismo final**: Último nivel de automatización cuya utilidad debe compararse con el riesgo de errores silenciosos.

## Terminos relacionados

- publicación
- Markdown
- audio
- cuestionario
- saltos de línea
- nombres de archivo
- dependencias
- automatización
- Play
- formato literal

## Procesamientos derivados

- Explicar: [20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.explain.md](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.explain.md)
- Sugerencias: [20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.suggest.md](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.suggest.md)
- Investigar: [20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.research.md](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.research.md)
- Dialectica: [20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.dialectic.md](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.dialectic.md)
