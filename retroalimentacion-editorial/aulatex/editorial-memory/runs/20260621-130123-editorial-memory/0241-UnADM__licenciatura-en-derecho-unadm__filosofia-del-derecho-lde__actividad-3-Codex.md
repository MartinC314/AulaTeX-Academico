{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, ejes editoriales y control de calidad sin regresión.",
    "Se mantiene bloqueo de propagación si no hay JSON parseable y normalización previa obligatoria.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de un hermano.",
    "Se mantiene política de supuestos para todo dato no confirmado en consigna local de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Usar estructura base: problema, conceptos y fuentes, análisis propio, cierre jurídico.",
    "Separar marco normativo o doctrinal cuando aplique.",
    "Alinear el producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin eliminar ninguna útil.",
    "No copiar redacción literal ni conclusiones específicas entre actividades hermanas.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en actividad-3.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No reutilizar automáticamente bibliografía depurada de otra semana sin confirmación local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos hermanos solo reglas generales e identidad institucional.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo en ciclos con incidencias de parseo.",
    "Aplicar compresión por unión y deduplicación sin recorte semántico.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar bibliografía obligatoria específica de actividad-3.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica o a otra unidad [supuesto].",
    "Confirmar archivo .tex principal de actividad-3."
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
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Trazabilidad entre argumento y evidencia."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en producto académico verificable.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
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
        "filosofia-del-derecho-clean.bib [uso condicionado, supuesto]"
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
          "justification": "Sin formato parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema, conceptos, producto, análisis y conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza transferencia lateral controlada por analogía.",
      "Se eliminan duplicados textuales manteniendo cobertura normativa y editorial.",
      "Se conserva política de no invención y marcado explícito de supuestos.",
      "Se preserva no regresión en reglas de estructura, calidad, LaTeX y bibliografía.",
      "Se mantiene separación entre memoria editorial y evidencia académica."
    ]
  }
}