{
  "summary": [
    "Consolidación transversal ciclo 16 aplicada al nodo materia.",
    "Destino: Antropología de la cultura en México, Licenciatura en Derecho, UnADM.",
    "Ubicación local confirmada: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se preserva identidad UnADM con integridad académica y trazabilidad.",
    "Se incorporan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se evita transferir contenido temático exclusivo de Filosofía del Derecho.",
    "Se mantiene alerta por salidas heredadas no JSON parseable.",
    "Se aplica unión-dedupe conservadora sin regresión.",
    "README, programa analítico y .bib local sostienen la estructura editorial.",
    "El cerebro editorial local prioriza problema, conceptos, evidencia, análisis propio y conclusión transferible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción: Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Citar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar fuente heredada desde ingeniería como provisional.",
    "Marcar fuente heredada desde GPT-Pro como provisional hasta validación local.",
    "Mantener autor y matrícula solo si coinciden con la actividad real.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Usar README de materia como entrada canónica.",
    "Usar programa analítico como guía editorial de productos.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Separar secciones: conceptos clave, marco antropológico o jurídico, análisis propio y cierre.",
    "Alinear cada entrega con el producto solicitado en la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales.",
    "Corregir rutas o nombres truncados antes de compilar.",
    "Resolver plantillas dinámicas tipo $(@{...}.Slug) a nombres literales."
  ],
  "activity_rules": [
    "Definir problema jurídico, social o cultural al inicio.",
    "Integrar conceptos antropológicos, culturales, jurídicos o sociales pertinentes.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Relacionar el producto solicitado con la planeación semanal.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión transferible a la práctica jurídica o profesional.",
    "No asumir que fuentes de otra semana o materia corresponden a la actividad local.",
    "Verificar que el producto corresponda a la consigna específica."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No aceptar contenido sin estructura mínima del esquema requerido.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que semestre, bloque, tipo y créditos coincidan con la malla curricular local.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que rutas del README no contengan placeholders o caracteres corruptos.",
    "Verificar que no queden plantillas sin resolver en README, programa analítico ni .tex.",
    "Revisar que portada, encabezados y bibliografía compilen sin errores.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar.",
    "Validar correspondencia del producto con la consigna de actividad."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad académica justificada.",
    "Usar letterpaper y oneside si no hay instrucción distinta.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Mantener universityname como Universidad Abierta y a Distancia de México.",
    "Mantener coursename como Antropología de la cultura en México.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode LDE-S4B2 salvo indicación institucional distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Usar configuración en español coherente con la plantilla.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y nombres de archivo."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Usar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de Filosofía del Derecho corresponde a esta materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Propagar identidad UnADM y criterios de integridad académica a nodos laterales.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "No transferir contenido temático exclusivo de Filosofía del Derecho.",
    "Etiquetar como supuesto todo elemento heredado no confirmado localmente.",
    "Propagar como provisional cualquier regla heredada desde otra disciplina.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Mantener método de compresión unión-dedupe con preservación total.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Ciclo 1 necesita normalización manual si se reutiliza memoria heredada."
  ],
  "open_questions": [
    "Confirmar estándar único de citas para la Licenciatura en Derecho.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar si el .bib usa nombre literal o plantilla dinámica como nombre definitivo.",
    "Confirmar alcance real de reglas heredadas desde ingeniería en contexto Derecho.",
    "Confirmar rúbricas específicas de actividades locales.",
    "Confirmar productos exactos solicitados por cada semana.",
    "Confirmar si autor y matrícula de plantilla corresponden a todas las entregas reales.",
    "Confirmar si la ubicación institucional en plantilla debe mantenerse fija o actualizarse."
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
        "Respeto al contexto curricular local.",
        "No traslape de metadatos entre materias."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Evidencia verificable.",
      "Problema jurídico, social o cultural.",
      "Conceptos antropológicos, culturales, jurídicos o sociales.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica o profesional transferible.",
      "Normalización estructurada.",
      "Sincronización transversal conservadora.",
      "Unión-dedupe sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en entregables verificables.",
      "Conectar cultura, sociedad y Derecho sin reducir una dimensión a otra.",
      "Sostener afirmaciones con fuentes trazables.",
      "Formar criterio propio con pertinencia jurídica y sensibilidad cultural.",
      "Cerrar cada producto con valor profesional aplicable."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Problema contextualizado.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados.",
      "Fuentes trazables.",
      "Puente entre análisis cultural y relevancia jurídica.",
      "Postura propia diferenciada del resumen.",
      "Cierre con transferencia profesional.",
      "Metadatos locales consistentes.",
      "Rutas y placeholders resueltos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Concepto cultural -> contexto social -> implicación jurídica.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Dato empírico -> lectura antropológica -> criterio jurídico.",
      "Planeación semanal -> producto solicitado -> formato adecuado.",
      "Supuesto no verificado -> marca explícita -> validación pendiente.",
      "Fuente heredada -> provisionalidad -> confirmación local."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Antropología de la cultura en México",
        "Semestre 4 bloque 2",
        "Integridad académica",
        "Evidencia verificable",
        "Citas trazables",
        "Problema jurídico social o cultural",
        "Conceptos antropológicos",
        "Conceptos culturales",
        "Conceptos jurídicos",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Planeación semanal",
        "Producto solicitado",
        "Normalización estructurada",
        "Validación JSON parseable",
        "Unión-dedupe sin regresión",
        "Fuentes provisionales",
        "Placeholders LaTeX",
        "Archivo BibTeX local"
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Antropología de la cultura en México",
          "kind": "develops",
          "justification": "La materia se encuadra localmente dentro del programa de Derecho."
        },
        {
          "source": "Semestre 4 bloque 2",
          "target": "Antropología de la cultura en México",
          "kind": "supports",
          "justification": "README local y malla curricular ubican la materia en ese contexto."
        },
        {
          "source": "Validación JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "La propagación confiable requiere estructura parseable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Unión-dedupe sin regresión",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin duplicar ruido."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica se fortalece con respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "El cierre útil surge del razonamiento y no del resumen."
        },
        {
          "source": "Conceptos antropológicos",
          "target": "Conceptos jurídicos",
          "kind": "develops",
          "justification": "La materia requiere conectar cultura y Derecho mediante puente argumentativo."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "supports",
          "justification": "El formato de entrega debe derivarse de la consigna vigente."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Citas trazables",
          "kind": "contrasts",
          "justification": "Una fuente provisional no debe tratarse como respaldo definitivo."
        },
        {
          "source": "Placeholders LaTeX",
          "target": "Archivo BibTeX local",
          "kind": "depends_on",
          "justification": "Los tokens deben resolverse al nombre literal antes de citar o compilar."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis propio y cierre.",
        "Archivo .bib local: entrada unadmSitioWeb.",
        "Archivo .bib local: entrada unadmMallaDerecho2024.",
        "Plantilla .tex local: coursename Antropologia de la cultura en Mexico.",
        "Plantilla .tex local: coursecode LDE-S4B2.",
        "Memoria origen: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria destino previa: evitar transferir contenidos temáticos exclusivos de Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16 conserva reglas locales verificadas del destino.",
      "Ciclo 16 incorpora abstracciones estables del origen sin contenido temático ajeno.",
      "Ciclo 16 refuerza validación JSON antes de propagación recursiva.",
      "Ciclo 16 refuerza resolución de placeholders en README, programa y rutas.",
      "Ciclo 16 mantiene fuentes heredadas como provisionales hasta confirmación local.",
      "Ciclo 16 consolida patrón problema-conceptos-evidencia-análisis-conclusión.",
      "Ciclo 16 preserva bibliografía local unadmSitioWeb y unadmMallaDerecho2024.",
      "Ciclo 16 evita regresión mediante unión-dedupe conservadora."
    ]
  }
}