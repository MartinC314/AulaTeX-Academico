{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido específico.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene la regla de normalización JSON obligatoria antes de propagación recursiva.",
    "Se consolida deduplicación lossless y se eliminan redundancias formales, no reglas útiles.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular explícitamente la actividad con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica operativa.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas ni bibliografía exclusiva de otra actividad sin validar pertinencia.",
    "Registrar supuesto operativo cuando haya duda de alcance y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización recursiva.",
    "Comprobar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando existan tokens sin expandir en README o programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura, calidad y método argumentativo.",
    "No transferir redacción literal, conclusiones concretas ni listas bibliográficas exclusivas del hermano.",
    "Aplicar unión y deduplicación sin pérdida semántica en cada ciclo.",
    "Mantener bandera histórica de riesgo por incidentes de parseo en ciclos previos.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas.",
    "Evitar regresiones: conservar reglas útiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib operativo de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Supuesto: el contexto visible no incluye todos los documentos de actividad."
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
      "Resolver un problema jurídico con base conceptual y normativa.",
      "Sostener postura propia con evidencia trazable.",
      "Cerrar con conclusión transferible a la práctica jurídica.",
      "Preservar estructura y calidad antes que volumen textual."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con rigor jurídico.",
      "Garantizar continuidad editorial entre actividades sin contaminación de contenido específico.",
      "Asegurar memoria persistente, verificable y reutilizable en propagación recursiva."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y explícitas.",
      "Trazabilidad entre afirmación y fuente.",
      "Uso visible de supuestos cuando falte dato local.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Bibliografía base",
        "Bibliografía específica de actividad"
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
          "justification": "La pauta institucional define tono, formato y exigencia argumentativa."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis solo es sólido si parte de una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis propio y cierre.",
        "Historial de parseo obliga gate estricto de estructura antes de propagar.",
        "Token Slug sin expandir en archivos visibles exige validación de nombres canónicos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: refuerzo lateral aplicado por analogía controlada entre actividades hermanas.",
      "Se consolidaron reglas duplicadas sin pérdida de restricciones útiles.",
      "Se mantuvo separación entre patrones transferibles y contenido específico no transferible.",
      "Se añadieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}