{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se mantiene normalización estructurada obligatoria antes de propagar.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva antecedente de salidas no parseables como gate crítico de calidad.",
    "Supuesto: la consigna específica de Actividad 4 no está visible completa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico de la asignatura.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entrega solo descriptiva; exigir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No transferir conclusiones específicas ni redacción literal desde Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna real de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico antes de fijar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y argumentación.",
    "Evitar regresiones; conservar reglas útiles previas ya verificadas.",
    "Aplicar unión-dedupe sin recorte semántico.",
    "Cuando falte dato local, propagar plantilla base y pregunta abierta.",
    "Mantener bandera de normalización manual para ciclos con historial no estructurado."
  ],
  "open_questions": [
    "Confirmar consigna oficial de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del .bib de la asignatura tras resolver token Slug.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere .bib incremental."
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y análisis propio.",
      "Postura académica argumentada.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar trazabilidad entre problema, evidencia y conclusión.",
      "Preservar consistencia institucional y técnica en toda entrega."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita para cada afirmación sustantiva.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura justificada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
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
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden y contenido mínimo del producto."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión válida depende de evidencia y análisis trazable."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico define cinco ejes de trabajo reutilizables.",
        "Historial de salidas no parseables justifica gate de JSON estricto.",
        "Token Slug sin resolver en rutas documentales requiere validación previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 32: deduplicación integral aplicada sin pérdida de reglas útiles.",
      "Ciclo 32: se reforzó gate de JSON parseable por riesgo histórico.",
      "Ciclo 32: se consolidaron patrones transferibles hermano-a-hermano sin copiar contenido específico.",
      "Ciclo 32: se preservó trazabilidad institucional, curricular y bibliográfica."
    ]
  }
}