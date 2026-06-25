{
  "summary": [
    "Se sincronizan al destino solo abstracciones editoriales estables desde actividad de Filosofia del Derecho.",
    "Se preserva identidad UnADM y encuadre curricular local de la electiva en semestre 7, bloque 2.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolida patron transversal: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantienen alertas por salidas no parseables heredadas como riesgo de calidad, no como contenido tematico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, tipo electiva.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "No mezclar identidad de otras carreras en entregables de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra asignatura aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre consigna, producto entregable y cierre argumentativo."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada academica completa.",
    "No compilar con placeholders o tokens sin expandir.",
    "Conservar configuracion base: article, spanish, letterpaper, oneside salvo instruccion distinta.",
    "Mantener claves BibTeX estables y referencias sin roturas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversal y recursivamente solo reglas generales validadas.",
    "Evitar transferir redaccion literal o contenido tematico no equivalente.",
    "Aplicar compresion lossless por union y deduplicacion sin recorte util.",
    "Mantener estrategia progresiva y conservadora para evitar regresiones.",
    "Si hay memoria no estructurada en nodos vecinos, normalizar antes de integrar."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para README y portada.",
    "Confirmar nombre oficial final de la materia en malla curricular.",
    "Confirmar figura docente para plantilla base.",
    "Supuesto: falta consigna local de actividades especificas de la electiva.",
    "Confirmar politica final de year vs fecha de consulta en fuentes web institucionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Garantizar consistencia editorial transversal entre actividades y materia.",
      "Asegurar calidad institucional antes de toda propagacion."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte informacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
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
          "source": "identidad institucional UnADM",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Define limites formales y curriculares del entregable."
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
          "justification": "La postura propia requiere sustento comprobable."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita utilidad juridica practica."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y carpeta canonica.",
        "Programa analitico local fija ejes de problema, conceptos, producto, analisis y cierre.",
        "Bib local contiene base institucional verificable.",
        "Supuesto: no hay consigna especifica de actividad local en este ciclo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se deduplican reglas repetidas y se preservan reglas utiles previas.",
      "Ciclo 15: se transfiere solo abstraccion estable desde nodo no equivalente.",
      "Ciclo 15: se refuerzan gates de JSON parseable y normalizacion manual.",
      "Ciclo 15: se evita importar contenido tematico especifico de Filosofia del Derecho."
    ]
  }
}