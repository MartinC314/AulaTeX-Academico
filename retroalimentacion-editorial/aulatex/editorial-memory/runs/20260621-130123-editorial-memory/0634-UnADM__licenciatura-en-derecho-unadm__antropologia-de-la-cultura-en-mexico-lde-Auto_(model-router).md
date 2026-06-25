{
  "summary": [
    "Consolidación transversal ciclo 5 para materia destino.",
    "Destino confirmado: Antropología de la cultura en México.",
    "Institución confirmada: UnADM.",
    "Carrera confirmada: Licenciatura en Derecho.",
    "Ubicación local confirmada: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se preserva pauta local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
    "Se aplica unión-dedupe lossless sin regresión.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se evita trasladar contenido temático exclusivo del origen.",
    "Se mantiene alerta por salidas heredadas no JSON parseable.",
    "README, programa analítico y .bib local son fuentes canónicas del destino.",
    "El destino ya posee cerebro editorial mínimo verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción: Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar fuente heredada desde ingeniería como provisional.",
    "Marcar fuente heredada desde Codex como provisional.",
    "Marcar fuente heredada desde GPT-Pro como provisional.",
    "No trasladar metadatos curriculares de Filosofía del Derecho al destino.",
    "Mantener autor y matrícula solo si coinciden con la actividad real.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular local."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Usar programa analítico como guía editorial de productos.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Separar secciones en conceptos clave, marco teórico o normativo, análisis propio y cierre.",
    "Alinear cada entrega con el producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Guardar fuentes específicas en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "Corregir rutas o nombres truncados antes de compilar.",
    "Resolver plantillas dinámicas tipo $(@{...}.Slug) antes de usar nombres de archivo."
  ],
  "activity_rules": [
    "Definir problema jurídico, social o cultural al inicio.",
    "Integrar conceptos antropológicos, culturales, jurídicos o sociales pertinentes.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el producto solicitado con la planeación semanal.",
    "Confirmar que el producto corresponda a la consigna de la actividad.",
    "No asumir que fuentes de semanas posteriores correspondan a una actividad previa.",
    "Marcar como supuesto cualquier dato no confirmado por la consigna."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No aceptar contenido sin estructura mínima del esquema requerido.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Comprobar que semestre, bloque, tipo y créditos coincidan con la malla curricular local.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que las rutas del README no contengan placeholders ni saltos corruptos.",
    "Verificar que no queden plantillas sin resolver en README, programa analítico ni .tex.",
    "Revisar que portada, encabezados y bibliografía compilen sin errores.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad académica justificada.",
    "Usar letterpaper y oneside si no hay instrucción distinta.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Mantener universityname como Universidad Abierta y a Distancia de México.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursename como Antropología de la cultura en México.",
    "Mantener coursecode LDE-S4B2 salvo indicación institucional distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Usar configuración en español coherente con la plantilla.",
    "Evitar cambios de clase o formato sin necesidad académica.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) en README, programa analítico y nombres de archivo.",
    "No copiar LaTeX completo en memoria editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Usar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas por actividad en el .bib local.",
    "Registrar fuentes específicas en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "No asumir que bibliografía temática de Filosofía del Derecho aplica al destino.",
    "Confirmar fuentes obligatorias de cada semana antes de integrarlas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba y laterales solo reglas ya validadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Propagar identidad UnADM e integridad académica a nodos laterales.",
    "Propagar criterios de evidencia verificable, postura propia y coherencia argumentativa.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "No propagar contenidos temáticos exclusivos de Filosofía del Derecho al destino.",
    "Etiquetar como supuesto todo elemento heredado no confirmado en Derecho.",
    "Propagar como provisional cualquier regla heredada desde otra disciplina.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Aplicar normalización manual si se reutiliza memoria no estructurada.",
    "Mantener compresión por unión-dedupe con preservación total.",
    "No eliminar reglas útiles previas durante consolidaciones futuras.",
    "Reducir duplicados sin recortar significado editorial."
  ],
  "open_questions": [
    "Confirmar estándar único de citas para toda la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el .bib usa nombre literal o plantilla dinámica como nombre definitivo.",
    "Confirmar rúbricas específicas de actividades futuras.",
    "Confirmar producto exacto de cada actividad antes de desarrollar.",
    "Confirmar autor y matrícula por actividad real.",
    "Supuesto: reglas heredadas desde ingeniería aplican solo como alerta técnica.",
    "Supuesto: reglas heredadas desde Filosofía del Derecho aplican solo como abstracciones editoriales.",
    "Supuesto: la plantilla local mantiene LDE-S4B2 hasta validación institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible.",
        "Jurídicamente pertinente.",
        "Orientado a trazabilidad."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Metadatos institucionales consistentes.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Antropología de la cultura en México.",
        "Semestre 4, bloque 2.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Clave local LDE-S4B2 sujeta a confirmación.",
        "No traslape de metadatos entre materias."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Sensibilidad cultural.",
      "Pertinencia jurídica.",
      "Problema jurídico, social o cultural.",
      "Conceptos antropológicos, culturales, jurídicos o sociales.",
      "Producto solicitado por la planeación.",
      "Conclusión jurídica transferible.",
      "Sincronización transversal conservadora.",
      "Compresión lossless por deduplicación."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar cultura, sociedad y derecho sin reducir una dimensión a la otra.",
      "Sostener conclusiones jurídicas con evidencia cultural y razonamiento propio.",
      "Mantener memoria editorial reusable sin perder especificidad local."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y ordenadas.",
      "Conceptos definidos antes del análisis.",
      "Fuentes trazables junto a afirmaciones relevantes.",
      "Supuestos marcados de forma visible.",
      "Puente argumentativo entre cultura y derecho.",
      "Postura propia diferenciada del resumen.",
      "Cierre con valor profesional.",
      "Metadatos UnADM consistentes.",
      "Rutas y tokens resueltos antes de compilar."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Fenómeno cultural -> contexto social -> implicación jurídica.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Consigna -> producto solicitado -> formato adecuado.",
      "Bibliografía base -> fuentes específicas -> citas en texto.",
      "Dato no confirmado -> marca de supuesto -> verificación pendiente.",
      "Regla heredada -> validación local -> propagación segura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Antropología de la cultura en México.",
        "Semestre 4, bloque 2.",
        "Integridad académica.",
        "Evidencia verificable.",
        "Citas trazables.",
        "Análisis propio.",
        "Postura académica.",
        "Conclusión jurídica transferible.",
        "Problema jurídico, social o cultural.",
        "Conceptos antropológicos y culturales.",
        "Conceptos jurídicos pertinentes.",
        "Planeación semanal.",
        "Producto académico.",
        "Reporte.",
        "Presentación.",
        "Bibliografía local.",
        "Normalización estructurada.",
        "JSON parseable.",
        "Unión-dedupe lossless.",
        "Fuentes provisionales.",
        "Placeholders dinámicos.",
        "Malla curricular de Derecho."
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y metadatos consistentes."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4, bloque 2",
          "kind": "supports",
          "justification": "El README local declara la ubicación curricular con esa fuente."
        },
        {
          "source": "README de materia",
          "target": "Carpeta de materia como entrada canónica",
          "kind": "supports",
          "justification": "El README establece la carpeta como punto de entrada de la asignatura."
        },
        {
          "source": "Programa analítico",
          "target": "Problema -> conceptos -> evidencia -> análisis -> conclusión",
          "kind": "develops",
          "justification": "El programa define ejes de trabajo equivalentes para los productos académicos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica requiere respaldo trazable para evitar opinión no sustentada."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión útil surge del razonamiento aplicado y no del resumen descriptivo."
        },
        {
          "source": "Conceptos antropológicos y culturales",
          "target": "Conceptos jurídicos pertinentes",
          "kind": "supports",
          "justification": "La materia requiere puente argumentativo entre cultura, sociedad y derecho."
        },
        {
          "source": "Producto académico",
          "target": "Planeación semanal",
          "kind": "depends_on",
          "justification": "El formato debe ajustarse al producto solicitado por la consigna o planeación."
        },
        {
          "source": "Citas trazables",
          "target": "Bibliografía local",
          "kind": "depends_on",
          "justification": "Toda cita en texto debe existir en el archivo .bib o en referencias locales."
        },
        {
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagación confiable de memoria editorial."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Validación local",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas no verificadas no deben convertirse en reglas definitivas."
        },
        {
          "source": "Placeholders dinámicos",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens sin resolver rompen rutas, referencias y nombres de archivo."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente de ubicación curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, producto, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "Archivo .bib local: entrada unadmSitioWeb.",
        "Archivo .bib local: entrada unadmMallaDerecho2024.",
        "Plantilla .tex local: coursename Antropologia de la cultura en Mexico.",
        "Plantilla .tex local: coursecode LDE-S4B2.",
        "Memoria origen: normalización estructurada antes de propagar.",
        "Memoria origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Regla de salto: compartir solo abstracciones editoriales estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5 conserva identidad UnADM y metadatos locales del destino.",
      "Ciclo 5 deduplica reglas repetidas sin eliminar significado útil.",
      "Ciclo 5 refuerza normalización JSON antes de propagación recursiva.",
      "Ciclo 5 transfiere solo patrones editoriales generales desde Filosofía del Derecho.",
      "Ciclo 5 excluye conceptos y citas temáticas exclusivos del origen.",
      "Ciclo 5 preserva alerta sobre fuentes heredadas provisionales.",
      "Ciclo 5 refuerza puente cultura-sociedad-derecho como marca local.",
      "Ciclo 5 refuerza resolución de placeholders en README, programa y rutas.",
      "Ciclo 5 mantiene .bib local como registro bibliográfico canónico.",
      "Ciclo 5 deja abiertas dudas sobre clave oficial, estándar de citas y fuentes base."
    ]
  }
}