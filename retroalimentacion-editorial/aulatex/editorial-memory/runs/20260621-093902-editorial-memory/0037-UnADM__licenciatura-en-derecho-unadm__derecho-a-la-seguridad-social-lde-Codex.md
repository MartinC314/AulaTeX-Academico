{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva compresion lossless por union-dedupe sin regresion.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato al producto solicitado en la planeacion semanal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, conceptos y opinion propia.",
    "No asumir fuentes de otras semanas sin validacion local.",
    "Relacionar cada actividad con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base y personalizar solo campos variables.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres o rutas con marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar referencias.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar correspondencia entre cada cita LaTeX y una entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y estables.",
    "Compartir abstracciones editoriales; no transferir redaccion literal.",
    "Mantener reglas curriculares especificas dentro de la materia destino.",
    "Reutilizar gates de JSON parseable y normalizacion en nodos laterales compatibles.",
    "Mantener bandera de riesgo historica por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar vigencia de cualquier fuente provisional heredada externa al campo juridico [supuesto].",
    "Confirmar si todas las actividades usan reporte, presentacion o ambos formatos.",
    "Confirmar rubrica oficial de evaluacion para granularidad argumentativa."
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
      "Problema juridico delimitado.",
      "Marco normativo y conceptual pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para practica profesional.",
      "Preservar consistencia editorial entre reporte, presentacion y programa analitico.",
      "Garantizar trazabilidad, verificabilidad y propagacion segura."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion visible entre marco, analisis y cierre.",
      "Etiquetado explicito de [supuesto].",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia argumentada.",
      "Concluir con implicacion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
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
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis necesita una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida se funda en normas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Evita afirmaciones infundadas."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin regresion."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y archivos base.",
        "Programa analitico fija proposito y ejes de trabajo de seguridad social.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial previo confirma necesidad de gate JSON parseable y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 37: se consolidan reglas transversales estables sin mezclar contenido tematico de origen.",
      "Ciclo 37: se refuerzan gates de calidad y trazabilidad de supuestos.",
      "Ciclo 37: se mantiene estrategia conservadora de union-dedupe sin recorte."
    ]
  }
}