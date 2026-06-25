{
  "summary": [
    "Se consolida sincronización transversal conservadora para Derechos de autor con identidad UnADM.",
    "Se preserva compresión lossless por unión y deduplicación sin recorte.",
    "Se mantiene regla crítica: no propagar salidas no estructuradas sin normalización.",
    "Se refuerzan ejes estables transferibles: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se marcan como provisionales las herencias no verificadas localmente (Codex, GPT-Pro).",
    "Se prioriza estructura reusable y gates de calidad sobre redacción literal de actividad origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener enfoque jurídico con criterio propio en la conclusión."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Conservar separación entre reporte, presentación y bibliografía.",
    "Normalizar nombres de archivo con slug canónico de asignatura.",
    "Corregir tokens de plantilla no resueltos en README y programa analítico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Agregar fuentes específicas por actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa por caracteres anómalos y marcadores de plantilla.",
    "Corregir campos pendientes de plantilla antes de publicar."
  ],
  "latex_rules": [
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de cargar plantilla base cuando aplique.",
    "Evitar comandos incompletos o paquetes sin argumento.",
    "Mover paquetes al preámbulo efectivo según plantilla.",
    "Compilar sin errores críticos, referencias rotas ni tokens sin expandir.",
    "No propagar datos personales entre materias."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y normativas jurídicas vigentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Mantener claves BibTeX estables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo abstracciones editoriales estables.",
    "Evitar transferencia de redacción literal entre nodos no equivalentes.",
    "Preservar reglas útiles previas sin regresión.",
    "Mantener bandera de normalización manual para herencia de ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar si clave LDE-S5B1 es oficial en toda la suite. [Supuesto]",
    "Definir nombre de figura docente en plantilla de reporte.",
    "Validar si ubicación institucional debe permanecer fija en portada. [Supuesto]",
    "Confirmar sustitución total de tokens $(@{...}.Slug) por nombres canónicos.",
    "Confirmar si se mantiene `derechos-de-autor.bib` como archivo canónico único."
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
        "Entrada canónica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Sostener consistencia editorial transversal en la suite."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente.",
      "Usar secciones funcionales y trazables.",
      "Mantener coherencia entre portada, cuerpo y referencias.",
      "Normalizar antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Análisis con postura propia.",
      "Cierre con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad bibliográfica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Toda afirmación debe tener respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada fortalece la aplicabilidad profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia editorial transversal",
          "kind": "supports",
          "justification": "Unifica tono, formato y criterio entre nodos."
        }
      ],
      "evidence": [
        "README de la materia define ubicación curricular y pauta editorial.",
        "Programa analítico fija ejes de trabajo reutilizables.",
        "Bib local contiene base institucional verificable.",
        "Se detectaron tokens y nombres corruptos que exigen normalización previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se preservan reglas válidas previas sin eliminación.",
      "Ciclo 3: se deduplican reglas repetidas y se mantienen como abstracciones estables.",
      "Ciclo 3: se refuerza gate de JSON parseable como condición de propagación.",
      "Ciclo 3: se mantiene estado provisional de herencias no verificadas."
    ]
  }
}