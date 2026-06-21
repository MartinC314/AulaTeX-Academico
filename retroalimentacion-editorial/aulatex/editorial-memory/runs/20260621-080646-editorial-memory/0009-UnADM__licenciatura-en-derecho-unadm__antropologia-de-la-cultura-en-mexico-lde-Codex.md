{
  "summary": [
    "Sincronizacion transversal ciclo 9 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reutilizable y gates de calidad.",
    "Se transfieren solo abstracciones editoriales entre nodos no equivalentes.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantiene alerta por salidas no JSON parseable como riesgo operativo transversal.",
    "Se refuerza resolucion de placeholders y tokens dinamicos en README, programa y rutas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar fuentes de otras semanas o materias sin justificacion.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones o marcarlas como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y configuracion base salvo justificacion academica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Verificar y corregir rutas con caracteres truncados antes de compilar.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales de archivo."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener como base local: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Transferir solo abstracciones editoriales estables entre materias transversales.",
    "Etiquetar supuestos y provisionalidad en cada salto lateral.",
    "Preservar reglas utiles previas; aplicar solo union-dedupe sin recorte.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materia.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Antropologia; confirmar formatos por semana.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o solo local.",
    "Confirmar si toda actividad exige conclusion juridica explicita en esta materia.",
    "Confirmar politica final para placeholders en README y programa."
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
      "Normalizacion estructurada antes de propagar.",
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables y argumentados.",
      "Asegurar coherencia institucional y calidad transversal entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Transferencia transversal por abstracciones estables"
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
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Transferencia transversal por abstracciones estables",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite sincronizar sin contaminar contenido tematico local."
        }
      ],
      "evidence": [
        "README destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes de trabajo y proposito.",
        ".bib local: fuentes base institucionales verificables.",
        "Memoria origen: gates de parseo JSON y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolidan reglas estables sin eliminar reglas utiles previas.",
      "Ciclo 9: se refuerzan gates JSON y normalizacion manual para salidas no estructuradas.",
      "Ciclo 9: se preserva separacion entre abstraccion editorial y contenido disciplinar especifico.",
      "Ciclo 9: se mantiene alerta de fuentes heredadas provisionales hasta validacion local."
    ]
  }
}