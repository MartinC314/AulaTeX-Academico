{
  "summary": [
    "Se sincroniza ADN editorial transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preservan reglas utiles del destino y se aplica union-dedupe lossless.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto: JSON parseable y normalizacion previa a propagacion.",
    "Se confirma README y programa analitico como canon local de la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver tokens sin expandir antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias; marcar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables en ciclos tempranos.",
    "Aplicar sincronizacion transversal de forma progresiva y conservadora.",
    "Evitar regresiones: toda regla util previa debe permanecer."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial o solo etiqueta operativa [supuesto].",
    "Confirmar datos faltantes de figura docente para portada [supuesto].",
    "Confirmar si hay rubrica especifica por actividad en planeaciones locales [supuesto]."
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
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas en productos juridicos verificables.",
      "Sostener toda entrega en problema, fundamento, evidencia, analisis y cierre.",
      "Preservar memoria editorial con compresion lossless por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables evaluables y trazables.",
      "Asegurar calidad formal, argumentativa y bibliografica en cada actividad.",
      "Permitir propagacion segura de reglas editoriales entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con utilidad juridica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico delimitado",
        "Marco normativo y doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
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
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion focalizada."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige sustento comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion lossless requiere estructura valida."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica local.",
        "Programa analitico define proposito y ejes de trabajo del destino.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Regla persistente: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 93: se preservan reglas previas sin recorte.",
      "Ciclo 93: se transfieren solo abstracciones estables por relacion transversal.",
      "Ciclo 93: se refuerzan quality gates y trazabilidad de supuestos.",
      "Ciclo 93: se evita contaminacion tematica entre materias no equivalentes."
    ]
  }
}