{
  "summary": [
    "Se consolida refuerzo lateral entre actividades de Filosofía del Derecho sin copiar contenido específico.",
    "Se preservan reglas núcleo: identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene compresión lossless por deduplicación y normalización de reglas repetidas.",
    "Se agrega control explícito de transferencia: solo patrones reutilizables, no conclusiones ni bibliografía exclusiva.",
    "Supuesto: falta consigna local de Actividad 5; se conserva plantilla base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance o formato de la consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización recursiva.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando existan tokens sin expandir en README o programa analítico.",
    "Supuesto: archivo .bib canónico esperado filosofia-del-derecho.bib por Slug institucional."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente específico de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y relaciones conceptuales.",
    "No transferir redacción literal, conclusiones locales ni bibliografía exclusiva de actividad hermana.",
    "Aplicar unión y deduplicación sin pérdida antes de guardar memoria.",
    "Mantener bandera de riesgo histórico por incidentes previos de parseo.",
    "Si falta dato local, propagar plantilla base y dejar pregunta abierta."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato exigido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografía existente o requiere .bib propio.",
    "Confirmar nombre canónico final del .bib ante tokens sin expandir en documentos guía."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con evidencia y cierre argumentativo.",
      "Asegurar trazabilidad entre consigna, desarrollo y conclusión jurídica.",
      "Sostener continuidad editorial entre actividades sin contaminar especificidades."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales no ornamentales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falte información.",
      "Consistencia cita-.bib."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a práctica profesional."
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
          "justification": "La pauta institucional define tono, rigor y forma del entregable."
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
          "justification": "La conclusión jurídica válida exige respaldo trazable."
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
          "justification": "La base orienta el curso; la específica responde a la consigna local."
        },
        {
          "source": "Patrones reutilizables",
          "target": "Refuerzo lateral entre hermanos",
          "kind": "develops",
          "justification": "Permite continuidad sin copiar conclusiones ni fuentes exclusivas."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, fuentes, análisis y cierre.",
        "Historial: incidentes de parseo obligan gate estructural previo a propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: deduplicación integral aplicada sin pérdida de reglas útiles.",
      "Ciclo 62: se fortaleció regla de transferencia controlada entre nodos hermanos.",
      "Ciclo 62: se mantuvo separación entre bibliografía base y bibliografía específica.",
      "Ciclo 62: se preservó bloqueo de propagación ante JSON no parseable."
    ]
  }
}