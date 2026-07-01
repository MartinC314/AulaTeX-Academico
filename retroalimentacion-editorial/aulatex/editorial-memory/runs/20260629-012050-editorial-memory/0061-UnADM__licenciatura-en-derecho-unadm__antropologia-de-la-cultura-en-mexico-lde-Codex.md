{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, ejes editoriales y gates de calidad ya validados.",
    "Se incorporan solo abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "No se transfieren contenidos tematicos exclusivos de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de materias no equivalentes."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion de artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias estructurales primarias."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar automaticamente fuentes o consignas de semanas o materias distintas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente toda respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas antes de compilar.",
    "Corregir rutas con caracteres truncados o anomalias de nombre de archivo."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia destino.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes del .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico de la materia origen.",
    "Mantener compresion lossless por deduplicacion, sin recorte semantico.",
    "Conservar alertas historicas de parseo como control transversal reutilizable.",
    "Estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: falta consigna local concreta por actividad en el destino; confirmar productos exigidos por semana.",
    "Confirmar estandar unico de citacion aplicable a la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o solo operacional local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades antropologicas.",
    "Confirmar cierre definitivo de placeholders dinamicos en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Sensible al contexto cultural mexicano."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica.",
        "Uso explicito de supuestos cuando falte evidencia local."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible a la practica juridica.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar coherencia entre identidad institucional, rigor argumentativo y verificabilidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Afirmaciones respaldadas por fuentes.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
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
        "Supuestos marcados",
        "Sincronizacion transversal conservadora"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad requiere respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio personal gana solidez con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento."
        },
        {
          "source": "Supuestos marcados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita presentar inferencias no verificadas como hechos."
        }
      ],
      "evidence": [
        "README destino: pauta de identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico destino: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local destino: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de bloquear salidas no JSON parseable.",
        "Memoria origen: objetivo puntual, postura propia y sustento verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicadas reglas repetidas de identidad, estructura, actividad y gates.",
      "Ciclo 2: retenidas alertas de parseo no estructurado como control transversal persistente.",
      "Ciclo 2: transferidas solo abstracciones estables; excluidos contenidos doctrinales especificos de Filosofia del Derecho.",
      "Ciclo 2: reforzada regla de no regresion y no eliminacion de normas utiles previas."
    ]
  }
}