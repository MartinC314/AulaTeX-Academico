{
  "summary": [
    "Se consolida sincronizacion transversal con reglas estables entre actividad y materia sin mover contenido tematico especifico.",
    "Se preserva identidad UnADM y encuadre local de Derecho semestre 7 bloque 2 electiva.",
    "Se refuerza gate critico: no propagar memoria no parseable sin normalizacion previa.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se agrega correccion operativa de placeholders y rutas rotas detectadas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar encuadre curricular local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "No mezclar identidad curricular de otras carreras o asignaturas.",
    "Conservar autoria y matricula en portada cuando aplique.",
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
    "Registrar supuestos operativos cuando falten instrucciones de actividad.",
    "No transferir contenido tematico especifico de otra asignatura sin validacion documental."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizacion recursiva.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y nombres rotos en README y programa analitico antes de publicar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base de nuevos entregables.",
    "Mantener documentclass article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Conservar macros de titulo, subtitulo, autor, curso y universidad.",
    "Sustituir Actividad X por nombre real del producto.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales pertinentes al encargo local.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No importar bibliografia tematica de Filosofia del Derecho sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico puntual.",
    "Mantener bandera de normalizacion manual en ciclos con insumos no estructurados.",
    "Aplicar union-dedupe en cada ciclo para evitar duplicados sin perder informacion."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen sin confirmacion local.",
    "Supuesto: nombre oficial final de la electiva sigue pendiente contra malla curricular.",
    "Confirmar si year 2026 en unadmSitioWeb debe mantenerse o migrar solo a fecha de consulta.",
    "Confirmar figura docente para cerrar portada base.",
    "Confirmar que todos los placeholders de rutas fueron corregidos en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria antes de propagacion.",
        "Carpeta de materia como entrada canonica."
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
      "Convertir planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Asegurar coherencia entre objetivo, desarrollo, evidencia y cierre.",
      "Sostener una memoria editorial reutilizable y segura en propagacion recursiva."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos etiquetados cuando falta evidencia.",
      "Separacion explicita entre descripcion, analisis y conclusion.",
      "Control estricto de verificabilidad documental."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer conceptos y normas pertinentes.",
      "Contrastar fuentes con postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Normalizacion editorial",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion editorial",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis se fundamenta en un conflicto definido."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento sustentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "La integridad academica exige fuentes comprobables."
        }
      ],
      "evidence": [
        "README local de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico local con ejes de trabajo y proposito.",
        "Archivo electiva-semestre-7-bloque-2.bib con claves base institucionales.",
        "Gate persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos heredados y se alinearon al destino.",
      "Se excluyo contenido tematico puntual de Filosofia del Derecho por no ser estable transversal.",
      "Se reforzo control de placeholders por evidencia local verificable."
    ]
  }
}