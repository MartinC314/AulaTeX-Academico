{
  "summary": [
    "Materia consolidada con identidad institucional UnADM.",
    "Sincronización transversal aplicada desde Filosofía del Derecho sin traslado temático literal.",
    "Contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Fuente curricular local confirmada: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Se conservan ejes editoriales estables: problema jurídico, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se conserva control obligatorio de normalización JSON antes de propagar.",
    "Persisten incidencias técnicas locales: rutas truncadas, placeholder de Slug y plantilla LaTeX incompleta.",
    "Se aplica compresión por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho.",
    "Usar enfoque de Derecho de la responsabilidad civil y daños.",
    "Usar contexto curricular local confirmado: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no confirmado por guía oficial o consigna.",
    "Tratar memorias heredadas de Codex y GPT-Pro como fuentes provisionales.",
    "No cambiar la convención local danos/daños sin confirmación documental.",
    "No declarar oficial el código LDE-S6B1 sin fuente documental explícita."
  ],
  "structure_rules": [
    "Alinear cada producto a la consigna y planeación semanal vigentes.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía local.",
    "Incluir ejes del programa analítico cuando aplique.",
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
    "Cerrar con criterio propio, conclusión jurídica y transferencia práctica.",
    "Adaptar actividades heredadas solo si son compatibles con responsabilidad civil y daños.",
    "No arrastrar contenido temático de origen si no aplica al daño o a la responsabilidad civil.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia con la pauta editorial de la materia.",
    "Confirmar que toda afirmación jurídica tenga fuente, cita o marca de análisis propio.",
    "Marcar como supuesto todo dato sin respaldo documental.",
    "Validar metadatos curriculares contra la malla local antes de citarlos.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar caracteres rotos, rutas truncadas y placeholders sin resolver.",
    "Validar compilación LaTeX después de completar la plantilla local.",
    "Aplicar control de no regresión sobre reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Usar español con acentos correctos en .tex y .bib.",
    "Evitar caracteres rotos en rutas, nombres de archivo y comandos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas truncadas de reporte y referencias antes de compilar.",
    "Verificar que el archivo .bib local sea derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Supuesto: la plantilla .tex local está truncada en authortable y debe completarse.",
    "Supuesto: el código LDE-S6B1 no es oficial hasta confirmación documental."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar fuentes institucionales locales ya registradas.",
    "Registrar fuentes específicas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Separar fuentes verificables de análisis propio.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Registrar vacíos bibliográficos como preguntas abiertas.",
    "Conservar la malla curricular de Derecho como fuente curricular local.",
    "Entradas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Propagar identidad, estructura reusable, controles de calidad y grafo conceptual general.",
    "No propagar redacción literal de actividades de origen.",
    "No propagar contenido temático de Filosofía del Derecho como regla local.",
    "No propagar detalles exclusivos de una actividad si no aplican a toda la materia.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Mantener alerta de normalización manual por antecedentes de salida no estructurada.",
    "Propagar control de rutas truncadas y placeholders como regla editorial general.",
    "No propagar el código LDE-S6B1 como oficial hasta confirmación.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 2 necesita normalización manual si se reutiliza.",
    "Ciclo 3 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si existe guía oficial de formato para actividades de esta materia.",
    "Confirmar convención final de nombres con danos versus daños en todo el árbol.",
    "Confirmar si el código LDE-S6B1 es oficial.",
    "Resolver placeholder interpolado del nombre de archivo .bib en README y programa analítico.",
    "Validar y corregir truncamientos en README: reporte y referencias.",
    "Completar la sección authortable truncada en la plantilla .tex.",
    "Confirmar rúbricas de evaluación específicas por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar producto exacto solicitado por cada actividad."
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
        "Fuentes heredadas no verificadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derecho de la responsabilidad civil y daños.",
        "Fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "Código LDE-S6B1 marcado como supuesto hasta confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Responsabilidad civil.",
      "Daño.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Integridad académica.",
      "Normalización estructurada JSON."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Construir entregas útiles para la práctica jurídica en responsabilidad civil y daños.",
      "Preservar memoria editorial sin regresión y sin invención de fuentes."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente cuando falte evidencia documental.",
      "Usar secciones funcionales y verificables.",
      "Diferenciar fuente, análisis propio y conclusión.",
      "Evitar relleno descriptivo sin postura jurídica.",
      "Usar cierre con criterio jurídico propio y utilidad profesional.",
      "Mantener consistencia entre metadatos, ruta, .tex y .bib.",
      "Corregir placeholders y truncamientos antes de compilar.",
      "No trasladar temática ajena sin compatibilidad jurídica."
    ],
    "argumentative_patterns": [
      "Plantear problema jurídico inicial.",
      "Delimitar objetivo de la actividad.",
      "Definir conceptos clave antes del análisis.",
      "Vincular norma, doctrina o dato con el problema.",
      "Sostener afirmaciones con citas verificables.",
      "Contrastar evidencia con postura propia.",
      "Aplicar el razonamiento al daño o a la responsabilidad civil.",
      "Cerrar con conclusión jurídica transferible.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho de la responsabilidad civil y daños",
        "Responsabilidad civil",
        "Daño",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Conceptos jurídicos pertinentes",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Bibliografía local",
        "Normalización estructurada JSON",
        "Propagación recursiva segura",
        "Rutas truncadas",
        "Placeholders sin resolver",
        "Plantilla LaTeX incompleta"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la responsabilidad civil y daños",
          "kind": "develops",
          "justification": "El README local ubica la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Derecho de la responsabilidad civil y daños",
          "target": "Responsabilidad civil",
          "kind": "develops",
          "justification": "La materia se organiza alrededor del campo de responsabilidad civil."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La memoria local reconoce el daño como eje conceptual de la materia."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis requiere una pregunta jurídica definida y contextualizada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe derivar de fundamentos jurídicos y fuentes verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones jurídicas deben respaldarse con citas o marcarse como análisis propio."
        },
        {
          "source": "Bibliografía local",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El .bib local registra fuentes institucionales y debe recibir fuentes específicas por actividad."
        },
        {
          "source": "Normalización estructurada JSON",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "La validación JSON evita reutilizar salidas ambiguas o no parseables."
        },
        {
          "source": "Placeholders sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir y rutas truncadas impiden una compilación confiable."
        },
        {
          "source": "Plantilla LaTeX incompleta",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "La sección authortable truncada debe completarse antes de validar el documento."
        },
        {
          "source": "Actividad de Filosofía del Derecho",
          "target": "Materia de responsabilidad civil y daños",
          "kind": "contrasts",
          "justification": "La transferencia es transversal; solo pasan abstracciones editoriales estables, no temática literal."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de trabajo problema, conceptos, fuentes, análisis propio y conclusión.",
        "Archivo .bib local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Contexto local: README contiene rutas truncadas de reporte y referencias.",
        "Contexto local: README y programa analítico contienen placeholder $(@{...}.Slug).",
        "Contexto local: plantilla .tex aparece truncada en authortable.",
        "Memoria de origen: normalización JSON obligatoria antes de propagar.",
        "Memoria de origen: no inventar fuentes y validar consistencia entre citas y .bib.",
        "Memoria heredada institucional: revisar salida no estructurada antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 conserva reglas útiles de ciclos previos sin regresión.",
      "Se deduplican formulaciones equivalentes sin eliminar contenido normativo.",
      "Se refuerza identidad UnADM y contexto curricular local confirmado.",
      "Se mantiene el enfoque local en responsabilidad civil y daños.",
      "Se evita trasladar contenido temático de Filosofía del Derecho.",
      "Se incorporan solo abstracciones transversales verificables.",
      "Se preservan alertas técnicas locales sobre rutas, placeholders y authortable.",
      "Se mantiene bloqueo de propagación ante JSON no parseable.",
      "Se consolidan citas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024.",
      "Se dejan abiertos vacíos que requieren guía oficial, rúbrica o consigna."
    ]
  }
}