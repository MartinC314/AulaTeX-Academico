# Prototipo cerrado de Actividad 1 agentica

## 1. Objetivo del prototipo

Aterrizar el enfoque de ingeniería inversa agentica de AulaTeX en una prueba cerrada: lograr que una Actividad 1 pueda generarse, repararse o validarse mediante flujo de agentes, no por lógica manual.

El prototipo debe probar el ciclo:

```text
extractor -> realizador -> evaluador -> memoria -> extractor
```

Pero con límites estrictos por etapa, contrato objetivo verificable y matriz de pruebas antes de escalar a materia, carrera o institución.

## 2. Principio de diseño

No se empieza diseñando agentes. Se empieza definiendo el resultado esperado.

```text
resultado esperado -> contrato verificable -> componentes -> agentes -> bucles -> memoria -> validación
```

La Actividad 1 existente no debe tratarse solo como ejemplo. Debe convertirse en especificación inicial de diseño.

## 3. Contrato objetivo de Actividad 1

### 3.1 Muestra base

Reunir entre 10 y 20 actividades 1 consideradas correctas dentro del workspace.

Fuentes candidatas:

- `reporte-*-Actividad-1.tex`
- PDFs correspondientes;
- planeaciones asociadas;
- `.bib` canónico de cada materia;
- memoria editorial de actividad 1 cuando exista.

### 3.2 Atributos observables

Cada actividad correcta debe descomponerse en:

| Atributo | Tipo | Descripción |
| --- | --- | --- |
| objetivo_pedagogico | obligatorio | Qué aprendizaje busca activar. |
| tipo_actividad | obligatorio | Mapa, cuadro, ensayo, estudio de caso, glosario, reporte, presentación. |
| estructura | obligatorio/configurable | Secciones mínimas y orden esperado. |
| dificultad | configurable | Baja, media, alta según carga conceptual y evidencias. |
| tono | configurable | Académico, jurídico, reflexivo, técnico, institucional. |
| formato_salida | obligatorio | TEX, PDF, presentación, mapa, tabla, etc. |
| restricciones_didacticas | obligatorio | Técnica didáctica y reglas de entrega. |
| criterios_evaluacion | obligatorio | Rúbrica, checklist, ponderación o criterios de aceptación. |
| bibliografia_minima | obligatorio | Fuentes o tipos de fuente requeridos. |
| trazabilidad | obligatorio | Relación entre afirmaciones, citas y fuentes. |
| cierre_argumentativo | obligatorio | Conclusión propia o transferencia profesional. |

### 3.3 Regla de obligatoriedad

- Si un atributo cambia la utilidad pedagógica, es obligatorio.
- Si solo afecta estilo o presentación, es configurable.
- Si los ejemplos correctos no coinciden, no se convierte todavía en regla fija.

### 3.4 Contrato JSON inicial

```json
{
  "activity_kind": "actividad-1",
  "required": {
    "objective": true,
    "instruction_source": true,
    "didactic_technique": true,
    "output_format": true,
    "bibliography": true,
    "traceability": true,
    "evaluation_criteria": true,
    "final_reflection": true
  },
  "acceptable_ranges": {
    "sections_min": 3,
    "sections_max": 8,
    "bibliography_entries_min": 3,
    "concepts_min": 5,
    "critical_errors_max": 0,
    "manual_corrections_max": 2
  },
  "flexible": {
    "tone": ["academico", "juridico", "reflexivo"],
    "visual_product": ["mapa", "cuadro", "tabla", "diagrama", "ninguno"],
    "extension": "segun planeacion"
  }
}
```

## 4. Mapa de componentes existentes

| Componente | Estado | Reutilización | Observación |
| --- | --- | --- | --- |
| `ExtractorAdapter` | existente | reutilizable con adaptación | Ya resuelve fuentes, planeación y artefactos; falta bucle de cobertura. |
| `scripts/extractor-conceptos-ideas/run.py` | existente | reutilizable sin cambios iniciales | Motor funcional de fichas; puede encapsularse. |
| `AulaTeXAgent` | existente | reutilizable con adaptación | Ejecuta roles LLM y herramientas; falta estado por actividad. |
| `EditorialMemoryBuilder` | existente | reutilizable con adaptación | Memoria fuerte, pero todavía editorial más que operativa. |
| `EditorialMemoryStore` | existente | reutilizable con adaptación | Debe separar memoria estable, evidencia y ejecución. |
| `ConstructionBuilder` | existente | reutilizable con adaptación | Útil si la actividad o materia no existe; no realiza actividad final. |
| `EditorialConsensusEngine` | existente | reemplazable o complementable | Útil como señal general; no basta para evaluar actividad. |
| `workspace.compile_tex` | existente | reutilizable sin cambios | Herramienta clara de compilación. |
| `activity_observer.py` | inexistente | necesario | Debe observar TEX, PDF, citas, `.bib`, extractor y pendientes. |
| `activity_evaluator.py` | inexistente | necesario | Debe emitir evaluación estructurada. |
| `activity_agent_state.py` | inexistente | necesario | Debe persistir `estado-agente.json`. |

