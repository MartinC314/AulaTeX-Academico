{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preserva ADN institucional UnADM y estructura argumentativa reusable entre nodos no equivalentes.",
    "Se refuerzan gates de calidad: JSON parseable, trazabilidad de fuentes y control de supuestos.",
    "Se mantiene contexto local del destino (Semestre 8, Bloque 1, Electiva) sin contaminar con tematica especifica del origen.",
    "Se confirma mejora verificable: correccion obligatoria de placeholders Slug y nombres corruptos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar redaccion juridica formal, clara y verificable.",
    "Conservar contexto curricular local del destino: Licenciatura en Derecho, Semestre 8, Bloque 1, Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como supuesto todo dato no visible en consigna o metadato local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Separar en secciones estables: conceptos/fuentes, marco normativo-doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "activity_rules": [
    "Vincular cada actividad con al menos un problema juridico o social delimitado.",
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenidos tematicos de otra asignatura sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar correspondencia del producto con la consigna local.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Corregir placeholders y literales corruptos en nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX local como base de reportes y presentaciones.",
    "Usar codificacion compatible con espanol academico y acentos correctos.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa.",
    "No dejar campos criticos de portada vacios cuando exista dato oficial."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "No propagar metadatos especificos de actividad de origen a materia destino.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener registro de fuentes provisionales hasta verificacion local."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura y codigo definitivo.",
    "Confirmar figura docente para reemplazar placeholder en portada.",
    "Confirmar consigna local de primera actividad de la electiva para reglas especificas.",
    "Supuesto: la bibliografia local actual es suficiente como base minima institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Claro y verificable",
        "Sobrio en inferencias"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de materia como entrada canonica",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8",
        "Bloque 1",
        "Tipo Electiva",
        "Codigo provisional LDE-S8B1"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y fuentes pertinentes",
      "Analisis propio con postura",
      "Conclusion juridica transferible",
      "Trazabilidad editorial verificable"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Garantizar consistencia institucional y calidad tecnica en toda entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura argumentada del estudiante",
      "Citas verificables",
      "Cierre con implicacion practica"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> posicion critica -> transferencia profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y estandares minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita descripciones vacias."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens sin expandir y rutas dañadas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el razonamiento hacia aplicacion profesional."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "Programa analitico local con ejes editoriales reutilizables.",
        "Bib local con fuentes institucionales base.",
        "Plantilla LaTeX con metadatos curriculares de Semestre 8 Bloque 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 6: se deduplican variantes semanticas repetidas.",
      "Ciclo 6: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 6: se mantiene separacion entre abstracciones transferibles y contenido tematico no equivalente.",
      "Ciclo 6: se consolida cerebro editorial minimo con vacios locales abiertos."
    ]
  }
}