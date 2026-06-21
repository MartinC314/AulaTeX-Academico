{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstracción ascendente y deduplicación lossless.",
    "Se preserva identidad UnADM, ubicación curricular y función editorial de la asignatura.",
    "Se refuerza normalización obligatoria de insumos no estructurados antes de propagación.",
    "Se elevan patrones reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva trazabilidad entre actividad, archivos .tex, claves de cita y .bib de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito académico.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencia provisional Codex/GPT-Pro solo como riesgo de ingesta, no como autoridad final. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el tipo de entregable a la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad explícita entre consigna, desarrollo y conclusión."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Validar que el producto corresponda exactamente a la consigna activa.",
    "Conservar vínculo editorial con los cinco ejes de trabajo del programa analítico."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar correspondencia entre citas en .tex y entradas en .bib.",
    "Evitar regresión: no eliminar reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos, sin referencias rotas y con rutas válidas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canónicos.",
    "Corregir caracteres anómalos en nombres/rutas detectados en README.",
    "No copiar bloques LaTeX completos en memoria; guardar solo reglas reutilizables."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, SCJN, UNAM-IIJ y normativa vigente verificable.",
    "Registrar fuentes específicas por actividad en el .bib de materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Mantener como [supuesto] que filosofia-del-derecho-clean.bib corresponde a Semana 7 hasta validación final."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analítico y .bib local.",
    "Elevar al ancestro patrones argumentativos e identidad, no redacción literal de actividad.",
    "Reusar puertas de calidad institucional en nodos laterales de Derecho.",
    "Mantener compresión unión-deduplicación sin pérdida semántica.",
    "Registrar incidencias de parseo como riesgo operativo y conservar contenido útil normalizado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar plantilla final.",
    "Confirmar nombre canónico definitivo del .bib de la asignatura.",
    "Confirmar si actividad-1 requiere .bib propio o reutiliza el de materia.",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Resolver de forma definitiva placeholders $(@{...}.Slug) en README y programa analítico."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables y útiles para práctica jurídica.",
      "Sostener consistencia editorial entre actividades, reportes, presentaciones y bibliografía."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura propia explícita.",
      "Cierre jurídico aplicado.",
      "Marcado explícito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar críticamente con evidencia.",
      "Defender postura propia.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Integridad académica",
        "Trazabilidad cita-.bib"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y efectos de normas."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "Sin sustento normativo no hay cierre sólido."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura articula validez jurídica y dimensión axiológica."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analítico: propósito y cinco ejes.",
        "filosofia-del-derecho-clean.bib: claves jurídicas recurrentes.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: se elevan reglas transferibles desde actividad-1 a materia.",
      "Ciclo 45: se deduplican variantes semánticamente equivalentes sin recorte de reglas útiles.",
      "Ciclo 45: se mantiene bloqueo de propagación para salidas no parseables.",
      "Ciclo 45: se conserva trazabilidad de citas recurrentes y riesgos de fuente provisional."
    ]
  }
}