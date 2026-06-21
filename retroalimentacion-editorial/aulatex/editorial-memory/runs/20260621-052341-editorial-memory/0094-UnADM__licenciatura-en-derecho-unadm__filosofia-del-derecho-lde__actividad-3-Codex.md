{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-3 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene bloqueo de propagación ante salidas no JSON parseable y exigencia de normalización previa.",
    "Se conserva política de supuestos: no inventar consigna, formato ni bibliografía específica de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, forma y propósito.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si no hay consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo de cada afirmación o marcarla como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas/normativas/jurisprudenciales de antecedentes editoriales.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos, referencias rotas ni rutas inválidas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Agregar al .bib solo entradas realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar aplicabilidad en actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no contenido específico.",
    "Aplicar unión + deduplicación lossless en cada ciclo.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando exista antecedente de salida no estructurada.",
    "Reforzar reglas institucionales comunes y mantener especificidad local cuando exista evidencia."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar bibliografía obligatoria de la semana de actividad-3.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica o a otro tema.",
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Análisis propio con postura académica.",
      "Evidencia verificable y trazable.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Mantener continuidad editorial entre actividades hermanas sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con cita verificable.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Ejes editoriales estables",
        "Supuestos controlados",
        "Bibliografía verificable",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Ejes editoriales estables",
          "kind": "supports",
          "justification": "La pauta institucional define problema, evidencia, análisis propio y cierre jurídico."
        },
        {
          "source": "Normalización JSON",
          "target": "Ejes editoriales estables",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagación confiable de reglas."
        },
        {
          "source": "Supuestos controlados",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "Evita inventar fuentes y mantiene trazabilidad."
        },
        {
          "source": "Ejes editoriales estables",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre depende de un análisis sustentado y no descriptivo."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 94: deduplicación completa de reglas repetidas en destino.",
      "Ciclo 94: refuerzo lateral de estructura argumentativa base desde actividad-1.",
      "Ciclo 94: conservación explícita de política de no invención y de supuestos marcados.",
      "Ciclo 94: mantenimiento de compresión lossless por unión sin recorte de reglas útiles."
    ]
  }
}