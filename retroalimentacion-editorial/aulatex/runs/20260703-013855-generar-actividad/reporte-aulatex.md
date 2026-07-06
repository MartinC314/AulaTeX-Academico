# Reporte AulaTeX

- Objetivo: `UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde`
- Nivel: materia
- Accion: generar-actividad
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

### Plan breve por fases (Actividad 1 · Historia del Derecho en México · UnADM)

## 1) Fase de investigación y encuadre
**Objetivo:** delimitar qué pide la Actividad 1 y con qué evidencias debe cumplirse.

- Levantar consigna oficial de la Actividad 1 (aula/guía semanal).
- Identificar: producto solicitado, extensión, formato, criterios de evaluación, fecha.
- Mapear el producto al encuadre de la materia (semestre 1, bloque 1, obligatoria, 8 créditos).
- Definir problema jurídico-histórico central y alcance temporal/geográfico.

**Criterios de aceptación**
- **Institución (UnADM):** identidad institucional visible, integridad académica, redacción formal.
- **Carrera (Derecho):** enfoque jurídico (no solo narrativo histórico), uso de categorías legales.
- **Materia:** relación explícita con evolución del Derecho en México.
- **Actividad 1:** cumplimiento exacto de entregable, estructura y rúbrica.

---

## 2) Fase de diseño y generación de contenido
**Objetivo:** producir el borrador académico en la plantilla `reporte-historia-del-derecho-en-mexico.tex`.

- Actualizar metadatos: título de actividad, semana, figura docente (si se conoce), fecha.
- Estructurar el reporte:
  1. Introducción (problema, objetivo, alcance).
  2. Desarrollo (conceptos, etapas históricas, fundamento normativo/doctrinal).
  3. Evidencia solicitada (cuadro/mapa/matriz, según consigna).
  4. Análisis propio (postura jurídica argumentada).
  5. Conclusión transferible a práctica jurídica.
- Insertar citas verificables y registrar entradas en `.bib` (sin inventar fuentes).
- Marcar supuestos cuando falte información oficial.

**Criterios de aceptación**
- Coherencia argumentativa y trazabilidad entre problema → análisis → conclusión.
- Citas y bibliografía consistentes (toda cita en texto aparece en `.bib`).
- Conclusión con criterio jurídico propio (no solo resumen).

---

## 3) Fase técnica de compilación
**Objetivo:** obtener PDF limpio y estable.

- Compilar LaTeX (BibTeX/Biber según configuración del template).
- Resolver errores de paquetes, rutas de imágenes y referencias.
- Revisar portada, índice, tipografía, watermark y tablas/figuras.

**Criterios de aceptación**
- PDF compila sin errores bloqueantes.
- Sin referencias rotas, sin “??”, sin claves BibTeX faltantes.
- Presentación formal y legible en formato institucional.

---

## 4) Fase de evaluación y validación final
**Objetivo:** verificar calidad académica y alineación con rúbrica.

- Checklist final:
  - Responde a la consigna real de Actividad 1.
  - Incluye fundamento histórico-jurídico suficiente.
  - Evidencia visual correctamente titulada e interpretada.
  - Conclusión con implicación jurídica práctica.
  - Ortografía y estilo académico.
- Validación cruzada con pauta editorial local (`README` y programa analítico).

**Criterios de aceptación**
- **Institucional:** cumplimiento formal UnADM.
- **Carrera:** razonamiento jurídico explícito.
- **Materia:** hilo histórico del Derecho en México bien sustentado.
- **Actividad:** rúbrica cubierta punto por punto.

---

## Riesgos, faltantes, placeholders y errores bloqueantes

### Riesgos
- No contar con la **consigna específica** de Actividad 1 (riesgo alto de desalineación).
- Bibliografía insuficiente o no verificable.
- Convertir el trabajo en relato histórico sin análisis jurídico.

### Faltantes detectados (contexto actual)
- No se proporcionó texto de la consigna/rúbrica de Actividad 1.
- En plantillas hay campos “por definir” (figura docente, semana, subtítulo exacto).
- Archivo de presentación parece truncado al final (`\se`), posible corrupción parcial.

### Placeholders a sustituir
- `Actividad X`, `Semana X`, `Nombre de la figura docente`.
- Secciones `\pendiente{...}` del reporte (encuadre y conclusión editable).
- Cualquier referencia genérica no vinculada a la actividad real.

### Errores bloqueantes
- Compilación fallida por:
  - comandos incompletos en `.tex` (p. ej., corte de archivo en presentación),
  - rutas inválidas de imágenes/logos,
  - claves `.bib` inexistentes o estilo bibliográfico mal configurado.
- Entrega sin consigna confirmada (bloqueante académico aunque compile técnicamente).

---

**Supuesto explícito:** este plan asume que la Actividad 1 se entregará como **reporte en LaTeX** y no exclusivamente como presentación. Si compartes la consigna exacta, adapto este plan a una versión operativa final (con estructura y checklist 100% alineados a la rúbrica).

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

## Extractor

- Estado: ERROR
- Manifest: `retroalimentacion-editorial/aulatex/extractor/runs/20260703-013906-extractor/manifest.json`
- Salida: `UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/extractor-aulatex`

## Compilacion

- No se compilaron archivos en este ciclo.
