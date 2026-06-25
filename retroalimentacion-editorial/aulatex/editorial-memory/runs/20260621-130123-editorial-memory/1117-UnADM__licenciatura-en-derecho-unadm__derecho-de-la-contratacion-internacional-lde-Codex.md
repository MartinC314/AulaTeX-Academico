{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad no equivalente con transferencia solo de abstracciones estables.",
    "Se preserva identidad UnADM, integridad academica y trazabilidad de herencia sin regresion.",
    "Se mantiene compresion lossless por union-dedupe y normalizacion estructurada obligatoria.",
    "Se refuerza el esquema reusable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica.",
    "Se conserva incidente historico de salidas no JSON parseables como gate activo hasta verificacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto local semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en consigna o planeacion.",
    "Conservar trazabilidad del origen heredado y etiquetar fuentes no verificadas como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, evidencia, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No transferir redaccion literal entre nodos; solo patrones editoriales."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca [Supuesto].",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar correspondencia entre nombres de archivos en README y archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside segun plantilla local.",
    "Conservar macros institucionales de curso, universidad y metadatos.",
    "Completar documenttitle y documentsubtitle con actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Corregir placeholders tipo $(@{...}.Slug) en README y programa antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio canonico local.",
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes a la actividad.",
    "Agregar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas si no fueron consultadas en la actividad destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y gates de calidad.",
    "Mantener estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles.",
    "Priorizar transferencia de identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar propagar rutas corruptas o placeholders sin normalizacion previa.",
    "Conservar incidente historico JSON como alerta activa hasta cierre verificado."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si la incidencia de salida no JSON parseable ya fue resuelta en este ciclo.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar consigna oficial por actividad para ajustar profundidad y evidencias.",
    "Confirmar correccion definitiva de entradas corruptas y placeholders en README/programa."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencia entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico que activa la actividad.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar consistencia editorial y tecnica en toda la materia.",
      "Permitir reutilizacion segura de memoria por reglas estables y verificables."
    ],
    "style_markers": [
      "Supuestos explicitados cuando falte informacion.",
      "Separacion clara entre descripcion y postura propia.",
      "Cierre con criterio juridico transferible.",
      "Sincronizacion transversal por abstracciones, no por copia textual."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica"
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
          "justification": "El marco institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "JSON valido permite reutilizacion segura entre ciclos y nodos."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura argumentativa parte de una cuestion juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe derivar de norma, doctrina y evidencia."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Se conserva contenido util sin recorte destructivo ni ambiguedad."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo reutilizables.",
        "Bib local: repositorio canonico con fuentes institucionales.",
        "Historial de incidentes: salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se preservo cobertura semantica completa.",
      "Se transfirieron solo abstracciones estables desde Filosofia del Derecho.",
      "Se mantuvieron gates institucionales de JSON, estructura y verificacion de fuentes.",
      "Se reforzo ADN argumentativo comun sin contaminar con contenido tematico no local."
    ]
  }
}