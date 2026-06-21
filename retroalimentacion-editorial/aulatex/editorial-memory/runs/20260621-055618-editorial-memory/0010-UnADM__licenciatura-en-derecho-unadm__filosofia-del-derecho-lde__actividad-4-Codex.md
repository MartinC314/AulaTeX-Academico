{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfiere solo patrón reusable; no se copian conclusiones ni redacción específica de Actividad 1.",
    "Supuesto: la consigna textual de Actividad 4 no está visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear producto final a la planeación semanal y consigna de Actividad 4.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otra semana aplica automáticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves bibliográficas ya usadas en documentos activos.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por slug institucional."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad y requiere validación antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión-dedupe sin recorte semántico.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Cuando falte dato local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica de evaluación.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del archivo .bib por token no resuelto en README.",
    "Confirmar si se usa .bib incremental o único de asignatura para esta actividad."
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico sólido.",
      "Asegurar trazabilidad entre problema, fuentes y postura.",
      "Formar criterio jurídico propio con base verificable."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales claras.",
      "Cita explícita de afirmaciones relevantes.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y norma aplicable.",
      "Contrastar fuentes con análisis propio.",
      "Sostener postura razonada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
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
          "justification": "La pauta editorial exige coherencia institucional."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden de desarrollo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON estricta",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay propagación segura."
        },
        {
          "source": "Relación problema-evidencia-conclusión",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Evita resumen descriptivo y exige postura fundada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Antecedentes locales: salidas no parseables requieren gate técnico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se reforzó transferencia lateral por analogía controlada.",
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se mantuvieron reglas útiles previas y se añadieron supuestos explícitos donde falta consigna local."
    ]
  }
}