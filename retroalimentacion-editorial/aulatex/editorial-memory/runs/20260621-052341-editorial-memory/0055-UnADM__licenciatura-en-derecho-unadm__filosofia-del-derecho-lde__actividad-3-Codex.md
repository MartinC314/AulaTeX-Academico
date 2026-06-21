{
  "summary": [
    "Memoria lateral consolidada para actividad-3 con deduplicación lossless desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, análisis propio, conclusión jurídica transferible.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se conserva política de supuestos para datos no visibles en la consigna local.",
    "Se evita transferencia de redacción literal, conclusiones específicas y bibliografía exclusiva de actividad-1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular.",
    "Marcar como supuesto todo dato no confirmado por consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas reutilizables de actividad-1 sin copiar redacción literal.",
    "No asumir semana, formato ni consigna específica de actividad-3 sin evidencia local.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas en la actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Interpretación jurídica (Semana 7) y su uso en actividad-3 depende de coincidencia temática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validación JSON y estructura mínima.",
    "Transferir a nodos hermanos solo patrones institucionales, estructurales y de calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Conservar bandera de riesgo si hay antecedente de salida no estructurada.",
    "Reforzar conexiones problema->análisis->conclusión en actividades de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografía de Semana 7 o requiere .bib propio.",
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
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falta evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
      "Cierre jurídico aplicable a la práctica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
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
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad académica y citas verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Política de supuestos",
          "kind": "supports",
          "justification": "Estructura formal obliga a marcar incertidumbre explícita y evita inferencias opacas."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se activa desde un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "Sin evidencia verificable no hay cierre sólido."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables, conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Bibliografía local: clean.bib marcado como específico de Semana 7."
      ]
    },
    "reinforcement_log": [
      "Ciclo 55: deduplicación de reglas duplicadas con preservación total de contenido útil.",
      "Ciclo 55: refuerzo lateral de identidad, estructura y calidad sin migrar conclusiones específicas.",
      "Ciclo 55: consolidación de política de supuestos para actividad-3 por falta de consigna local.",
      "Ciclo 55: mantenimiento de no regresión y compatibilidad editorial recursiva."
    ]
  }
}