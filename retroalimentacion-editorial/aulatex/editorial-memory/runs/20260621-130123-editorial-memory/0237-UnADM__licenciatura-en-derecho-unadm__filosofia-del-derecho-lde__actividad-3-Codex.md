{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantienen ejes editoriales estables: problema, conceptos y fuentes, análisis propio y conclusión jurídica transferible.",
    "Se conserva regla crítica: bloquear propagación sin JSON parseable y normalizar salidas no estructuradas.",
    "Se mantiene política de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividades hermanas sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o consigna de actividad-3 sin evidencia local.",
    "Si faltan datos locales, usar estructura base y dejar supuestos explícitos."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivos canónicos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas y resolver tokens sin expandir tipo $(@{...}.Slug).",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "No usar memoria editorial como bibliografía académica.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y requiere validación de pertinencia para actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Propagar reglas generales cuando falte consigna textual local.",
    "Conservar bandera de riesgo cuando existan antecedentes de parseo inválido.",
    "Aplicar compresión por unión y deduplicación sin pérdida."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad-3; confirmar producto exacto solicitado.",
    "Confirmar si actividad-3 requiere reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si aplica bibliografía de interpretación jurídica (Semana 7) o se requiere .bib específico.",
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Trazabilidad entre afirmación y fuente.",
      "Supuestos etiquetados cuando falta evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo consistente -> cierre verificable."
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
        "Política de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicabilidad condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable entre nodos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis nace de un problema delimitado y evita descripción vacía."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La verificabilidad de fuentes sostiene la validez académica del producto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: propósito y ejes de trabajo de la asignatura.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Regla persistente: marcar supuestos cuando falte consigna local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicación integral de reglas repetidas en origen y destino.",
      "Ciclo 16: se conserva no regresión y control de parseo como compuerta obligatoria.",
      "Ciclo 16: se transfiere patrón argumentativo reusable sin copiar contenido específico de actividad-1.",
      "Ciclo 16: se mantiene condición de aplicabilidad para bibliografía de Semana 7 como supuesto."
    ]
  }
}