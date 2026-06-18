# AulaTeX stage

- Etapa: planificar
- Rol: Planificador editorial
- Mision: descomponer el objetivo en plan ejecutable y criterios de aceptacion
- Motor: Codex
- Estado: ok

Claro. **Rol Planificador activado**.  
A continuación presento un **plan breve por fases** para la actividad solicitada (*Acción: generar-actividad, Actividad 1*) en:

**UnADM / Licenciatura en Derecho / Historia del Derecho en México (LDE-S1B1)**.

---

## Plan por fases (flujo con estados)

### Fase 1. Investigación y encuadre (Estado: `RECOLECCION`)
**Objetivo:** delimitar qué pide la Actividad 1 y qué evidencia académica debe entregarse.

Tareas:
1. Revisar consigna oficial de Actividad 1 (si no está disponible, marcar supuesto).
2. Extraer propósito, formato, extensión, criterios de evaluación y fecha.
3. Definir problema jurídico-histórico central alineado con la materia.
4. Identificar fuentes verificables (institucionales y académicas) para `.bib`.

Salida esperada:
- Ficha de requisitos de la actividad.
- Lista inicial de fuentes reales y citables.

---

### Fase 2. Diseño académico-editorial (Estado: `PLAN_DISENO`)
**Objetivo:** estructurar el contenido con identidad UnADM y lógica jurídica.

Tareas:
1. Ajustar metadatos en `reporte-historia-del-derecho-en-mexico.tex`:
   - título de actividad, subtítulo, semana, figura docente (si falta, marcar).
2. Definir esquema de secciones:
   - Introducción, desarrollo conceptual-histórico, análisis propio, conclusión jurídica.
3. Diseñar producto solicitado (cuadro, línea del tiempo, matriz, mapa conceptual, etc.).
4. Planear citas y correspondencia con bibliografía `.bib`.

Salida esperada:
- Guion de redacción + estructura final del reporte/presentación.

---

### Fase 3. Generación del producto (Estado: `REDACCION`)
**Objetivo:** redactar versión completa de la Actividad 1 en formato LaTeX.

Tareas:
1. Redactar contenido académico en español formal.
2. Integrar análisis propio (no solo resumen histórico).
3. Incorporar citas en texto y referencias en `historia-del-derecho-en-mexico.bib`.
4. Completar conclusión con transferencia a práctica jurídica.

Salida esperada:
- Documento `.tex` completo y consistente con la consigna.

---

### Fase 4. Compilación técnica (Estado: `COMPILACION`)
**Objetivo:** asegurar que el documento compile sin errores y con formato institucional.

Tareas:
1. Compilar (`pdflatex` + `bibtex/biber` según plantilla).
2. Corregir errores de codificación, paquetes, rutas de imágenes y bibliografía.
3. Verificar portada, índice, tablas/figuras y bibliografía final.

Salida esperada:
- PDF funcional, limpio y legible.

---

### Fase 5. Verificación y validación (Estado: `QA`)
**Objetivo:** validar calidad académica, integridad y cumplimiento institucional.

Tareas:
1. Lista de cotejo editorial (README + programa analítico).
2. Revisión de integridad académica (sin invención de fuentes).
3. Validación argumentativa: problema, fundamento, análisis y conclusión jurídica.
4. Revisión de estilo y ortografía.

Salida esperada:
- Versión final aprobada para entrega.

---

### Fase 6. Consenso multiagente y cierre (Estado: `CIERRE`)
**Objetivo:** consolidar decisión de “listo para entrega”.

Roles de consenso:
- **Agente Académico:** pertinencia jurídica e histórica.
- **Agente Editorial:** claridad, estructura y tono.
- **Agente Técnico LaTeX:** compilación y formato.
- **Agente de Integridad:** citas, fuentes y transparencia de supuestos.

Salida esperada:
- Acta breve de conformidad + pendientes (si existen).

---

## Criterios de aceptación

### 1) Institución (UnADM)
- Mantiene identidad institucional en portada y enfoque.
- Evidencia integridad académica: citas y referencias verificables.
- Lenguaje formal y estructura de producto universitario.

### 2) Carrera (Licenciatura en Derecho)
- Enfoque jurídico explícito (no solo narración histórica).
- Uso de categorías de análisis legal (norma, institución, efectos jurídicos).
- Cierre con utilidad para práctica profesional del derecho.

### 3) Materia (Historia del Derecho en México)
- Periodización y contexto histórico-jurídico correctos.
- Relación entre procesos históricos e instituciones jurídicas mexicanas.
- Postura crítica del estudiante sobre evolución del derecho en México.

### 4) Actividad 1
- Responde exactamente a la consigna y formato solicitado.
- Incluye producto/evidencia pedida (cuadro, mapa, síntesis, etc.).
- Contiene: introducción, desarrollo fundamentado, análisis propio y conclusión jurídica.
- Bibliografía incorporada en `.bib` y citada en el texto.

---

## Supuestos (marcados por falta de información)
1. **No se proporcionó la consigna textual de la Actividad 1** en el contexto compartido.  
2. Se asume que la entrega principal será en `reporte-historia-del-derecho-en-mexico.tex` (y opcionalmente presentación).  
3. Se asume uso de bibliografía académica adicional además de las dos fuentes institucionales ya existentes.

---

Si quieres, en el siguiente paso ejecuto la **Fase 2** y te devuelvo una **plantilla ya aterrizada para Actividad 1** (títulos, secciones y campos listos para llenar/compilar).
