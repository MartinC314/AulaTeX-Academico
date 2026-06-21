{
  "summary": [
    "Se consolida refuerzo lateral para actividad-3 con transferencia de patrones reutilizables desde actividad-1.",
    "Se mantiene compresión lossless por unión y deduplicación sin recorte de reglas útiles.",
    "Se preservan ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerza política de supuestos para datos no visibles en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
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
    "Heredar reglas válidas entre actividades hermanas sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva de otra actividad.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar acentos y codificación española correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas y nombres solo con verificación local.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas realmente citadas.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo cuando exista historial de salida no estructurada.",
    "Aplicar deduplicación semántica conservando cobertura total de reglas.",
    "Priorizar identidad, estructura, calidad y relaciones conceptuales sobre contenido puntual."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3.",
    "Confirmar rúbrica específica de evaluación de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 reutiliza bibliografía depurada de Semana 7 [supuesto].",
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
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina y evidencia pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Normalización estructurada como condición de memoria confiable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Conservar coherencia institucional entre actividades hermanas.",
      "Garantizar transferencia editorial sin pérdida ni contaminación temática."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre jurídico con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
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
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y rigor formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay trazabilidad ni control editorial."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se articula desde un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica con criterio propio.",
        "Programa analítico: ejes de trabajo y propósito de transformación del producto.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: refuerzo lateral aplicado por analogía controlada entre nodos hermanos.",
      "Se eliminaron duplicados formales y se conservaron todas las reglas útiles.",
      "Se evitó transferencia de conclusiones o bibliografía exclusiva de actividad-1.",
      "Se añadieron marcas de supuesto donde faltan datos locales verificables."
    ]
  }
}