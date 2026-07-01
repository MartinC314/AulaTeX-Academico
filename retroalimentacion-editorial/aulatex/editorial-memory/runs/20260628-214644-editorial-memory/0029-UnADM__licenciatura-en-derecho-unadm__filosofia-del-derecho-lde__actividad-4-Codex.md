{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales transferibles desde Actividad 1.",
    "Se refuerza normalización estructurada y validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva del nodo hermano.",
    "Supuesto: la consigna específica de Actividad 4 no está visible y requiere confirmación local."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Conservar integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar cada afirmación relevante con fuente verificable y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar la redacción al tipo de producto requerido en Actividad 4.",
    "No asumir fuentes de otras semanas sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Verificar esquema mínimo completo antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables; no renombrar claves activas sin migración completa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, sin referencias rotas y sin archivos faltantes.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar en el .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de la actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra semana; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin perder especificidad local.",
    "Aplicar unión y deduplicación; evitar regresiones de reglas útiles previas.",
    "Transferir solo patrones generales cuando falte consigna textual.",
    "Mantener bandera de normalización manual en ciclos con salidas heredadas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del .bib por token Slug no resuelto en README.",
    "Confirmar si se reutiliza .bib existente o se crea uno incremental para Actividad 4."
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
        "Integridad académica con trazabilidad de fuentes.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 créditos: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Producto alineado a planeación.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Asegurar coherencia entre identidad institucional, argumentación y evidencia.",
      "Preservar memoria editorial reutilizable sin copiar contenido específico entre hermanos."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y trazables.",
      "Citas verificables en puntos críticos.",
      "Supuestos marcados cuando falten datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Relación problema-evidencia-conclusión jurídica"
      ],
      "citations": [
        "README.md de la asignatura",
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
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden de desarrollo del producto."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe estar respaldada por evidencia citada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y criterio propio en conclusión.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Historial: hubo salidas no parseables; se requiere gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza transferencia lateral por analogía controlada.",
      "Se depuraron duplicados semánticos preservando reglas útiles previas.",
      "Se mantuvo separación entre patrones reutilizables y contenido específico no transferible.",
      "Se añadieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}