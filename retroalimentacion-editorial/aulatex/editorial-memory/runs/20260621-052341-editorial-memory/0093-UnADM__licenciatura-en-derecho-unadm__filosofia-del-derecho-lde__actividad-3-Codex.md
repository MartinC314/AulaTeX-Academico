{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar contenido específico.",
    "Se preservan reglas institucionales UnADM, estructura base y compresión lossless por deduplicación.",
    "Se mantiene bloqueo de propagación cuando no hay JSON parseable.",
    "Se refuerza política de supuestos para datos no confirmados de actividad-3.",
    "Se corrige alcance: transferir patrones reutilizables, no conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memoria editorial heredada como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y etiquetar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin eliminar reglas útiles previas.",
    "No copiar redacción literal ni conclusiones específicas entre nodos hermano.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Confirmar marca de supuesto en toda inferencia no verificada.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: conservar reglas útiles existentes."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves usadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas o nombres de archivo solo con verificación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como uso condicionado por tema y consigna [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de normalización y validación JSON.",
    "Transferir solo patrones estables: identidad, estructura, calidad, conceptos recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Propagar reglas específicas de Filosofía del Derecho solo dentro de la misma asignatura.",
    "Registrar incidencias de parseo como riesgo técnico, no como evidencia académica."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar bibliografía obligatoria de actividad-3.",
    "Confirmar si aplica bibliografía de interpretación jurídica de Semana 7 [supuesto].",
    "Confirmar nombre canónico final del .bib de la asignatura tras resolver token Slug."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico.",
      "Asegurar coherencia entre problema, evidencia, análisis y cierre.",
      "Mantener continuidad editorial entre actividades sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos etiquetados.",
      "Citas verificables por afirmación relevante.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
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
          "justification": "La pauta institucional exige citas verificables y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Política de supuestos",
          "kind": "supports",
          "justification": "La estructura obliga a distinguir dato confirmado de supuesto."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere delimitación inicial del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida se deriva de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Sin fuentes comprobables no hay trazabilidad académica."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, producto, análisis y cierre.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Token Slug sin expandir detectado en README y programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 93: deduplicación lossless aplicada sin eliminar reglas útiles.",
      "Ciclo 93: se transfiere solo patrón reusable de nodo hermano.",
      "Ciclo 93: se evita copiar bibliografía o conclusiones específicas de actividad-1.",
      "Ciclo 93: se mantiene riesgo técnico por parseo como control de calidad persistente."
    ]
  }
}