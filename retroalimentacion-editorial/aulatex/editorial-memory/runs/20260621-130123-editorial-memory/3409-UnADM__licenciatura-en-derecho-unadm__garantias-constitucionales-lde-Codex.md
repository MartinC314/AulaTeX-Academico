{
  "summary": [
    "Se sincroniza memoria transversal desde actividad no equivalente con estrategia conservadora.",
    "Se preservan reglas estables de identidad, estructura, calidad, LaTeX y bibliografía.",
    "Se mantiene compresión lossless por unión y deduplicación sin regresión.",
    "Se refuerza que la transferencia es editorial, no disciplinar.",
    "Se conserva alerta institucional: bloquear propagación si no hay JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No transferir contenido disciplinar de Filosofía del Derecho a Garantías Constitucionales sin validación expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir hechos, normas, doctrina y opinión propia.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliográfico.",
    "Verificar correspondencia del producto con la consigna específica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Compilar sin errores críticos y sin referencias rotas.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No introducir paquetes nuevos sin necesidad editorial o técnica verificable.",
    "Resolver placeholders o tokens sin expandir en README, programa analítico y rutas.",
    "Verificar cierre completo de macros de portada antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar identificador, emisor y fecha cuando se citen normas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales validadas.",
    "Evitar propagar contenido temático entre materias no equivalentes.",
    "Conservar trazabilidad de supuestos y de fuentes provisionales por ciclo.",
    "Mantener alertas institucionales de calidad aunque cambie la asignatura.",
    "Si falta contexto local, crear cerebro editorial mínimo y abrir vacíos explícitos.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de la primera actividad de Garantías Constitucionales.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar estilo de citación exigido en la materia (APA, jurídico mexicano u otro).",
    "Confirmar figura docente en plantilla LaTeX.",
    "Confirmar corrección total de truncamientos en README y portada .tex.",
    "Confirmar si la fecha debe ser automática o fija por entrega."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Marcado explícito de [Supuesto].",
        "Separación entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantías Constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Marco conceptual y normativo verificable.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Consistencia cita-texto-bibliografía.",
      "Propagación segura basada en estructura."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Sostener calidad editorial transversal sin contaminar contenido disciplinar.",
      "Garantizar continuidad institucional del nodo como memoria persistente."
    ],
    "style_markers": [
      "Frases cortas, verificables y accionables.",
      "Primero problema, luego sustento, después postura.",
      "Cierre con aplicabilidad jurídica concreta.",
      "Supuestos visibles cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial delimitado.",
      "Marco normativo o doctrinal pertinente.",
      "Contraste de fuentes y criterio propio.",
      "Conclusión operativa para práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "JSON parseable",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-texto-bib",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "Sin formato válido no hay propagación confiable."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa parte de un conflicto definido."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La aplicabilidad jurídica exige sustento verificable."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y errores de trazabilidad."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "No transferencia disciplinar automática",
          "kind": "develops",
          "justification": "Se comparten patrones editoriales estables entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de Garantías Constitucionales con ubicación curricular y pauta editorial.",
        "Programa analítico con ejes: problema, conceptos/fuentes, producto, análisis, conclusión.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Historial institucional: respuestas no estructuradas requieren normalización previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se deduplican reglas repetidas y se preserva todo patrón útil previo.",
      "Ciclo 17: se refuerza gate de JSON parseable como condición dura de propagación.",
      "Ciclo 17: se mantiene separación entre abstracción editorial y contenido disciplinar.",
      "Ciclo 17: se consolida grafo conceptual mínimo reusable para propagación recursiva."
    ]
  }
}