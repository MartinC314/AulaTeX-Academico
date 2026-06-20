# AulaTeX stage

- Etapa: planificar
- Rol: Planificador editorial
- Mision: descomponer el objetivo en plan ejecutable y criterios de aceptacion
- Motor: Codex
- Estado: ok

### Plan breve por fases (Actividad 1 — *Derecho a la Seguridad Social*, UnADM)

## 1) Fase de investigación (insumos verificables)
**Objetivo:** reunir base normativa e institucional suficiente para sustentar el producto jurídico.

**Acciones:**
- Delimitar la consigna en un **problema jurídico concreto**.
- Revisar fuentes locales obligatorias:
  - `programa-analitico-derecho-a-la-seguridad-social.md`
  - `derecho-a-la-seguridad-social.bib`
  - plantilla `reporte-derecho-a-la-seguridad-social-Actividad-1.tex`
- Extraer fundamento mínimo:
  - CPEUM (marco constitucional),
  - LSS,
  - LISSSTE,
  - encuadre UnADM.
- Identificar 1–2 criterios jurisprudenciales **solo si se cuenta con fuente verificable**.  
  **Supuesto:** si no hay tesis/jurisprudencia confirmada en repositorio confiable, se omite y se declara límite.

**Criterios de aceptación:**
- **Institución (UnADM):** trazabilidad de fuentes y formato académico.
- **Carrera (Derecho):** problema jurídico + fundamentación normativa.
- **Materia:** alineación con ejes (constitucional, instituciones, principios, justiciabilidad).
- **Actividad 1:** insumos suficientes para construir análisis propio, no solo resumen.

---

## 2) Fase de generación (redacción jurídica en plantilla)
**Objetivo:** convertir la consigna en entregable estructurado y argumentado.

**Estructura mínima a llenar en `.tex`:**
1. Introducción (planteamiento del problema).
2. Encuadre institucional y jurídico.
3. Desarrollo del producto solicitado (según consigna).
4. Análisis propio (postura jurídica argumentada).
5. Conclusión (aprendizaje + implicación profesional).
6. Referencias (BibTeX local).

**Reglas editoriales:**
- No inventar fuentes ni datos.
- Marcar vacíos con `\pendiente{...}` solo en borrador interno.
- Redacción en español académico, precisión terminológica.

**Criterios de aceptación:**
- **Institución:** identidad y estructura canónica respetadas.
- **Carrera:** argumentación jurídica clara (hecho-norma-aplicación-conclusión).
- **Materia:** uso explícito de principios (universalidad, progresividad, igualdad/no discriminación).
- **Actividad 1:** producto completo y coherente con la consigna concreta.

---

## 3) Fase de compilación (control técnico)
**Objetivo:** obtener PDF estable y citable.

**Acciones:**
- Verificar archivo principal: `reporte-derecho-a-la-seguridad-social-Actividad-1.tex`.
- Ejecutar secuencia: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Corregir:
  - referencias sin resolver,
  - caracteres/acentos,
  - secciones vacías visibles.

**Criterios de aceptación:**
- **Institución:** entrega técnicamente legible y formal.
- **Carrera:** citas y bibliografía funcionales.
- **Materia:** referencias normativas correctamente enlazadas al análisis.
- **Actividad 1:** PDF final sin marcadores pendientes visibles.

---

## 4) Fase de evaluación (verificación y validación final)
**Objetivo:** confirmar calidad académica y pertinencia jurídica antes de entregar.

**Lista de validación:**
- ¿Existe problema jurídico delimitado?
- ¿Se sustenta en norma vigente verificable?
- ¿Hay análisis propio y no mera descripción?
- ¿La conclusión responde al problema inicial?
- ¿Las fuentes citadas coinciden con `.bib` y texto?
- ¿Se eliminaron notas internas de edición (`\pendiente{}`)?

**Criterios de aceptación global (rúbrica sintética):**
- **Institución UnADM:** cumplimiento formal, honestidad académica, trazabilidad.
- **Licenciatura en Derecho:** solidez argumentativa y técnica jurídica básica.
- **Derecho a la Seguridad Social:** dominio del marco constitucional-legal e instituciones clave.
- **Actividad 1:** producto terminado, claro, verificable y defendible.

---

Si deseas, en el siguiente paso te genero una **rúbrica de evaluación en tabla (0–100)** lista para pegar en LaTeX.
