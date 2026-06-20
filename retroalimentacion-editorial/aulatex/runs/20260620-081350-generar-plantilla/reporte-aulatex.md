# Reporte AulaTeX

- Objetivo: `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde`
- Nivel: materia
- Accion: generar-plantilla
- Actividad: 1

## Arquitectura agentica

- Planificacion con memoria compartida
- Uso de herramientas con invocacion segura
- Flujo con maquina de estados y auditoria
- Verificacion/validacion editorial
- Consenso multiagente con critico adversarial

## Contexto de ejecucion

- Modo de generacion: direct
- Padre editorial: N/A
- Nivel hijo: N/A
- Hijo solicitado: N/A
- Vista previa: N/A

## Ciclo LLM

### 1. planificar - Planificador editorial - Codex

## Plan breve por fases (Actividad 1 · Derecho a la Seguridad Social · UnADM)

### Fase 1. Investigación y delimitación jurídica
**Objetivo:** convertir la consigna en problema jurídico verificable.  
**Acciones:**
1. Precisar el tema central de Actividad 1 (supuesto: aún no se adjunta consigna completa).
2. Delimitar pregunta jurídica, alcance temporal, normativo e institucional.
3. Levantar marco mínimo con fuentes vigentes: CPEUM, LSS, LISSSTE y material UnADM.
4. Identificar 1–2 criterios jurisprudenciales pertinentes (si la actividad lo exige).

**Entregable de fase:** esquema: *problema → fundamento → análisis → conclusión*.

---

### Fase 2. Generación de contenido en plantilla LaTeX
**Objetivo:** llenar `reporte-derecho-a-la-seguridad-social-Actividad-1.tex` con contenido académico.  
**Acciones:**
1. Sustituir todos los `\pendiente{...}` por redacción final.
2. Completar portada (figura docente, fecha definitiva, lugar si aplica).
3. Redactar secciones sustantivas:
   - Introducción con problema jurídico.
   - Encuadre normativo (constitucional + legal).
   - Desarrollo del producto solicitado por la actividad.
   - Análisis propio argumentado.
   - Conclusión con postura jurídica.
4. Integrar citas `\citep{...}` solo de fuentes verificables en `.bib`.

**Entregable de fase:** archivo `.tex` completo, sin marcadores pendientes.

---

### Fase 3. Compilación técnica y control editorial
**Objetivo:** obtener PDF estable y trazable.  
**Acciones:**
1. Verificar cierre correcto de bibliografía (actualmente hay corte: `\bibliog...`).
2. Ejecutar compilación (pdflatex + bibtex + pdflatex + pdflatex).
3. Corregir warnings críticos: referencias sin resolver, figuras faltantes, codificación.
4. Revisar formato institucional (tipografía, interlineado, portada, índice).

**Entregable de fase:** PDF final compilado + log sin errores bloqueantes.

---

### Fase 4. Evaluación académica y validación final
**Objetivo:** asegurar cumplimiento de rúbrica y enfoque UnADM.  
**Acciones:**
1. Validar coherencia entre consigna, argumento y conclusión.
2. Confirmar trazabilidad de citas (norma vigente y fuente identificable).
3. Revisar lenguaje académico-jurídico y ortografía.
4. Aplicar checklist final de calidad (fondo y forma).

**Entregable de fase:** versión de entrega lista para plataforma.

---

## Criterios de aceptación

### 1) Institución (UnADM)
- Formato académico formal, portada completa, índice, estructura lógica.
- Fuentes verificables y vigentes; sin invención bibliográfica.
- Redacción clara, objetiva y profesional.

### 2) Carrera (Licenciatura en Derecho)
- Problema jurídico explícito y delimitado.
- Fundamentación normativa sólida (Constitución y leyes aplicables).
- Argumentación jurídica propia, no solo descriptiva.

### 3) Materia (Derecho a la Seguridad Social)
- Inclusión de ejes: marco constitucional, IMSS/ISSSTE, principios (universalidad, progresividad, igualdad/no discriminación), acceso y justiciabilidad.
- Uso correcto de terminología de seguridad social.
- Relación entre norma y realidad práctica.

### 4) Actividad 1
- Producto solicitado desarrollado exactamente en el formato pedido por la consigna (ensayo, cuadro, análisis de caso, etc.).
- Evidencia de aprendizaje inicial: comprensión conceptual + aplicación jurídica.
- Conclusión útil y argumentada, no genérica.

---

## Riesgos, faltantes, placeholders y errores bloqueantes

### Riesgos
- **R1:** No contar con la consigna textual de Actividad 1 → riesgo de desalineación con rúbrica.
- **R2:** Citas normativas desactualizadas al momento de entrega.
- **R3:** Desarrollo excesivamente descriptivo, sin postura jurídica personal.

### Faltantes detectados
- Nombre de **figura docente** pendiente en portada.
- No se incluye aún el **producto específico** solicitado por la actividad.
- Falta corroborar si se exige jurisprudencia obligatoria.

### Placeholders activos
- `\pendiente{...}` en:
  - Introducción
  - Desarrollo del producto
  - Análisis propio
  - Conclusión

### Errores bloqueantes (técnicos)
- Corte de comando de bibliografía al final del `.tex`: aparece `\bibliog...` incompleto.  
  **Debe corregirse** a:
  - `\bibliography{derecho-a-la-seguridad-social}` (o nombre exacto del `.bib` en la carpeta).
- Posible ruta de logo no portable: `img/departamentos/UnADM.pdf` (validar existencia real).

---

## Supuestos explícitos
1. **Supuesto A:** la consigna detallada de Actividad 1 no fue proporcionada en el contexto.
2. **Supuesto B:** se mantiene `natbib` como estilo de citación institucional para esta entrega.
3. **Supuesto C:** el archivo `.bib` local es la base primaria y se ampliará solo con fuentes verificables.

## Consenso y validacion

- Puntuacion de consenso: 9.23/10
- Estado: PASS

### Criterios
- identidad_institucional: OK
- bibliografia: OK
- trazabilidad: OK
- compilacion: OK
- riesgos: OK

### Puntuacion por rol
- Planificador editorial: 8.60/10

### Recomendaciones
- Usar el reporte como retroalimentacion editorial aplicable al objetivo.

## Compilacion

- UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex: OK (0)
- UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex: OK (0)

## Materializacion de plantilla

- Estado: OK
- Carpeta: `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde`

### Artefactos
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/referencias-derecho-a-la-seguridad-social`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/planeaciones-derecho-a-la-seguridad-social`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/assets-derecho-a-la-seguridad-social`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex`
- `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json`
