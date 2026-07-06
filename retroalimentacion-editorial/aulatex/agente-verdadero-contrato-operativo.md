# Contrato operativo del verdadero agente AulaTeX

## Proposito

Definir el contrato minimo para que AulaTeX deje de operar como una secuencia fija
de prompts y pase a operar como un agente con bucle real de observacion,
decision, accion y reevaluacion.

El principio central es este: el LLM no es el agente completo. El agente es el
controlador que observa archivos, artefactos, fallas y criterios de aceptacion;
el LLM participa como modulo cognitivo dentro de ese controlador.

## Alcance inicial

Este contrato se propone primero para nivel `actividad`, porque ahi el bucle es
mas verificable y el criterio de exito es mas concreto.

Entradas minimas del ciclo:

- memoria editorial heredada;
- base de conocimiento de investigacion;
- fuentes bibliograficas y `.bib`;
- salidas del extractor de conceptos e ideas;
- borrador o TEX de la actividad;
- resultado de compilacion y evaluacion.

## Artefacto de control

Cada corrida de agente por actividad debe persistir un archivo
`estado-agente.json` dentro de una carpeta de corrida, por ejemplo:

```text
retroalimentacion-editorial/aulatex/runs/<timestamp>-realizar-actividad/
  estado-agente.json
  observaciones.md
  decisiones.md
  evaluacion.json
  reporte-aulatex.md
```

Ese archivo es la memoria operativa del ciclo. No sustituye la memoria
editorial persistente ni la base de conocimiento; las referencia y coordina.

## Contrato exacto de estado-agente.json

```json
{
  "schema_version": 1,
  "run_id": "20260702-153045-realizar-actividad",
  "agent_mode": "activity-loop",
  "status": "running",
  "current_phase": "evaluate",
  "current_iteration": 3,
  "objective": {
    "action": "realizar-actividad",
    "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/actividad-01",
    "level": "actividad",
    "target_path": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/actividad-01",
    "activity_number": 1,
    "success_definition": [
      "Existe un borrador utilizable de la actividad.",
      "La actividad se sostiene con evidencia trazable.",
      "El TEX canonico compila.",
      "La evaluacion final no deja huecos criticos."
    ]
  },
  "inputs": {
    "editorial_memory_ref": "retroalimentacion-editorial/aulatex/editorial-memory/scopes/UnADM__licenciatura-en-derecho-unadm__filosofia-del-derecho.json",
    "knowledge_ref": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/investigacion-aulatex/base-conocimiento.json",
    "web_sources_ref": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/investigacion-aulatex/fuentes-web.md",
    "bib_ref": "UnADM/bibliografia-unadm.bib",
    "extractor_output_dir": "salidas/fichas/filosofia-del-derecho/semana-01",
    "plan_ref": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/actividad-01/plan.md",
    "working_tex_ref": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho/actividad-01/main.tex"
  },
  "observed_state": {
    "memory_ready": true,
    "knowledge_ready": true,
    "bibliography_ready": false,
    "extractor_ready": false,
    "draft_ready": false,
    "compile_ready": false,
    "evaluation_ready": false,
    "missing_artifacts": [
      "fichas_conceptos.json",
      "ideas_detectadas.json",
      "al menos 3 entradas bibliograficas utilizables"
    ],
    "detected_risks": [
      "La actividad aun no tiene cobertura conceptual verificable.",
      "La bibliografia canonica no cubre la consigna completa."
    ]
  },
  "working_memory": {
    "current_hypothesis": "La siguiente accion debe reforzar bibliografia y extractor antes de redactar.",
    "decision_rationale": [
      "Sin conceptos trazables, redactar ahora amplificaria alucinacion o relleno.",
      "Sin .bib suficiente, la trazabilidad quedaria debil desde el inicio."
    ],
    "notes": [
      "Mantener la salida del extractor ligada a la planeacion y a fuentes reales.",
      "No promover contenido no compilado a artefacto final."
    ]
  },
  "evaluators": {
    "bibliography": {
      "status": "fail",
      "threshold": "min_entries=3",
      "observed": "entries=1"
    },
    "concept_coverage": {
      "status": "fail",
      "threshold": "min_concepts=8",
      "observed": "concepts=0"
    },
    "traceability": {
      "status": "warn",
      "threshold": "claim_source_ratio>=0.80",
      "observed": "ratio=0.00"
    },
    "draft_quality": {
      "status": "pending",
      "threshold": "required_sections_complete",
      "observed": "sin borrador"
    },
    "compilation": {
      "status": "pending",
      "threshold": "latexmk_rc=0",
      "observed": "sin corrida"
    },
    "rubric": {
      "status": "pending",
      "threshold": "all_required_checks_pass",
      "observed": "sin evaluacion"
    }
  },
  "action_policy": {
    "allowed_actions": [
      "build-editorial-memory",
      "run-investigation",
      "run-extractor",
      "draft-activity",
      "revise-activity",
      "repair-bibliography",
      "repair-compilation",
      "evaluate-activity",
      "request-human-review",
      "finalize"
    ],
    "max_iterations": 8,
    "max_same_action_retries": 2,
    "max_compile_attempts": 3,
    "stop_on_destructive_action": true,
    "require_human_approval_for": [
      "overwrite-canonical-tex",
      "delete-bibliography-entries",
      "replace-approved-output"
    ]
  },
  "planned_actions": [
    {
      "priority": 1,
      "action": "repair-bibliography",
      "reason": "La bibliografia no cumple el minimo operativo.",
      "expected_artifacts": [
        "*.bib actualizado",
        "bibliography_notes consolidadas"
      ]
    },
    {
      "priority": 2,
      "action": "run-extractor",
      "reason": "Faltan conceptos e ideas trazables para la consigna.",
      "expected_artifacts": [
        "fichas_conceptos.json",
        "ideas_detectadas.json",
        "trazabilidad_fuentes.json"
      ]
    },
    {
      "priority": 3,
      "action": "draft-activity",
      "reason": "Una vez cubierta la evidencia, ya es seguro redactar."
    }
  ],
  "executed_actions": [
    {
      "iteration": 1,
      "action": "run-investigation",
      "status": "ok",
      "artifacts_created": [
        "investigacion-aulatex/base-conocimiento.json",
        "investigacion-aulatex/fuentes-web.md"
      ],
      "artifacts_updated": [
        "bibliografia-unadm.bib"
      ],
      "summary": "Se consolido la base de conocimiento, pero la bibliografia sigue insuficiente.",
      "next_hint": "Intentar reparacion bibliografica antes del extractor."
    },
    {
      "iteration": 2,
      "action": "repair-bibliography",
      "status": "partial",
      "artifacts_created": [],
      "artifacts_updated": [
        "bibliografia-unadm.bib"
      ],
      "summary": "Se anadio evidencia, pero aun no se alcanza el umbral minimo.",
      "next_hint": "Volver a investigar o incorporar fuentes locales."
    }
  ],
  "stop_criteria": {
    "complete_when": [
      "bibliography.status == pass",
      "concept_coverage.status == pass",
      "draft_quality.status == pass",
      "compilation.status == pass",
      "rubric.status == pass"
    ],
    "block_when": [
      "current_iteration >= max_iterations",
      "same_action_retries > max_same_action_retries",
      "faltan fuentes base y no hay sustituto trazable",
      "se requiere una accion con aprobacion humana"
    ]
  },
  "final_resolution": {
    "outcome": "pending",
    "message": "",
    "handoff_required": false,
    "handoff_reason": ""
  }
}
```

