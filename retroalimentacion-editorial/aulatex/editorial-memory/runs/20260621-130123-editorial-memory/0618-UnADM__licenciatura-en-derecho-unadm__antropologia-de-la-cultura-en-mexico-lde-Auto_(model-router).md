{
  "summary": [
    "Consolidación transversal progresiva para Antropología de la cultura en México.",
    "Se preserva identidad UnADM y adscripción a Licenciatura en Derecho.",
    "Se conserva ubicación local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se integran abstracciones estables del origen sin trasladar contenido temático exclusivo.",
    "Se refuerzan ejes: problema, conceptos, evidencia, análisis propio y conclusión transferible.",
    "Se mantiene alerta por salidas no JSON parseables en memorias heredadas.",
    "Se aplica unión-dedupe conservadora sin regresión editorial.",
    "Se prioriza trazabilidad bibliográfica y verificación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción a Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de Filosofía del Derecho al destino.",
    "Mantener autor y matrícula solo si corresponden a la actividad real.",
    "Citar la malla curricular de Derecho para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco teórico o normativo, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Usar el README local como entrada canónica.",
    "Usar el programa analítico local como guía editorial.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos.",
    "Mantener separación entre reporte, presentación, bibliografía e insumos documentales.",
    "Cerrar con conclusión sociojurídica transferible a la práctica profesional.",
    "Corregir rutas truncadas antes de compilar.",
    "Resolver placeholders dinámicos antes de referenciar archivos."
  ],
  "activity_rules": [
    "Definir el problema jurídico, social o cultural al inicio.",
    "Integrar conceptos antropológicos, culturales, jurídicos o sociales pertinentes.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Relacionar el producto con la planeación semanal.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna de la actividad.",
    "No asumir que fuentes de otras semanas o materias aplican al destino.",
    "Marcar como supuesto cualquier elemento no confirmado localmente."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No aceptar contenido sin estructura mínima del esquema requerido.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Comprobar semestre, bloque, tipo y créditos contra la malla curricular local.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que rutas del README no contengan placeholders ni caracteres corruptos.",
    "Verificar que portada, encabezados y bibliografía compilen sin errores.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar.",
    "No transferir contenidos temáticos exclusivos de Filosofía del Derecho."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad académica justificada.",
    "Usar letterpaper y oneside si no hay instrucción distinta.",
    "Mantener configuración en español coherente con la plantilla.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropología de la cultura en México.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de México.",
    "Mantener coursecode LDE-S4B2 salvo indicación institucional distinta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) en README, programa analítico y rutas."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables y realmente consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "Registrar fuentes específicas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "No citar una fuente que no exista en el .bib o referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Usar la malla curricular de Derecho como fuente de ubicación curricular.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de Filosofía del Derecho corresponde al destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias distintas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado en Derecho.",
    "Propagar como provisional cualquier regla heredada desde otra disciplina.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "Registrar incidencias de parseo como alerta reutilizable intermaterias.",
    "Mantener unión-dedupe con preservación total de reglas útiles.",
    "Evitar regresiones respecto de reglas previas.",
    "Aplicar normalización manual si se reutiliza memoria no estructurada.",
    "Ciclo 1 requiere especial control de estructura y trazabilidad."
  ],
  "open_questions": [
    "Confirmar estándar único de citas para la licenciatura.",
    "Confirmar si la clave LDE-S4B2 es oficial o local.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar nombre canónico definitivo del archivo .bib local.",
    "Confirmar si el .bib usa nombre literal o plantilla dinámica como origen.",
    "Confirmar rúbrica específica por actividad.",
    "Confirmar producto exacto solicitado en cada actividad.",
    "Confirmar alcance real de reglas heredadas desde ingeniería.",
    "Confirmar alcance transversal de reglas heredadas desde Filosofía del Derecho.",
    "Supuesto: la regla de conclusión sociojurídica aplica por pauta local.",
    "Supuesto: las fuentes heredadas no verificadas permanecen provisionales."
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
        "Fuentes heredadas tratadas como provisionales.",
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Antropología de la cultura en México.",
        "Semestre 4, bloque 2.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Clave local LDE-S4B2 sujeta a confirmación."
      ]
    },
    "essence": [
      "Problema jurídico, social o cultural como punto de partida.",
      "Conceptos antropológicos y jurídicos articulados.",
      "Evidencia verificable como base del análisis.",
      "Análisis propio con postura académica.",
      "Puente argumentativo entre cultura y derecho.",
      "Conclusión sociojurídica transferible.",
      "Producto alineado con planeación semanal.",
      "Identidad UnADM sin pérdida de trazabilidad.",
      "Compresión editorial por deduplicación conservadora.",
      "Separación entre reglas locales y herencias provisionales."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la materia con claridad y fundamento.",
      "Convertir planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis y cierre argumentativo.",
      "Fortalecer criterio propio en contexto cultural y jurídico mexicano.",
      "Evitar descripciones sin análisis.",
      "Evitar traslados temáticos impropios entre asignaturas.",
      "Sostener memoria editorial persistente y reutilizable.",
      "Prevenir propagación de salidas no estructuradas."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre contextual breve.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Afirmaciones relevantes con fuente trazable.",
      "Postura propia diferenciada de la evidencia.",
      "Cierre con valor profesional.",
      "Lenguaje académico sin relleno.",
      "Precisión conceptual en cultura y derecho.",
      "Evitar redacción literal heredada."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Concepto cultural -> contexto social -> implicación jurídica.",
      "Dato empírico -> lectura antropológica -> pertinencia para Derecho.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Consigna -> producto esperado -> estructura adecuada.",
      "Supuesto -> marca explícita -> verificación pendiente.",
      "Fuente heredada -> provisionalidad -> validación local.",
      "Resumen descriptivo -> contraste crítico -> postura argumentada.",
      "Planeación semanal -> artefacto académico -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Antropología de la cultura en México",
        "Ubicación curricular local",
        "Malla curricular de Derecho",
        "Problema jurídico, social o cultural",
        "Conceptos antropológicos",
        "Conceptos jurídicos",
        "Evidencia verificable",
        "Integridad académica",
        "Análisis propio",
        "Postura académica",
        "Conclusión sociojurídica transferible",
        "Planeación semanal",
        "Producto académico",
        "Reporte",
        "Presentación",
        "Bibliografía local",
        "Archivo BibTeX local",
        "Normalización estructurada",
        "Validación JSON parseable",
        "Unión-dedupe conservadora",
        "Fuente provisional",
        "Placeholder dinámico",
        "Rutas truncadas",
        "No transferencia temática impropia"
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
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular local",
          "kind": "supports",
          "justification": "El README local la declara como fuente para semestre, bloque, tipo y créditos."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Antropología de la cultura en México",
          "kind": "develops",
          "justification": "Define el encuadre institucional de la materia destino."
        },
        {
          "source": "Problema jurídico, social o cultural",
          "target": "Conceptos antropológicos",
          "kind": "develops",
          "justification": "El problema inicial orienta la selección conceptual pertinente."
        },
        {
          "source": "Conceptos antropológicos",
          "target": "Conceptos jurídicos",
          "kind": "supports",
          "justification": "La materia requiere puente argumentativo entre cultura y Derecho."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica debe apoyarse en fuentes trazables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión sociojurídica transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento, no del resumen."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "depends_on",
          "justification": "El formato de entrega debe ajustarse a la consigna."
        },
        {
          "source": "Producto académico",
          "target": "Reporte",
          "kind": "develops",
          "justification": "El reporte es una plantilla local disponible para entregables escritos."
        },
        {
          "source": "Producto académico",
          "target": "Presentación",
          "kind": "develops",
          "justification": "La presentación es una plantilla local disponible para productos expositivos."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Bibliografía local",
          "kind": "supports",
          "justification": "Las fuentes específicas de actividad deben registrarse en el .bib de la materia."
        },
        {
          "source": "Validación JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagación confiable."
        },
        {
          "source": "Unión-dedupe conservadora",
          "target": "No transferencia temática impropia",
          "kind": "supports",
          "justification": "La sincronización transversal conserva reglas útiles sin importar contenidos exclusivos."
        },
        {
          "source": "Fuente provisional",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar provisionalidad evita convertir herencias no verificadas en autoridad."
        },
        {
          "source": "Placeholder dinámico",
          "target": "Archivo BibTeX local",
          "kind": "contrasts",
          "justification": "El placeholder debe resolverse al nombre literal antes de compilar o citar."
        },
        {
          "source": "Rutas truncadas",
          "target": "Producto académico",
          "kind": "contrasts",
          "justification": "Las rutas corruptas impiden reproducibilidad y compilación confiable."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: propósito de transformar planeación en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis y conclusión.",
        "Programa analítico local: fuentes específicas en archivo .bib de la materia.",
        "BibTeX local: entrada unadmSitioWeb.",
        "BibTeX local: entrada unadmMallaDerecho2024.",
        "Plantilla local: coursename Antropología de la cultura en México.",
        "Plantilla local: coursecode LDE-S4B2.",
        "Memoria heredada: alerta por salida no JSON parseable.",
        "Origen transversal: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
        "Origen transversal: no propagar sin validación JSON y estructura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar contenido útil.",
      "Se preservó la identidad local de Antropología de la cultura en México.",
      "Se bloquearon metadatos específicos de Filosofía del Derecho para este destino.",
      "Se conservaron abstracciones transversales de estructura y calidad.",
      "Se reforzó el puente cultura-derecho como rasgo local.",
      "Se normalizó la alerta de JSON no parseable como gate transversal.",
      "Se mantuvo la provisionalidad de fuentes heredadas no verificadas.",
      "Se incorporó la corrección de placeholders y rutas truncadas como control LaTeX.",
      "Se conservaron citas locales verificadas: unadmSitioWeb y unadmMallaDerecho2024.",
      "Se dejó abierta la confirmación de clave, estándar de citas y fuentes oficiales adicionales."
    ]
  }
}