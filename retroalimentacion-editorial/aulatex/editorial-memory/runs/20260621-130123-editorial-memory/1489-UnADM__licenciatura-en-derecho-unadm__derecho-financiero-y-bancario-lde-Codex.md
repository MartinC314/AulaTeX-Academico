{
  "summary": [
    "Se consolida sincronizacion transversal con compresion lossless por union-dedupe.",
    "Se preservan reglas institucionales UnADM sin regresion y sin traslado literal de actividad origen.",
    "Se refuerzan abstracciones estables: identidad, estructura reusable, calidad, LaTeX y bibliografia.",
    "Se mantiene foco en JSON parseable, trazabilidad documental y supuestos marcados.",
    "Se confirma contexto destino: Derecho financiero y bancario, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene vacio local de consignas por actividad como pendiente abierto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Mantener datos curriculares verificados: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Conservar autoria y matricula solo si coinciden con .tex local vigente."
  ],
  "structure_rules": [
    "Abrir con problema juridico o social delimitado.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna.",
    "Adaptar profundidad del analisis a rubrica cuando exista."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Validar deduplicacion semantica antes de guardar.",
    "Confirmar trazabilidad de cada regla a contexto local o herencia validada.",
    "Bloquear campos obligatorios vacios si no tienen marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar documentclass y macros institucionales salvo instruccion formal.",
    "Reemplazar titulos de plantilla por datos reales de actividad antes de entrega.",
    "Completar 'Figura docente' con dato real o etiqueta [Supuesto].",
    "Resolver tokens de plantilla sin expandir en README y programa.",
    "Usar derecho-financiero-y-bancario.bib como nombre canonico del .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias ni metadatos bibliograficos.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar entradas solo con fuente consultable real.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Transferir transversalmente solo abstracciones estables, no redaccion literal.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar normalizacion manual si reaparece salida no estructurada.",
    "Mantener registro de supuestos para cierre posterior por nodo actividad."
  ],
  "open_questions": [
    "Confirmar consigna concreta de la primera actividad en esta materia.",
    "Confirmar nombre real de figura docente.",
    "Confirmar si grupo debe mostrarse en portada.",
    "Confirmar formato de citacion obligatorio (supuesto: no definido).",
    "Confirmar si localizacion de portada sigue vigente por lineamiento institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad entre README, programa, .tex y .bib.",
        "No regresion de reglas utiles."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Asegurar coherencia editorial entre identidad institucional y practica profesional."
    ],
    "style_markers": [
      "Frases directas y auditables.",
      "Supuestos marcados de forma explicita.",
      "Sin fuentes inventadas.",
      "Consistencia entre estructura, citas y conclusion."
    ],
    "argumentative_patterns": [
      "Encuadre breve del problema.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio apoyado en evidencia.",
      "Cierre con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe derivar de respaldo comprobable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y cita valida."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema orienta el hilo argumentativo."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con ejes de trabajo y proposito.",
        "derecho-financiero-y-bancario.bib con fuentes base institucionales.",
        "Historial de salidas no parseables que justifica gate de JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 21: transferidas solo abstracciones estables desde nodo no equivalente.",
      "Ciclo 21: preservada disciplina de supuestos y trazabilidad documental.",
      "Ciclo 21: reforzado control de calidad para propagacion recursiva."
    ]
  }
}