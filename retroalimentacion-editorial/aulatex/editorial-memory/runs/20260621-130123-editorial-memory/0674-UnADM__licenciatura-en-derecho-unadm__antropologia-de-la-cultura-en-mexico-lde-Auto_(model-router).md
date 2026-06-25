{
  "summary": [
    "Consolidación transversal ciclo 15 para Antropología de la cultura en México.",
    "Se aplica unión-dedupe lossless sin regresión editorial.",
    "Se preserva identidad UnADM y adscripción a Licenciatura en Derecho.",
    "Se confirma contexto local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Se reutilizan abstracciones estables del origen: objetivo, evidencia, análisis propio y cierre.",
    "Se evita transferir contenido temático exclusivo de Filosofía del Derecho.",
    "Se mantiene alerta por salidas heredadas no JSON parseable.",
    "Se refuerza normalización estructurada antes de propagar.",
    "Se conserva el README de materia como punto de entrada canónico.",
    "Se reconoce el .bib local como registro bibliográfico de la asignatura."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropología de la cultura en México.",
    "Conservar adscripción: Licenciatura en Derecho.",
    "Conservar ubicación curricular local: semestre 4, bloque 2, obligatoria, 8 créditos.",
    "Usar clave local LDE-S4B2 salvo indicación institucional distinta.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar fuente heredada desde ingeniería como provisional.",
    "Marcar fuente heredada desde GPT-Pro como provisional.",
    "No trasladar metadatos curriculares de otra materia al destino.",
    "Mantener autor y matrícula solo si coinciden con la actividad real."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Usar programa analítico como guía editorial de productos.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico, social o cultural.",
    "Separar secciones en conceptos clave, marco teórico o normativo, análisis propio y cierre.",
    "Alinear entregables con ejes: problema, conceptos, producto, análisis y conclusión.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex cuando aplique.",
    "Conservar carpeta de referencias local para insumos documentales.",
    "Corregir rutas o nombres truncados antes de compilar."
  ],
  "activity_rules": [
    "Definir problema jurídico, social o cultural al inicio.",
    "Relacionar el producto solicitado con la planeación semanal.",
    "Integrar conceptos antropológicos, culturales, jurídicos o sociales pertinentes.",
    "Distinguir evidencia, interpretación y opinión personal.",
    "Sustentar afirmaciones relevantes con fuente trazable.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Evitar reducir el análisis cultural a afirmaciones jurídicas sin puente argumentativo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión transferible a la práctica jurídica cuando la consigna lo permita.",
    "Confirmar producto exacto antes de adaptar estructura.",
    "No asumir fuentes de otra semana o materia como obligatorias del destino."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagación si falta estructura mínima del esquema requerido.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente memorias heredadas no estructuradas.",
    "Confirmar que no existan afirmaciones sin respaldo o marca de supuesto.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Verificar semestre, bloque, tipo y créditos contra la malla curricular local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que README, programa y archivos .tex no conserven placeholders.",
    "Revisar que portada, encabezados y bibliografía compilen sin errores.",
    "No propagar reglas provisionales como definitivas sin validación disciplinar."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad académica justificada.",
    "Usar letterpaper y oneside si no hay instrucción distinta.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Usar codificación y acentos correctos en español.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropología de la cultura en México.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de México.",
    "Mantener coursecode LDE-S4B2 salvo indicación institucional distinta.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y rutas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes específicas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Usar malla curricular de Derecho como fuente de ubicación curricular.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empíricos.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "No citar una fuente ausente del .bib o de referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Evitar transferir redacción literal de actividades de otra materia.",
    "No propagar metadatos específicos de esta materia a materias distintas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado.",
    "Propagar fuentes heredadas no verificadas solo como provisionales.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Mantener método unión-dedupe con preservación total.",
    "No eliminar reglas útiles previas en consolidaciones futuras.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Revalidar pertinencia disciplinar antes de bajar reglas a actividades locales."
  ],
  "open_questions": [
    "Confirmar estándar único de citas para la Licenciatura en Derecho.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar si la conclusión jurídica debe aparecer en todas las actividades antropológicas.",
    "Confirmar producto exacto de cada actividad local.",
    "Confirmar rúbrica de evaluación por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si el .bib usa nombre literal como archivo definitivo.",
    "Validar alcance real de reglas heredadas desde ingeniería en contexto Derecho.",
    "Confirmar autor y matrícula para cada entrega real.",
    "Confirmar si existen materiales antropológicos locales en carpeta de referencias.",
    "Confirmar si actividades requieren reporte, presentación o producto visual."
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
      "Análisis propio.",
      "Sensibilidad cultural.",
      "Pertinencia jurídica.",
      "Conclusión transferible.",
      "Normalización estructurada.",
      "Validación JSON parseable.",
      "Sincronización transversal sin regresión."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la materia con claridad y fundamento.",
      "Transformar la planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre.",
      "Conectar cultura, sociedad y derecho sin reduccionismos.",
      "Producir conclusiones útiles para la práctica jurídica.",
      "Preservar memoria editorial reutilizable y validada."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones funcionales y ordenadas.",
      "Conceptos definidos antes del análisis.",
      "Puente entre evidencia cultural y relevancia jurídica.",
      "Supuestos marcados de forma visible.",
      "Citas verificables y trazables.",
      "Cierre con valor profesional.",
      "Metadatos UnADM consistentes.",
      "Lenguaje académico sin afirmaciones gratuitas."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis -> conclusión.",
      "Afirmación relevante -> fuente verificable -> interpretación propia.",
      "Fenómeno cultural -> contexto social -> implicación jurídica.",
      "Consigna -> producto esperado -> estructura de entrega.",
      "Pregunta guía -> desarrollo coherente -> respuesta final.",
      "Fuente institucional -> ubicación curricular -> metadatos.",
      "Evidencia empírica -> lectura crítica -> postura académica.",
      "Supuesto no confirmado -> marca explícita -> verificación pendiente."
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
        "Sensibilidad cultural",
        "Pertinencia jurídica",
        "Conclusión jurídica transferible",
        "Problema jurídico social o cultural",
        "Conceptos antropológicos",
        "Marco teórico o normativo",
        "Planeación semanal",
        "Producto académico",
        "Normalización estructurada",
        "Validación JSON parseable",
        "Archivo BibTeX local",
        "Malla curricular de Derecho",
        "Fuentes heredadas provisionales",
        "Resolución de placeholders",
        "Unión-dedupe lossless"
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
          "justification": "La pauta local exige identidad institucional, citas verificables y cuidado académico."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 4 bloque 2",
          "kind": "supports",
          "justification": "El README local declara la malla curricular como fuente de ubicación."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las fuentes citadas deben existir en el .bib o referencias locales."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura académica se fortalece con respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre profesional debe derivar del razonamiento y no solo del resumen."
        },
        {
          "source": "Sensibilidad cultural",
          "target": "Pertinencia jurídica",
          "kind": "supports",
          "justification": "La materia requiere articular fenómenos culturales con implicaciones jurídicas."
        },
        {
          "source": "Problema jurídico social o cultural",
          "target": "Conceptos antropológicos",
          "kind": "develops",
          "justification": "El encuadre del problema define qué conceptos son pertinentes."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "supports",
          "justification": "El entregable debe ajustarse al producto solicitado."
        },
        {
          "source": "Validación JSON parseable",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "La propagación confiable requiere salida estructurada y parseable."
        },
        {
          "source": "Resolución de placeholders",
          "target": "Compilación LaTeX",
          "kind": "supports",
          "justification": "Los tokens sin expandir y nombres truncados rompen rutas, citas o compilación."
        },
        {
          "source": "Fuentes heredadas provisionales",
          "target": "Validación disciplinar",
          "kind": "depends_on",
          "justification": "Una fuente heredada no debe volverse definitiva sin confirmación local."
        },
        {
          "source": "Unión-dedupe lossless",
          "target": "Sincronización transversal sin regresión",
          "kind": "supports",
          "justification": "La consolidación preserva reglas útiles y elimina duplicados sin recorte."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 4, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y cierre.",
        "BibTeX local: entrada unadmSitioWeb.",
        "BibTeX local: entrada unadmMallaDerecho2024.",
        "Plantilla local: coursename Antropología de la cultura en México.",
        "Plantilla local: coursecode LDE-S4B2.",
        "Memoria heredada: salida no JSON parseable requiere normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15 conserva reglas locales verificadas del destino.",
      "Ciclo 15 incorpora solo abstracciones estables del origen.",
      "Ciclo 15 excluye contenidos temáticos exclusivos de Filosofía del Derecho.",
      "Ciclo 15 refuerza validación JSON antes de propagación.",
      "Ciclo 15 refuerza resolución de placeholders en README, programa y rutas.",
      "Ciclo 15 mantiene fuentes heredadas como provisionales.",
      "Ciclo 15 preserva entradas bibliográficas locales verificables.",
      "Ciclo 15 evita regresión por deduplicación conservadora."
    ]
  }
}