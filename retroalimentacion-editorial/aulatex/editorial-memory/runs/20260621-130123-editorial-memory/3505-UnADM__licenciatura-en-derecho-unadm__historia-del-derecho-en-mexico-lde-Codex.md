{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia Historia del Derecho en Mexico sin copiar contenido tematico literal.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y control de calidad parseable.",
    "Se mantiene estrategia conservadora: transferir abstracciones reusables y marcar supuestos no verificados localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de materia: Historia del Derecho en Mexico [supuesto: acentuacion pendiente de confirmacion institucional].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto solicitado, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto de planeacion semanal: reporte, presentacion o visual.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "No transferir bibliografia ni contenido tematico de otra materia sin consulta efectiva local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de cualquier propagacion recursiva.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun producto requerido.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename, coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad.",
    "Corregir placeholders de Slug en README y programa antes de compilar o citar.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar trazabilidad minima: origen y fecha de consulta cuando aplique."
  ],
  "propagation_hints": [
    "Propagar solo reglas transversales verificables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos propios de otra asignatura.",
    "Mantener alerta historica de salidas no parseables en niveles superiores.",
    "No propagar datos curriculares especificos de esta materia a otras materias."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial del nombre de materia: Mexico/México [supuesto].",
    "Confirmar si LDE-S1B1 es codigo oficial o local de plantilla.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Corregir en README los cortes de render en nombres de archivo (eporte/eferencias) [supuesto].",
    "Confirmar fuente operativa definitiva para consolidacion de memoria (Codex/GPT-Pro como historico provisional)."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral.",
      "Problema juridico con evidencia verificable.",
      "Analisis propio y cierre juridico transferible.",
      "Coherencia entre consigna y producto.",
      "Trazabilidad bibliografica y tecnica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Preservar identidad institucional sin sacrificar voz estudiantil argumentada.",
      "Garantizar reutilizacion segura por memoria estructurada y parseable."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Citas explicitas en afirmaciones sustantivas.",
      "Conclusion con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer conceptos y marco normativo/doctrinal pertinente.",
      "Contrastar evidencia con postura propia.",
      "Cerrar con conclusion juridica aplicable.",
      "Verificar correspondencia entre consigna, desarrollo y producto final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "El marco institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La integridad depende de fuentes consultables y metadatos completos."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge de razonamiento propio sustentado."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad local.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: fuentes institucionales base.",
        "Historial de ciclos: alerta persistente por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se refuerza transferencia transversal por abstracciones estables, sin copiar temas de Filosofia del Derecho.",
      "Ciclo 19: se mantiene regla dura de bloqueo por JSON no parseable.",
      "Ciclo 19: se consolida union-dedupe y no regresion en identidad, estructura y calidad."
    ]
  }
}