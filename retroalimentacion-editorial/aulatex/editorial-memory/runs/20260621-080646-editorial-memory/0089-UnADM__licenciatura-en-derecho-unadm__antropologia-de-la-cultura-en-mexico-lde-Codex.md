{
  "summary": [
    "Sincronizacion transversal conservadora aplicada con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM y gates de calidad vigentes.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se mantiene alerta sobre fuentes heredadas no verificadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre oficial de materia: Antropologia de la cultura en Mexico.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar secciones en: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas.",
    "Resolver placeholders y tokens dinamicos en rutas y nombres antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Integrar conceptos antropologicos y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia.",
    "Usar codificacion en español coherente en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion contraria.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres/rutas truncadas detectadas en README antes de referenciar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de activos locales cuando se cite archivo institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas ya validadas en JSON estructurado.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos disciplinares cerrados.",
    "Conservar historial de alertas de parseo como señal institucional reutilizable.",
    "Aplicar estrategia progresiva y conservadora: sumar sin regresion ni borrado util."
  ],
  "open_questions": [
    "Supuesto: falta confirmar rubrica local de evaluacion para Antropologia.",
    "Supuesto: falta confirmar formato obligatorio por actividad (reporte, presentacion u otro).",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia."
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
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Sincronizacion transversal sin contaminar contexto disciplinar local."
    ],
    "reason_for_being": [
      "Guiar productos academicos consistentes con identidad UnADM.",
      "Asegurar calidad verificable en contenido, estructura y citas.",
      "Permitir reutilizacion editorial segura entre nodos relacionados."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas y trazabilidad."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial institucional: alerta por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: se consolidan reglas estables de actividad a materia sin regresion.",
      "Ciclo 89: se refuerza gate de JSON parseable y normalizacion previa.",
      "Ciclo 89: se mantiene separacion entre abstracciones transferibles y contenido tematico local.",
      "Ciclo 89: se preserva criterio de fuentes provisionales hasta validacion disciplinar."
    ]
  }
}