{
  "summary": [
    "Consolidación transversal ciclo 1 aplicada al nodo materia.",
    "Destino local: Antropología de la cultura en México, Licenciatura en Derecho, UnADM.",
    "Se preserva ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se integran solo abstracciones editoriales estables del origen.",
    "Se evita transferir contenido temático exclusivo de Filosofía del Derecho.",
    "Se refuerza identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
    "Se mantiene alerta por salidas heredadas no JSON parseables.",
    "Se aplica unión-dedupe conservadora sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción: Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de Filosofía del Derecho al destino.",
    "Mantener autor y matrícula solo si coinciden con la actividad real."
  ],
  "structure_rules": [
    "Usar README de materia como entrada canónica.",
    "Usar programa analítico local como guía editorial.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Separar secciones en conceptos clave, marco teórico o normativo, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Distinguir reporte, presentación, referencias e insumos documentales.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Guardar fuentes específicas en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos locales.",
    "Corregir rutas truncadas antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de citar o compilar.",
    "Cerrar con conclusión transferible a la práctica jurídica."
  ],
  "activity_rules": [
    "Definir problema jurídico, social o cultural al inicio.",
    "Integrar conceptos antropológicos, culturales, jurídicos y sociales pertinentes.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el producto con la planeación semanal.",
    "Confirmar que el producto corresponda a la consigna específica."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "No aceptar contenido sin estructura mínima del esquema requerido.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmación relevante tenga respaldo o marca de supuesto.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Validar semestre, bloque, tipo y créditos contra la malla curricular local.",
    "Verificar correspondencia del producto con la consigna de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Revisar que portada, encabezados y bibliografía compilen sin errores.",
    "Verificar que no queden placeholders en README, programa ni .tex.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar."
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
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Usar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Agregar entradas BibTeX específicas por actividad en el .bib local.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No citar fuentes ausentes del .bib o de referencias locales.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "Supuesto: antropologia-de-la-cultura-en-mexico.bib es el .bib canónico local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo reglas generales entre materias no equivalentes.",
    "Propagar identidad UnADM e integridad académica a nodos laterales.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado localmente.",
    "Marcar como provisional cualquier regla heredada desde otra disciplina.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Mantener unión-dedupe lossless sin eliminar reglas útiles previas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Ciclo 1 requiere normalización manual si se reutiliza memoria no estructurada."
  ],
  "open_questions": [
    "Confirmar estándar único de citas para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar producto exacto de cada actividad: reporte, presentación u otro formato.",
    "Confirmar rúbrica específica antes de fijar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el .bib usa nombre literal o plantilla dinámica como nombre definitivo.",
    "Supuesto: reglas heredadas desde ingeniería aplican solo como alerta técnica.",
    "Supuesto: abstracciones de Filosofía del Derecho aplican como estructura, no como contenido temático."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Orientado a trazabilidad.",
        "Sensible al contexto cultural mexicano."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Metadatos institucionales consistentes.",
        "Fuentes heredadas marcadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Antropología de la cultura en México.",
        "Semestre 4, bloque 2, obligatoria, 8 créditos.",
        "Clave local: LDE-S4B2.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico, social o cultural como punto de partida.",
      "Conceptos antropológicos, culturales, jurídicos y sociales pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Puente argumentativo entre cultura y derecho.",
      "Producto alineado con planeación semanal.",
      "Conclusión jurídica transferible a la práctica profesional.",
      "Normalización estructurada antes de propagar.",
      "Compilación LaTeX limpia y referencias consistentes."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la materia con claridad, fundamento y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular la reflexión cultural con la formación jurídica.",
      "Garantizar trazabilidad editorial desde README, programa, .tex y .bib.",
      "Evitar regresiones durante sincronizaciones transversales."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Afirmaciones respaldadas con fuente.",
      "Diferencia clara entre evidencia e interpretación.",
      "Postura personal argumentada.",
      "Cierre con valor profesional.",
      "Metadatos UnADM consistentes.",
      "Rutas y nombres de archivo resueltos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Concepto cultural -> contexto social -> implicación jurídica.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Consigna -> producto solicitado -> formato LaTeX adecuado.",
      "Fuente institucional -> ubicación curricular -> metadatos del documento.",
      "Supuesto no confirmado -> marca explícita -> verificación pendiente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Antropología de la cultura en México",
        "Licenciatura en Derecho",
        "Ubicación curricular local",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Problema jurídico, social o cultural",
        "Conceptos antropológicos",
        "Conceptos culturales",
        "Conceptos jurídicos",
        "Puente cultura-derecho",
        "Conclusión jurídica transferible",
        "Planeación semanal",
        "Producto académico",
        "Normalización estructurada",
        "JSON parseable",
        "Bibliografía local",
        "Plantilla LaTeX de materia",
        "Placeholders dinámicos",
        "Fuentes provisionales heredadas"
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
          "justification": "La pauta local exige conservar identidad UnADM, citas verificables y criterio propio."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "README y programa local fijan semestre, bloque, tipo y créditos."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular local",
          "kind": "supports",
          "justification": "El README declara la malla curricular como fuente de ubicación."
        },
        {
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay propagación confiable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "La memoria heredada exige revisar salidas no estructuradas antes de aplicar aguas abajo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El criterio personal debe legitimarse con respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión útil surge del razonamiento y no del resumen."
        },
        {
          "source": "Conceptos antropológicos",
          "target": "Puente cultura-derecho",
          "kind": "develops",
          "justification": "La materia requiere integrar cultura, sociedad y derecho sin reducir lo cultural a lo jurídico."
        },
        {
          "source": "Placeholders dinámicos",
          "target": "Compilación LaTeX limpia",
          "kind": "contrasts",
          "justification": "Los tokens sin resolver rompen rutas, citas o nombres de archivo."
        },
        {
          "source": "Fuentes provisionales heredadas",
          "target": "Reglas definitivas locales",
          "kind": "contrasts",
          "justification": "Lo heredado no verificado no debe tratarse como validado para la materia."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa indica transformar la planeación en reportes, presentaciones o productos visuales."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local conserva fuentes institucionales y debe recibir fuentes específicas por actividad."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis propio y cierre.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la materia.",
        "Archivo .bib local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local: coursename, coursecode, documentsubject y universityname definidos.",
        "Memoria heredada: alerta por salida no JSON parseable desde Codex.",
        "Origen transversal: reglas estables de objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
        "Origen transversal: no transferir contenido temático exclusivo entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se consolidó memoria por unión-dedupe conservadora.",
      "Se preservó identidad local de Antropología de la cultura en México.",
      "Se mantuvieron reglas útiles previas sin degradar especificidad local.",
      "Se añadieron abstracciones estables desde Filosofía del Derecho.",
      "Se descartó transferencia temática específica del origen.",
      "Se reforzó el puente cultura-derecho como patrón argumentativo local.",
      "Se reforzó bloqueo de propagación ante JSON no parseable.",
      "Se reforzó resolución de placeholders en README, programa, .tex y .bib.",
      "Se mantuvo provisionalidad de fuentes heredadas no verificadas.",
      "Se consolidó grafo conceptual con citas locales verificables."
    ]
  }
}