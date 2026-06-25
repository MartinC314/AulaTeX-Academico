{
  "summary": [
    "Memoria de actividad-3 consolidada con deduplicación lossless y sin regresión.",
    "Se refuerza transferencia lateral de patrones reutilizables desde actividad-1.",
    "Se mantiene identidad UnADM, estructura argumentativa base y control de supuestos.",
    "Se preserva bloqueo de propagación cuando no haya JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, consigna o formato de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y memoria editorial."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar al .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad de interpretación jurídica (Semana 7) y su uso en actividad-3 requiere confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar conclusiones específicas ni bibliografía exclusiva de otra actividad.",
    "Mantener bandera de riesgo cuando existan incidencias previas de parseo.",
    "Aplicar compresión por unión y deduplicación sin pérdida semántica.",
    "Cuando falten datos locales, propagar preguntas abiertas en lugar de contenido inventado."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3 (reporte, presentación u otro).",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar bibliografía obligatoria de la semana correspondiente.",
    "Confirmar si actividad-3 usa bibliografía base o requiere .bib específico.",
    "Confirmar nombre final canónico del .bib operativo en esta actividad."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con fundamento jurídico.",
      "Asegurar evidencia verificable y coherencia argumentativa.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminar contenido específico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo consistente -> cierre verificable."
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
          "justification": "La pauta institucional exige evidencia verificable y rigor formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Política de supuestos",
          "kind": "supports",
          "justification": "La estructura obliga a declarar incertidumbre en vez de inventar datos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida deriva de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Sin fuentes comprobables no hay trazabilidad académica."
        }
      ],
      "evidence": [
        "README: identidad UnADM e integridad académica.",
        "Programa analítico: ejes problema-conceptos-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Contexto local: tokens Slug sin expandir en README/programa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicación completa de reglas repetidas con conservación semántica.",
      "Ciclo 22: refuerzo lateral de estructura argumentativa común entre actividades hermanas.",
      "Ciclo 22: mantenimiento explícito de no regresión y control de supuestos.",
      "Ciclo 22: preservación de separación entre memoria editorial y evidencia académica."
    ]
  }
}