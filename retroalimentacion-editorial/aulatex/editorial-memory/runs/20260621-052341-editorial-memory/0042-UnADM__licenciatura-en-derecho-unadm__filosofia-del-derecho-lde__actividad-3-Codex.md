{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 hacia Actividad 3 con deduplicación lossless.",
    "Se preserva ADN UnADM: identidad institucional, integridad académica, citas verificables y cierre jurídico propio.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica transferible.",
    "Se conserva política de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar reglas válidas entre actividades hermanas sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva de otra actividad.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato ni tema de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Confirmar que cada afirmación sin respaldo quede marcada como [supuesto]."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves usadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] el .bib canónico filosofia-del-derecho.bib hasta validación final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como [supuesto de uso condicionado] por estar orientado a Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión + deduplicación sin pérdida en cada ciclo.",
    "Mantener bandera de riesgo si hubo incidencias de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 3.",
    "Confirmar formato de entrega de Actividad 3 (reporte, presentación u otro).",
    "Confirmar rúbrica de evaluación específica de Actividad 3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 3 usa bibliografía propia o reutiliza .bib existente.",
    "Confirmar archivo .tex principal canónico para Actividad 3."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Garantizar fundamento jurídico, evidencia verificable y transferencia profesional.",
      "Conservar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con evidencia verificable.",
      "Supuestos etiquetados de forma visible.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis propio -> conclusión jurídica.",
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
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
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
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 42: se consolidan reglas hermanas reutilizables sin copiar contenido específico.",
      "Ciclo 42: se elimina duplicación semántica y se preserva cobertura total.",
      "Ciclo 42: se refuerza uso de supuestos en ausencia de consigna local.",
      "Ciclo 42: se mantiene compatibilidad editorial para propagación recursiva."
    ]
  }
}