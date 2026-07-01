{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de origen hacia materia destino sin copiar redaccion literal.",
    "Se preserva identidad UnADM, estructura de cinco ejes y control de supuestos como reglas estables.",
    "Se refuerza compresion lossless por union-dedupe y no regresion de reglas utiles.",
    "Se mantiene incidente historico de salidas no JSON parseable hasta cierre verificado.",
    "Se crea cerebro editorial minimo completo para la materia con vacios locales declarados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular la materia a Licenciatura en Derecho, semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad del origen transversal: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas previas utiles; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Diferenciar con claridad descripcion, analisis y toma de postura.",
    "Declarar limites del analisis cuando falten datos de actividad.",
    "No asumir fuentes de otras semanas sin evidencia de pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna y producto entregado.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol, letterpaper y oneside salvo justificacion.",
    "Conservar macros institucionales de curso, autor y universidad.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad real.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir en README y programa los placeholders tipo $(@{...}.Slug).",
    "Corregir nombres corruptos de archivos en README (supuesto: saltos iniciales en reporte/referencias)."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No trasladar citas del nodo origen si no fueron usadas en destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o referencias no verificadas.",
    "Mantener union-dedupe lossless y evitar regresiones.",
    "Conservar etiqueta provisional del incidente JSON hasta resolucion confirmada."
  ],
  "open_questions": [
    "Supuesto: falta planeacion oficial detallada por actividad de esta materia.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar si ya quedo resuelto el incidente historico de salida no JSON parseable.",
    "Confirmar correccion definitiva de rutas/nombres corruptos en README y programa."
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
        "Trazabilidad de herencias editoriales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos evaluables con fundamento juridico y criterio propio.",
      "Asegurar consistencia institucional, verificabilidad y utilidad profesional."
    ],
    "style_markers": [
      "Frases directas y secciones funcionales.",
      "Supuestos etiquetados de forma explicita.",
      "Cierre con aplicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura propia sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad academica",
        "Trazabilidad editorial",
        "Normalizacion JSON"
      ],
      "citations": [
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se construye sobre un problema delimitado."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite reutilizacion segura y auditable."
        },
        {
          "source": "Ejes de trabajo de 5 pasos",
          "target": "Derecho de la contratacion internacional",
          "kind": "develops",
          "justification": "Patron reusable transversal aplicable a materias juridicas no equivalentes."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: existencia de repositorio base verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas entre origen y destino sin perdida semantica.",
      "Se mantuvieron reglas institucionales estables y se excluyeron contenidos tematicos no transferibles del origen.",
      "Se reforzo gate de JSON parseable por incidente historico activo.",
      "Se anclo el grafo conceptual a evidencias locales del destino."
    ]
  }
}