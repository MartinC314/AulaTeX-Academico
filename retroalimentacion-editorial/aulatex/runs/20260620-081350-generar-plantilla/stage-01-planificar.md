# AulaTeX stage

- Etapa: planificar
- Rol: Planificador editorial
- Mision: descomponer el objetivo en plan ejecutable y criterios de aceptacion
- Motor: Codex
- Estado: ok

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
