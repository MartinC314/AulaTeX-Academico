{
  "summary": [
    "Se sincronizan solo abstracciones editoriales estables desde actividad transversal no equivalente.",
    "Se conserva identidad UnADM, estructura reusable y control de calidad sin arrastrar redaccion literal.",
    "Se refuerza normalizacion JSON obligatoria antes de toda propagacion recursiva.",
    "Se mantiene estrategia progresiva y conservadora con compresion lossless por deduplicacion.",
    "Se preservan ejes nucleares: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene cerebro editorial minimo de materia y se dejan abiertos vacios de contexto local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar identidad de otras carreras en entregables de Derecho.",
    "Conservar autoria y matricula en portada cuando aplique.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre README, programa analitico, plantilla y .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra asignatura o semana aplica automaticamente.",
    "Etiquetar supuestos cuando falte instruccion operativa de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Corregir placeholders y tokens sin expandir antes de publicar o compilar.",
    "Verificar que rutas y archivos citados existan en el repositorio."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener documentclass article con spanish, letterpaper y oneside salvo consigna distinta.",
    "Conservar metadatos del curso LDE-S7B2 y portada academica completa.",
    "Sustituir placeholders como Actividad X por nombre real del producto.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Usar acentos y codificacion en espanol de forma consistente.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "No inventar fuentes; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL, y nota de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No trasladar bibliografia tematica de Filosofia del Derecho sin validacion documental local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas estables de identidad, estructura y calidad.",
    "Evitar transferir contenido tematico especifico entre nodos no equivalentes.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Mantener alertas historicas de ciclos con salida no estructurada.",
    "Si falta contexto local, conservar cerebro minimo y abrir preguntas de verificacion."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para README y portada.",
    "Confirmar figura docente de la plantilla.",
    "Corregir definitivamente placeholders de .bib en README y programa analitico.",
    "Definir politica local de year vs fecha de consulta para fuentes web institucionales.",
    "Supuesto: no hay consigna de actividad especifica en este nodo; validar al crear entregables concretos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia transversal."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Separacion estricta frente a identidades ajenas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
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
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Mantener coherencia institucional, juridica y tecnica entre documentos de la materia."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalizacion estructurada",
        "evidencia verificable",
        "postura argumentada",
        "conclusion transferible",
        "alineacion con consigna"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Define limites formales y curriculares del producto."
        },
        {
          "source": "normalizacion estructurada",
          "target": "evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad de respaldo."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere sustento documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio permite cierre util para practica juridica."
        }
      ],
      "evidence": [
        "README local de la materia como punto de entrada canonico.",
        "Programa analitico local con ejes editoriales comunes.",
        "Archivo .bib local con base institucional UnADM.",
        "Regla persistente de bloqueo por falta de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolida sincronizacion transversal sin importar redaccion literal.",
      "Ciclo 19: se preservan reglas utiles previas y se deduplican variantes repetidas.",
      "Ciclo 19: se refuerzan gates de JSON, supuestos y trazabilidad bibtex.",
      "Ciclo 19: se mantiene minimo editorial del destino y se abren vacios de contexto local."
    ]
  }
}