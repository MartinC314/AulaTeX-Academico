{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho hacia Antropologia.",
    "Se evita migrar contenido tematico propio de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion de placeholders y rutas antes de compilar o propagar.",
    "Se mantiene trazabilidad de fuentes heredadas como provisionales hasta verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable.",
    "Resolver tokens dinamicos en nombres de archivo antes de uso."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a practica juridica cuando la consigna lo pida.",
    "Evitar extrapolar fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla de la materia.",
    "Mantener metadatos institucionales completos y consistentes.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias faltantes.",
    "Corregir caracteres truncados en rutas y nombres de archivo.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y rutas .bib/.tex.",
    "No introducir comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia cuando se usen archivos locales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido disciplinar ajeno.",
    "Conservar alertas historicas de parseo como controles transversales reutilizables.",
    "Aplicar estrategia conservadora: agregar mejoras verificables sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna especifica de actividades locales de Antropologia; confirmar formatos requeridos.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar estandar de citacion oficial para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave institucional fija o convencion local.",
    "Confirmar politica final para placeholders dinamicos en archivos maestros."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Normalizacion estructurada antes de propagar.",
      "Compresion lossless por union-dedupe sin recorte.",
      "Supuestos explicitos cuando falte contexto."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Sostener coherencia institucional y calidad tecnica en LaTeX y BibTeX.",
      "Permitir sincronizacion transversal sin contaminar identidad disciplinar local."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y reutilizables.",
      "Citas trazables en cada afirmacion clave.",
      "Cierre con valor academico-profesional."
    ],
    "argumentative_patterns": [
      "Problema contextual -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia verificable -> interpretacion.",
      "Consigna -> desarrollo alineado -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Propagacion conservadora transversal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana validez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion conservadora transversal",
          "kind": "supports",
          "justification": "La identidad comun permite reglas estables entre materias."
        }
      ],
      "evidence": [
        "README destino confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico destino define ejes de trabajo reutilizables.",
        "Bib local contiene fuentes base institucionales verificables.",
        "Historial heredado registra incidencia de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion completa de reglas repetidas y preservacion de reglas utiles previas.",
      "Ciclo 19: refuerzo de gates JSON/estructura como precondicion de propagacion recursiva.",
      "Ciclo 19: transferencia limitada a abstracciones estables; sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 19: refuerzo tecnico de resolucion de placeholders y estabilidad BibTeX/LaTeX."
    ]
  }
}