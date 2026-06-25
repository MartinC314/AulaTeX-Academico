{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas utiles del destino y se refuerzan abstracciones estables del origen.",
    "Se mantiene normalizacion obligatoria para salidas no parseables antes de reutilizar o propagar.",
    "Se consolidan ejes editoriales comunes: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho no pertinente a Derecho laboral."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto solicitado con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en un conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenidos de otras materias sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver marcadores de plantilla sin expandir en nombres de archivo.",
    "Completar entornos truncados de la plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar fuentes en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Priorizar identidad, gates de calidad y grafo conceptual sobre redaccion literal."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades especificas de la materia destino.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de citacion juridica exigido por docente.",
    "Confirmar si el autor de plantilla es fijo institucional o variable por alumno.",
    "Confirmar canon final de nombres de artefactos y carpeta de referencias."
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
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico laboral delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio con postura academica.",
      "Evidencia trazable y citas consistentes.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos estructurados y verificables.",
      "Asegurar coherencia entre consigna, evidencia y conclusion juridica.",
      "Sostener continuidad editorial transversal sin perder identidad local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin contenido inventado.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas no parseables",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La integridad academica institucional exige citas verificables."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La argumentacion requiere delimitacion previa del caso."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento normativo."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida evita perdida de evidencia y citas."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura razonada conduce al cierre aplicado."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial UnADM.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo .bib local con claves institucionales verificables.",
        "Antecedentes de salidas no parseables que justifican gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se refuerza normalizacion previa a propagacion recursiva.",
      "Ciclo 10: se transfiere estructura argumentativa estable sin arrastrar contenido disciplinar ajeno.",
      "Ciclo 10: se consolida gate de no inventar fuentes y trazabilidad cita-.bib.",
      "Ciclo 10: se preserva union-dedupe lossless sin eliminar reglas utiles previas."
    ]
  }
}