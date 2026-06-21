{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM y marco curricular de Derecho sin copiar contenido específico entre hermanos.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se consolidan ejes estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se preserva regla de marcar supuestos cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad y precisión.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el producto al formato solicitado en la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante y evitar descripción plana.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otras semanas sin confirmar pertinencia.",
    "Si falta instrucción, declarar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación española consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres de archivo cuando README tenga tokens sin expandir.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta validar pertinencia."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales reutilizables entre hermanos.",
    "No transferir redacción literal ni conclusiones específicas de Actividad 1.",
    "No transferir bibliografía exclusiva sin validación contextual.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo histórico por salidas no parseables previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si Actividad 5 exige reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5."
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
      "Problema jurídico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre argumentativo.",
      "Preservar coherencia institucional y técnica en producción LaTeX."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin ornamento innecesario.",
      "Postura propia sustentada en evidencia.",
      "Uso explícito de supuestos cuando falte información."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
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
          "justification": "Define tono, encuadre y estándar académico del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida necesita respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta curso; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos: incidente de salida no parseable exige gate técnico estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: deduplicación integral de reglas repetidas sin pérdida semántica.",
      "Ciclo 76: refuerzo lateral controlado desde hermano Actividad 1 a Actividad 5.",
      "Ciclo 76: se preservan reglas útiles previas y se evita transferencia de contenido específico no reusable.",
      "Ciclo 76: se consolidan supuestos abiertos en lugar de inventar datos locales."
    ]
  }
}