{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preserva identidad UnADM y normalización estructurada obligatoria.",
    "Se transfieren ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita transferencia de contenido temático específico de Filosofía del Derecho al nodo de Propiedad y Registro.",
    "Se mantiene alerta histórica: bloquear reutilización de salidas no JSON parseables."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular verificada: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S7B1 cuando corresponda.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al entregable pedido en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación en reporte o presentación según consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar que el producto final corresponda a la actividad solicitada.",
    "No asumir fuentes de semanas posteriores sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders sin resolver en entregables."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar y corregir tokens sin expandir en README y programa analítico.",
    "Completar metadatos académicos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas de cada actividad en derecho-de-la-propiedad-y-registro.bib.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar redacción literal ni contenido temático específico del origen.",
    "Reutilizar gates institucionales sin perder especificidad local del destino.",
    "Aplicar compresión por unión y deduplicación sin eliminar reglas útiles previas."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterio de evaluación.",
    "Confirmar formato exigido por actividad: reporte, presentación u otro.",
    "Confirmar estilo de citación jurídica solicitado por figura docente.",
    "Confirmar corrección final de placeholders en authortable del .tex."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Identidad institucional sólida.",
      "Razonamiento jurídico con evidencia.",
      "Transferencia profesional de conclusiones.",
      "Trazabilidad editorial y bibliográfica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar calidad jurídica, claridad argumentativa y cumplimiento institucional."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos explícitos cuando falte evidencia local.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a la conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Trazabilidad bibliográfica"
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
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
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
          "source": "Evidencia verificable",
          "target": "Trazabilidad bibliográfica",
          "kind": "develops",
          "justification": "Las citas deben corresponder con entradas reales en .bib."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Bib local con claves institucionales existentes.",
        "Histórico institucional: salidas no JSON parseables requieren normalización previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se consolidan reglas transversales estables sin transferir contenido doctrinal específico del origen.",
      "Ciclo 22: se refuerza gate crítico de parseabilidad JSON como condición de propagación.",
      "Ciclo 22: se mantiene compresión lossless por deduplicación y unión conservadora."
    ]
  }
}