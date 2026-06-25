{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada y ejes editoriales juridicos.",
    "Se deduplican reglas repetidas sin recorte semantico y sin regresion.",
    "Se refuerza control de supuestos y trazabilidad cita-texto-bib.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable.",
    "Se fija cerebro editorial minimo reutilizable para actividades futuras de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar tono academico-juridico claro, preciso y argumentativo.",
    "Fijar autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Usar codigo de curso LDE-S8B2 en metadatos del reporte.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre el producto final con la consigna semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Transformar planeacion semanal en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido tematico especifico de otra materia sin validacion local.",
    "No asumir fuentes de semanas posteriores como obligatorias para actividades iniciales.",
    "Confirmar que el producto corresponda a la consigna de la actividad vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar coherencia de nombres de archivo entre documentos y carpeta real."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Conservar plantilla base reporte-electiva-semestre-8-bloque-2.tex.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) en nombres de archivo y referencias.",
    "Corregir nombres truncados en listados de estructura."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Distinguir bibliografia base institucional de bibliografia especifica por actividad.",
    "Marcar [supuesto] cuando falte dato bibliografico verificable."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico local no verificable.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Conservar etiqueta de herencia provisional hasta revision manual.",
    "Usar ciclo 1 y 2 como referencias de normalizacion manual obligatoria.",
    "Propagar recursivamente solo despues de validar JSON y estructura."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional de year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si el año 2026 del sitio UnADM requiere actualizacion.",
    "[supuesto] Confirmar plantilla final de producto por actividad (reporte/presentacion)."
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
        "Normalizacion estructurada antes de propagar.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Asegurar coherencia entre consigna, argumentacion y cierre profesional.",
      "Preservar memoria editorial reutilizable sin contaminar con supuestos no marcados."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito.",
      "Secciones ordenadas y funcionales.",
      "Postura propia sustentada.",
      "Cierre aplicable a practica juridica.",
      "Marcado visible de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Evitar descripcion pura; priorizar juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Problema juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Trazabilidad cita-texto-bib"
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
          "justification": "Evita heredar salidas no parseables y errores de forma."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad requiere correspondencia explicita entre evidencia y afirmacion."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La transferencia profesional depende del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Reduce afirmaciones impropias y separa datos confirmados de pendientes."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bib local: claves institucionales base.",
        "Historial: salidas no JSON parseables requieren normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 14: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 14: se mantiene politica de no inventar fuentes y marcar [supuesto].",
      "Ciclo 14: se refuerza gate de placeholders/tokens sin expandir.",
      "Ciclo 14: sin regresion de reglas utiles heredadas."
    ]
  }
}