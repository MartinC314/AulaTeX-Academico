{
  "summary": [
    "Se consolida memoria lateral para Actividad 2 con base parseable del origen y contexto local del destino.",
    "Se preservan reglas útiles previas y se deduplican sin recorte semántico.",
    "Se refuerza identidad UnADM y ubicación curricular común entre asignaturas hermanas.",
    "Se transfiere patrón editorial reusable: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica de normalización: no propagar salidas no parseables.",
    "Se confirma en destino la necesidad de resolver tokens Slug sin expandir en README y programa analítico.",
    "Se mantiene supuesto verificable de duplicados bibliográficos en el .bib local con política de alias pendiente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque de la asignatura Etica y Moral juridica en toda adaptación local.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como base de ubicación curricular."
  ],
  "structure_rules": [
    "Entregar siempre JSON válido y parseable en memoria editorial.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad de cambios por ciclo y por nodo."
  ],
  "activity_rules": [
    "Alinear cada actividad al eje: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores sin validación de consigna local.",
    "Ajustar profundidad argumentativa a la rúbrica disponible o marcar ausencia como supuesto."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresiones: no eliminar reglas útiles previamente consolidadas.",
    "Aplicar compresión lossless por unión y deduplicación."
  ],
  "latex_rules": [
    "Usar codificación UTF-8 y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Conservar como entradas canónicas reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Deduplicar obras equivalentes con distinta clave sin perder trazabilidad.",
    "Supuesto: mantener alias de claves duplicadas hasta definir política editorial definitiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos laterales solo patrones reutilizables, no redacción literal.",
    "Cuando falte consigna textual local, propagar estructura base y abrir preguntas.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad de asignatura.",
    "Aplicar normalización manual inmediata al detectar salida no estructurada en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 2 para ajustar tipo de producto.",
    "Confirmar rúbrica de evaluación específica de Actividad 2.",
    "Confirmar si Actividad 2 requiere reporte, presentación u otro formato.",
    "Confirmar política editorial final para claves BibTeX duplicadas como alias.",
    "Confirmar si existe listado de fuentes obligatorias por semana para Etica y Moral juridica."
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
        "Asignatura: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Fuentes verificables y cita explícita.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica profesional."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros y verificables.",
      "Asegurar fundamento jurídico, evidencia y criterio propio en cada entrega.",
      "Preservar continuidad editorial entre actividades y asignaturas hermanas sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados explícitamente.",
      "Sin inventar fuentes ni metadatos.",
      "Trazabilidad por ciclo, origen y destino."
    ],
    "argumentative_patterns": [
      "Abrir con encuadre del problema.",
      "Delimitar objetivo de la actividad.",
      "Desarrollar marco conceptual y normativo.",
      "Sostener una postura propia con evidencia.",
      "Cerrar con conclusión jurídica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ubicación curricular común",
        "Problema jurídico o social",
        "Marco conceptual y doctrinal",
        "Evidencia verificable",
        "Postura argumentada",
        "Conclusión transferible",
        "Normalización JSON",
        "Deduplicación bibliográfica con alias"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de etica-y-moral-juridica-lde",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ubicación curricular común",
          "kind": "supports",
          "justification": "La consistencia institucional fija tono, formato y contexto académico."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Postura argumentada",
          "kind": "depends_on",
          "justification": "La postura se construye desde un problema delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional requiere sustento comprobable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Deduplicación bibliográfica con alias",
          "target": "Estabilidad LaTeX",
          "kind": "supports",
          "justification": "Reduce conflicto de claves sin romper citas heredadas."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, ubicación curricular y pauta editorial.",
        "Programa analítico local define propósito y ejes de trabajo reutilizables.",
        ".bib local muestra duplicados de obras con claves distintas [supuesto verificado por metadatos repetidos].",
        "Memoria origen valida patrón estructural transversal en asignaturas de Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se integra patrón transversal desde Filosofía del Derecho hacia Etica y Moral juridica.",
      "Ciclo 1: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 1: se añade refuerzo técnico para tokens Slug sin expandir en archivos guía.",
      "Ciclo 1: se conserva política de no recorte y deduplicación lossless."
    ]
  }
}