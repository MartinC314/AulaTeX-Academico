{
  "summary": [
    "Se consolida sincronización transversal conservadora entre Filosofía del Derecho y Derechos de autor.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y control de calidad por JSON.",
    "Se refuerza transferencia por abstracciones reutilizables y no por redacción literal.",
    "Se mantiene compresión lossless por unión y deduplicación sin regresión.",
    "Se detectan vacíos locales del destino y se dejan como preguntas abiertas con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho con datos curriculares locales del destino.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar herencias Codex y GPT-Pro como provisionales hasta validación local.",
    "Sostener integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Corregir tokens de plantilla y nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar bibliografía específica por actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias sin confirmación local."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación sensible.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analítico para tokens sin expandir.",
    "Corregir campos pendientes en portada antes de versión final."
  ],
  "latex_rules": [
    "Mantener codificación y acentos correctos en español.",
    "Declarar macros de metadatos antes de cargar plantilla.",
    "Evitar comandos incompletos o paquetes sin argumento.",
    "Mover paquetes al preámbulo efectivo según plantilla.",
    "Compilar sin errores críticos, referencias rotas ni rutas inválidas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables y verificables.",
    "Priorizar materiales institucionales UnADM y fuentes jurídicas confiables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir fecha de consulta en recursos web.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "Evitar transferir contenido temático específico de Filosofía del Derecho al destino.",
    "Mantener bandera de normalización manual para herencia histórica no estructurada.",
    "No propagar datos personales del alumno entre nodos.",
    "Registrar mejoras verificables en cada ciclo sin eliminar reglas útiles previas."
  ],
  "open_questions": [
    "Supuesto: clave LDE-S5B1 sigue vigente; confirmar en documentación oficial.",
    "Confirmar nombre de figura docente para reemplazar marcador pendiente.",
    "Confirmar si ubicacion institucional en portada debe fijarse o variar por actividad.",
    "Confirmar orden definitivo de paquetes LaTeX respecto a \\input{template}.",
    "Confirmar retiro o conservación de advertencias históricas Codex/GPT-Pro tras validación local."
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
        "Entrada canónica por carpeta de asignatura.",
        "Normalización estructurada previa a propagación.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derechos de autor.",
        "Semestre 5, bloque 1, obligatoria, 8 créditos."
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
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Preservar coherencia editorial transversal en la suite LaTeX de UnADM."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte dato local.",
      "Secciones funcionales y trazables.",
      "Correspondencia estricta entre texto, citas y bibliografía."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Análisis con postura propia.",
      "Cierre con implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad bibliográfica",
        "Propagación segura"
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
          "justification": "Reduce herencia de salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliográfica",
          "kind": "supports",
          "justification": "Toda afirmación debe mapear a cita rastreable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada produce utilidad profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagación segura",
          "kind": "depends_on",
          "justification": "La consistencia editorial habilita sincronización transversal."
        }
      ],
      "evidence": [
        "README del destino define ubicación curricular y pauta editorial.",
        "Programa analítico del destino fija ejes problema-conceptos-producto-análisis-cierre.",
        "Archivo derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectan tokens sin expandir y líneas corruptas en estructura local.",
        "Se detecta preámbulo LaTeX con comando \\usepackage incompleto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se consolidan abstracciones estables transversales sin mover contenido temático específico.",
      "Ciclo 9: se refuerza gate de JSON parseable como condición de propagación recursiva.",
      "Ciclo 9: se preservan reglas previas útiles y se eliminan duplicados semánticos.",
      "Ciclo 9: se mantienen fuentes heredadas como provisionales hasta validación local."
    ]
  }
}