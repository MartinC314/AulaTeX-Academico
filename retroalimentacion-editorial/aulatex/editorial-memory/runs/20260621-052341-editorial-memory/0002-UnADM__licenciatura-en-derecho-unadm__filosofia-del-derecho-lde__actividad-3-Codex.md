{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerza la estructura base: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene la regla de normalización: no propagar sin JSON parseable.",
    "Se conserva política de supuestos para datos no confirmados en la consigna local.",
    "Se evita traslado de conclusiones o bibliografía exclusiva de un hermano sin validación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios académicos.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna de Actividad 3.",
    "Tratar memorias editoriales Codex o GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y declarar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de Actividad 1 sin copiar redacción literal.",
    "No trasladar conclusiones específicas entre actividades hermanas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar marca de supuesto en todo dato no verificado.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables y sin renombres innecesarios.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas y nombres de archivo solo con verificación local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en Actividad 3.",
    "Mantener metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar aplicabilidad a Actividad 3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no contenido específico.",
    "Conservar bandera de riesgo cuando existan antecedentes de parseo fallido.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "No propagar supuestos como hechos confirmados.",
    "Reforzar reglas institucionales comunes y mantener especificidad local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de Actividad 3.",
    "Confirmar bibliografía obligatoria de la semana correspondiente.",
    "Confirmar si aplica o no la bibliografía depurada de Semana 7.",
    "Confirmar nombre canónico final del .bib de la asignatura."
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
      "Problema jurídico delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Asegurar coherencia entre identidad institucional, método argumentativo y calidad verificable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos declarados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo consistente -> cierre alineado."
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
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
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
          "justification": "El análisis parte de la delimitación del problema."
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
          "justification": "Las fuentes comprobables sostienen la validez del producto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica con criterio propio.",
        "Programa analítico: ejes de trabajo y propósito de realización.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas sin pérdida semántica.",
      "Ciclo 2: se preservan reglas institucionales y de calidad heredadas.",
      "Ciclo 2: se refuerza transferencia lateral controlada por analogía.",
      "Ciclo 2: se mantienen abiertos los vacíos de consigna para evitar invención."
    ]
  }
}