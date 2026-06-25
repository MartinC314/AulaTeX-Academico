{
  "summary": [
    "Se consolida memoria lateral para Actividad 8 con transferencia reutilizable desde Actividad 1.",
    "Se preservan reglas válidas previas y se refuerza normalización estructurada obligatoria.",
    "Se mantiene identidad institucional UnADM y contexto curricular común entre asignaturas.",
    "Se transfieren ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita copiar conclusiones o bibliografía exclusiva del origen por regla de salto lateral.",
    "Se agrega mejora verificable: resolver tokens Slug sin expandir en README y programa analítico.",
    "Se agrega mejora verificable: registrar y gestionar duplicados BibTeX como alias trazables sin inventar fuentes.",
    "Supuesto: no se cuenta con consigna textual de Actividad 8 en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre jurídico.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular cuando aplique."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable.",
    "Usar el esquema canónico completo sin omitir secciones.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Integrar conceptos, normas o doctrina pertinentes antes de concluir.",
    "Ajustar el artefacto al formato solicitado en la actividad.",
    "No asumir fuentes de otras semanas sin validación en la consigna local.",
    "Supuesto: si falta consigna, usar estructura base y abrir preguntas de validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar ausencia de afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas durante la fusión.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria previa."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Mantener consistencia de nombres de archivos .tex y .bib según slug de la materia."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar duplicados BibTeX como alias trazables antes de normalizar claves.",
    "Supuesto: existe entrada truncada en etica-y-moral-juridica.bib y debe corregirse antes de compilar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Mantener bandera de normalización manual mientras persistan salidas no estructuradas en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8 y producto solicitado.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar lista canónica de claves BibTeX para una clave principal por obra y alias trazables.",
    "Confirmar corrección de la entrada truncada sierraUniversidadNacional1910 en el .bib.",
    "Confirmar si Actividad 8 requiere reporte, presentación u otro formato principal."
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
        "Asignatura destino: Ética y Moral jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Asegurar trazabilidad editorial y calidad técnica en LaTeX y bibliografía.",
      "Permitir propagación segura entre nodos mediante normalización estructurada."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin inventar fuentes ni datos no verificables.",
      "Sin copia literal de redacción entre nodos laterales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Definir marco conceptual y normativo antes del análisis.",
      "Contrastar postura propia con evidencia verificable.",
      "Cerrar con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Ejes editoriales de actividad",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Ética y moral jurídica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define estructura y criterios mínimos de entrega."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia segura entre nodos."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Claves estables y metadatos completos reducen errores y mejoran verificabilidad."
        },
        {
          "source": "Ejes editoriales de actividad",
          "target": "Ética y moral jurídica",
          "kind": "develops",
          "justification": "Los cinco ejes operan como patrón transversal entre asignaturas del mismo bloque."
        }
      ],
      "evidence": [
        "README.md de etica-y-moral-juridica-lde define identidad, ubicación curricular y pauta editorial.",
        "programa-analitico-etica-y-moral-juridica.md define propósito y cinco ejes de trabajo.",
        "etica-y-moral-juridica.bib evidencia duplicados de claves y una entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se transfiere patrón institucional y estructural común desde Filosofía del Derecho.",
      "Ciclo 1: se refuerza gate de JSON parseable como condición de propagación.",
      "Ciclo 1: se añade control de tokens Slug sin expandir como mejora técnica verificable.",
      "Ciclo 1: se mantiene política de no inventar fuentes y de marcar supuestos."
    ]
  }
}