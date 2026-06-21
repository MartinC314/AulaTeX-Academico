{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron transversal estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica transferible.",
    "Se conserva regla critica: bloquear propagacion si no hay JSON parseable y normalizar salidas no estructuradas.",
    "Se consolida compresion lossless por union-dedupe y politica de no regresion.",
    "Se alinea la memoria al canon local del destino: README, programa analitico y .bib de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar solo union-dedupe sin regresion."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto solicitado, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Delimitar el problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal.",
    "Distinguir hechos, conceptos, normas y opinion propia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todo .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver tokens/marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y abstractas en nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual comun.",
    "Conservar reglas locales de seguridad social como capa primaria del destino.",
    "Mantener bandera historica: ciclo 1 con salida no parseable requiere normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria del curso (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 debe figurar siempre en portada [supuesto].",
    "Confirmar nombre oficial de figura docente para plantillas de actividad [supuesto].",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto]."
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
      "Marco normativo verificable.",
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en productos juridicos verificables y utiles para practica profesional.",
      "Preservar memoria editorial persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte evidencia local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de reglas heredadas provisionales."
    ],
    "argumentative_patterns": [
      "Encuadre breve del problema.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Contraste de evidencia.",
      "Postura propia fundada.",
      "Cierre con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Normalizacion estructurada",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "La propagacion segura exige estructura valida."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Compresion union-dedupe",
          "kind": "supports",
          "justification": "Permite consolidar reglas sin perdida ni duplicados."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica debe sostenerse con fuentes trazables."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Asegura coherencia formativa y profesional del producto."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos oficiales.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo derecho-a-la-seguridad-social.bib confirma base normativa local.",
        "Historial institucional registra riesgo por salida no parseable en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Se preservaron todas las reglas utiles previas del destino.",
      "Se incorporaron solo abstracciones estables del origen transversal.",
      "Se evito transferir contenido tematico especifico de Filosofia del Derecho.",
      "Se reforzaron gates de JSON, normalizacion y control bibliografico.",
      "Se mantuvo estrategia progresiva y conservadora en ciclo 28."
    ]
  }
}