{
  "summary": [
    "Materia consolidada con identidad institucional UnADM.",
    "Contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Fuente curricular local confirmada: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Se sincronizan abstracciones transversales desde Filosofía del Derecho sin trasladar contenido temático literal.",
    "Ejes editoriales activos: problema jurídico, conceptos y fuentes, análisis propio y conclusión jurídica transferible.",
    "Persisten incidencias técnicas locales: salida no estructurada previa, rutas truncadas, placeholders sin resolver y plantilla LaTeX incompleta.",
    "Se aplica compresión por unión y deduplicación sin regresión de reglas útiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho.",
    "Usar enfoque local de Derecho de la responsabilidad civil y danos.",
    "Usar contexto curricular confirmado: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Citar la malla curricular local para ubicación curricular.",
    "Marcar como supuesto cualquier dato no confirmado por guía oficial o consigna.",
    "Tratar memorias heredadas de Codex y GPT-Pro como fuentes provisionales.",
    "No cambiar la convención local danos/daños sin confirmación documental.",
    "No declarar oficial el código LDE-S6B1 sin fuente documental explícita.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada producto a problema, conceptos o fuentes, análisis propio y conclusión jurídica.",
    "Respetar el producto solicitado por la planeación semanal y la consigna vigente.",
    "Usar el programa analítico local para orientar productos semanales.",
    "Incluir ejes de trabajo del programa analítico cuando aplique.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía local.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Corregir nombres truncados o plantillas interpoladas antes de usarlos como rutas finales."
  ],
  "activity_rules": [
    "Formular un problema jurídico o social que active la responsabilidad civil.",
    "Integrar conceptos, normas, doctrina o datos pertinentes según la actividad.",
    "Separar fundamento jurídico, evidencia y postura académica.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar actividades heredadas solo si son compatibles con responsabilidad civil y danos.",
    "No arrastrar contenido temático de origen si no aplica al daño o a la responsabilidad civil.",
    "Cerrar con criterio propio, conclusión jurídica y transferencia a práctica jurídica.",
    "Confirmar producto exacto de cada actividad antes de fijar formato final."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Aplicar control de no regresión sobre reglas útiles heredadas.",
    "Validar metadatos curriculares contra la malla local antes de citarlos.",
    "Verificar que toda afirmación jurídica tenga fuente o se marque como análisis propio.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar caracteres rotos, rutas truncadas y placeholders sin resolver en archivos locales.",
    "Validar compilación LaTeX después de completar la plantilla local.",
    "Verificar correspondencia del producto con la consigna de actividad vigente."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Usar título, subtítulo, asignatura, autor, universidad y departamento coherentes con la materia.",
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar que el archivo .bib local se llame derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Supuesto: la plantilla .tex local está truncada en authortable y debe completarse antes de compilar.",
    "Supuesto: el código de curso LDE-S6B1 no es oficial hasta confirmación documental."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar la malla curricular de Derecho como fuente curricular local.",
    "Registrar fuentes específicas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Separar fuentes verificables de análisis propio.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Registrar vacíos bibliográficos como preguntas abiertas.",
    "Entradas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas estables y no temáticas de una actividad puntual.",
    "Compartir identidad, estructura reusable, controles de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "No propagar detalles exclusivos de Filosofía del Derecho al destino.",
    "No propagar detalles exclusivos de una actividad si no aplican a toda la materia.",
    "Aplicar normalización manual por antecedentes de salida no estructurada.",
    "Propagar control de rutas truncadas y placeholders como regla editorial general.",
    "No propagar el código LDE-S6B1 como oficial hasta confirmación.",
    "Usar compresión por unión y deduplicación sin recorte semántico.",
    "Mantener alerta de normalización manual en ciclos posteriores."
  ],
  "open_questions": [
    "Confirmar si existe guía oficial de formato para actividades de esta materia.",
    "Confirmar convención final de nombres de archivos con danos versus daños en todo el árbol.",
    "Confirmar si el código de curso LDE-S6B1 es oficial.",
    "Validar plantilla .tex por truncamiento local y completar authortable.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Resolver placeholder interpolado del nombre de archivo .bib en README y programa analítico.",
    "Confirmar fuentes obligatorias por actividad o semana.",
    "Confirmar rúbricas de evaluación específicas.",
    "Confirmar producto exacto solicitado para cada actividad.",
    "Confirmar si cada actividad requiere reporte, presentación u otro formato principal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Metadatos coherentes con la Licenciatura en Derecho.",
        "Fuentes heredadas no verificadas tratadas como provisionales.",
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho de la responsabilidad civil y danos.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "Código LDE-S6B1 marcado como supuesto hasta confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social que activa la asignatura.",
      "Responsabilidad civil.",
      "Daño.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible a la práctica profesional.",
      "Producto solicitado por la planeación."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicado a responsabilidad civil y daños.",
      "Conservar trazabilidad entre consigna, fuentes, análisis y conclusión."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente cuando falte evidencia documental.",
      "Mantener estructura por secciones funcionales y verificables.",
      "Usar cierre con criterio jurídico propio y utilidad profesional.",
      "Evitar texto meramente descriptivo.",
      "Separar voz del estudiante, fuente normativa y fuente doctrinal.",
      "No trasladar contenido temático de origen sin compatibilidad local.",
      "Normalizar antes de propagar.",
      "Mantener nombres de archivos y claves bibliográficas estables."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y contextualizado.",
      "Objetivo puntual de la actividad.",
      "Marco conceptual y normativo con fuentes.",
      "Evidencia diferenciada del análisis propio.",
      "Contraste de ideas cuando existan posiciones doctrinales.",
      "Aplicación al caso, actividad o práctica jurídica.",
      "Conclusión jurídica fundada y transferible.",
      "Verificación final contra consigna, citas y archivo .bib."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho de la responsabilidad civil y danos",
        "Responsabilidad civil",
        "Daño",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Conceptos jurídicos pertinentes",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Práctica profesional",
        "Integridad académica",
        "Bibliografía local",
        "Normalización estructurada JSON",
        "Propagación recursiva segura",
        "Rutas truncadas",
        "Placeholders sin resolver",
        "Plantilla LaTeX truncada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "El marco institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la responsabilidad civil y danos",
          "kind": "develops",
          "justification": "La materia pertenece al contexto curricular local confirmado."
        },
        {
          "source": "Derecho de la responsabilidad civil y danos",
          "target": "Responsabilidad civil",
          "kind": "develops",
          "justification": "La asignatura organiza el análisis alrededor de la responsabilidad civil."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La memoria local articula la responsabilidad a partir de la noción jurídica de daño."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere una pregunta o conflicto jurídico definido."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe apoyarse en fuentes verificables y razonamiento jurídico."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las fuentes explícitas reducen afirmaciones sin respaldo."
        },
        {
          "source": "Análisis propio",
          "target": "Postura académica",
          "kind": "develops",
          "justification": "La postura del estudiante surge del análisis fundado, no del resumen."
        },
        {
          "source": "Conclusión jurídica transferible",
          "target": "Práctica profesional",
          "kind": "supports",
          "justification": "El cierre debe conectar la actividad con utilidad jurídica aplicada."
        },
        {
          "source": "Bibliografía local",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El archivo .bib local conserva fuentes institucionales y específicas."
        },
        {
          "source": "Normalización estructurada JSON",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no parseables o ambiguas."
        },
        {
          "source": "Placeholders sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los placeholders impiden rutas finales confiables y pueden romper la compilación."
        },
        {
          "source": "Rutas truncadas",
          "target": "Entrada canónica por carpeta de materia",
          "kind": "contrasts",
          "justification": "Las rutas truncadas contradicen la trazabilidad editorial local."
        },
        {
          "source": "Plantilla LaTeX truncada",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "La sección authortable incompleta debe resolverse antes de compilar."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión transferible.",
        "Archivo .bib local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "README y programa analítico: placeholder $(@{...}.Slug) sin resolver para archivo .bib.",
        "README local: nombres truncados de reporte y referencias.",
        "Plantilla .tex local: authortable truncado [supuesto técnico local].",
        "Memoria heredada: antecedente de salida no JSON parseable.",
        "Sincronización transversal: se heredan patrones editoriales estables, no contenido temático de Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5 conserva identidad UnADM y contexto curricular local confirmado.",
      "Ciclo 5 deduplica reglas repetidas sin eliminar controles útiles.",
      "Ciclo 5 refuerza transferencia transversal solo con abstracciones editoriales estables.",
      "Ciclo 5 mantiene bloqueo de propagación ante JSON no parseable.",
      "Ciclo 5 conserva alertas locales sobre rutas truncadas, placeholders y plantilla incompleta.",
      "Ciclo 5 evita trasladar bibliografía o conceptos temáticos de Filosofía del Derecho al destino.",
      "Ciclo 5 consolida grafo conceptual con responsabilidad civil, daño, evidencia, análisis propio y conclusión transferible."
    ]
  }
}