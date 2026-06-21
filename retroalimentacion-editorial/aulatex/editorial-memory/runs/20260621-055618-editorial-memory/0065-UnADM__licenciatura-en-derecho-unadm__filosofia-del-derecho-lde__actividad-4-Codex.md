{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable de Filosofía del Derecho.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control de calidad: JSON parseable y normalización obligatoria antes de propagar.",
    "Supuesto: la consigna específica de Actividad 4 no está visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear la entrega a UnADM, Licenciatura en Derecho, Filosofía del Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con citas verificables.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: confirmar formato exacto de entrega de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar codificación española correcta en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos en README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin confirmación."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables, no conclusiones específicas de otro hermano.",
    "Aplicar unión y deduplicación sin recorte de reglas útiles.",
    "Preservar reglas institucionales y de calidad en nodos laterales.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar producto requerido: reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica de Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre final canónico del .bib ante token sin resolver en README.",
    "Confirmar si la bibliografía de interpretación jurídica (Semana 7) aplica o no a Actividad 4."
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
        "Normalización obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables con fundamento jurídico y evidencia.",
      "Garantizar trazabilidad editorial y consistencia institucional en cada actividad."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita de fuentes verificables.",
      "Marcado de supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura razonada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON",
        "Relación problema-evidencia-conclusión jurídica"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
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
          "justification": "Los ejes fijan orden de desarrollo y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe sustentarse en evidencia y análisis."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica con criterio propio.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salida no parseable: refuerzan gate de JSON estricto.",
        "Token Slug sin resolver en README/programa: requiere validación de nombres de archivo."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se eliminaron transferencias no permitidas de contenido específico entre hermanos.",
      "Se conservaron reglas útiles previas de calidad, estructura e identidad.",
      "Se añadieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}