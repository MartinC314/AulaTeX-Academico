{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reutilizable desde actividad-1.",
    "Se mantiene identidad UnADM, contexto curricular y ejes editoriales sin regresión.",
    "Se refuerza normalización JSON obligatoria antes de propagación recursiva.",
    "Se conserva política de supuestos para datos no visibles en la consigna.",
    "Se aplica deduplicación lossless de reglas y patrones argumentativos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Registrar incidencias de parseo como metadato técnico, no como evidencia disciplinar."
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
    "Heredar reglas válidas de actividades hermanas sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva no verificada para actividad-3.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana temática ni formato final sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar rutas y nombres de archivo antes de referenciarlos en documentos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales normativos, doctrinales o jurisprudenciales pertinentes.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y argumentación.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo cuando existan antecedentes de salida no estructurada.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Priorizar refuerzo lateral entre actividades de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3 (reporte, presentación u otro).",
    "Confirmar rúbrica específica de evaluación de actividad-3.",
    "Confirmar bibliografía obligatoria local de actividad-3.",
    "Supuesto: la bibliografía depurada de Semana 7 puede no aplicar a actividad-3; validar.",
    "Confirmar nombre canónico final del .bib operativo de la asignatura."
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
      "Problema jurídico o social delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Disciplina técnica en normalización y trazabilidad."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar fundamento jurídico con evidencia verificable.",
      "Sostener continuidad editorial entre actividades sin pérdida de reglas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmaciones relevantes con cita.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre orientado a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre verificable."
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
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad académica y citas comprobables."
        },
        {
          "source": "Normalización JSON",
          "target": "Política de supuestos",
          "kind": "depends_on",
          "justification": "La trazabilidad de supuestos requiere estructura parseable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión robusta depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "Pauta editorial de README: identidad, integridad, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes de problema, conceptos, producto, análisis y cierre.",
        "Regla persistente de calidad: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: deduplicación lossless aplicada sin eliminar reglas útiles.",
      "Ciclo 41: reforzada normalización estructurada previa a propagación recursiva.",
      "Ciclo 41: transferidos patrones reutilizables desde nodo hermano sin copiar contenido específico.",
      "Ciclo 41: mantenida separación entre evidencia académica y metadatos editoriales provisionales."
    ]
  }
}