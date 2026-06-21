{
  "summary": [
    "Se consolida refuerzo lateral para actividad-3 con deduplicación lossless y sin regresión.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica: normalizar y validar JSON parseable antes de propagación recursiva.",
    "Se conserva política de supuestos: no inventar consigna, formato ni bibliografía específica de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1, sin copiar redacción literal.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otra semana aplica a actividad-3 sin confirmación.",
    "Registrar diferencias de actividad-3 como [supuesto] hasta validar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir evidencia académica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar rutas y nombres de archivo antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Transferir a hermanos reglas institucionales, estructura, calidad y patrones argumentativos.",
    "No propagar conclusiones específicas ni bibliografía exclusiva de una actividad hermana.",
    "Mantener compresión por unión+dedeuplicación lossless, sin recorte semántico.",
    "Preservar bandera de riesgo cuando existan antecedentes de parseo fallido.",
    "Cuando falten datos locales, propagar plantilla base con preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido (reporte, presentación u otro).",
    "Confirmar rúbrica específica de evaluación para actividad-3.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica u otro tema.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-3 [supuesto actual: no confirmado].",
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
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Asegurar transferibilidad profesional del cierre argumentativo.",
      "Estandarizar calidad editorial entre actividades hermanas sin perder contexto local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Marcado explícito de [supuesto] cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
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
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Bibliografía verificable",
          "kind": "depends_on",
          "justification": "La trazabilidad de reglas y fuentes requiere estructura parseable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis surge de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        },
        {
          "source": "Política de supuestos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita presentar inferencias no verificadas como hechos."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y cierre jurídico propio.",
        "Programa analítico: ejes de trabajo y propósito de transformación de productos.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Nota local: bibliografía clean orientada a Semana 7; aplicación a actividad-3 no confirmada [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicación completa de reglas repetidas con preservación semántica.",
      "Ciclo 17: se refuerza transferencia lateral controlada solo de patrones reutilizables.",
      "Ciclo 17: se mantiene no regresión en calidad, LaTeX y bibliografía.",
      "Ciclo 17: se conservan preguntas abiertas donde faltan datos locales verificables."
    ]
  }
}