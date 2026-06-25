{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia Historia del Derecho en Mexico sin mover contenido tematico especifico.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion JSON y trazabilidad bibliografica.",
    "Se refuerza estrategia conservadora: union-dedupe lossless, sin recorte de reglas utiles previas.",
    "Se mantiene alerta historica por salidas no JSON parseables y bloqueo de propagacion hasta normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre de materia local: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders de Slug y errores de render en listados antes de automatizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar solo conceptos y fuentes pertinentes al problema planteado.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna.",
    "No transferir contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del esquema editorial antes de propagar.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Verificar correspondencia entre consigna y producto final."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex y presentacion-historia-del-derecho-en-mexico.tex como bases segun tipo de entrega.",
    "Conservar metadatos: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores verificables.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Conservar entradas institucionales existentes y su trazabilidad.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir nota de origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva en la materia destino."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables: identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar datos curriculares especificos a nodos laterales no equivalentes.",
    "Reutilizar modelo de cinco ejes con ajuste tematico por asignatura.",
    "Mantener alerta de salidas no parseables en niveles superiores y laterales.",
    "Ejecutar propagacion recursiva solo tras validar JSON y estructura minima."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial del nombre de materia: Mexico/México [supuesto].",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Corregir en README los cortes anomalos de render en nombres de archivo [supuesto].",
    "Confirmar fuente operativa definitiva para reemplazar etiquetas provisionales de motor."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto conforme a planeacion.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible.",
      "Control estricto de estructura y verificabilidad."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y verificables.",
      "Sostener continuidad editorial entre actividades y materias sin contaminar tematicas.",
      "Preservar memoria institucional util para propagacion recursiva segura."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Citas explicitas.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer conceptos y marco normativo/doctrinal.",
      "Contrastar evidencia con postura propia.",
      "Concluir con implicacion practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalizacion JSON",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor de cita y formato verificable."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de metadatos completos y fuentes consultables."
        }
      ],
      "evidence": [
        "README de materia y programa analitico local.",
        "historia-del-derecho-en-mexico.bib con entradas institucionales.",
        "Plantillas .tex locales de reporte y presentacion.",
        "Memoria origen: cinco ejes, normalizacion estructurada y gates de calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se transfiere solo abstraccion editorial estable desde nodo no equivalente.",
      "Ciclo 8: se conserva regla de bloqueo por JSON no parseable.",
      "Ciclo 8: se refuerza union-dedupe lossless sin regresion.",
      "Ciclo 8: se mantiene separacion entre reglas transversales y contenido tematico local."
    ]
  }
}