## Significado operativo de los campos

### Identidad de corrida

- `schema_version`: version del contrato para permitir migraciones futuras.
- `run_id`: identificador unico de la corrida.
- `agent_mode`: perfil del agente. Para el MVP debe ser `activity-loop`.
- `status`: `running`, `blocked`, `completed`, `aborted`.
- `current_phase`: `observe`, `decide`, `act`, `evaluate`, `handoff`.

### Objetivo

- `objective`: fija accion, scope y criterio de exito.
- `success_definition`: evita que el agente cierre por simple generacion textual.

### Entradas

- `inputs`: referencias a artefactos reales, no solo a texto en memoria.
- Si falta una ruta, debe registrarse como vacio observable, no ocultarse.

### Estado observado

- `observed_state`: resume disponibilidad de memoria, investigacion, extractor,
  borrador, compilacion y evaluacion.
- `missing_artifacts`: lista concreta de archivos o evidencias faltantes.
- `detected_risks`: riesgos editoriales, bibliograficos o tecnicos.

### Memoria de trabajo

- `working_memory.current_hypothesis`: hipotesis local para la siguiente accion.
- `working_memory.decision_rationale`: por que la accion actual tiene prioridad.
- `working_memory.notes`: restricciones tacticas del ciclo.

### Evaluadores

Cada evaluador debe devolver `pass`, `warn`, `fail` o `pending`.

Evaluadores minimos del MVP:

- `bibliography`
- `concept_coverage`
- `traceability`
- `draft_quality`
- `compilation`
- `rubric`

### Politica de accion

- `allowed_actions`: el repertorio legal del agente.
- `max_iterations`: cota total del bucle.
- `max_same_action_retries`: evita girar en falso.
- `require_human_approval_for`: protege acciones irreversibles.

### Plan y ejecucion

- `planned_actions`: cola priorizada calculada desde el estado observado.
- `executed_actions`: historial de iteraciones con resultado y pista del siguiente paso.

### Cierre

- `stop_criteria.complete_when`: condiciones de cierre exitoso.
- `stop_criteria.block_when`: condiciones de bloqueo o escalamiento.
- `final_resolution`: salida final de la corrida.

## Tabla de decision del agente

La politica inicial debe ser explicita y determinista. No conviene empezar con
un planificador completamente libre.

