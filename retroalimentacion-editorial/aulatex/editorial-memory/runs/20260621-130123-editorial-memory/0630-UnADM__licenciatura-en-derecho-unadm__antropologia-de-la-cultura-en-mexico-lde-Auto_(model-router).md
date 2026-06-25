{
  "summary": [
    "Consolidación transversal ciclo 4 aplicada al nodo materia.",
    "Destino: Antropología de la cultura en México, Licenciatura en Derecho, UnADM.",
    "Se preserva identidad UnADM, integridad académica, trazabilidad y conclusión con criterio propio.",
    "Se mantiene ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se trasladan contenidos temáticos exclusivos de Filosofía del Derecho.",
    "Se refuerza normalización estructurada antes de propagar.",
    "Se conserva alerta por salidas heredadas no JSON parseable.",
    "Se refuerza resolución de placeholders y rutas corruptas antes de compilar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción: Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Citar la malla curricular de Derecho para ubicación curricular.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Mantener autor y matrícula solo si coinciden con la actividad real.",
    "No transferir metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Usar programa analítico como guía editorial de productos.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Separar secciones: conceptos clave, marco normativo o teórico, análisis propio y cierre.",
    "Alinear el entregable con la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación, referencias e insumos documentales.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex cuando aplique.",
    "Guardar fuentes específicas en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales."
  ],
  "activity_rules": [
    "Definir problema jurídico, social o cultural al inicio.",
    "Integrar conceptos antropológicos, culturales, jurídicos o sociales pertinentes.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el producto con la planeación semanal.",
    "Cerrar con conclusión transferible a la práctica jurídica cuando la consigna lo permita.",
    "Confirmar que el producto corresponda a la consigna específica de actividad."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si falta estructura mínima del esquema requerido.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Comprobar semestre, bloque, tipo y créditos contra malla curricular local.",
    "Verificar que el producto corresponda a la consigna real.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que README, programa y .tex no contengan placeholders sin resolver.",
    "Corregir rutas truncadas o caracteres anómalos antes de compilar.",
    "Revisar que portada, encabezados, referencias y bibliografía compilen sin errores.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad académica justificada.",
    "Usar letterpaper y oneside si no hay instrucción distinta.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Usar configuración en español coherente con la plantilla.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Mantener universityname como Universidad Abierta y a Distancia de México.",
    "Mantener coursename como Antropología de la cultura en México.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode LDE-S4B2 salvo indicación institucional distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens dinámicos tipo $(@{...}.Slug) antes de usar archivos.",
    "Corregir rutas truncadas como eporte o eferencias antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y realmente consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Usar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas por actividad en el .bib local.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta y nota de procedencia cuando corresponda.",
    "No asumir que bibliografía de otra materia corresponde a esta asignatura."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar hacia arriba y laterales solo reglas ya validadas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado localmente.",
    "Propagar como provisional cualquier regla heredada desde otra disciplina.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Mantener método unión-dedupe sin regresión.",
    "No eliminar reglas útiles previas durante consolidaciones futuras."
  ],
  "open_questions": [
    "Supuesto: la clave LDE-S4B2 es local; confirmar si es oficial.",
    "Confirmar estándar único de citas para la licenciatura.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar consigna y rúbrica específica de cada actividad.",
    "Confirmar producto exacto solicitado por la planeación semanal.",
    "Confirmar si autor y matrícula de la plantilla corresponden a la entrega real.",
    "Confirmar alcance de reglas heredadas desde ingeniería en contexto Derecho.",
    "Confirmar si el nombre literal del .bib sustituye definitivamente al token dinámico.",
    "Confirmar si existen referencias locales obligatorias en la carpeta de insumos."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Conclusión transferible a la práctica jurídica.",
      "Normalización estructurada.",
      "Sin regresión editorial."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en entregables adecuados a la consigna.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Construir puentes entre cultura, sociedad y Derecho.",
      "Evitar reduccionismos jurídicos en el análisis antropológico.",
      "Garantizar trazabilidad de fuentes y coherencia argumentativa."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y ordenadas.",
      "Conceptos definidos antes del análisis.",
      "Fuentes citadas con trazabilidad.",
      "Supuestos marcados de forma visible.",
      "Postura personal argumentada.",
      "Cierre con valor profesional.",
      "Metadatos UnADM consistentes.",
      "Terminología cultural y jurídica precisa."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Concepto antropológico -> contexto social -> implicación jurídica.",
      "Dato o fuente -> lectura crítica -> postura académica.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Norma o doctrina -> puente cultural -> aplicación profesional.",
      "Consigna -> producto requerido -> formato adecuado.",
      "Supuesto marcado -> verificación pendiente -> uso provisional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Antropología de la cultura en México",
        "Semestre 4 bloque 2",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión jurídica transferible",
        "Problema jurídico social o cultural",
        "Conceptos antropológicos",
        "Conceptos culturales",
        "Marco normativo o teórico",
        "Planeación semanal",
        "Producto académico",
        "Normalización estructurada",
        "Validación JSON parseable",
        "Compresión unión-dedupe",
        "Fuentes provisionales",
        "Resolución de placeholders",
        "Archivo BibTeX local",
        "Malla curricular de Derecho"
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
          "justification": "La pauta local exige conservar identidad UnADM, citas verificables y trazabilidad."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4 bloque 2",
          "kind": "supports",
          "justification": "El README local registra la malla curricular como fuente de ubicación."
        },
        {
          "source": "Antropología de la cultura en México",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "El contexto local define la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Problema jurídico social o cultural",
          "target": "Conceptos antropológicos",
          "kind": "develops",
          "justification": "El análisis debe partir de un problema y precisar los conceptos pertinentes."
        },
        {
          "source": "Conceptos antropológicos",
          "target": "Marco normativo o teórico",
          "kind": "develops",
          "justification": "La materia requiere puente entre cultura, sociedad y Derecho."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica se legitima con respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre profesional debe derivar del razonamiento y no solo del resumen."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "depends_on",
          "justification": "El formato del entregable se define por la consigna y la planeación."
        },
        {
          "source": "Validación JSON parseable",
          "target": "Normalización estructurada",
          "kind": "supports",
          "justification": "Sin estructura parseable no hay propagación confiable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Compresión unión-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicación conservadora requiere memoria estructurada."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar procedencia no verificada evita convertir supuestos en hechos."
        },
        {
          "source": "Resolución de placeholders",
          "target": "Archivo BibTeX local",
          "kind": "supports",
          "justification": "El README y programa contienen tokens dinámicos que deben resolverse antes de citar."
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
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "BibTeX local: unadmSitioWeb.",
        "BibTeX local: unadmMallaDerecho2024.",
        "Plantilla LaTeX local: article, spanish, letterpaper, oneside.",
        "Plantilla LaTeX local: coursename Antropologia de la cultura en Mexico.",
        "Plantilla LaTeX local: coursecode LDE-S4B2.",
        "Memoria heredada: alerta por salida no JSON parseable.",
        "Origen transversal: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4 preserva reglas locales y elimina duplicados semánticos.",
      "Se consolidan abstracciones estables del origen sin mover contenido temático exclusivo.",
      "Se refuerza patrón problema-conceptos-evidencia-análisis-conclusión.",
      "Se mantiene alerta de normalización por salidas no estructuradas.",
      "Se refuerza control de placeholders en README, programa, rutas .bib y .tex.",
      "Se preservan citas locales verificables unadmSitioWeb y unadmMallaDerecho2024.",
      "Se marca LDE-S4B2 como clave local pendiente de confirmación oficial.",
      "Se conserva regla de no inventar fuentes.",
      "Se conserva regla de no propagar metadatos entre materias distintas.",
      "Se fortalece puente editorial entre análisis cultural y pertinencia jurídica."
    ]
  }
}