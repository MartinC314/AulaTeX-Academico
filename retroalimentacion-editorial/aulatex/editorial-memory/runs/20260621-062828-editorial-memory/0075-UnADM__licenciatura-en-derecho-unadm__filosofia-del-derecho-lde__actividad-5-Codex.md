{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM, encuadre jurídico y estructura editorial base.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita transferir redacción literal, conclusiones específicas y bibliografía exclusiva de otro hermano.",
    "Supuesto: falta consigna local de Actividad 5; se mantiene plantilla argumentativa y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad y precisión.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales, no académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte información de consigna o rúbrica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar salidas no estructuradas antes de reutilización recursiva.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias indefinidas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar solo tras validación de JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Aplicar deduplicación lossless por unión semántica, no por recorte.",
    "Evitar regresiones: nunca eliminar reglas útiles previas.",
    "Transferir entre hermanos solo patrones generales reutilizables.",
    "Si falta dato local, propagar plantilla y preguntas abiertas, no contenido inventado."
  ],
  "open_questions": [
    "Confirmar enunciado oficial de Actividad 5.",
    "Confirmar rúbrica y criterios de evaluación de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico definitivo del .bib de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Confirmar fuentes obligatorias específicas de la semana correspondiente."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables jurídicos sólidos.",
      "Asegurar fundamento, trazabilidad y utilidad profesional.",
      "Estandarizar calidad editorial sin perder adaptación por actividad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos marcados cuando falte información.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia del argumento a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
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
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterios mínimos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay razonamiento jurídico sólido."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez de la conclusión depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura y la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial: incidentes de salida no parseable requieren gate estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 75: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 75: transferidos patrones reutilizables de hermano a hermano.",
      "Ciclo 75: reforzada prohibición de copiar conclusiones y bibliografía exclusiva de Actividad 1.",
      "Ciclo 75: mantenido control de supuestos por falta de consigna local.",
      "Ciclo 75: consolidada prioridad de calidad estructural antes de propagación."
    ]
  }
}