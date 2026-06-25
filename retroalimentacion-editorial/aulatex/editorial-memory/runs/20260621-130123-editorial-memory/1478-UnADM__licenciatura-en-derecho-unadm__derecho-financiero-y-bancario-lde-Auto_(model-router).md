{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho financiero y bancario.",
    "Se preserva identidad UnADM con compresión union-dedupe sin regresión.",
    "Se sincronizan abstracciones transversales desde Filosofía del Derecho.",
    "Se conservan solo reglas estables entre nodos no equivalentes.",
    "La materia local está ubicada en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La carpeta local es punto de entrada canónico de la asignatura.",
    "El destino exige integridad académica, citas verificables y conclusión jurídica propia.",
    "Se detectan artefactos de plantilla en README y programa analítico.",
    "El reporte local conserva título y subtítulo de plantilla pendientes de actividad real.",
    "Existen antecedentes de salidas no parseables desde Codex y GPT-Pro."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y metadatos.",
    "Usar la Licenciatura en Derecho como programa académico del destino.",
    "Usar materia local: Derecho financiero y bancario.",
    "Usar clave local: LDE-S3B2.",
    "Usar ubicación curricular local: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente curricular institucional.",
    "Conservar autor local Martin Jonathan de la Cruz según .tex.",
    "Conservar matrícula local ES2611202040 según .tex.",
    "Conservar localización Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado en consigna, docente o grupo.",
    "Tratar memorias heredadas de Codex y GPT-Pro como provisionales y auditables.",
    "No usar contenido heredado de otra asignatura como contenido local sin verificación."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canónica.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Alinear cada entrega a la planeación semanal confirmada.",
    "Iniciar con problema jurídico o social delimitado.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar fuentes antes de formular conclusiones.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar la estructura al producto solicitado: reporte, presentación o producto visual.",
    "No eliminar reglas previas válidas; agregar solo mejoras verificables.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token de plantilla del .bib a derecho-financiero-y-bancario.bib."
  ],
  "activity_rules": [
    "Confirmar la consigna antes de crear una actividad específica.",
    "Verificar que el producto corresponda a la actividad real.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables.",
    "Usar citas explícitas para afirmaciones jurídicas relevantes.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Vincular el análisis al campo financiero y bancario cuando la consigna lo permita.",
    "No asumir fuentes de semanas posteriores como fuentes de la actividad vigente.",
    "Marcar como supuesto cualquier alcance no visible en la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que el producto final responda a la consigna real.",
    "Auditar fuentes heredadas antes de usarlas como evidencia local."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Sincronizar título, subtítulo, materia y actividad entre portada y contenido.",
    "Reemplazar título y subtítulo de plantilla antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres faltantes en nombres del README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas usadas y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener compresión union-dedupe con pérdida cero.",
    "Propagar a nivel materia reglas generales de identidad, estructura, calidad y bibliografía.",
    "Propagar lateralmente solo abstracciones independientes de actividad específica.",
    "Evitar transferir redacción literal de Filosofía del Derecho.",
    "Evitar transferir bibliografía específica de Filosofía del Derecho al destino.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Mantener vacíos de contexto local como preguntas abiertas con marca de supuesto.",
    "Reforzar conexiones entre problema, evidencia, análisis propio y conclusión."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Definir formato obligatorio de citación: supuesto no confirmado.",
    "Validar si la localización de portada debe mantenerse.",
    "Verificar si los nombres del README deben corregirse manualmente o regenerarse.",
    "Confirmar rúbrica de evaluación específica por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si habrá carpeta local de referencias por actividad."
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
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita.",
        "No regresión de reglas útiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos.",
        "Fuente curricular institucional: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre narrativa, citas y estructura.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Orientar reportes, presentaciones y productos visuales con fundamento jurídico.",
      "Asegurar transferencia profesional desde la conclusión jurídica.",
      "Preservar memoria editorial útil sin introducir fuentes no verificadas."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos marcados de forma explícita.",
      "Fuentes verificables antes de afirmaciones fuertes.",
      "Consistencia entre portada, contenido, citas y bibliografía.",
      "Separación clara entre descripción, análisis y postura.",
      "Cierre con implicación práctica.",
      "Sin redacción literal transferida entre asignaturas no equivalentes.",
      "Sin fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio diferenciado del resumen.",
      "Postura jurídica razonada.",
      "Conclusión derivada de la evidencia.",
      "Implicación profesional aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Ubicación curricular",
        "Planeación semanal",
        "Problema jurídico o social",
        "Conceptos jurídicos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Conclusión transferible",
        "Integridad académica",
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
          "justification": "La identidad institucional exige trazabilidad, formalidad y citas verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho financiero y bancario",
          "kind": "develops",
          "justification": "La materia pertenece al programa académico local verificado."
        },
        {
          "source": "Ubicación curricular",
          "target": "Derecho financiero y bancario",
          "kind": "supports",
          "justification": "Semestre, bloque, tipo y créditos contextualizan la materia."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "depends_on",
          "justification": "El formato de entrega debe derivar de la consigna vigente."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje argumentativo del desarrollo."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las fuentes jurídicas respaldan el razonamiento académico."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fuentes comprobables."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Postura argumentada del estudiante",
          "kind": "develops",
          "justification": "La postura surge del razonamiento y no del resumen descriptivo."
        },
        {
          "source": "Consistencia .tex-.bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas deben corresponder con entradas bibliográficas reales."
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
          "justification": "La deduplicación conserva reglas útiles sin recorte semántico."
        },
        {
          "source": "Supuesto editorial",
          "target": "Calidad verificable",
          "kind": "supports",
          "justification": "Los vacíos de contexto deben declararse antes de argumentar."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "README local: nombres con caracteres faltantes y token .bib sin expandir.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "Bib local: entradas base unadmSitioWeb y unadmMallaDerecho2024.",
        "Tex local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Tex local: título y subtítulo de plantilla pendientes de actividad real.",
        "Memoria origen: normalización estructurada obligatoria antes de propagar.",
        "Memoria origen: no inventar fuentes y usar citas verificables.",
        "Memoria heredada: revisar salida no estructurada antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se deduplican reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 18: se conserva ubicación curricular local verificada.",
      "Ciclo 18: se evita transferir bibliografía específica de Filosofía del Derecho.",
      "Ciclo 18: se refuerza el patrón problema-evidencia-análisis-conclusión.",
      "Ciclo 18: se mantienen Codex y GPT-Pro como fuentes provisionales auditables.",
      "Ciclo 18: se corrigen relaciones del grafo a tipos permitidos.",
      "Ciclo 18: se dejan vacíos locales como preguntas abiertas."
    ]
  }
}