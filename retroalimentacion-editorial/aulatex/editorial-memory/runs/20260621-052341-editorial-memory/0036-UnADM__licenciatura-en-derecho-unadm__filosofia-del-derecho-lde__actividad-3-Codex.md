{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se mantiene compresión lossless por unión y deduplicación sin recorte de reglas útiles.",
    "Se refuerza identidad UnADM, estructura argumentativa y control de supuestos.",
    "Se preserva bloqueo de propagación ante salida no JSON parseable.",
    "Se normaliza referencia canónica de bibliografía por Slug: filosofia-del-derecho.bib [supuesto verificado por README con token]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente académica.",
    "Registrar incidencias técnicas de parseo sin convertirlas en evidencia disciplinar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato exigido por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato ni bibliografía específica de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar filosofia-del-derecho.bib como archivo canónico [supuesto fuerte por Slug en README]."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en actividad-3.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar conclusiones temáticas específicas entre actividades hermanas.",
    "Mantener bandera de riesgo cuando exista historial de salida no estructurada.",
    "Aplicar deduplicación semántica por equivalencia ortográfica y acentual.",
    "Escalar primero reglas institucionales y de calidad; luego reglas locales condicionadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica a actividad-3 [supuesto].",
    "Confirmar archivo .tex principal real de actividad-3 en repositorio.",
    "Confirmar fuentes obligatorias semanales no visibles en contexto local."
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
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en producto académico verificable.",
      "Garantizar trazabilidad entre argumento, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades sin contaminación temática."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas con orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre aplicable a práctica jurídica.",
      "Consistencia entre README, programa analítico y entrega."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre verificable."
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
        "filosofia-del-derecho-clean.bib [uso condicionado, supuesto]"
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
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes de trabajo y propósito de realización.",
        "Regla persistente: bloquear propagación si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: deduplicación ortográfica y semántica aplicada sin pérdida.",
      "Ciclo 36: se conservan reglas de no regresión y normalización obligatoria.",
      "Ciclo 36: se restringe transferencia a patrones reutilizables entre nodos hermanos.",
      "Ciclo 36: se mantienen supuestos abiertos donde faltan datos locales."
    ]
  }
}