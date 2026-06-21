{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerzan ejes estables reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla de normalizacion estructurada obligatoria antes de propagacion.",
    "Se agrega control explicito de tokens sin expandir en README y programa analitico como incidencia tecnica local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los entregables.",
    "Conservar contexto curricular del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "No mezclar metadatos curriculares del nodo origen con el destino.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canonica.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas para la actividad en curso.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar cambios aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar correspondencia entre consigna de actividad y producto entregado.",
    "Verificar presencia de tokens sin expandir en README y programa analitico antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Compilar sin errores criticos, referencias rotas ni entornos truncados.",
    "Conservar nombres de archivo locales salvo normalizacion editorial acordada.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar rutas y nombres con caracteres anómalos antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Validar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Evitar traslado de contenido tematico especifico de Filosofia del Derecho al destino.",
    "Preservar reglas utiles previas y deduplicar sin perdida semantica.",
    "No propagar supuestos como reglas definitivas.",
    "Aplicar propagacion recursiva solo tras validar JSON y gates de calidad."
  ],
  "open_questions": [
    "Confirmar criterio final de normalizacion ortografica en nombres de archivo y metadatos (publico/publico).",
    "Confirmar si la materia requiere plantilla adicional para producto visual distinto de reporte/presentacion.",
    "Confirmar si se corrigen de inmediato los tokens Slug sin expandir en README y programa analitico.",
    "Supuesto: la consigna local de cada actividad seguira variando por semana y se resolvera en nodos de actividad."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Consigna valida estructura del entregable.",
      "Evidencia verificable sostiene la conclusion juridica.",
      "Analisis propio es obligatorio en toda actividad.",
      "Calidad tecnica y calidad argumentativa se validan juntas."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos claros, verificables y transferibles.",
      "Sostener continuidad editorial entre nodos sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Control de tokens sin expandir"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El tipo de producto define forma y profundidad del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion solo es valida si esta sustentada documentalmente."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de tokens sin expandir",
          "kind": "develops",
          "justification": "Ambos son gates tecnicos para propagacion y compilacion seguras."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y claves inexistentes."
        }
      ],
      "evidence": [
        "README destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales verificadas.",
        "Incidencia local: presencia de token $(@{...}.Slug) sin expandir."
      ]
    },
    "reinforcement_log": [
      "Ciclo 63: se consolidan reglas transversales estables sin mover contenido tematico del origen.",
      "Ciclo 63: se refuerza gate de JSON parseable y normalizacion previa a propagacion.",
      "Ciclo 63: se agrega control tecnico de tokens sin expandir como mejora verificable local."
    ]
  }
}