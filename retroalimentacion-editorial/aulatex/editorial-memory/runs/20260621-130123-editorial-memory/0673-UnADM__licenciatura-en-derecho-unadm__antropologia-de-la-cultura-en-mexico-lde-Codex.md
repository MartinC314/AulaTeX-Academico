{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM y estructura canonica de materia.",
    "Se integran abstracciones estables del origen: objetivo, evidencia, postura y coherencia.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho.",
    "Se mantiene alerta de salidas no JSON parseables y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de otras materias."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco teorico-normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Resolver placeholders de README y programa antes de ejecutar flujo editorial."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Mantener puente argumentativo entre dimension cultural y pertinencia juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base canonica.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en rutas y nombres de archivo.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido disciplinar especifico del origen.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Aplicar estrategia progresiva y conservadora: agregar sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas; confirmar productos exactos.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo local.",
    "Confirmar estandar de citas unico para la licenciatura.",
    "Confirmar si conclusion juridica aplica a todas las actividades de la materia.",
    "Confirmar nombre final canonico del .bib si persisten placeholders en documentos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible y juridicamente pertinente."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Sincronizacion transversal por abstracciones estables.",
      "Compresion lossless por union-dedupe sin recorte."
    ],
    "reason_for_being": [
      "Orientar productos academicos consistentes, verificables y utiles para la practica juridica.",
      "Mantener memoria editorial persistente sin regresion entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional.",
      "Trazabilidad de cada afirmacion relevante."
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
        "Separacion de artefactos editoriales"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El juicio propio se legitima con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional fija estandares de calidad."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        "Bib local confirma fuentes base institucionales verificables.",
        "Historial previo confirma gate de bloqueo por no-JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerzan gates de parseo JSON y normalizacion.",
      "Ciclo 15: se consolidan patrones argumentativos transferibles.",
      "Ciclo 15: se preserva contexto curricular local sin traslape de metadatos.",
      "Ciclo 15: se mantienen reglas de placeholders y estabilidad BibTeX."
    ]
  }
}