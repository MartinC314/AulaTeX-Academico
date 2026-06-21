{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de parseo JSON.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita trasladar contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerza marcaje de supuestos y tratamiento provisional de fuentes heredadas no verificadas.",
    "Se mantiene alerta por antecedentes de salidas no JSON parseables (Codex y GPT-Pro).",
    "Se corrigen como regla los placeholders tipo $(@{...}.Slug) a nombres literales antes de compilar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar nombre de asignatura: Antropologia de la cultura en Mexico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Estructurar en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar entregas solo descriptivas.",
    "Integrar conceptos culturales y juridicos con puente argumentativo explicito.",
    "Verificar que el producto final corresponda a la consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar.",
    "Verificar correspondencia entre metadatos de materia y documento final."
  ],
  "latex_rules": [
    "Usar codificacion en espanol con acentos correctos en .tex y .bib.",
    "Mantener clase y plantilla base salvo justificacion academica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres de archivo con caracteres truncados antes de compilar.",
    "Actualizar documenttitle y documentsubtitle por actividad sin alterar identidad institucional."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves inexistentes en el .bib local.",
    "Marcar como supuesto cualquier inferencia bibliografica no confirmada por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico especifico de otra asignatura.",
    "Mantener metodo union-dedupe lossless en cada ciclo.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si la conclusion juridica aplica a todas las actividades de antropologia o solo a productos argumentativos.",
    "[Supuesto] Confirmar estandar de citacion institucional unico para la licenciatura.",
    "[Supuesto] Confirmar si LDE-S4B2 es clave oficial institucional o clave operativa local.",
    "[Supuesto] Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "[Supuesto] Confirmar si existe bibliografia obligatoria adicional a unadmSitioWeb y unadmMallaDerecho2024."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de propagacion.",
      "Compresion lossless por deduplicacion sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Sostener coherencia institucional y calidad editorial entre nodos transversales."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con transferencia a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Supuestos explicitados",
        "Propagacion transversal conservadora"
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
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige cita y trazabilidad."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla de normalizacion y gate JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 72: se consolidan abstracciones estables de Filosofia del Derecho sin arrastre tematico.",
      "Ciclo 72: se refuerzan gates de parseo JSON y normalizacion previa.",
      "Ciclo 72: se mantiene politica de fuentes provisionales no verificadas.",
      "Ciclo 72: se refuerza resolucion de placeholders dinamicos en rutas y .bib."
    ]
  }
}