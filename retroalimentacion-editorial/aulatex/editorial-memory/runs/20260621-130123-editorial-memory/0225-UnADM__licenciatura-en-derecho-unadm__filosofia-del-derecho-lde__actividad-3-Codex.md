{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-3 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se conserva política de supuestos para datos no confirmados en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas del nodo hermano sin copiar redacción literal.",
    "No trasladar conclusiones específicas de actividad-1 a actividad-3.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib puede no aplicar a actividad-3 si corresponde a otra semana."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Ante salidas no estructuradas, aplicar normalización manual previa.",
    "Mantener compresión por unión y deduplicación sin recorte semántico."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 usa bibliografía depurada de Semana 7 o requiere otra.",
    "Confirmar archivo .tex principal de actividad-3."
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
        "Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Consistencia entre consigna, desarrollo y cierre."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial sin perder adaptación por actividad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre con implicación jurídica práctica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo alineado -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Supuestos explícitos"
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
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de la delimitación del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La evidencia trazable evita afirmaciones infundadas."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-análisis-cierre.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Token Slug sin expandir detectado en README y programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicación de reglas repetidas sin pérdida de contenido útil.",
      "Ciclo 13: refuerzo lateral de patrones institucionales y de calidad.",
      "Ciclo 13: preservación de política de supuestos y no invención de fuentes.",
      "Ciclo 13: mantenimiento de no regresión y compresión lossless."
    ]
  }
}