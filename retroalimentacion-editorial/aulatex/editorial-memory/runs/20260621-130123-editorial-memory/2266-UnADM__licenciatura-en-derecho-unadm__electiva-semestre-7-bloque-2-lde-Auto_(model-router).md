{
  "summary": [
    "Materia electiva de Derecho UnADM en semestre 7, bloque 2.",
    "La carpeta local es punto de entrada canónico de la asignatura.",
    "Se sincronizan abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se evita transferir contenido temático no equivalente.",
    "Se preserva compresión por unión y deduplicación sin regresión.",
    "Se conserva la alerta sobre salidas previas no parseables.",
    "El contexto local confirma README, programa analítico, plantilla y bibliografía base.",
    "Supuesto: falta contexto temático específico de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Conservar autor, matrícula y datos académicos en portada cuando aplique.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 en portada local.",
    "No mezclar identidad de Ingeniería con productos de Derecho.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en consigna, rúbrica, README o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar la malla curricular local solo para ubicación curricular verificable.",
    "No importar identidad curricular de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Organizar cada producto con problema, conceptos o normas, evidencia, postura y conclusión.",
    "Mantener el programa analítico como guía editorial de reportes, presentaciones y productos visuales.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar la estructura al producto solicitado: reporte, presentación o producto visual.",
    "Evitar redacción literal heredada de nodos no equivalentes."
  ],
  "activity_rules": [
    "Vincular cada actividad con el problema jurídico o social que la activa.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, objetivo, desarrollo y conclusión.",
    "Registrar supuestos cuando la actividad no aporte instrucciones completas.",
    "Agregar fuentes específicas de cada actividad al .bib local.",
    "No asumir que bibliografía de otra semana o asignatura aplica automáticamente.",
    "Verificar que el producto corresponda a la consigna local.",
    "No importar reglas temáticas de Filosofía del Derecho sin verificación documental."
  ],
  "quality_gates": [
    "Validar que toda memoria entrante sea JSON parseable antes de propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Verificar coherencia entre objetivo, análisis, evidencia y conclusión.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que las rutas citadas existan en el repositorio local.",
    "Corregir placeholders y nombres rotos en README antes de usarlos como plantilla.",
    "Validar el nombre oficial de la electiva antes de publicarlo.",
    "Verificar créditos vacíos antes de cerrar portada o README.",
    "Revisar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base de nuevos reportes.",
    "Usar documentclass article con spanish, letterpaper y oneside salvo instrucción distinta.",
    "Mantener metadatos del curso: LDE-S7B2, semestre 7, bloque 2.",
    "Conservar portada con tabla de identificación académica completa.",
    "Mantener macros editoriales de título, subtítulo, autor, curso, universidad y portada.",
    "Sustituir Actividad X por el nombre real del producto.",
    "Conservar Figura docente como Nombre por definir hasta confirmación.",
    "Mantener Tipo/Créditos como Electiva solo hasta confirmar créditos oficiales.",
    "Mantener universitydepartmentimage en departamentos/UnADM con height 1.57cm.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "No compilar con placeholders tipo $(@{...}) sin normalizarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas jurídicas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar entradas locales unadmSitioWeb y unadmMallaDerecho2024 como base.",
    "Agregar fuentes específicas de cada actividad como entradas BibTeX completas.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Verificar fecha de consulta y disponibilidad antes de citar fuentes web.",
    "Usar archivo local de malla curricular solo si permanece disponible en assets-unadm.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No trasladar bibliografía de Filosofía del Derecho sin verificación temática y documental.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Separar reglas institucionales de reglas temáticas de asignatura.",
    "Reusar estas reglas en actividades hijas de la materia con unión y deduplicación.",
    "Mantener compresión lossless por deduplicación, no por recorte.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar como alerta institucional la necesidad de revisar salidas no estructuradas.",
    "Mantener bandera de normalización manual para ciclos con salida no parseable.",
    "No propagar contenido temático lateral sin evidencia local.",
    "Aplicar estrategia progresiva y conservadora en ciclos posteriores."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en la malla curricular.",
    "Confirmar créditos oficiales de la electiva.",
    "Definir nombre de figura docente en plantilla base.",
    "Corregir en README los nombres generados con placeholder.",
    "Corregir en programa analítico el nombre del archivo .bib con placeholder.",
    "Confirmar si la entrada unadmSitioWeb debe conservar year 2026 o solo fecha de consulta.",
    "Confirmar temática local y competencias específicas de la electiva.",
    "Confirmar rúbrica local de evaluación.",
    "Confirmar productos esperados por actividad.",
    "Confirmar fuentes obligatorias de cada semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador en transferencia transversal."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canónica.",
        "Trazabilidad entre README, programa, plantilla y .bib.",
        "Separación estricta entre identidad de Derecho e identidades ajenas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 7, bloque 2, electiva.",
        "Curso local: Electiva Semestre 7 Bloque 2.",
        "Código local: LDE-S7B2.",
        "Producción orientada a planeación semanal y transferencia profesional.",
        "Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Identidad institucional UnADM.",
      "Alineación con consigna local.",
      "Normalización estructurada previa a propagación.",
      "Transferencia transversal sin arrastre temático indebido."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en entregables coherentes y verificables.",
      "Conectar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar que cada actividad tenga utilidad jurídica práctica.",
      "Preservar identidad UnADM y trazabilidad documental.",
      "Permitir propagación segura de reglas editoriales entre nodos relacionados."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explícito antes del desarrollo.",
      "Secciones explícitas y trazables.",
      "Conceptos definidos antes del análisis.",
      "Afirmaciones acompañadas de evidencia.",
      "Supuestos etiquetados cuando falte información.",
      "Postura personal argumentada.",
      "Cierre con implicación jurídica práctica.",
      "Citas verificables y coherentes con el .bib.",
      "Sin redacción literal importada de nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> análisis -> conclusión.",
      "Consigna -> objetivo -> desarrollo -> verificación final.",
      "Afirmación -> evidencia -> interpretación propia.",
      "Fuente institucional -> ubicación curricular -> límite editorial.",
      "Supuesto -> advertencia -> confirmación pendiente.",
      "Contexto local -> regla reusable -> producto específico.",
      "Evidencia verificable -> postura argumentada -> conclusión transferible.",
      "Normalización -> validación -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Semestre 7 bloque 2.",
        "Electiva.",
        "Carpeta canónica de materia.",
        "Malla curricular de Derecho.",
        "Problema jurídico o social.",
        "Conceptos clave.",
        "Marco normativo o doctrinal.",
        "Evidencia verificable.",
        "Postura argumentada.",
        "Conclusión transferible.",
        "Planeación semanal.",
        "Producto solicitado.",
        "Bibliografía local.",
        "Normalización estructurada.",
        "Propagación transversal segura.",
        "Supuestos editoriales.",
        "Placeholders de plantilla.",
        "Integridad académica."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Alineación con consigna local",
          "kind": "supports",
          "justification": "La identidad fija límites formales, curriculares y de trazabilidad."
        },
        {
          "source": "Carpeta canónica de materia",
          "target": "Plantilla local",
          "kind": "supports",
          "justification": "La carpeta contiene README, programa, .tex y .bib base."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README la declara como fuente para semestre, bloque y tipo."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Conceptos clave",
          "kind": "develops",
          "justification": "El problema determina los conceptos y normas pertinentes."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El marco requiere delimitar los conceptos antes de aplicarlos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental explícito."
        },
        {
          "source": "Postura argumentada",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "El análisis propio permite cerrar con utilidad jurídica práctica."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "supports",
          "justification": "La planeación define formato, alcance y criterios del entregable."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local centraliza las fuentes consultables."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación transversal segura",
          "kind": "supports",
          "justification": "Evita heredar ruido, duplicados y salidas no parseables."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los placeholders sin resolver rompen trazabilidad y pueden afectar compilación."
        },
        {
          "source": "Contenido temático de Filosofía del Derecho",
          "target": "Materia electiva semestre 7 bloque 2",
          "kind": "contrasts",
          "justification": "La relación es transversal, no equivalente; solo se transfieren abstracciones editoriales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 2, tipo Electiva.",
        "README local: créditos vacíos pendientes de confirmación.",
        "README local: fuente curricular declarada en malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: propósito de transformar planeación en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis y conclusión.",
        "Bibliografía local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla local: curso LDE-S7B2 y portada académica.",
        "Plantilla local: Figura docente pendiente de definición.",
        "Origen transversal: refuerza problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Origen transversal: exige JSON parseable antes de propagar.",
        "Origen transversal: no inventar fuentes y marcar supuestos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17 conserva reglas locales válidas y elimina duplicados semánticos.",
      "Ciclo 17 transfiere solo abstracciones estables desde Filosofía del Derecho.",
      "Ciclo 17 evita arrastrar bibliografía temática de Filosofía del Derecho.",
      "Ciclo 17 refuerza identidad UnADM para Derecho semestre 7 bloque 2.",
      "Ciclo 17 mantiene alerta por salidas previas no parseables.",
      "Ciclo 17 refuerza gates de JSON, estructura, citas y compilación.",
      "Ciclo 17 marca créditos, docente, nombre oficial y temática como pendientes.",
      "Ciclo 17 actualiza grafo conceptual con relaciones permitidas.",
      "Ciclo 17 conserva estrategia progresiva y conservadora.",
      "Ciclo 17 preserva compresión lossless por deduplicación."
    ]
  }
}