| Prioridad | Condicion observable | Accion | Artefactos esperados | Revaluacion inmediata |
| --- | --- | --- | --- | --- |
| 1 | No existe memoria editorial suficiente o falta `plan.md` | `build-editorial-memory` o `generation` | memoria consolidada, plan.md, maqueta inicial | volver a medir `memory_ready` |
| 2 | Existe memoria, pero no hay `base-conocimiento.json` o faltan consultas clave | `run-investigation` | base-conocimiento.json, fuentes-web.md, `.bib` reforzado | volver a medir `knowledge_ready` y `bibliography` |
| 3 | La bibliografia no alcanza el umbral minimo o faltan claves citables | `repair-bibliography` | `.bib` actualizado, notas bibliograficas | volver a medir `bibliography.status` |
| 4 | Faltan `fichas_conceptos`, `ideas_detectadas` o `trazabilidad_fuentes` | `run-extractor` | fichas_conceptos.*, ideas_detectadas.json, trazabilidad_fuentes.json | volver a medir `concept_coverage` y `traceability` |
| 5 | Ya hay memoria, conocimiento y conceptos, pero no existe borrador | `draft-activity` | TEX o borrador inicial de la actividad | volver a medir `draft_quality` |
| 6 | Existe borrador, pero faltan citas, estructura o correspondencia con la consigna | `revise-activity` | TEX revisado, observaciones de correccion | volver a medir `draft_quality` y `traceability` |
| 7 | El TEX existe, pero la compilacion falla | `repair-compilation` | log de compilacion, TEX corregido | volver a medir `compilation.status` |
| 8 | Compila, pero falla la rubrica editorial o academica | `evaluate-activity` y luego `revise-activity` | evaluacion.json, TEX ajustado | volver a medir `rubric.status` |
| 9 | Todas las comprobaciones pasan | `finalize` | estado final, reporte, manifest | marcar `status=completed` |
| 10 | Se agotaron iteraciones, hay bucle improductivo o falta aprobacion humana | `request-human-review` | handoff documentado | marcar `status=blocked` |

## Reglas de no regresion

- No redactar la actividad si `concept_coverage` o `bibliography` estan en `fail`.
- No cerrar corrida si `compilation` esta en `pending` o `fail`, salvo que el
  objetivo no incluya TEX compilable.
- No sobrescribir un TEX canonico aprobado sin registrar respaldo o sin cumplir
  la politica de aprobacion humana.
- No introducir bibliografia inventada para resolver huecos rapidamente.
- No promover una respuesta LLM a salida final si no hay artefactos trazables que
  la sostengan.

## Mapeo con modulos actuales de AulaTeX

- `build-editorial-memory` -> `EditorialMemoryBuilder` en
  `scripts/aulatex/editorial_memory.py`
- `run-investigation` -> `InvestigationBuilder` en
  `scripts/aulatex/investigation.py`
- `build-editorial-memory` para nodos nuevos o `generation` ->
  `ConstructionBuilder` en `scripts/aulatex/construction.py`
- `run-extractor` -> `ExtractorAdapter` en `scripts/aulatex/extractor_adapter.py`,
  que envuelve `scripts/extractor-conceptos-ideas/run.py`
- `draft-activity`, `revise-activity`, `evaluate-activity`, `repair-compilation`
  -> nueva capa supervisora sobre `scripts/aulatex/agent.py`

## Ciclos masivos con LLM

AulaTeX debe soportar dos escalas de trabajo:

- prueba corta: 1 o 2 ciclos para verificar prompts, herramientas y estado;
- corrida intensiva: 100 o mas ciclos cuando se busque consenso, refinamiento o memoria profunda.

Regla operativa:

- `stages`: `iterations` significa numero de etapas del ciclo base.
- `full`: `iterations` significa numero de ciclos completos.

En modo `full`, cada ciclo completo recorre todos los roles agenticos: planificador, investigador, arquitecto, verificador y critico. Por tanto, 100 ciclos pueden equivaler a 500 llamadas LLM antes de contar herramientas. Debe registrarse siempre:

- modo de ciclo;
- iteraciones solicitadas;
- numero real de tareas expandidas;
- motor usado;
- aceptacion o rechazo de cada salida;
- costo/riesgo cuando se mida.

Para ciclos intensivos se recomienda:

1. correr primero 1 o 2 ciclos con `--cycle-mode full`;
2. revisar manifest y workflow;
3. activar 20, 50 o 100 ciclos por lotes;
4. usar checkpoints o manifest por corrida;
5. no compilar ni extraer en todos los ciclos salvo que la politica de accion lo exija.

## Estado minimo del MVP

Se considera que AulaTeX ya tiene un verdadero agente para actividades cuando
puede hacer esto de forma repetible:

1. observar si faltan memoria, investigacion, bibliografia o conceptos;
2. decidir la siguiente accion desde reglas explicitas;
3. ejecutar una herramienta real del repositorio;
4. registrar el resultado en `estado-agente.json`;
5. reevaluar y cambiar de accion si el entorno no mejoro;
6. cerrar o escalar con una razon verificable.

Sin ese ciclo, el sistema sigue siendo una buena orquestacion editorial, pero no
un agente pleno en sentido operativo.