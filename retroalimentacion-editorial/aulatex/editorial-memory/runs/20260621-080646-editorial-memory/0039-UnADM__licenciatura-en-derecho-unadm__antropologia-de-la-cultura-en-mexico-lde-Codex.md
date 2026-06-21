{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y estructura canonica de materia destino.",
    "Se incorporan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Se mantiene alerta de salidas no JSON parseables como gate global reutilizable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco de referencia, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener artefactos separados: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico local como guias primarias."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar conceptos antropologicos y juridicos con puente argumentativo explicito.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre metadatos de materia y documento final.",
    "Validar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base estable.",
    "Usar configuracion de espanol coherente y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion.",
    "Resolver placeholders dinamicos tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres de archivo con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni ejemplos tematicos de otra asignatura.",
    "Conservar reglas utiles previas sin eliminacion; solo agregar mejoras verificables.",
    "Registrar incidencias de parseo como alertas institucionales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad especifica; confirmar producto exacto por semana.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si toda actividad de antropologia exige conclusion juridica explicita.",
    "Confirmar si persisten placeholders en archivos adicionales no inspeccionados."
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
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles profesionalmente.",
      "Asegurar coherencia editorial transversal en la suite LaTeX UnADM."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor practico profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
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
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay memoria confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se sostiene con fuentes trazables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La utilidad profesional surge del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La norma institucional exige rigor y trazabilidad."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo .bib local con fuentes institucionales base.",
        "Memoria origen valida para abstracciones editoriales estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 39: deduplicacion integral aplicada sin perdida semantica.",
      "Ciclo 39: se reforzaron gates de JSON y normalizacion estructurada.",
      "Ciclo 39: se incorporaron patrones argumentativos transferibles desde origen.",
      "Ciclo 39: se excluyo transferencia de contenido tematico no equivalente."
    ]
  }
}