{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de otra materia hacia materia destino.",
    "Se preservan reglas institucionales estables y se evita arrastre de contenido tematico no laboral.",
    "Se mantiene normalizacion obligatoria de salidas no parseables antes de propagacion.",
    "Se refuerza esquema reusable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica.",
    "Se consolida union-dedupe lossless sin eliminar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular del destino: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir etiquetas curriculares del origen cuando no correspondan al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener estructura minima completa antes de reutilizar o propagar."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en una pregunta guia verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas o materias distintas sin validacion de pertinencia.",
    "Vincular conceptos laborales con aplicacion profesional comprobable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir rutas o nombres mal renderizados antes de canonizarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia de materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no transversal.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades concretas de la materia destino; confirmar producto exacto por semana.",
    "Confirmar rubrica oficial para convertir criterios en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente (APA, ISO 690 u otro).",
    "Confirmar si el autor de plantilla es fijo institucional o variable por alumno.",
    "Confirmar normalizacion final de nombres con artefactos de plantilla en README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia transversal.",
        "Explicito al marcar supuestos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia trazable y verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar consistencia institucional, trazabilidad de fuentes y calidad editorial reproducible.",
      "Permitir sincronizacion transversal sin perder especificidad local de la materia."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Sin duplicados semanticos.",
      "Supuestos marcados de forma explicita.",
      "Sin fuentes inventadas.",
      "Sin copia literal entre nodos transversales."
    ],
    "argumentative_patterns": [
      "Abrir con problema y objetivo puntual.",
      "Desarrollar conceptos y marco normativo/doctrinal.",
      "Contrastar evidencia y sostener postura propia.",
      "Cerrar con conclusion juridica aplicable.",
      "Verificar coherencia entre pregunta, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico laboral",
        "Marco normativo y doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable",
        "Trazabilidad de citas",
        "Propagacion recursiva conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad de citas",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica verificable."
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
          "justification": "La conclusion profesional requiere sustento juridico verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva conservadora",
          "kind": "depends_on",
          "justification": "No se reutiliza memoria no estructurada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva conservadora",
          "kind": "supports",
          "justification": "Reduce regresiones y mantiene consistencia entre nodos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura academica se fortalece con fuentes trazables."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "Bibliografia local: claves institucionales base disponibles en .bib.",
        "Antecedentes de salidas no parseables: regla activa de normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Se reforzo gate de JSON parseable como condicion de propagacion recursiva.",
      "Se reforzo esquema argumentativo reusable sin arrastrar contenido tematico del origen.",
      "Se reforzo manejo de supuestos y fuentes provisionales no verificadas.",
      "Se reforzo control de tokens de plantilla sin expandir en nombres y rutas.",
      "Se mantuvo compresion lossless por union-dedupe sin recorte."
    ]
  }
}