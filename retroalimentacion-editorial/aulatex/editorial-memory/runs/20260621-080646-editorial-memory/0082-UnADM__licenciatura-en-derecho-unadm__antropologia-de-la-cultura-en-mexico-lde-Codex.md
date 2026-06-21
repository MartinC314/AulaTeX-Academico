{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia.",
    "Se preservan reglas validas del destino y se agregan abstracciones estables del origen sin transferir contenido tematico especifico.",
    "Se refuerza compresion lossless por union-dedupe y control de no regresion.",
    "Se mantiene alerta institucional: bloquear propagacion ante salida no JSON parseable y normalizar antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones reusables: conceptos clave, marco de referencia, analisis propio y cierre.",
    "Alinear el artefacto al producto solicitado en la planeacion semanal.",
    "Separar artefactos por tipo: reporte, presentacion y bibliografia.",
    "Resolver placeholders de rutas y nombres antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Mantener puente argumentativo entre enfoque cultural y utilidad juridica.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre metadatos del documento y datos curriculares locales.",
    "Verificar ausencia de afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local de la materia como base.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato actuales salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir nombres de archivo corruptos o truncados detectados en README/programa."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas y academicas pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o conceptos tematicos exclusivos del origen.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Mantener estrategia progresiva y conservadora: agregar sin borrar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: no se confirma aun rubrica oficial unica de citas para toda la licenciatura.",
    "Supuesto: falta confirmar si LDE-S4B2 es clave institucional definitiva o local.",
    "Confirmar si todas las actividades de la materia exigen conclusion juridica explicita.",
    "Confirmar si existe consigna local que modifique la estructura base por tipo de actividad."
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
      "Compresion lossless por union-dedupe sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles profesionalmente.",
      "Sostener coherencia editorial transversal entre materias sin mezclar contenidos disciplinares."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados.",
      "Cierre con valor juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Coherencia estricta entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Compresion union-dedupe lossless"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige trazabilidad documental."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana validez cuando se fundamenta."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion aplicada deriva del razonamiento argumentado."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de normalizacion y bloqueo por no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 82: se reforzo gate JSON parseable como requisito de propagacion.",
      "Ciclo 82: se incorporo del origen la abstraccion 'objetivo puntual + postura propia + coherencia argumentativa'.",
      "Ciclo 82: se excluyo transferencia de contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 82: se mantuvo no regresion y deduplicacion semantica en reglas repetidas."
    ]
  }
}