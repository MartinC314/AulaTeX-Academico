{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reutilizable desde Actividad 1.",
    "Se preservan reglas válidas previas sin regresión y con deduplicación lossless.",
    "Se refuerza identidad UnADM, estructura argumentativa y control de supuestos.",
    "Se mantiene bloqueo de propagación para salidas no JSON parseables.",
    "Se evita trasladar conclusiones o bibliografía exclusiva no verificada entre hermanos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local de Actividad 3.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Verificar consistencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Heredar reglas generales válidas de Actividad 1 sin copiar redacción literal.",
    "No asumir consigna, semana o formato de Actividad 3 sin evidencia local.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Registrar diferencias de Actividad 3 como supuestos hasta confirmar guía oficial.",
    "No trasladar bibliografía exclusiva de un hermano si no está citada localmente."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Validar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas y nombres de archivo antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib solo entradas realmente citadas en Actividad 3.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no contenido específico.",
    "Preservar ejes editoriales estables: problema, conceptos/fuentes, análisis propio, conclusión jurídica.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo cuando exista antecedente de salida no estructurada.",
    "Aplicar compresión por unión y deduplicación sin recorte semántico."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 3.",
    "Confirmar si aplica bibliografía de Interpretación jurídica (Semana 7) [supuesto].",
    "Confirmar nombre canónico final del .bib de la asignatura tras resolver token Slug."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Análisis propio sustentado en evidencia.",
      "Conclusión jurídica transferible a la práctica.",
      "Control explícito de supuestos y trazabilidad."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia entre identidad institucional y calidad argumentativa.",
      "Mantener memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Afirmación con evidencia y cita verificable.",
      "Supuestos marcados cuando falta dato local.",
      "Cierre jurídico con aplicación profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo alineado -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Supuestos controlados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de la delimitación del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica, citas verificables y cierre jurídico propio.",
        "Programa analítico fija ejes: problema, conceptos/fuentes, producto, análisis y conclusión.",
        "Memoria previa confirma regla de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 80: deduplicación de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 80: transferencia lateral controlada desde hermano sin copiar conclusiones específicas.",
      "Ciclo 80: se refuerza política de supuestos para datos no confirmados de Actividad 3.",
      "Ciclo 80: se mantiene no regresión y compresión lossless por unión-dedupe."
    ]
  }
}