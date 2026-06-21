{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y ubicación curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se conserva gate crítico: no propagar sin JSON parseable y estructura mínima completa.",
    "Se refuerza transferencia entre hermanos con patrones reutilizables, sin copiar conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda entrega a identidad institucional UnADM.",
    "Vincular explícitamente la actividad a Filosofía del Derecho en Licenciatura en Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en cada tramo argumental.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance o rúbrica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memorias afectadas por incidentes previos de parseo.",
    "Rechazar salidas no estructuradas para propagación recursiva."
  ],
  "latex_rules": [
    "Mantener acentos y codificación en español consistentes en .tex y .bib.",
    "Conservar claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres de archivo reales cuando README muestre tokens sin expandir.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Aplicar unión y deduplicación sin eliminar reglas útiles previas.",
    "Transferir patrones generales entre hermanos, no redacción literal.",
    "Preservar bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Escalar preguntas abiertas cuando falte consigna local.",
    "Evitar regresiones de identidad, calidad y trazabilidad."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si bibliografía de Semana 7 es reutilizable en Actividad 5.",
    "Supuesto: referencias de A1 transferidas son patrón, no obligación temática en A5."
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
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar consistencia institucional y argumentativa en cada actividad.",
      "Permitir propagación confiable mediante estructura validada."
    ],
    "style_markers": [
      "Inicio breve con encuadre del problema.",
      "Secciones funcionales sin ornamento redundante.",
      "Uso explícito de supuestos cuando falte información.",
      "Cierre con implicación práctica jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, formato y estándar académico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez del cierre depende del respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a consigna local."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo obliga gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: consolidación lateral entre hermanos sin copiar contenido específico.",
      "Se deduplicaron reglas repetidas y se preservó cobertura funcional completa.",
      "Se reforzó separación entre patrones transferibles y contenido dependiente de consigna.",
      "Se mantiene política de supuestos explícitos ante ausencia de datos locales."
    ]
  }
}