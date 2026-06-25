{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial sin copiar contenido específico del hermano.",
    "Se mantiene normalización estructurada y validación JSON estricta como precondición de propagación.",
    "Se refuerzan ejes recurrentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: la consigna local completa de Actividad 4 no está visible; se conserva estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM.",
    "Alinear toda entrega con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la planeación semanal vigente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de semanas distintas sin confirmar aplicabilidad.",
    "Adaptar Actividad 4 a los cinco ejes editoriales del programa analítico.",
    "Supuesto: confirmar formato exacto solicitado para Actividad 4 antes de cierre."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre producto entregable y consigna local.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Verificar nombres reales de archivos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna activa.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a interpretación jurídica; confirmar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales reutilizables.",
    "Evitar traslado de conclusiones o redacción literal entre hermanos.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar unión y deduplicación semántica antes de guardar.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no parseables.",
    "Transferir identidad, estructura, calidad, conceptos marco y relaciones estables."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar tipo de producto requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de Actividad 4.",
    "Confirmar nombre canónico final del .bib ante token Slug no resuelto en README.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere bloque bibliográfico propio."
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
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar fundamento jurídico, claridad y transferencia profesional.",
      "Estandarizar calidad editorial entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y orden argumental estable.",
      "Citas explícitas en afirmaciones sustantivas.",
      "Supuestos marcados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Problema inicial -> marco conceptual -> análisis propio -> conclusión jurídica.",
      "Hechos y normas separados de opinión personal.",
      "Cierre con criterio profesional transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica",
        "Ejes editoriales de Filosofía del Derecho",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Definen el orden mínimo del desarrollo académico."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe derivar de evidencia y análisis verificables."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables, conclusión jurídica.",
        "Programa analítico: cinco ejes de trabajo recurrentes.",
        "Antecedentes de salidas no parseables: gate de JSON estricto obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza transferencia lateral por patrones reutilizables, sin copia literal.",
      "Ciclo 2: se conserva regla de bloqueo por JSON no parseable.",
      "Ciclo 2: se mantiene deduplicación lossless y se eliminan redundancias semánticas.",
      "Ciclo 2: se preserva la marca de supuestos para faltantes de consigna local."
    ]
  }
}