{
  "summary": [
    "Se consolida sincronización transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva ADN UnADM y se refuerzan ejes comunes: problema, conceptos, evidencia, análisis y conclusión jurídica.",
    "Se mantiene política de normalización obligatoria para salidas no JSON parseables.",
    "Se aplica compresión lossless por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular verificada: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre pregunta guía, desarrollo y conclusión."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Relacionar el análisis con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validar consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar resolución de placeholders y tokens sin expandir."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Conservar clase y metadatos base salvo instrucción local distinta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas con caracteres anómalos antes de compilar.",
    "Completar campos pendientes en authortable antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar fuentes específicas de actividad en derecho-de-la-propiedad-y-registro.bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y no ambiguas.",
    "Transferir solo abstracciones editoriales estables entre nodos transversales.",
    "Evitar trasladar redacción literal o contenido temático específico de Filosofía del Derecho.",
    "Mantener estrategia progresiva y conservadora sin eliminar reglas útiles previas.",
    "Si falta contexto local, conservar núcleo mínimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterios de evaluación.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar estilo de citación jurídica requerido por figura docente.",
    "Confirmar corrección final de nombres de archivo afectados por tokens corruptos.",
    "Confirmar figura docente para sustituir placeholder en portada."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Problema jurídico relevante.",
      "Marco conceptual y normativo suficiente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos claros, verificables y transferibles.",
      "Asegurar coherencia entre identidad institucional, método argumentativo y evidencia."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explícitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad, rigor y formato consistente."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La estructura parseable evita pérdida y ambigüedad en propagación."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento verificable."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia texto-.bib respalda verificabilidad."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento argumentado."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Archivo .bib local: claves institucionales activas.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se deduplican reglas repetidas y se preservan todas las útiles.",
      "Ciclo 4: se incorporan abstracciones estables desde actividad transversal sin arrastre temático literal.",
      "Ciclo 4: se refuerza gate de normalización para antecedentes no estructurados.",
      "Ciclo 4: se mantiene compatibilidad con estrategia progresiva y conservadora."
    ]
  }
}