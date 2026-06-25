{
  "summary": [
    "Memoria de materia consolidada para Derecho financiero y bancario con identidad UnADM.",
    "Sincronización transversal desde Filosofía del Derecho aplicada solo como abstracción editorial estable.",
    "Se preservan reglas institucionales, estructurales, bibliográficas y de calidad sin regresión.",
    "La materia local se ubica en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene el flujo editorial: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se detectan artefactos de plantilla en README, programa analítico y portada .tex.",
    "Se conservan antecedentes de salidas no parseables desde Codex y GPT-Pro como riesgo editorial.",
    "Se aplica compresión lossless por unión semántica y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar la Licenciatura en Derecho como programa académico del destino.",
    "Usar datos locales: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar tipo obligatoria y 8 créditos según README local.",
    "Conservar autor Martin Jonathan de la Cruz y matrícula ES2611202040 según .tex local.",
    "Marcar como supuesto cualquier dato no confirmado del docente, grupo o consigna.",
    "Conservar Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Tratar fuentes heredadas de Codex y GPT-Pro como provisionales y auditables.",
    "Citar la malla curricular local solo para ubicación curricular verificable."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, análisis propio y conclusión transferible.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeación semanal.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Usar reportes, presentaciones o productos visuales según consigna confirmada.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token de plantilla del .bib a derecho-financiero-y-bancario.bib.",
    "Corregir nombres rotos de archivos y carpetas antes de referenciarlos.",
    "No eliminar reglas útiles previas; agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Iniciar cada actividad con un problema jurídico o social delimitado.",
    "Sustentar afirmaciones con normas, doctrina, datos o fuentes verificables.",
    "Distinguir descripción conceptual, análisis propio y conclusión jurídica.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas puramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar el producto a la planeación semanal confirmada.",
    "No asumir fuentes de otra semana o actividad sin confirmación local.",
    "Cerrar con conclusión aplicable a la práctica profesional.",
    "Marcar como supuesto cualquier vacío de consigna o rúbrica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Bloquear campos obligatorios vacíos sin marca de supuesto.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna específica.",
    "Revisar que README, programa analítico, .tex y .bib no se contradigan."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado del .tex.",
    "Mantener título, subtítulo y materia sincronizados con la actividad real.",
    "Reemplazar título y subtítulo de plantilla antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explícita de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas .bib.",
    "No trasladar citas específicas de Filosofía del Derecho sin uso real en esta materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar lateralmente solo reglas independientes de actividad o asignatura específica.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Mantener compresión union-dedupe con pérdida cero.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Compartir identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferir redacción literal de actividades no equivalentes.",
    "Mantener vacíos de contexto local como preguntas abiertas.",
    "Ciclo 15 conserva riesgo histórico de salidas no parseables desde motores externos."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar producto exacto solicitado por cada actividad.",
    "Confirmar rúbrica específica de evaluación.",
    "Definir formato obligatorio de citación; supuesto: no definido aún.",
    "Validar si la localización de portada debe mantenerse o actualizarse.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Verificar si los nombres rotos del README deben corregirse manualmente o regenerarse.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si existen lineamientos locales para productos visuales o presentaciones."
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
      "Producto alineado a planeación.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia .tex-.bib.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Garantizar trazabilidad institucional y bibliográfica.",
      "Sostener una voz jurídica propia sin perder rigor académico.",
      "Convertir vacíos de contexto en supuestos explícitos o preguntas abiertas."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos explícitos.",
      "Fuentes reales y consultables.",
      "Consistencia entre narrativa, citas y estructura.",
      "Portada y metadatos institucionales sincronizados.",
      "Conclusiones prácticas y jurídicas.",
      "Separación clara entre descripción, análisis y postura.",
      "Dedupe semántico sin pérdida editorial."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Evidencia verificable como soporte.",
      "Análisis propio con criterio jurídico.",
      "Contraste entre fuentes cuando proceda.",
      "Cierre con implicación profesional.",
      "Coherencia entre pregunta guía, desarrollo y conclusión.",
      "Adaptación del producto a la consigna confirmada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Ubicación curricular",
        "Malla curricular de Derecho",
        "Problema jurídico o social",
        "Conceptos jurídicos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Producto solicitado por planeación",
        "Conclusión transferible",
        "Integridad académica",
        "Consistencia .tex-.bib",
        "Normalización estructurada",
        "Propagación recursiva segura",
        "Artefactos de plantilla",
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y criterio propio."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la señala como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje del desarrollo argumentativo."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Las afirmaciones jurídicas requieren fuentes comprobables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de respaldo normativo, doctrinal o documental."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Estructura de entrega",
          "kind": "develops",
          "justification": "La planeación define si corresponde reporte, presentación o producto visual."
        },
        {
          "source": "Consistencia .tex-.bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas deben corresponder con entradas bibliográficas reales."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura de memoria."
        },
        {
          "source": "Artefactos de plantilla",
          "target": "Calidad editorial",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir y nombres rotos degradan la entrega final."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "develops",
          "justification": "Las fuentes de actividad amplían la base institucional sin sustituirla."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de trabajo basados en problema, conceptos, producto, análisis y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la materia.",
        "derecho-financiero-y-bancario.bib: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte local .tex: autor, matrícula, curso, clave, semestre, bloque, tipo y créditos.",
        "Contexto local: README contiene nombres rotos y token $(@{...}.Slug).",
        "Contexto local: .tex conserva título y subtítulo de plantilla.",
        "Memoria heredada: revisar respuestas no estructuradas antes de aplicar aguas abajo.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se consolidó memoria de materia con estrategia progresiva y conservadora.",
      "Se deduplicaron reglas repetidas sin recortar contenido útil.",
      "Se transfirieron solo abstracciones estables desde Filosofía del Derecho.",
      "Se excluyeron citas y conceptos específicos de Filosofía del Derecho no verificados para esta materia.",
      "Se reforzó el eje problema-conceptos-evidencia-análisis-conclusión.",
      "Se preservaron datos curriculares locales verificados del destino.",
      "Se mantuvieron autoría y matrícula observadas en el .tex local.",
      "Se marcó como pendiente la figura docente.",
      "Se reforzó la normalización JSON como gate de propagación.",
      "Se documentó el riesgo de artefactos de plantilla en README, programa y .tex.",
      "Se sostuvo el archivo derecho-financiero-y-bancario.bib como bibliografía canónica.",
      "Se mantuvo la regla de no inventar fuentes."
    ]
  }
}