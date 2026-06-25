{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad no equivalente hacia materia destino.",
    "Se preservan reglas institucionales UnADM y normalizacion estructurada previa a propagacion.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo por salida no JSON parseable y necesidad de normalizacion manual en ciclos heredados.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos en README/programa.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre reporte, presentacion y bibliografia de la materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin validacion local.",
    "Agregar fuentes especificas de cada actividad al .bib de la materia.",
    "Conectar conclusion con aplicacion practica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo, lateral o ascendente.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar que rutas y archivos listados en README existan.",
    "Corregir artefactos de nombres truncados en README [supuesto].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre completo de entornos LaTeX en reporte principal [supuesto]."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes a la actividad.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "No citar fuentes no agregadas al .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar contenido doctrinal especifico entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora sin regresiones.",
    "Aplicar normalizacion manual en ciclos con antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica local de la primera actividad de la materia destino.",
    "Confirmar si documentauthor de plantilla debe parametrizarse por actividad [supuesto].",
    "Confirmar valor final del Slug y corregir tokens no expandidos en README/programa.",
    "Confirmar si year=2026 en unadmSitioWeb se usa como año bibliografico o fecha de consulta.",
    "Confirmar integridad del archivo de reporte por posible truncamiento observado [supuesto]."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Asegurar consistencia editorial entre identidad institucional, argumentacion y evidencia.",
      "Permitir propagacion segura por memoria estructurada y validada."
    ],
    "style_markers": [
      "Frases directas y trazables.",
      "Sin afirmaciones sin fuente.",
      "Supuestos etiquetados.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte del criterio personal.",
      "Coherencia entre pregunta guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define tono, formato y estandar de calidad."
        },
        {
          "source": "Estructura de entregables",
          "target": "Transferencia profesional",
          "kind": "develops",
          "justification": "Ordena el razonamiento hacia aplicacion practica."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves institucionales.",
        "Memoria origen validada por deduplicacion y filtrado transversal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se reforzo identidad y gates sin mover contexto curricular local.",
      "Ciclo 10: se incorporo patron argumentativo reusable y no literal.",
      "Ciclo 10: se mantuvo alerta de placeholders y posible truncamiento LaTeX [supuesto].",
      "Ciclo 10: se excluyo transferencia doctrinal especifica de Filosofia del Derecho."
    ]
  }
}