{
  "summary": [
    "Materia UnADM consolidada con memoria editorial transversal en ciclo 10.",
    "Contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Fuente curricular local confirmada: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Se preserva identidad institucional UnADM con integridad académica y citas verificables.",
    "Se refuerza estructura reusable: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se conserva alerta de normalización por salidas previas no estructuradas.",
    "Persisten incidencias locales: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta.",
    "La transferencia desde Filosofía del Derecho se limita a abstracciones editoriales estables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho.",
    "Usar enfoque de Derecho de la responsabilidad civil y danos.",
    "Usar ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente curricular local.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no confirmado por consigna, guía oficial o fuente local.",
    "Tratar memorias heredadas de Codex y GPT-Pro como fuentes provisionales.",
    "No cambiar la convención local danos/daños sin confirmación documental.",
    "No declarar oficial el código LDE-S6B1 sin fuente documental explícita."
  ],
  "structure_rules": [
    "Alinear cada producto a problema, conceptos o fuentes, análisis propio y conclusión jurídica.",
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final con la planeación semanal y la consigna vigente.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía local.",
    "Incluir ejes del programa analítico cuando aplique.",
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
    "Cerrar con criterio propio, conclusión jurídica y transferencia a práctica jurídica.",
    "Adaptar actividades heredadas solo si son compatibles con responsabilidad civil y danos.",
    "No arrastrar contenido temático de origen si no aplica al daño o a la responsabilidad civil.",
    "Verificar que el producto corresponda a la consigna de la actividad vigente."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar consistencia con la pauta editorial de la materia.",
    "Verificar que toda afirmación jurídica tenga fuente o se marque como análisis propio.",
    "Confirmar que no existan datos sin respaldo o sin marca de supuesto.",
    "Validar metadatos curriculares contra la malla local antes de citarlos.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar caracteres rotos, rutas truncadas y placeholders sin resolver.",
    "Validar compilación LaTeX después de completar la plantilla local.",
    "Aplicar control de no regresión sobre reglas útiles heredadas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Usar título, subtítulo, asignatura, autor, universidad y departamento coherentes con la materia.",
    "Usar español con acentos correctos en .tex y .bib.",
    "Evitar caracteres rotos en rutas, nombres de archivo y comandos.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas truncadas antes de compilar.",
    "Completar la sección authortable truncada antes de compilar.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar que el archivo .bib local se llame derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Supuesto: el código LDE-S6B1 no es oficial hasta confirmación documental."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Conservar fuentes institucionales locales ya registradas.",
    "Entradas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar fuentes específicas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Separar fuentes verificables de análisis propio.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Si falta referencia, registrar pregunta abierta.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas estables y no temáticas.",
    "Compartir identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "No propagar detalles exclusivos de una actividad si no aplican a toda la materia.",
    "Mantener alerta de normalización manual por antecedentes de salida no estructurada.",
    "Propagar control de rutas truncadas y placeholders como regla editorial general.",
    "No propagar el código LDE-S6B1 como oficial hasta confirmación.",
    "Usar compresión por unión y deduplicación sin recorte semántico.",
    "Conservar reglas útiles previas sin regresión.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Ciclo 10 continúa sincronización transversal conservadora."
  ],
  "open_questions": [
    "Confirmar si existe guía oficial de formato para actividades de esta materia.",
    "Confirmar convención final de nombres con danos versus daños en todo el árbol.",
    "Confirmar si el código de curso LDE-S6B1 es oficial.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Resolver placeholder interpolado del nombre de archivo .bib en README y programa analítico.",
    "Corregir nombres truncados en README: reporte y referencias.",
    "Validar plantilla .tex por truncamiento local.",
    "Completar la sección authortable truncada en la plantilla .tex.",
    "Confirmar producto exacto solicitado por cada actividad.",
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
        "Carpeta de materia como entrada canónica.",
        "Metadatos coherentes con la Licenciatura en Derecho.",
        "Normalización estructurada previa a propagación.",
        "Fuentes heredadas no verificadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho de la responsabilidad civil y danos.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
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
      "Análisis propio.",
      "Postura académica.",
      "Conclusión jurídica transferible.",
      "Integridad académica."
    ],
    "reason_for_being": [
      "Orientar productos académicos de responsabilidad civil con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en productos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar la conclusión con práctica jurídica profesional.",
      "Evitar traslado temático no pertinente desde materias transversales.",
      "Proteger consistencia institucional, técnica y bibliográfica."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente cuando falte evidencia documental.",
      "Usar secciones funcionales y verificables.",
      "Abrir con problema jurídico contextualizado.",
      "Diferenciar fuente, norma, doctrina, dato y opinión propia.",
      "Evitar resumen descriptivo sin postura.",
      "Cerrar con criterio jurídico propio y utilidad profesional.",
      "Mantener lenguaje jurídico preciso.",
      "Conservar convención local danos en archivos hasta confirmación.",
      "No copiar redacción literal entre nodos no equivalentes.",
      "Normalizar antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y contextualizado.",
      "Objetivo puntual antes del desarrollo.",
      "Conceptos clave definidos con fuentes.",
      "Marco normativo o doctrinal verificable.",
      "Análisis propio con contraste de ideas.",
      "Distinción entre evidencia y postura académica.",
      "Conclusión jurídica aplicada.",
      "Transferencia a práctica profesional.",
      "Correspondencia entre consigna, desarrollo y cierre.",
      "Adaptación temática al daño y a la responsabilidad civil."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho de la responsabilidad civil y danos",
        "Responsabilidad civil",
        "Daño",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Normalización estructurada JSON",
        "Planeación semanal",
        "Producto académico",
        "Bibliografía local",
        "Plantilla LaTeX",
        "Placeholders sin resolver",
        "Rutas truncadas",
        "Fuentes provisionales"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica con criterio propio."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la responsabilidad civil y danos",
          "kind": "develops",
          "justification": "El README local ubica la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Derecho de la responsabilidad civil y danos",
          "target": "Responsabilidad civil",
          "kind": "develops",
          "justification": "El nombre y programa local centran la materia en responsabilidad civil."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La materia articula responsabilidad civil y daños como eje conceptual local."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder a una cuestión jurídica previamente delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones jurídicas deben tener fuente o marcarse como análisis propio."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa local indica transformar la planeación en reportes, presentaciones o productos visuales."
        },
        {
          "source": "Normalización estructurada JSON",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no parseables o ambiguas."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local contiene fuentes institucionales y debe recibir fuentes específicas por actividad."
        },
        {
          "source": "Placeholders sin resolver",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los placeholders en README y programa analítico impiden rutas finales confiables."
        },
        {
          "source": "Rutas truncadas",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los nombres truncados deben corregirse antes de compilar o referenciar archivos."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Datos confirmados",
          "kind": "contrasts",
          "justification": "Las memorias heredadas Codex y GPT-Pro requieren verificación local antes de fijarse."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: bibliografía específica por actividad en .bib local.",
        "Archivo .bib local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "README local: nombres truncados de reporte y referencias.",
        "README y programa analítico: placeholder $(@{...}.Slug) sin resolver.",
        "Plantilla .tex local: sección authortable truncada.",
        "Memoria institucional heredada: antecedente de salida no JSON parseable.",
        "Sincronización transversal: se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10 conserva reglas locales verificables sin regresión.",
      "Ciclo 10 deduplica reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 10 refuerza la ruta canónica de materia.",
      "Ciclo 10 mantiene alerta de normalización JSON previa a propagación.",
      "Ciclo 10 limita la transferencia temática desde Filosofía del Derecho.",
      "Ciclo 10 conserva ejes transversales: problema, conceptos, fuentes, análisis propio y cierre.",
      "Ciclo 10 refuerza conclusión jurídica aplicada a práctica profesional.",
      "Ciclo 10 preserva incidencias técnicas locales como gates obligatorios.",
      "Ciclo 10 mantiene fuentes heredadas como provisionales hasta verificación.",
      "Ciclo 10 consolida citas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024."
    ]
  }
}