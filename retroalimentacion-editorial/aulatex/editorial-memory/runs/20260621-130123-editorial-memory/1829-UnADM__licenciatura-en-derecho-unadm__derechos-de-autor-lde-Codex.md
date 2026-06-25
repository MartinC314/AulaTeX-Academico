{
  "summary": [
    "Se consolida sincronización transversal hacia Derechos de autor con enfoque conservador.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se refuerza normalización obligatoria antes de propagación recursiva.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se conserva tratamiento provisional de herencias Codex y GPT-Pro no verificadas.",
    "Se prioriza transferencia de abstracciones reutilizables y no redacción literal entre materias no equivalentes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Mantener enfoque jurídico con criterio propio en la conclusión.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como soporte curricular cuando aplique."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar separación entre reporte, presentación y bibliografía local.",
    "Corregir tokens de plantilla y nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas de cada actividad al .bib local.",
    "No asumir fuentes de semanas distintas sin validación de consigna.",
    "Confirmar que el producto entregado coincide con la consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analítico para tokens sin expandir.",
    "Corregir campos pendientes de plantilla como 'Nombre por definir'.",
    "Mantener normalización manual para contenido heredado de ciclos tempranos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de cargar la plantilla del documento.",
    "Evitar comandos incompletos o paquetes truncados en preámbulo.",
    "No dejar \\usepackage sin argumento.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens $(@{...}.Slug) en README, programa analítico y nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes institucionales o verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de actividad en derechos-de-autor.bib salvo convención local validada.",
    "Asegurar correspondencia bidireccional entre citas y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir lateralmente solo reglas abstractas estables entre materias distintas.",
    "Evitar propagar redacción literal o contenido temático específico de Filosofía del Derecho.",
    "Propagar gates de calidad e identidad institucional como núcleo común.",
    "Mantener bandera de provisionalidad para herencias Codex y GPT-Pro hasta validación local.",
    "Preservar reglas útiles previas sin regresión."
  ],
  "open_questions": [
    "Supuesto: LDE-S5B1 es clave oficial; confirmar en documentos maestros.",
    "Confirmar nombre de figura docente para eliminar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de México debe permanecer fijo en portada.",
    "Confirmar orden correcto de carga de paquetes respecto a template en esta plantilla.",
    "Confirmar cierre definitivo de tokens Slug en README y programa analítico."
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
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 créditos.",
        "Asignatura destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar continuidad editorial entre actividades y materia sin perder identidad local."
    ],
    "style_markers": [
      "Supuestos explícitos.",
      "Secciones funcionales trazables.",
      "Consistencia entre portada, contenido y referencias.",
      "Lenguaje técnico sin rigidez innecesaria."
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
          "justification": "Toda afirmación requiere respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura razonada habilita transferencia profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia editorial de materia",
          "kind": "depends_on",
          "justification": "Portada, metadatos y tono deben permanecer alineados."
        }
      ],
      "evidence": [
        "README de Derechos de autor define ubicación curricular y pauta editorial.",
        "Programa analítico fija ejes problema-conceptos-producto-análisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectaron tokens de plantilla sin expandir y nombres de archivo corruptos.",
        "Se detectó preámbulo LaTeX con comando \\usepackage incompleto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se refuerza núcleo transversal estable sin mover contenido temático específico del origen.",
      "Ciclo 18: se mantienen gates de parseo JSON, estructura mínima y trazabilidad bibliográfica.",
      "Ciclo 18: se preserva política de fuentes heredadas como provisionales.",
      "Ciclo 18: se consolida cerebro editorial mínimo de materia con vacíos locales explícitos."
    ]
  }
}