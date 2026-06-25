{
  "summary": [
    "Se consolida sincronizacion transversal hacia Garantias constitucionales con estrategia conservadora.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se bloquea transferencia de contenido disciplinar de Filosofia del Derecho por no equivalencia de nodo.",
    "Se refuerza normalizacion obligatoria cuando existan salidas no estructuradas o no parseables.",
    "Se confirma contexto local destino: semestre 2, bloque 1, obligatoria, 8 creditos [verificado en README]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local del destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar contenido disciplinar de Filosofia del Derecho sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders y nombres truncados en README o programa antes de operar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Ajustar el producto al tipo de entrega solicitado por actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib local.",
    "Verificar congruencia entre portada, metadatos y datos curriculares del destino.",
    "Compilar LaTeX sin errores criticos ni referencias rotas antes de entrega."
  ],
  "latex_rules": [
    "Conservar plantilla local de la materia y no introducir paquetes sin necesidad verificable.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Completar campos de portada pendientes antes de entrega.",
    "Corregir truncamiento detectado en macro de portada del reporte local [verificado en archivo .tex].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar nombres de archivo locales verificados al referenciar artefactos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Agregar identificador, emisor y fecha para normas juridicas cuando se citen.",
    "Mantener trazabilidad entre cita en texto y entrada bibliografica local.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico de otra materia.",
    "Mantener union-dedupe y politica sin regresion en cada ciclo.",
    "Etiquetar ciclos con herencia no estructurada para normalizacion manual.",
    "Conservar alerta institucional historica sobre salidas no parseables."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantias constitucionales.",
    "Confirmar nombre de figura docente en plantilla.",
    "Confirmar estilo de citacion requerido (APA, juridico mexicano u otro).",
    "Confirmar si la fecha debe ir automatica con \\today o fija por entrega.",
    "Confirmar que todos los placeholders de Slug en README/programa queden reemplazados.",
    "Confirmar cierre completo de la macro de portada truncada en reporte-garantias-constitucionales.tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Marcado explicito de supuestos.",
        "Separacion entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion transferible.",
      "Consistencia cita-texto-bib.",
      "Control de calidad previo a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Sostener una memoria editorial persistente, estable y reutilizable entre actividades.",
      "Reducir riesgo de regresion mediante union-dedupe y validaciones estructurales."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Sin duplicados.",
      "Sin contenido inventado.",
      "Supuestos etiquetados.",
      "Cierre con aplicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> objetivo puntual -> marco normativo/doctrinal -> analisis propio -> conclusion aplicada.",
      "Cada afirmacion relevante debe tener sustento verificable o marca de supuesto.",
      "Separar con claridad descripcion, fundamentacion y postura personal."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Transferencia transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion confiable."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta juridica definida."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia cita-texto-bib",
          "kind": "supports",
          "justification": "La integridad academica exige trazabilidad documental."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Es condicion tecnica minima de reutilizacion."
        }
      ],
      "evidence": [
        "README de Garantias constitucionales con datos curriculares verificados.",
        "Programa analitico con ejes editoriales reutilizables.",
        "garantias-constitucionales.bib con base institucional existente.",
        "Truncamiento visible en reporte-garantias-constitucionales.tex [supuesto de correccion pendiente].",
        "Historial institucional de salidas no parseables heredadas (Codex/GPT-Pro)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicadas reglas repetidas de origen y destino sin perdida semantica.",
      "Ciclo 6: reforzada prohibicion de transferir contenido disciplinar entre materias no equivalentes.",
      "Ciclo 6: reforzado gate de JSON parseable y normalizacion previa.",
      "Ciclo 6: incorporada verificacion local de placeholders Slug y truncamientos de plantilla.",
      "Ciclo 6: mantenida politica de no regresion y compresion lossless por union-dedupe."
    ]
  }
}