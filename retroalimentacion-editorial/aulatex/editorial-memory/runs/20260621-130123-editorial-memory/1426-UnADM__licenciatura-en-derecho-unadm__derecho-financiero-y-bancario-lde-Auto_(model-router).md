{
  "summary": [
    "Materia destino consolidada con identidad UnADM y compresión union-dedupe.",
    "Se sincroniza ADN editorial transversal desde Filosofía del Derecho sin trasladar redacción local.",
    "Derecho financiero y bancario se ubica en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La carpeta local funciona como punto de entrada canónico de la materia.",
    "Se preservan reglas de integridad académica, citas verificables y conclusión jurídica propia.",
    "Se mantienen antecedentes de salida no JSON parseable como riesgo editorial.",
    "README y programa analítico contienen artefactos de plantilla pendientes de corrección.",
    "El reporte base usa título y subtítulo de plantilla pendientes de personalizar por actividad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar el programa académico Licenciatura en Derecho.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Registrar tipo obligatoria y 8 créditos según README local.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Conservar Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado del docente, grupo o consigna.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "Usar la carpeta de materia como entrada canónica."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, análisis propio y conclusión transferible.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeación semanal.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token de plantilla del .bib como derecho-financiero-y-bancario.bib.",
    "No eliminar reglas válidas previas; agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Confirmar consigna antes de crear una actividad específica.",
    "Delimitar el problema jurídico o social de la actividad.",
    "Sustentar afirmaciones con norma, doctrina, datos o fuentes verificables.",
    "Incluir postura argumentada del estudiante, no solo descripción.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión aplicable a la práctica profesional.",
    "Evitar asumir fuentes de otras semanas sin confirmación local.",
    "Adaptar reporte, presentación o producto visual a la planeación confirmada."
  ],
  "quality_gates": [
    "Verificar que toda salida sea JSON parseable antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear propagación si hay campos obligatorios vacíos sin marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Comprobar que cada mejora sea verificable y no invente fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Verificar correspondencia del producto con la consigna de actividad."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Reemplazar título y subtítulo de plantilla por los de la actividad real.",
    "Mantener título, subtítulo y materia sincronizados entre portada y contenido.",
    "Completar Figura docente con dato real o etiqueta de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres faltantes en nombres de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular local como fuente de ubicación curricular.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, deduplicadas y parseables.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Propagar lateralmente solo abstracciones independientes de una actividad específica.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias no equivalentes.",
    "Etiquetar origen de reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada de ciclos previos.",
    "Conservar vacíos de contexto local como preguntas abiertas con marca de supuesto."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Definir formato obligatorio de citación para la materia.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Validar si la localización de portada debe mantenerse.",
    "Verificar si los nombres del README deben corregirse manualmente o regenerarse.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar rúbrica específica antes de ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita.",
        "No regresión de reglas útiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex, .bib, README y programa analítico.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos jurídicos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Producir reportes, presentaciones o productos visuales según consigna.",
      "Conectar la formación jurídica con aplicación profesional.",
      "Sostener memoria editorial persistente sin regresión."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados explícitamente.",
      "Fuentes no inventadas.",
      "Citas consistentes con el .bib.",
      "Estructura visible por secciones.",
      "Conclusión con criterio jurídico propio.",
      "Corrección previa de plantillas y tokens.",
      "Lenguaje académico en español."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Análisis propio con soporte verificable.",
      "Contraste entre descripción y postura crítica.",
      "Cierre con implicación práctica jurídica.",
      "Coherencia entre pregunta guía, desarrollo y conclusión.",
      "Ajuste del producto al formato solicitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Ubicación curricular",
        "Problema jurídico o social",
        "Conceptos jurídicos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Conclusión transferible",
        "Planeación semanal",
        "Producto académico",
        "Consistencia .tex-.bib",
        "Normalización estructurada",
        "Propagación recursiva",
        "Compresión union-dedupe",
        "Supuesto editorial",
        "Bibliografía base",
        "Bibliografía específica de actividad"
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
          "justification": "La identidad institucional exige trazabilidad, fuentes verificables y formato consistente."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho financiero y bancario",
          "kind": "develops",
          "justification": "La materia pertenece al programa académico local confirmado."
        },
        {
          "source": "Ubicación curricular",
          "target": "Derecho financiero y bancario",
          "kind": "supports",
          "justification": "README local confirma semestre 3, bloque 2, tipo obligatoria y 8 créditos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje de análisis y evita entregas meramente descriptivas."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "El análisis requiere fundamento jurídico o doctrinal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "La planeación determina si la entrega será reporte, presentación o producto visual."
        },
        {
          "source": "Consistencia .tex-.bib",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las citas del texto deben corresponder con entradas bibliográficas reales."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura de memoria."
        },
        {
          "source": "Compresión union-dedupe",
          "target": "No regresión editorial",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin recortar contenido válido."
        },
        {
          "source": "Supuesto editorial",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar datos no confirmados evita presentar inferencias como hechos."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "develops",
          "justification": "Las fuentes institucionales sostienen el marco general y cada actividad agrega fuentes propias."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "derecho-financiero-y-bancario.bib: entrada unadmSitioWeb.",
        "derecho-financiero-y-bancario.bib: entrada unadmMallaDerecho2024.",
        ".tex local: autor Martin Jonathan de la Cruz.",
        ".tex local: matrícula ES2611202040.",
        ".tex local: título y subtítulo de plantilla.",
        "Memoria heredada: revisar salida no estructurada antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5 consolida destino a nivel materia con sincronización transversal.",
      "Se preservan reglas locales verificadas de Derecho financiero y bancario.",
      "Se transfieren solo abstracciones estables desde Filosofía del Derecho.",
      "Se eliminan duplicados semánticos sin recortar reglas útiles.",
      "Se refuerza bloqueo de propagación ante JSON no parseable.",
      "Se corrigen relaciones del grafo a tipos permitidos.",
      "Se mantiene abierto todo vacío de contexto local no confirmado.",
      "Se evita importar citas doctrinales específicas de la actividad origen."
    ]
  }
}