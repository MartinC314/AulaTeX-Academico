{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 a actividad-3 con deduplicación lossless.",
    "Se preservan reglas útiles previas sin regresión ni copia literal de contenidos específicos.",
    "Se mantiene núcleo editorial: problema, conceptos y fuentes, análisis propio y conclusión jurídica transferible.",
    "Se refuerza normalización obligatoria: bloquear propagación si no hay JSON parseable.",
    "Se mantiene política de supuestos para datos no confirmados en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar patrones reutilizables de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas de un nodo hermano.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de reutilizar memoria.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Exigir marca de supuesto en todo dato no verificado localmente.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como supuesto canónico filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo entradas realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de asignatura y bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de actividad-3 [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validación estructural y JSON parseable.",
    "Transferir a nodos hermanos solo reglas generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión más deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando exista antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar bibliografía obligatoria de la semana de actividad-3.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-3 [supuesto].",
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos y fuentes pertinentes con respaldo verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional.",
      "Normalización estructurada previa a toda propagación."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros, sustentados y transferibles.",
      "Asegurar consistencia institucional y metodológica entre actividades hermanas.",
      "Preservar memoria editorial útil sin pérdida ni regresión."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas visibles en afirmaciones relevantes.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
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
        "filosofia-del-derecho-clean.bib [uso condicionado][supuesto]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y formato académico."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
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
          "justification": "La conclusión válida depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las fuentes comprobables sostienen la trazabilidad del texto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema, conceptos, producto, análisis y conclusión.",
        "Regla persistente: no propagar sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 30: se deduplican reglas repetidas de origen y destino sin pérdida.",
      "Ciclo 30: se conserva política de no regresión y de supuestos explícitos.",
      "Ciclo 30: se refuerza transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 30: se mantiene separación entre memoria editorial y evidencia académica."
    ]
  }
}