{
  "summary": [
    "Se mantiene cerebro editorial de materia con identidad UnADM y contexto curricular local verificado.",
    "Se incorpora transferencia transversal estable desde actividad origen: normalizacion estructurada obligatoria y eje argumentativo de cinco pasos.",
    "Se conserva estrategia conservadora: no trasladar contenido tematico propio de Filosofia del Derecho al curso de Derecho Internacional Publico.",
    "Se refuerza control de calidad por parseo JSON, consistencia cita-bibliografia y marcado explicito de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Alinear metadatos curriculares al destino: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional.",
    "Marcar como [Supuesto] todo dato no visible en consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre el formato final al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas para la actividad vigente.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos.",
    "Corregir nombres de archivo con caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, generales y verificadas.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "No propagar contenido tematico de materias no equivalentes; solo abstracciones editoriales.",
    "Conservar incidencias historicas de salida no estructurada como alertas de proceso.",
    "No convertir supuestos en reglas definitivas sin verificacion local."
  ],
  "open_questions": [
    "[Supuesto] Confirmar criterio oficial de acentuacion en nombre de la materia (publico/publico).",
    "Confirmar y corregir tokens Slug sin expandir en README y programa analitico.",
    "Confirmar reparacion completa del entorno tabular truncado en reporte .tex.",
    "Confirmar rubrica local por actividad para ajustar profundidad argumentativa.",
    "Confirmar si cada actividad requiere .bib propio o uso acumulativo del .bib de materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar metadatos curriculares con materias origen."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y profesionalmente utiles.",
      "Asegurar consistencia institucional y trazabilidad editorial en toda la materia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        }
      ],
      "evidence": [
        "README de materia destino.",
        "Programa analitico de materia destino.",
        "Archivo .bib local con claves institucionales.",
        "Memoria origen: regla de normalizacion estructurada y eje editorial de cinco pasos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 28: se transfiere solo abstraccion estable desde actividad origen.",
      "Ciclo 28: se deduplican reglas repetidas y se conserva contenido util previo sin regresion.",
      "Ciclo 28: se refuerzan gates de parseo JSON, supuestos etiquetados y coherencia cita-.bib.",
      "Ciclo 28: se mantienen vacios locales abiertos donde falta consigna o rubrica especifica."
    ]
  }
}