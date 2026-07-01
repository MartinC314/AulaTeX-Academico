{
  "summary": [
    "Se consolida cerebro editorial minimo para Derecho financiero y bancario con enfoque transversal UnADM.",
    "Se preservan reglas estables de identidad, estructura, calidad y trazabilidad sin copiar redaccion literal del origen.",
    "Se mantiene compresion lossless por union-dedupe y control de no regresion.",
    "Se refuerza el flujo reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna o documentos locales.",
    "Tratar salidas heredadas no verificadas de motor como provisionales y auditables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de otras semanas sin confirmacion local.",
    "Adaptar profundidad y formato a la consigna real de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar trazabilidad de reglas a contexto local o memoria heredada.",
    "Bloquear campos obligatorios vacios sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar deduplicacion semantica antes de guardar memoria."
  ],
  "latex_rules": [
    "Mantener espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico.",
    "Sincronizar titulo, subtitulo y materia con la actividad real antes de entrega."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables, no contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual base.",
    "Aplicar estrategia progresiva: agregar mejoras verificables sin borrar reglas utiles previas.",
    "Mantener etiqueta de supuestos para huecos de contexto local.",
    "Si reaparece salida no estructurada, normalizar manualmente antes de nuevo ciclo."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio de la materia (supuesto: no definido).",
    "Confirmar figura docente y grupo para completar portada (supuesto: pendiente).",
    "Confirmar planeacion semanal vigente para tipificar productos por actividad.",
    "Confirmar si la localizacion de portada debe mantenerse por lineamiento institucional."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho financiero y bancario."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y calidad verificable.",
      "Asegurar coherencia entre identidad UnADM, evidencia, argumentacion y transferencia profesional."
    ],
    "style_markers": [
      "Frases precisas y orientadas a accion.",
      "Separacion explicita entre descripcion y analisis.",
      "Uso explicito de supuestos cuando falta dato.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Evaluacion critica de evidencia.",
      "Toma de postura argumentada.",
      "Conclusion transferible a practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Normalizacion estructurada"
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
          "justification": "La identidad editorial exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa valida requiere respaldo comprobable."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento y no del resumen."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar salidas no auditables o ambiguas."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "derecho-financiero-y-bancario.bib: fuentes institucionales base."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas entre memoria origen y destino.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se preservaron gates criticos: JSON parseable, supuestos, trazabilidad, dedupe.",
      "Se mantuvieron vacios locales como preguntas abiertas sin inventar fuentes."
    ]
  }
}