{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se refuerza flujo editorial común: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica: no propagar salidas no parseables sin normalización.",
    "Se conserva distinción entre reglas reutilizables y contenido específico de actividad.",
    "Supuesto: la consigna local completa de Actividad 4 no está visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Vincular contexto curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear formato final al producto pedido por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a ejes del programa analítico sin copiar conclusiones de Actividad 1.",
    "Incluir explícitamente problema, evidencia y postura argumentada.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Confirmar tipo de producto solicitado antes de redactar versión final."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas.",
    "No aceptar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en español en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) antes de cerrar entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de actividad en .bib de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y puede no aplicar completo a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir patrones reutilizables, no redacción literal ni cierres específicos.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión-dedupe en cada ciclo de consolidación.",
    "Mantener bandera de normalización manual para memorias con antecedentes no estructurados.",
    "Escalar mejoras verificables de calidad a nodos hermanos."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias de la semana específica.",
    "Confirmar nombre canónico final del .bib de asignatura tras resolver slug.",
    "Confirmar si se reutiliza .bib existente o se crea .bib incremental."
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
      "Conceptos y marco normativo con evidencia.",
      "Análisis propio con postura sustentada.",
      "Conclusión jurídica aplicable.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos claros y verificables.",
      "Asegurar coherencia entre consigna, argumentación y cierre jurídico.",
      "Mantener continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita de afirmaciones relevantes.",
      "Marcado de supuestos cuando falten datos locales.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Problematizar contexto jurídico.",
      "Definir conceptos y marco aplicable.",
      "Contrastar fuentes con análisis propio.",
      "Formular postura razonada.",
      "Concluir con criterio jurídico transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Normalización estructurada",
        "Validación JSON",
        "Relación problema-evidencia-conclusión"
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
          "target": "Tono formal académico",
          "kind": "supports",
          "justification": "La pauta editorial exige consistencia institucional."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan desarrollo y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe estar respaldada por evidencia."
        }
      ],
      "evidence": [
        "README define identidad, integridad y punto de entrada canónico.",
        "Programa analítico define cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Regla de transferencia exige patrones reutilizables sin copia literal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicación ortográfica y semántica aplicada sin recorte útil.",
      "Ciclo 7: se refuerza separación entre patrón reusable y contenido específico.",
      "Ciclo 7: se mantiene control de supuestos por falta de consigna completa local.",
      "Ciclo 7: se conserva prioridad de validación JSON antes de propagación."
    ]
  }
}