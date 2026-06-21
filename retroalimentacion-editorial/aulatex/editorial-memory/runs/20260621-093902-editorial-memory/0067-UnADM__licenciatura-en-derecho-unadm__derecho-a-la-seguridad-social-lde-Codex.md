{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no parseables sin normalizacion.",
    "Se evita transferencia tematica literal de Filosofia del Derecho hacia Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia destino como entrada canonica.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar sin regresion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Delimitar problema juridico al inicio de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Confirmar que la compresion sea lossless por union-dedupe, no por recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y editar solo campos variables.",
    "Mantener compatibilidad tecnica; evitar comandos no estandar sin justificacion.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas corruptas.",
    "Normalizar nombres de archivo con tokens sin expandir antes de usarlos como canon.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como repositorio bibliografico central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "Agregar solo fuentes consultables con metadatos minimos completos.",
    "No inventar referencias.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita LaTeX tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas generales ya validadas.",
    "Transferir abstracciones estables; no redaccion literal ni contenido tematico ajeno.",
    "Preservar reglas locales de Seguridad Social al recibir reglas transversales.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 debe figurar siempre en portada [supuesto].",
    "Validar si existen fuentes obligatorias por actividad en planeaciones no cargadas [supuesto].",
    "Confirmar datos pendientes de figura docente en plantillas [supuesto]."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco normativo y doctrinal verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Garantizar continuidad editorial entre actividades, materia y nivel institucional.",
      "Evitar perdida de reglas utiles mediante compresion lossless por deduplicacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto] cuando falte evidencia local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Seguridad social en Mexico"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicados ni recorte."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa del problema."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia editorial transversal",
          "kind": "supports",
          "justification": "Uniforma tono, formato y criterios de calidad."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y archivos base.",
        "Programa analitico destino fija proposito y ejes de trabajo.",
        "Bib local confirma base normativa e institucional verificable.",
        "Memoria origen confirma gates de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 67: se consolida transferencia transversal de reglas estables entre nodos no equivalentes.",
      "Ciclo 67: se refuerzan gates de calidad y estructura reusable sin mezclar contenido tematico de Filosofia.",
      "Ciclo 67: se mantiene politica de no regresion y compresion lossless por union-dedupe."
    ]
  }
}