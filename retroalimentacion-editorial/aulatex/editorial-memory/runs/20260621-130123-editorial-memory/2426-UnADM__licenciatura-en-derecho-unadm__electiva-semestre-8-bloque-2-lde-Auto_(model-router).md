{
  "summary": [
    "Memoria de materia consolidada para Electiva Semestre 8 Bloque 2 con identidad UnADM.",
    "Sincronización transversal aplicada desde Filosofía del Derecho solo con abstracciones estables.",
    "Se preservan reglas institucionales de normalización, integridad académica y trazabilidad bibliográfica.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho sin validación local.",
    "Se refuerza el eje editorial: problema, conceptos, fuentes, análisis propio y conclusión jurídica transferible.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "La herencia histórica no estructurada se conserva como provisional hasta revisión manual.",
    "El alumno confirmado es Martin Jonathan de la Cruz, matrícula ES2611202040.",
    "La materia destino conserva código LDE-S8B2 y ubicación curricular semestre 8, bloque 2, tipo Electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos del reporte.",
    "Fijar autor Martin Jonathan de la Cruz y matrícula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] todo dato institucional no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "No trasladar ubicación curricular de otra materia al destino.",
    "Citar la malla curricular de Derecho solo para ubicación curricular verificable."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación semanal en entregables concretos.",
    "Alinear la entrega al producto solicitado por la consigna vigente.",
    "Incluir cierre argumentativo transferible a la práctica jurídica.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y archivo .bib local.",
    "Corregir placeholders de plantillas en nombres de archivo y referencias.",
    "Restaurar nombres truncados en listados de estructura antes de entrega."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Incluir análisis jurídico propio, no solo resumen de fuentes.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar cada actividad con conclusión aplicable a la práctica jurídica.",
    "No asumir fuentes de otra semana sin confirmación local.",
    "No trasladar contenido específico de otra materia sin fuente verificable.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Ajustar formato final a reporte, presentación o producto visual según consigna."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia con metadatos institucionales.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Reemplazar Actividad X por el número real de actividad antes de entrega.",
    "Completar figura docente solo con dato confirmado.",
    "Completar créditos solo con dato confirmado.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad de nombres de archivos entre .tex y recursos de la materia.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Marcar como [supuesto] cualquier dato bibliográfico no confirmado.",
    "No asumir bibliografía específica de Filosofía del Derecho para la electiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y sin ambigüedad.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias.",
    "Etiquetar reglas de integridad académica como transversales UnADM.",
    "No propagar datos incompletos de créditos o figura docente.",
    "Mantener etiqueta de herencia provisional hasta revisión manual.",
    "Usar ciclo 1 como etapa de normalización, no como evidencia definitiva.",
    "Propagar la corrección de placeholders como lección transversal de generación.",
    "Aplicar compresión por unión y deduplicación sin eliminar reglas útiles.",
    "No reducir especificidad local al incorporar reglas heredadas."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar consignas concretas de actividades de la electiva.",
    "[supuesto] Confirmar rúbricas específicas antes de ajustar profundidad argumentativa.",
    "[supuesto] Confirmar fuentes obligatorias de cada semana.",
    "[supuesto] Confirmar si el sitio institucional UnADM debe citarse con fecha de consulta actualizada.",
    "[supuesto] Confirmar si el año 2026 del sitio UnADM en .bib es correcto o placeholder.",
    "[supuesto] Confirmar política institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar nombres reales de carpetas de referencias si existen.",
    "[supuesto] Confirmar si reporte y presentación son obligatorios para todas las actividades."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Metadatos institucionales consistentes.",
        "Control explícito de supuestos.",
        "Trazabilidad entre documentos locales.",
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Electiva Semestre 8 Bloque 2.",
        "Semestre 8.",
        "Bloque 2.",
        "Tipo Electiva.",
        "Código de curso LDE-S8B2.",
        "[supuesto] Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad cita-texto-bib.",
      "Control de supuestos.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Evitar entregas descriptivas sin juicio jurídico propio.",
      "Garantizar correspondencia entre consigna, desarrollo, citas y conclusión.",
      "Proteger la memoria editorial contra herencias no verificadas."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones explícitas y ordenadas.",
      "Marco conceptual, normativo o doctrinal visible.",
      "Postura propia respaldada.",
      "Citas verificables.",
      "Cierre con transferencia profesional.",
      "Marcado explícito de [supuesto].",
      "Metadatos UnADM consistentes.",
      "Lenguaje jurídico claro."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> conceptos -> fuentes -> análisis propio -> conclusión.",
      "Hecho o consigna -> norma o doctrina -> razonamiento -> consecuencia jurídica.",
      "Afirmación -> fuente verificable -> interpretación propia.",
      "Dato no confirmado -> marca [supuesto] -> pregunta abierta.",
      "Producto solicitado -> formato adecuado -> checklist editorial.",
      "Evidencia institucional -> ubicación curricular -> metadatos consistentes.",
      "Control de placeholders -> compilación limpia -> entrega confiable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 2",
        "Código LDE-S8B2",
        "Integridad académica",
        "Normalización estructurada",
        "Problema jurídico",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Compresión unión-dedupe",
        "Propagación recursiva segura",
        "Corrección de placeholders",
        "Consistencia README-programa-tex-bib",
        "Fuentes institucionales UnADM",
        "Malla curricular de Derecho"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos institucionales consistentes",
          "kind": "supports",
          "justification": "La portada, el curso y la carpeta deben expresar la misma pertenencia institucional."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "develops",
          "justification": "La materia destino pertenece al trayecto curricular local confirmado."
        },
        {
          "source": "Electiva Semestre 8 Bloque 2",
          "target": "Código LDE-S8B2",
          "kind": "depends_on",
          "justification": "El código identifica la materia en los metadatos locales."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones, citas y bibliografía."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "La memoria no debe propagarse si no es parseable y verificable."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis responde al problema delimitado por la actividad."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El razonamiento jurídico requiere base conceptual o normativa."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional surge del razonamiento del estudiante."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Estructura del entregable",
          "kind": "depends_on",
          "justification": "El formato final debe obedecer la consigna vigente."
        },
        {
          "source": "Corrección de placeholders",
          "target": "Compilación limpia",
          "kind": "supports",
          "justification": "Los tokens sin expandir rompen coherencia documental y pueden romper compilación."
        },
        {
          "source": "Consistencia README-programa-tex-bib",
          "target": "Entrega confiable",
          "kind": "supports",
          "justification": "Los documentos locales deben referirse a los mismos archivos, fuentes y metadatos."
        },
        {
          "source": "Fuentes institucionales UnADM",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "La malla curricular local respalda semestre, bloque y tipo de materia."
        },
        {
          "source": "Contenido temático de Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "contrasts",
          "justification": "La relación transversal permite reglas editoriales, no transferencia temática automática."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 2, tipo Electiva.",
        "README local: créditos vacíos y fuente malla-curricular-derecho-unadm.pdf.",
        "README local: pauta editorial con identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: propósito de transformar planeación en productos con problema, conceptos, fuentes, análisis propio y cierre.",
        "Programa analítico local: ejes de trabajo reutilizables.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte local: autor Martin Jonathan de la Cruz.",
        "Reporte local: matrícula ES2611202040.",
        "Reporte local: código de curso LDE-S8B2.",
        "README y programa local: tokens $(@{...}.Slug) sin expandir.",
        "README local: nombres truncados eporte y eferencias.",
        "Herencia institucional: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Origen transversal: bloquear propagación si la salida no es JSON parseable.",
        "Origen transversal: no inventar referencias y usar fuentes verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se deduplicaron reglas repetidas de identidad, estructura, bibliografía y calidad.",
      "Ciclo 13: se conservaron reglas útiles previas sin regresión.",
      "Ciclo 13: se incorporaron solo abstracciones transferibles desde Filosofía del Derecho.",
      "Ciclo 13: se bloqueó transferencia temática específica del origen por relación no equivalente.",
      "Ciclo 13: se reforzó control de placeholders y nombres truncados como riesgo transversal.",
      "Ciclo 13: se mantuvo autor y matrícula confirmados en memoria del destino.",
      "Ciclo 13: se dejaron abiertos créditos, figura docente, consignas y política de fechas bibliográficas.",
      "Ciclo 13: se normalizó el grafo con relaciones permitidas: supports, contrasts, depends_on y develops."
    ]
  }
}