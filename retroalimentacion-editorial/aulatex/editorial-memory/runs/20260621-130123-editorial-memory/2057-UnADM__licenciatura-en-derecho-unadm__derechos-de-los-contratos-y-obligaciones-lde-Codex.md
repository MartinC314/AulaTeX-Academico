{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Contratos y Obligaciones.",
    "Se preserva el nucleo estable UnADM: identidad institucional, estructura por ejes y cierre juridico con criterio propio.",
    "Se refuerza control tecnico: normalizacion obligatoria de salidas no estructuradas y bloqueo sin JSON parseable.",
    "Se mantiene transferencia por abstracciones estables, sin copiar contenido tematico de otra materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares confirmados del destino: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque disciplinar en contratos y obligaciones.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "Distinguir bibliografia base de fuentes especificas por actividad.",
    "No trasladar contenido literal de Filosofia del Derecho; adaptar al contexto contractual.",
    "Confirmar formato del producto por actividad cuando la consigna no sea visible [supuesto]."
  ],
  "quality_gates": [
    "Bloquear persistencia y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar toda herencia no estructurada antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Actualizar documenttitle y documentsubtitle al producto real antes de compilar.",
    "Verificar codificacion en español y caracteres validos en rutas y nombres.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "Usar como .bib canonico local: derechos-de-los-contratos-y-obligaciones.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Separar bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables.",
    "Excluir metadatos especificos cuando el nodo destino no comparta contexto curricular.",
    "Aplicar compatibilidad disciplinar antes de propagacion lateral.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Registrar cada refuerzo en log para evitar regresiones en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion juridica obligatoria en esta materia.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar alcance de fuentes por actividad: federales, locales o mixtas.",
    "Confirmar si el autor por defecto debe mantenerse sin cambios [supuesto]."
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
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de los contratos y obligaciones."
      ]
    },
    "essence": [
      "Modelo de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
      "Normalizacion estructurada como condicion de memoria valida.",
      "Transferencia transversal por abstracciones estables, no por texto literal."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos trazables y verificables.",
      "Sostener continuidad editorial entre nodos sin perder especificidad disciplinar."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y auditables.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema delimitado.",
      "Marco conceptual-normativo pertinente.",
      "Analisis propio con evidencia.",
      "Conclusion juridica operativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas comprobables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La memoria solo se propaga cuando el formato es valido."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El razonamiento parte de una pregunta delimitada."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del argumento sustentado."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "supports",
          "justification": "Son ejes disciplinares vinculados en la materia destino."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo transversales.",
        "Archivo .bib local: entradas institucionales base verificables.",
        "Regla tecnica vigente: resolver placeholders $(@{...}.Slug) en rutas y nombres."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 9: se reforzo gate de JSON parseable como condicion dura de propagacion.",
      "Ciclo 9: se transfirieron patrones argumentativos estables sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 9: se mantuvo enfoque contractual del destino con compatibilidad transversal."
    ]
  }
}