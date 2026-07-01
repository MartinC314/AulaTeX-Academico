{
  "summary": [
    "Se consolida memoria transversal para Electiva Semestre 8 Bloque 2.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se sincronizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se evita trasladar contenido temático específico de otra asignatura sin validación local.",
    "Se mantienen ejes editoriales: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se refuerza normalización obligatoria antes de propagar memoria.",
    "Se conserva regla de salida JSON parseable para toda consolidación.",
    "Se mantiene autor confirmado: Martin Jonathan de la Cruz.",
    "Se mantiene matrícula confirmada: ES2611202040.",
    "Se detectan placeholders y nombres truncados en documentos locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Alinear la materia con semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos locales.",
    "Fijar autor Martin Jonathan de la Cruz en front matter.",
    "Fijar matrícula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "No propagar datos curriculares de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave y marco normativo o doctrinal.",
    "Incluir análisis propio diferenciado de resumen descriptivo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la entrega al producto solicitado por la consigna semanal.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según corresponda.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y .bib local.",
    "Corregir rutas, nombres truncados y placeholders antes de entrega.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres literales.",
    "Restaurar nombres truncados como eporte y eferencias cuando aparezcan."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otra semana como fuentes de la actividad actual.",
    "No trasladar contenido específico de Filosofía del Derecho sin fuente verificable.",
    "Adaptar profundidad argumentativa a la rúbrica confirmada.",
    "Cerrar cada actividad con aplicación jurídica práctica."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de propagarlas.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Confirmar ausencia de placeholders visibles en README, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Compilar artefactos LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Reemplazar Actividad X por la actividad real.",
    "Completar figura docente solo con dato confirmado.",
    "Completar créditos solo con dato confirmado.",
    "Usar codificación y acentos correctos en español.",
    "Mantener compatibilidad entre nombres de archivos, rutas y recursos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar malla curricular de Derecho como fuente institucional local.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Marcar como [supuesto] cualquier dato bibliográfico no confirmado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba y laterales solo reglas validadas y sin ambigüedad.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Etiquetar reglas de integridad académica como transversales UnADM.",
    "No propagar contenido temático local de una materia a otra sin validación.",
    "No propagar datos incompletos de créditos o figura docente.",
    "Mantener compresión por unión y deduplicación.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Usar ciclo 1 como etapa de normalización, no como evidencia definitiva.",
    "Propagar la corrección de placeholders como lección transversal verificable.",
    "Mantener herencias Codex o GPT-Pro como provisionales hasta revisión manual."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto.",
    "[supuesto] Confirmar consigna textual de cada actividad antes de producir entregables.",
    "[supuesto] Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "[supuesto] Confirmar fuentes obligatorias de cada semana.",
    "[supuesto] Confirmar política institucional para año y fecha de consulta del sitio UnADM.",
    "[supuesto] Confirmar si el año 2026 en unadmSitioWeb es dato vigente o placeholder.",
    "[supuesto] Confirmar nombre canónico final del archivo .bib si cambia el slug local.",
    "[supuesto] Confirmar si se requiere reporte, presentación u otro formato principal por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia entre materias.",
        "Directo y modular."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Metadatos locales consistentes.",
        "Herencias no verificadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2.",
        "Tipo Electiva.",
        "Curso LDE-S8B2.",
        "Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Trazabilidad de fuentes.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización técnica de artefactos LaTeX.",
      "Sincronización transversal sin copia temática literal."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en entregables concretos.",
      "Sostener razonamiento jurídico con fuentes verificables.",
      "Evitar entregas descriptivas sin postura.",
      "Garantizar consistencia entre documentos locales.",
      "Crear memoria editorial reutilizable sin perder especificidad local.",
      "Proteger la publicabilidad técnica de reportes y presentaciones."
    ],
    "style_markers": [
      "Frases directas.",
      "Secciones modulares.",
      "Marcado explícito de [supuesto].",
      "Citas verificables.",
      "Cierre argumentativo práctico.",
      "Evitar relleno descriptivo.",
      "Evitar contenido temático ajeno sin validación.",
      "Usar vocabulario jurídico preciso.",
      "Mantener coherencia entre portada, cuerpo y bibliografía.",
      "Corregir placeholders antes de compilar."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer conceptos clave.",
      "Ubicar marco normativo o doctrinal.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Conectar fuentes con el problema.",
      "Verificar coherencia interna.",
      "Cerrar con implicación jurídica transferible.",
      "Ajustar producto a la consigna real."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 2",
        "Integridad académica",
        "Trazabilidad de fuentes",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Producto solicitado por la planeación",
        "Normalización JSON",
        "Normalización LaTeX",
        "Placeholders de plantilla",
        "Bibliografía local verificable",
        "Malla curricular de Derecho",
        "Carpeta de materia canónica",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Licenciatura en Derecho",
          "kind": "develops",
          "justification": "La materia se presenta como parte de la carrera en documentos locales."
        },
        {
          "source": "Electiva Semestre 8 Bloque 2",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "Su ubicación curricular local pertenece a la Licenciatura en Derecho."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Toda afirmación relevante requiere respaldo verificable."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Bibliografía local verificable",
          "kind": "depends_on",
          "justification": "Las citas deben corresponder a claves existentes en el .bib local."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README la declara como fuente institucional de ubicación."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El análisis debe responder al problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "El marco aporta criterios para argumentar."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión deriva de la postura razonada del estudiante."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Estructura del entregable",
          "kind": "depends_on",
          "justification": "El formato final debe seguir la consigna real."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación editorial",
          "kind": "supports",
          "justification": "Solo memoria estructurada puede aplicarse aguas abajo."
        },
        {
          "source": "Normalización LaTeX",
          "target": "Publicabilidad del entregable",
          "kind": "supports",
          "justification": "La compilación limpia permite reutilización y entrega."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Publicabilidad del entregable",
          "kind": "contrasts",
          "justification": "Los placeholders visibles degradan el artefacto final."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "Contenido temático específico",
          "kind": "contrasts",
          "justification": "La sincronización lateral comparte reglas, no contenido disciplinar ajeno."
        },
        {
          "source": "Carpeta de materia canónica",
          "target": "Consistencia documental",
          "kind": "supports",
          "justification": "Centraliza README, programa, plantillas y bibliografía local."
        }
      ],
      "evidence": [
        "README local declara materia de Licenciatura en Derecho de la UnADM.",
        "README local ubica semestre 8, bloque 2, tipo Electiva.",
        "README local deja créditos sin completar.",
        "README local declara fuente malla-curricular-derecho-unadm.pdf.",
        "README local contiene nombres truncados eporte y eferencias.",
        "README local contiene token $(@{...}.Slug) sin resolver.",
        "Programa analítico local define propósito de transformar planeación en productos académicos.",
        "Programa analítico local fija ejes: problema, conceptos, producto, análisis y conclusión.",
        "Archivo .bib local contiene unadmSitioWeb.",
        "Archivo .bib local contiene unadmMallaDerecho2024.",
        "Plantilla LaTeX local fija autor Martin Jonathan de la Cruz.",
        "Plantilla LaTeX local fija matrícula ES2611202040.",
        "Plantilla LaTeX local usa curso LDE-S8B2.",
        "Plantilla LaTeX local mantiene figura docente por definir.",
        "Memoria origen refuerza bloquear propagación si no hay JSON parseable.",
        "Memoria origen refuerza no inventar fuentes.",
        "Memoria origen refuerza estructura problema-conceptos-marco-análisis-cierre."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad UnADM.",
      "Se conservaron datos confirmados del front matter local.",
      "Se mantuvieron vacíos curriculares como [supuesto].",
      "Se integraron ejes transversales desde Filosofía del Derecho sin copiar contenido temático.",
      "Se reforzó gate de JSON parseable.",
      "Se reforzó gate de trazabilidad bibliográfica.",
      "Se reforzó corrección de placeholders como regla transversal verificable.",
      "Se preservó estrategia progresiva y conservadora.",
      "Se evitó propagar semestre, bloque y créditos del origen.",
      "Se consolidó grafo conceptual mínimo para la materia destino."
    ]
  }
}