{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita transferir conclusiones específicas o bibliografía exclusiva de un hermano."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar asumir que fuentes de otras semanas aplican sin validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que el producto corresponda a la consigna específica de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar y corregir nombres de archivo con tokens sin resolver del README.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por slug institucional."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con consigna y claves citadas."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura y calidad.",
    "No copiar redacción literal ni conclusiones concretas entre actividades hermanas.",
    "Mantener unión-dedupe sin regresión de reglas útiles previas.",
    "Aplicar propagación recursiva solo tras validación JSON y estructura.",
    "Cuando falten datos locales, transferir plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extensión y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar si la actividad usa bibliografía propia o reutiliza parte de la existente.",
    "Confirmar nombre final del .bib canónico ante token de plantilla sin resolver."
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
        "Normalización estructurada obligatoria antes de propagar.",
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Garantizar fundamento jurídico, evidencia y criterio propio.",
      "Asegurar trazabilidad editorial y reutilización segura entre nodos."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita de cada afirmación relevante.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problematizar el caso o tema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura razonada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización segura."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan contenido y cierre argumentativo."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe estar respaldada y no ser descriptiva."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica y conclusión jurídica.",
        "Programa analítico: cinco ejes de trabajo.",
        "Historial: antecedente de salidas no parseables; gate JSON estricto necesario.",
        "Supuesto: consigna local de Actividad 4 no visible en el contexto entregado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se deduplican reglas repetidas y se conserva contenido útil previo.",
      "Ciclo 7: se refuerzan gates de parseo JSON y normalización.",
      "Ciclo 7: se transfiere patrón argumentativo común sin copiar contenido específico de Actividad 1.",
      "Ciclo 7: se mantiene separación entre bibliografía base y bibliografía por actividad."
    ]
  }
}