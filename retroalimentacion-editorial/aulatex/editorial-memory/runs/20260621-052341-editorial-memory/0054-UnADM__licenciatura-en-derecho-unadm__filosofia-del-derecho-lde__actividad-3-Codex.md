{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 hacia Actividad 3 con deduplicación lossless.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales comunes de la asignatura.",
    "Se mantiene regla crítica: no propagar memorias sin JSON parseable y sin normalización previa.",
    "Se evita traslado de conclusiones específicas o bibliografía exclusiva entre actividades hermanas.",
    "Se refuerza transferencia por patrones reutilizables: estructura, calidad, trazabilidad y LaTeX/BibTeX."
  ],
  "identity_rules": [
    "Mantener tono y formato institucional UnADM.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato de entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo reglas reutilizables de actividades hermanas.",
    "No copiar redacción literal, conclusiones específicas ni bibliografía exclusiva de otra actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Exigir marca de supuesto cuando no exista respaldo local.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar filosofia-del-derecho.bib como canónico [supuesto] hasta verificación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No trasladar automáticamente bibliografía de Semana 7 a Actividad 3 sin confirmar aplicabilidad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales de identidad, estructura y calidad.",
    "Mantener bandera de riesgo cuando existan antecedentes de parseo fallido.",
    "Aplicar unión-dedupe lossless para evitar duplicados sin perder reglas.",
    "No propagar supuestos como hechos confirmados.",
    "Escalar dudas locales como preguntas abiertas en lugar de completar con invención."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 3.",
    "Confirmar formato de entrega requerido en Actividad 3.",
    "Confirmar rúbrica de evaluación específica de Actividad 3.",
    "Confirmar bibliografía obligatoria de la semana correspondiente.",
    "Confirmar si Actividad 3 usa reporte, presentación u otro artefacto principal.",
    "Confirmar nombre canónico final del .bib de asignatura y su uso por actividad."
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
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Trazabilidad entre argumentos y fuentes."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico sólido y verificable.",
      "Integrar fundamento jurídico, evidencia y criterio propio.",
      "Mantener continuidad editorial entre actividades sin contaminación de contenidos específicos."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con respaldo verificable.",
      "Supuestos etiquetados.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Estructura argumentativa jurídica",
        "Análisis propio",
        "Bibliografía verificable",
        "Supuestos marcados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "La pauta institucional define forma y rigor del producto."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica exige evidencia trazable."
        },
        {
          "source": "Supuestos marcados",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos confirmados."
        },
        {
          "source": "Actividad 1",
          "target": "Actividad 3",
          "kind": "develops",
          "justification": "Se transfieren patrones editoriales reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, producto, análisis, conclusión.",
        "Histórico de ciclo exige bloqueo por no-JSON parseable y normalización previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: deduplicación integral de reglas repetidas con equivalencia semántica.",
      "Ciclo 54: retención de reglas críticas de calidad y no regresión.",
      "Ciclo 54: refuerzo lateral controlado sin copiar contenido específico de Actividad 1.",
      "Ciclo 54: mantenimiento de política de supuestos ante falta de consigna local."
    ]
  }
}