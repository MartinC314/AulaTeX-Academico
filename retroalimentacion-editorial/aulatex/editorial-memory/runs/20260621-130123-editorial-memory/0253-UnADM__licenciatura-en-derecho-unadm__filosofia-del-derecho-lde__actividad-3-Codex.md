{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y control de calidad sin regresión.",
    "Se aplica deduplicación lossless y se eliminan duplicados semánticos.",
    "Se mantiene política de supuestos para todo dato no confirmado en consigna local.",
    "Se refuerza que la propagación recursiva depende de JSON parseable y estructura mínima completa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas del nodo hermano sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato ni bibliografía específica de Actividad 3 sin evidencia local.",
    "Registrar diferencias locales como supuestos hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No renombrar archivos o rutas sin verificación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales normativos, doctrinales o jurisprudenciales verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo entradas efectivamente citadas.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como uso condicionado por consigna [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar conclusiones temáticas específicas entre actividades hermanas.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener compresión por unión y deduplicación sin pérdida.",
    "Conservar bandera de riesgo cuando existan antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido en Actividad 3 (reporte, presentación u otro).",
    "Confirmar rúbrica de evaluación específica de Actividad 3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica a Actividad 3 [supuesto].",
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
      "Transformar la planeación semanal en productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Mantener continuidad editorial entre actividades sin contaminar contenido específico.",
      "Garantizar consistencia metodológica y trazabilidad de evidencia."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con evidencia verificable.",
      "Supuestos marcados de forma explícita.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo alineado -> cierre consistente."
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
        "No regresión editorial"
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
          "target": "No regresión editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite preservar reglas sin pérdida."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis sólido requiere delimitación previa del problema."
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
          "justification": "La verificación de fuentes evita afirmaciones sin respaldo."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, evidencia, análisis y cierre.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se transfiere patrón lateral reusable desde Actividad 1 a Actividad 3.",
      "Ciclo 20: se deduplican reglas repetidas en acentuación y forma sin pérdida de significado.",
      "Ciclo 20: se preservan controles de calidad y política de supuestos.",
      "Ciclo 20: no se transfieren conclusiones temáticas ni bibliografía exclusiva de hermano a hermano."
    ]
  }
}