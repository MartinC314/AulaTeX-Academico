{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM, estructura base y gates de calidad sin regresion.",
    "Se refuerza normalizacion obligatoria de JSON y deduplicacion lossless por union.",
    "Se mantiene contexto local verificado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino no equivalente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Conservar trazabilidad del origen heredado y del ciclo.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Alinear cada entrega al eje: problema, conceptos o normas, evidencia, analisis propio, conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en marco conceptual o normativo, analisis y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables.",
    "Corregir placeholders o rutas corruptas en README y programa antes de reutilizar."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir conclusion juridica transferible a practica profesional.",
    "Declarar limites del analisis cuando falten datos de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Mantener clase article en espanol y formato letterpaper con oneside en plantilla actual.",
    "Conservar macros institucionales de curso, universidad y metadatos.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Usar codificacion y acentos consistentes en .tex y .bib."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar fuentes; registrar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes.",
    "Incluir metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas del origen si no fueron usadas en el destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales generales.",
    "Mantener incidente historico de JSON no parseable hasta cierre verificado.",
    "Aplicar deduplicacion semantica por union, sin recorte destructivo.",
    "Si falta contexto local de actividad, propagar reglas generales y abrir vacios."
  ],
  "open_questions": [
    "Confirmar si la incidencia JSON historica ya quedo resuelta en este ciclo.",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar correccion definitiva de placeholders Slug en README y programa.",
    "Supuesto: la planeacion oficial por actividad aun no esta incorporada al nodo materia."
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
        "Trazabilidad de herencia editorial entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Garantizar consistencia institucional, metodologica y tecnica en LaTeX.",
      "Sostener aprendizaje transferible a practica juridica."
    ],
    "style_markers": [
      "Supuestos explicitados.",
      "Separacion entre descripcion y postura propia.",
      "Cierre con criterio juridico.",
      "Citas trazables y verificables."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Bibliografia local canonica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion recursiva requiere estructura valida."
        },
        {
          "source": "JSON parseable",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Permite auditar reglas por ciclo y origen."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de una cuestion juridica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "El cierre debe estar juridicamente fundamentado."
        },
        {
          "source": "Bibliografia local canonica",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Centraliza fuentes consultadas y evita citas no trazables."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin recorte destructivo."
        }
      ],
      "evidence": [
        "README de materia con identidad UnADM y ubicacion curricular.",
        "Programa analitico con ejes editoriales reutilizables.",
        "Archivo .bib local existente y utilizable como canonico.",
        "Registro historico de incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo contenido util.",
      "Se preservaron gates institucionales de parseo y normalizacion.",
      "Se reforzo transferencia transversal por abstracciones estables.",
      "Se excluyo contenido tematico no transferible de la materia origen.",
      "Se mantuvo apertura de vacios locales con preguntas accionables."
    ]
  }
}