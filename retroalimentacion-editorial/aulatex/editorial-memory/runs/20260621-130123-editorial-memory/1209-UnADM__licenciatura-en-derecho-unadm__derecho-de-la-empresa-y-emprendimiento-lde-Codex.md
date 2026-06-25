{
  "summary": [
    "Se conserva memoria institucional UnADM y compresion por union-dedupe sin recorte.",
    "Se transfiere solo marco editorial estable desde actividad origen a materia destino.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla de normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Supuesto: no se transfiere doctrina especifica de Filosofia del Derecho por no equivalencia disciplinar."
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
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar al .bib local solo fuentes realmente consultables.",
    "No asumir fuentes de semanas o materias distintas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de generar entregables."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar que nombres de archivos referenciados existan y no tengan artefactos de salto.",
    "Supuesto: el reporte local esta truncado; confirmar cierre de entornos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas aplicables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "No citar fuentes ausentes del .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base hasta nueva consigna."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar contenido doctrinal especifico entre materias no equivalentes.",
    "Propagar primero gates de calidad y reglas de identidad.",
    "Aplicar normalizacion manual cuando haya salidas no estructuradas heredadas.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar si el autor de portada debe parametrizarse por actividad.",
    "Confirmar valor final del Slug en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb es año bibliografico o solo fecha de consulta.",
    "Confirmar estado real del archivo de reporte y cierre completo de entornos LaTeX.",
    "Supuesto: falta consigna local de actividad especifica para ajustar profundidad y formato final."
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
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y aplicables.",
      "Asegurar consistencia institucional, tecnica y argumentativa en toda la materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Sin afirmaciones sin fuente.",
      "Supuestos etiquetados.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Marco normativo y doctrinal como soporte del criterio personal.",
      "Coherencia entre pregunta guia y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos",
        "Tokens Slug sin expandir"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Define tono y estandar de cierre profesional."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio personal requiere respaldo trazable."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos confirmados."
        },
        {
          "source": "Tokens Slug sin expandir",
          "target": "Calidad de entregables",
          "kind": "depends_on",
          "justification": "Los placeholders rompen rutas y consistencia documental."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local.",
        "Memoria origen de actividad con ejes editoriales estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza transferencia transversal de reglas estables sin arrastrar contenido doctrinal especifico.",
      "Ciclo 17: se preservan gates de parseo JSON, normalizacion y no regresion.",
      "Ciclo 17: se mantiene alerta tecnica por Slug sin expandir y posible truncamiento LaTeX."
    ]
  }
}