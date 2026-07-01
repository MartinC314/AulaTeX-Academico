{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad y materia con abstracciones estables.",
    "Se preserva identidad UnADM y marco curricular local del destino sin mezclar asignaturas.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva gate critico: no propagar insumos no parseables sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Conservar autoria y matricula en portada cuando aplique.",
    "No mezclar identidad ni contenido curricular de otras carreras o materias.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar carpeta de materia como entrada canonica para plantillas y referencias."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Registrar supuestos operativos cuando falten instrucciones.",
    "Agregar fuentes especificas de cada actividad al .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion recursiva.",
    "Validar estructura minima completa del esquema editorial.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y nombres de archivos existan en el repositorio local."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener documentclass article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Conservar macros de metadatos academicos y portada.",
    "No compilar con placeholders o tokens sin expandir.",
    "Corregir nombres rotos en README y programa analitico antes de referenciarlos.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al encargo local.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Mantener claves BibTeX estables para evitar rupturas en compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y deduplicadas.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico local de otra asignatura.",
    "Mantener bandera de normalizacion manual para ciclos con insumos no estructurados.",
    "Evitar regresiones: conservar toda regla util previa."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen pendientes; confirmar en malla curricular.",
    "Supuesto: nombre oficial final de la electiva sigue pendiente; confirmar en malla.",
    "Confirmar figura docente para portada base.",
    "Corregir placeholders residuales en README y programa analitico.",
    "Confirmar politica local para year vs fecha de consulta en fuentes web institucionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Normalizacion obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producto alineado a planeacion semanal.",
        "Supuesto: creditos oficiales pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Asegurar transferencia profesional mediante cierre argumentativo util."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Separacion explicita entre descripcion, analisis y cierre.",
      "Supuestos etiquetados cuando falta evidencia.",
      "Consistencia formal entre portada, contenido y bibliografia."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Delimitar conceptos y norma aplicable.",
      "Sustentar con evidencia citada.",
      "Contrastar y fijar postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Normalizacion manual",
        "Planeacion semanal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion manual",
          "kind": "contrasts",
          "justification": "Si no hay parseo valido, se activa normalizacion manual."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis parte de un caso o tension concreta."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento sustentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige trazabilidad de fuentes y rigor formal."
        },
        {
          "source": "Planeacion semanal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "El producto final debe responder a la consigna y cerrar con aplicacion practica."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves base institucionales.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas.",
      "Ciclo 2: incorporado gate transversal de parseo JSON como obligatorio.",
      "Ciclo 2: reforzada separacion entre abstraccion transferible y contenido tematico local.",
      "Ciclo 2: mantenida compresion lossless sin recorte de reglas utiles."
    ]
  }
}