{
  "summary": [
    "Sincronizacion transversal consolidada en materia destino con estrategia conservadora.",
    "Se preservan reglas validas previas y se deduplican sin perdida.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se evita migrar contenido tematico exclusivo de la materia origen.",
    "Se refuerzan identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se mantiene alerta historica: salidas no parseables de Codex y GPT-Pro requieren normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Iniciar con objetivo puntual y encuadre del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias operativas.",
    "Resolver placeholders y tokens dinamicos antes de compilar o citar rutas."
  ],
  "activity_rules": [
    "Definir problema y alcance al inicio de cada actividad.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Integrar puentes entre analisis cultural y razonamiento juridico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Validar consistencia entre metadatos del documento y contexto curricular local.",
    "Validar correspondencia entre citas en texto y entradas del .bib.",
    "Verificar que no queden placeholders sin resolver en README, programa, .tex y rutas.",
    "No convertir reglas provisionales en definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base canonica.",
    "Conservar configuracion en espanol y compatibilidad de acentos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener clase article, letterpaper y oneside salvo instruccion valida.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Verificar rutas y nombres de archivo antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia en notas cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Priorizar abstracciones editoriales sobre redaccion literal.",
    "Mantener union-dedupe lossless y sin regresion en cada ciclo.",
    "Preservar alertas de parseo como conocimiento institucional reutilizable.",
    "Etiquetar como supuesto lo no confirmado en el nodo receptor.",
    "Si falta contexto local, mantener cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta estandar unico de citas para toda la licenciatura; confirmar APA u otro.",
    "Confirmar si conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o convencion local.",
    "Confirmar lineamientos de autoria y matricula por actividad para evitar arrastre de plantilla.",
    "Supuesto: reglas heredadas de salidas GPT-Pro/Codex siguen provisionales hasta validacion local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema pertinente.",
      "Conceptos y marco.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y trazables.",
      "Asegurar coherencia entre identidad institucional, argumento y evidencia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos editoriales",
        "Manejo de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay memoria reutilizable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal requiere respaldo comprobable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Manejo de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos confirmados."
        }
      ],
      "evidence": [
        "README de materia destino: identidad UnADM y pauta editorial.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial institucional: incidencias de salida no parseable en Codex y GPT-Pro."
      ]
    },
    "reinforcement_log": [
      "Ciclo 65: consolidacion transversal conservadora aplicada.",
      "Se deduplicaron reglas repetidas sin eliminar reglas utiles.",
      "Se reforzaron gates de parseo y normalizacion estructurada.",
      "Se mantuvo separacion entre contenido estable y contenido tematico no transferible.",
      "Se conservaron alertas historicas como memoria institucional activa."
    ]
  }
}