## 5. Preguntas de clasificación por componente

Cada componente debe evaluarse así:

| Pregunta | Criterio |
| --- | --- |
| ¿Recibe entradas estructuradas? | Si no, necesita adaptador. |
| ¿Produce salidas consistentes? | Si no, necesita normalizador. |
| ¿Permite iteración? | Si no, necesita bucle externo. |
| ¿Expone señales útiles para evaluación o memoria? | Si no, necesita manifest enriquecido. |

Decisión:

- reutilizar primero lo que ya produce resultados correctos;
- adaptar lo que tenga trazabilidad;
- reemplazar solo lo que dependa de intervención manual o lógica implícita;
- no rediseñar todo el workspace antes de validar Actividad 1.

## 6. Flujo mínimo secuencial con bucles acotados

### 6.1 Orden inicial

```text
1. Extractor
2. Realizador
3. Evaluador
4. Memoria
```

### 6.2 Límites por etapa

| Etapa | Iteraciones iniciales | Salida | Condición de reintento |
| --- | ---: | --- | --- |
| Extractor | 2 | fichas + conceptos + trazabilidad | Cobertura conceptual baja o planeación mal interpretada. |
| Realizador | 2-3 | TEX candidato o parche | Estructura incompleta, citas mal usadas, baja claridad. |
| Evaluador | 1 | `evaluacion.json` + score | Normalmente no reintenta; emite dictamen. |
| Memoria | 1 | memoria de ciclo + memoria reusable candidata | Solo consolida lo accionable. |

### 6.3 Regla de retorno

- Falla crítica de contexto -> volver al extractor.
- Falla de ejecución textual -> volver al realizador.
- Falla bibliográfica -> activar reparador bibliográfico antes de realizador.
- Falla de compilación -> activar compilador/reparador.
- Falla menor -> parche puntual, no regeneración completa.

### 6.4 Detención

Detener cuando:

- score supera umbral;
- no hay errores críticos;
- la mejora marginal entre iteraciones es baja;
- se alcanza máximo de ciclos;
- falta información humana indispensable.

## 7. Memoria secuencial útil

La memoria no debe ser historial genérico. Debe servir para corrección.

### 7.1 Bloques de memoria

```json
{
  "contexto_persistente": {
    "materia": "",
    "nivel": "",
    "objetivo": "",
    "restricciones": []
  },
  "decisiones_tomadas": [
    {
      "decision": "",
      "razon": "",
      "evidencia": "",
      "aceptada": true
    }
  ],
  "errores_detectados": [
    {
      "tipo": "",
      "severidad": "",
      "causa_probable": "",
      "intervencion_recomendada": ""
    }
  ],
  "correcciones_efectivas": [
    {
      "accion": "",
      "mejora_score": 0,
      "regla_reutilizable": ""
    }
  ]
}
```

### 7.2 Memoria de corto plazo

Vive solo dentro del ciclo de la actividad.

Contiene:

- última versión aceptable;
- errores actuales;
- decisiones pendientes;
- observaciones del evaluador;
- siguiente acción.

### 7.3 Memoria reusable

Solo se consolida si:

- la corrección funcionó;
- el patrón aplica a más de una actividad;
- mejora score sin empeorar legibilidad o utilidad pedagógica;
- tiene evidencia trazable.

No se guarda:

- opinión sin acción;
- preferencia estilística aislada;
- corrección que solo aplica a un caso único;
- salida LLM sin verificación.

## 8. Matriz de validación

No se debe escalar a materia, carrera o institución hasta validar Actividad 1 en casos variados.

### 8.1 Casos de prueba

| Caso | Descripción | Objetivo |
| --- | --- | --- |
| A1-FD | Filosofía del Derecho Actividad 1 | Reparar claves antiguas y validar mapa conceptual. |
| A1-materia-con-bib | Actividad 1 con `.bib` completo | Validar flujo estándar. |
| A1-materia-sin-bib | Actividad 1 con bibliografía incompleta | Probar reparador bibliográfico. |
| A1-planeacion-pdf | Planeación solo en PDF | Probar parser/extractor. |
| A1-formato-visual | Actividad 1 con mapa/cuadro | Probar contrato de producto visual. |
| A1-entrada-incompleta | Falta rúbrica o consigna parcial | Probar solicitud de revisión humana. |
| A1-caso-limite | Texto con placeholders o citas rotas | Probar evaluador y corrección. |

