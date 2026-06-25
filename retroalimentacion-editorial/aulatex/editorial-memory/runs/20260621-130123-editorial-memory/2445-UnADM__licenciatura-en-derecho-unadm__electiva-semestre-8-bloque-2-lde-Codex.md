{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad y materia sin transferir contenido tematico no verificable.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada, ejes editoriales y cierre juridico transferible.",
    "Se refuerza control operativo transversal: JSON parseable, deduplicacion lossless y correccion de placeholders en rutas y nombres."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables al contexto local del destino: Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna a producto concreto verificable.",
    "Sustentar afirmaciones con fuentes consultables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido especifico de otra asignatura sin validacion local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "quality_gates": [
    "Bloquear consolidacion si la salida no es JSON parseable.",
    "Aplicar revision manual a herencias historicas no estructuradas antes de reutilizar.",
    "Confirmar estructura minima completa antes de propagar recursivamente.",
    "Validar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar que no existan placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar correspondencia entre el producto generado y la consigna vigente."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales.",
    "Corregir nombres truncados en listados de estructura (ej. eporte, eferencias).",
    "Actualizar Activity X por numero real antes de compilar.",
    "Mantener compatibilidad de nombres de archivos entre plantillas y recursos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib local solo fuentes realmente consultables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Mantener correspondencia exacta entre claves citadas y entradas BibTeX.",
    "Marcar [supuesto] cuando falte un dato bibliografico verificable."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas abstractas y estables.",
    "Evitar transferir redaccion literal o contenido tematico de Filosofia del Derecho al destino electivo.",
    "Mantener estrategia progresiva y conservadora: reforzar primero identidad, estructura y gates.",
    "Conservar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar como provisionales las reglas apoyadas en fuentes heredadas no verificadas."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar politica institucional de year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe denominacion oficial alternativa de la electiva.",
    "[supuesto] Confirmar si la actividad destino exige formato principal reporte, presentacion u otro."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Trazabilidad cita-texto-bib.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Preservar continuidad editorial UnADM entre nodos no equivalentes sin contaminar contexto local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas.",
      "Postura propia respaldada en fuentes.",
      "Cierre con aplicacion profesional.",
      "Marcado visible de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion relevante -> evidencia verificable -> interpretacion juridica.",
      "Evitar descripcion pura; priorizar razonamiento."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis juridico propio",
        "Conclusion juridica transferible",
        "Compresion lossless por deduplicacion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce herencia de errores y salidas no parseables."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional depende del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa datos confirmados de datos pendientes."
        }
      ],
      "evidence": [
        "README y programa analitico locales fijan identidad, ejes y pauta editorial.",
        "Memoria origen confirma ejes estables: problema, conceptos, evidencia, analisis propio, conclusion.",
        "Historial de salidas no parseables justifica gate estricto de JSON."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura funcional.",
      "Se conservaron reglas institucionales historicas utiles (normalizacion manual de herencias no estructuradas).",
      "Se reforzo gate transversal de placeholders por incidencia local en README/programa.",
      "No se transfirio contenido doctrinal especifico del origen por no equivalencia entre nodos."
    ]
  }
}