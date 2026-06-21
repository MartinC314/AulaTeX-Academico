{
  "summary": [
    "Sincronizacion transversal consolidada entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control institucional de normalizacion: no propagar salidas no parseables.",
    "Compresion aplicada como union-dedupe lossless, sin recorte y sin regresion de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y evidencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; incluir argumentacion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar no regresion: conservar reglas utiles previas del destino."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos, citas rotas ni referencias faltantes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivo y resolver marcadores o tokens no expandidos antes de compilar.",
    "No copiar bloques LaTeX completos en memoria editorial; guardar solo reglas reutilizables."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central de la materia.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar correspondencia uno a uno entre clave citada y entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas generales estables, no redaccion literal ni contenido tematico local.",
    "Propagar recursivamente solo despues de validar JSON, estructura y gates de calidad.",
    "Priorizar identidad, estructura reusable y control de calidad sobre detalles de una actividad especifica.",
    "Mantener trazabilidad de reglas provisionales heredadas con etiqueta [supuesto].",
    "Si falta contexto local en subnodos, crear cerebro minimo con identidad, estructura y gates.",
    "Aplicar estrategia conservadora: reforzar lo valido existente antes de agregar reglas nuevas."
  ],
  "open_questions": [
    "Confirmar si la materia exige norma de citacion juridica especifica adicional [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los artefactos [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto].",
    "Confirmar criterio institucional para manejo de datos personales en portadas [supuesto]."
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
      "Problema juridico bien delimitado.",
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y transferibles.",
      "Preservar continuidad editorial entre actividades, formatos y ciclos.",
      "Asegurar calidad tecnica y academica antes de toda propagacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiquetado de [supuesto] cuando falte evidencia local.",
      "Trazabilidad de decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe lossless",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control bibliografico"
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe lossless",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicar ni recortar contenido valido."
        },
        {
          "source": "Control bibliografico",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las citas comprobables sostienen afirmaciones academicas."
        }
      ],
      "evidence": [
        "README de materia destino con estructura canonica.",
        "Programa analitico destino con proposito y ejes de trabajo.",
        "Archivo .bib local con claves normativas vigentes.",
        "Regla institucional heredada: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 68: se refuerza transferencia transversal de reglas estables sin contaminar contenido tematico.",
      "Ciclo 68: se preservan gates criticos de JSON parseable y normalizacion previa.",
      "Ciclo 68: se consolida patron argumentativo comun reutilizable en actividades de Derecho.",
      "Ciclo 68: se mantiene compresion lossless por deduplicacion y no por recorte."
    ]
  }
}