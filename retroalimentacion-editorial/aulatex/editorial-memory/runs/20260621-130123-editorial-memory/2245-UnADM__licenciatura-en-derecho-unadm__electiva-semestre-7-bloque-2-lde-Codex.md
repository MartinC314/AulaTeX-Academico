{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia electiva sin trasladar contenido temático específico.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y normalización previa a propagación.",
    "Se refuerza compresión lossless por unión y deduplicación, sin regresión y sin recorte útil.",
    "Se mantiene estado de alertas por salidas no parseables en ciclos heredados y se exige normalización manual cuando aplique.",
    "Se consolida cerebro editorial mínimo reusable para actividades hijas de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar autoría y matrícula en portada cuando el formato lo requiera.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rúbrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar fuentes específicas de cada actividad en el .bib local de la materia.",
    "No asumir que bibliografía de otra semana o asignatura aplica automáticamente.",
    "Validar que el tipo de producto coincida con la consigna local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y archivos citados existan en el repositorio local.",
    "Corregir placeholders y tokens sin expandir antes de reutilizar plantillas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base de nuevos entregables.",
    "Mantener metadatos del curso LDE-S7B2 salvo actualización confirmada.",
    "Conservar codificación correcta para español en .tex y .bib.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores críticos ni referencias indefinidas.",
    "No introducir comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No trasladar bibliografía temática de Filosofía del Derecho sin verificación documental local."
  ],
  "propagation_hints": [
    "Propagar de forma recursiva solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal o contenido temático no equivalente.",
    "Aplicar unión-dedupe en cada ciclo y conservar reglas útiles previas.",
    "Mantener alertas históricas de ciclos con salida no parseable para control de riesgo."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para README y portada.",
    "Confirmar nombre oficial de la materia en malla curricular institucional.",
    "Confirmar si 'Nombre por definir' de figura docente debe sustituirse ya.",
    "Corregir definitivamente placeholders en README y programa analítico. [supuesto: persisten tokens]",
    "Definir política local para year vs fecha de consulta en fuentes web institucionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producción orientada a planeación semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables y útiles.",
      "Garantizar consistencia editorial transversal entre actividades y materia.",
      "Proteger calidad institucional mediante gates de validación técnica y académica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y trazables.",
      "Supuestos etiquetados cuando falta información.",
      "Cierre con implicación práctica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación propia.",
      "Consigna -> objetivo -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalización estructurada",
        "evidencia verificable",
        "postura argumentada",
        "conclusión transferible",
        "alineación con consigna"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineación con consigna",
          "kind": "supports",
          "justification": "Delimita formato, alcance y coherencia curricular del entregable."
        },
        {
          "source": "normalización estructurada",
          "target": "evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay trazabilidad de fuentes ni validación."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental explícito."
        },
        {
          "source": "postura argumentada",
          "target": "conclusión transferible",
          "kind": "develops",
          "justification": "El análisis razonado permite cierre aplicable a práctica jurídica."
        }
      ],
      "evidence": [
        "README local define identidad UnADM y carpeta canónica.",
        "Programa analítico local define ejes de problema, conceptos, análisis y cierre.",
        "Bibliografía local incluye base institucional verificable en archivo .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se deduplican reglas repetidas sin pérdida semántica.",
      "Ciclo 12: se preservan alertas históricas de insumos no parseables.",
      "Ciclo 12: se transfiere solo abstracción estable desde nodo no equivalente.",
      "Ciclo 12: se evita importar contenido temático específico de Filosofía del Derecho."
    ]
  }
}