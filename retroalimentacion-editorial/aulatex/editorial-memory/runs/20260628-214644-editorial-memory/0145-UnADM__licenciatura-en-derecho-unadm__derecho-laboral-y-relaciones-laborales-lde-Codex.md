{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM y ejes editoriales transferibles entre materias.",
    "Se refuerza normalizacion obligatoria de salidas no parseables antes de propagacion.",
    "Se mantiene enfoque juridico-laboral del destino sin copiar redaccion literal del origen.",
    "Se crea ADN editorial minimo reconstructible para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular del destino: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Tomar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social laboral.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en una pregunta guia verificable.",
    "Sustentar afirmaciones con fuentes trazables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar traslado automatico de contenido de otras materias sin validacion de pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo de afirmaciones o marca explicita de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizacion."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base por actividad.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Resolver marcadores sin expandir en rutas y nombres de archivo.",
    "Completar metadatos reales de actividad y autor antes de compilar.",
    "Compilar sin errores criticos, referencias rotas ni entornos truncados."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URL.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL; marcar faltantes como supuesto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar deduplicacion semantica por frases cortas y accionables."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad en Derecho laboral y relaciones laborales.",
    "Confirmar formato de citacion exigido por docente (supuesto: no especificado).",
    "Confirmar si el autor de plantilla es fijo o variable por alumno.",
    "Confirmar nombres canonicos finales de artefactos en README tras corregir marcadores.",
    "Confirmar fuentes obligatorias por unidad para poblar el .bib local."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables academicos verificables.",
      "Asegurar fundamento juridico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial sin perder pertinencia local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explicitos cuando falte evidencia local.",
      "Sin redaccion literal heredada entre materias.",
      "Sin fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio con contraste de fuentes.",
      "Cierre con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico laboral",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Trazabilidad de citas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial local exige ambos elementos en cada actividad."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se organiza desde una pregunta guia contextualizada."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere sustento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga memoria no parseable."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, citas verificables, conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "Bibliografia local: claves institucionales base ya disponibles."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas del origen y destino sin recorte funcional.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se reforzo gate de JSON parseable y normalizacion previa.",
      "Se inicializo ADN editorial del destino con grafo conceptual minimo."
    ]
  }
}