{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar contenido específico.",
    "Se preservan reglas útiles previas y se deduplican en formato accionable.",
    "Se mantiene identidad UnADM, estructura editorial base y control de supuestos.",
    "Se refuerza la política de normalización JSON antes de propagación recursiva.",
    "Se conserva la separación entre evidencia académica y memoria editorial provisional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar patrones reutilizables de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva de un hermano.",
    "Incluir postura argumentada del estudiante, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Confirmar correspondencia entre citas en texto y archivo .bib.",
    "Marcar o retirar afirmaciones sin respaldo verificable.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como supuesto operativo que el .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validación JSON y normalización estructurada.",
    "Propagar a nodos hermanos solo reglas generales e identidad institucional.",
    "Evitar propagar supuestos como hechos confirmados.",
    "Reforzar conexiones problema -> evidencia -> análisis -> conclusión en actividades laterales.",
    "Mantener compresión lossless por unión y deduplicación."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-3 [supuesto].",
    "Confirmar nombre canónico final del archivo .bib de la asignatura."
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
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Mantener continuidad editorial entre actividades sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Supuestos controlados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
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
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de una delimitación inicial del problema."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión sólida depende de respaldo normativo o doctrinal."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico fija ejes: problema, conceptos, producto, análisis, conclusión.",
        "Memoria previa reporta incidencias de parseo y exige normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza transferencia lateral por patrones, no por contenido literal.",
      "Ciclo 2: se mantiene no regresión de reglas de calidad y estructura.",
      "Ciclo 2: se agrega control explícito de supuestos para datos no confirmados.",
      "Ciclo 2: se conserva separación entre memoria editorial y evidencia académica."
    ]
  }
}