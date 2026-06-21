{
  "summary": [
    "Se consolida memoria lateral para actividad-3 con transferencia lossless por deduplicación.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos-fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene bloqueo de propagación cuando no haya JSON parseable.",
    "Se conserva política de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado en la consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana o formato de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir evidencia académica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya usadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con las citas reales de actividad-3 [supuesto de uso condicionado]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar conclusiones específicas ni bibliografía exclusiva de una actividad hermana.",
    "Aplicar unión-deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo si hubo incidencias de parseo en ciclos previos.",
    "Cuando falten datos locales, propagar preguntas abiertas en lugar de contenido inventado."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 usa bibliografía de interpretación jurídica (Semana 7) o requiere .bib propio.",
    "Confirmar archivo .tex principal canónico para actividad-3."
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico.",
      "Garantizar trazabilidad entre afirmaciones, fuentes y conclusión.",
      "Preservar coherencia institucional y utilidad profesional del cierre."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual-normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho.bib",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
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
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La estructura válida evita pérdida y ambigüedad en propagación editorial."
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
        },
        {
          "source": "Bibliografía verificable",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura académica requiere respaldo documental."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicación completa de reglas repetidas con conservación semántica.",
      "Ciclo 8: se trasladan solo patrones reutilizables desde actividad-1 a actividad-3.",
      "Ciclo 8: se evita transferir conclusiones específicas y bibliografía exclusiva del hermano.",
      "Ciclo 8: se mantiene política de supuestos y no invención de fuentes.",
      "Ciclo 8: se refuerza control de calidad para propagación recursiva."
    ]
  }
}