### 8.2 Métricas mínimas

| Métrica | Umbral inicial |
| --- | ---: |
| Aceptación sin corrección manual | >= 80% |
| Ciclos promedio por actividad | <= 2 |
| Errores críticos no detectados | 0 |
| Claves BibTeX faltantes al cierre | 0 |
| Placeholders activos al cierre | 0 |
| Compilación exitosa | >= 90% |
| Mejora por memoria reutilizable | medible en al menos 2 casos |
| Costo/tiempo por actividad | registrado, no necesariamente optimizado al inicio |

### 8.3 Puerta de escalamiento

Solo escalar a materia si:

```text
aceptacion >= 80%
ciclos_promedio <= 2
errores_criticos_controlados = true
memoria_mejora_resultados = true
```

Si falla:

- falla de consistencia -> mejorar extractor y contrato;
- falla de calidad de salida -> mejorar realizador;
- falla de detección -> mejorar evaluador;
- errores repetidos -> mejorar memoria.

## 9. Validación inicial con Filosofía del Derecho Actividad 1

### 9.1 Estado observado

La Actividad 1 actual existe y tiene PDF, pero usa claves antiguas que no coinciden con `filosofia-del-derecho.bib`.

Ejemplos:

- `finnis_estudios_2017` -> probable `finnisEstudiosTeoriaDerecho2017`
- `lovon_manual_2020` -> probable `lovonManualPracticoFilosofia2020`
- `ruiz_rodriguez_filosofia_derecho_2009` -> probable `ruizrodriguezFilosofiaDerecho2009`
- `rojas_gonzalez_filosofia_derecho_2018` -> probable `rojas-gonzalezFilosofiaDerecho2018`

### 9.2 Primera prueba sin modificar archivos

Generar solamente:

```text
estado-agente.json
evaluacion.json
acciones-recomendadas.md
```

Debe detectar:

- `bibliography_ready = false`
- `draft_ready = true`
- `compile_ready = unknown`
- `next_action = repair-bibliography`

### 9.3 Resultado de la primera ejecución monitoreada

Ejecución:

```powershell
.\scripts\aulatex.ps1 activity-observe --target .\UnADM\licenciatura-en-derecho-unadm\filosofia-del-derecho-lde --activity 1
```

Salida generada:

```text
retroalimentacion-editorial/aulatex/activity-observer/runs/20260703-113746-activity-01-observer/
  estado-agente.json
  evaluacion.json
  acciones-recomendadas.md
```

Resultado observado:

```json
{
  "bibliography_ready": false,
  "draft_ready": true,
  "extractor_ready": false,
  "compile_ready": "unknown",
  "next_action": "repair-bibliography",
  "score": 71.43
}
```

La ejecución confirma la hipótesis inicial: la Actividad 1 no necesita reescritura completa como primera acción; necesita reparación bibliográfica controlada.

### 9.4 Segunda prueba con reparación controlada

Aplicar cambios mínimos en una copia o rama de prueba:

1. migrar claves antiguas;
2. compilar;
3. evaluar;
4. actualizar memoria con regla reutilizable:

```text
Si actividad antigua usa claves con snake_case, buscar equivalentes camelCase o canónicos en .bib antes de regenerar contenido.
```

Resultado ejecutado:

```powershell
.\scripts\aulatex.ps1 bibliography-repair --target .\UnADM\licenciatura-en-derecho-unadm\filosofia-del-derecho-lde --activity 1 --apply
```

Artefactos:

```text
retroalimentacion-editorial/aulatex/bibliography-repair/runs/20260703-121030-activity-01-bib-repair/
  plan-reparacion-bibliografia.json
  reporte-reparacion-bibliografia.md
  manifest.json
```

Resultado:

```json
{
  "missing_bib_keys": [],
  "bibliography_ready": true,
  "compile_ready": false,
  "next_action": "repair-compilation",
  "compile_failure_category": "tex-environment-missing-class"
}
```

La reparación bibliográfica cerró correctamente la primera falla crítica. El siguiente bloqueo ya no es bibliográfico: es de entorno/compilación, específicamente falta `article.cls` en la distribución TeX activa.

## 10. Decisión final de diseño

El mayor acierto no será tener muchos agentes, sino que cada etapa tenga:

- responsabilidad clara;
- entradas exactas;
- salidas exactas;
- métricas propias;
- memoria accionable;
- condición de reintento;
- criterio de cierre.

El prototipo de Actividad 1 debe demostrar eso antes de ampliar AulaTeX al resto del workspace.
