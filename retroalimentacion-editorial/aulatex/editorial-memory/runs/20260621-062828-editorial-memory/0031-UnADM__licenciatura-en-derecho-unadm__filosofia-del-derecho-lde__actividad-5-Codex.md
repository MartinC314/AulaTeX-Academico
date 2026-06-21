{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 5 sin copiar contenido específico.",
    "Se preserva identidad UnADM, ubicación curricular y ejes editoriales troncales.",
    "Se mantiene regla crítica: normalizar y validar JSON antes de propagación recursiva.",
    "Se refuerza transferencia por patrones reutilizables: estructura, calidad, trazabilidad y consistencia cita-.bib.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene plantilla base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como insumo provisional, no como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir siempre afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear el formato final al producto pedido por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones ni bibliografía exclusiva de otra actividad sin validar pertinencia.",
    "Si falta dato operativo, declarar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar correspondencia entre citas en texto y entradas del .bib.",
    "Rechazar respuestas no estructuradas hasta normalización manual.",
    "Verificar que el producto responda a la consigna y no solo a ejes genéricos."
  ],
  "latex_rules": [
    "Usar español con codificación y acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin necesidad editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta validar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y control de estructura.",
    "Aplicar deduplicación por unión sin recorte semántico.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Transferir patrones, no redacción literal ni conclusiones de hermano a hermano.",
    "Mantener bandera histórica de riesgo por incidentes de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual y rúbrica exacta de Actividad 5.",
    "Confirmar tipo de producto requerido en Actividad 5: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib en la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica o no a Actividad 5.",
    "Confirmar fuentes obligatorias específicas de la semana de Actividad 5."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Trazabilidad entre consigna, evidencia y cierre."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos jurídicos sólidos.",
      "Asegurar consistencia editorial entre actividades hermanas sin contaminación de contenido específico.",
      "Garantizar salida técnica reusable mediante normalización estructurada."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Postura personal sustentada.",
      "Supuestos explícitos cuando falte información.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Supuestos explícitos",
        "Bibliografía base vs específica"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "El marco institucional define forma y criterio del producto."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La trazabilidad bibliográfica sostiene validez editorial."
        },
        {
          "source": "Bibliografía base vs específica",
          "target": "Pertinencia de fuentes",
          "kind": "develops",
          "justification": "Evita arrastre indebido entre actividades hermanas."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis propio y cierre.",
        "Historial de incidentes no parseables justifica gate técnico estricto.",
        "Token Slug sin expandir en README justifica regla de validación de rutas y .bib.",
        "Supuesto: consigna local de Actividad 5 no visible de forma completa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 31: deduplicación lossless aplicada sobre reglas repetidas.",
      "Ciclo 31: se refuerza separación patrón reutilizable vs contenido específico de hermano.",
      "Ciclo 31: se conserva gate de JSON parseable como condición de propagación.",
      "Ciclo 31: se mantiene distinción bibliografía base y bibliografía por actividad.",
      "Ciclo 31: se mantienen supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}