{
  "summary": [
    "Se consolida memoria transversal para Derecho administrativo y control sin regresión.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se preserva identidad UnADM y encuadre de Licenciatura en Derecho.",
    "Se mantiene ubicación local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se trasladan contenidos doctrinales específicos no verificados en la materia destino.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene alerta institucional ante salidas no JSON parseables.",
    "Se conserva normalización estructurada como requisito previo de propagación.",
    "Se detectan artefactos locales en README y programa analítico que requieren corrección."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Conservar encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Mantener coursecode local LDE-S6B1 salvo evidencia institucional distinta.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar como provisional toda regla heredada no verificada localmente.",
    "Tratar Codex desde ingeniería-en-sistemas-computacionales como fuente provisional. [supuesto]",
    "Tratar GPT-Pro desde Actividad 1 como fuente provisional hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar productos con problema, conceptos, normas, doctrina, análisis propio y cierre.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y conclusión.",
    "Alinear cada entrega a la planeación semanal y al programa analítico local.",
    "Explicitar el tipo de producto solicitado antes de desarrollar.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres con saltos de línea o caracteres espurios en README. [supuesto]"
  ],
  "activity_rules": [
    "Incluir postura académica propia en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Vincular el tema con control administrativo y práctica profesional.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna de la actividad.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados.",
    "No asumir que fuentes de otras semanas correspondan a una actividad local.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Identificar si el producto es reporte, presentación o visual."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicarla aguas abajo.",
    "Validar estructura mínima completa antes de consolidar memoria.",
    "Detener propagación si existen campos críticos vacíos.",
    "Verificar integridad académica con citas verificables.",
    "Bloquear fuentes inventadas o no consultables.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar trazabilidad entre afirmaciones, citas en texto y archivo .bib local.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Confirmar correspondencia entre producto final y consigna de actividad.",
    "Compilar LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y docente en portada.",
    "Asegurar coherencia entre documenttitle, documentsubtitle y actividad real.",
    "Reemplazar Actividad X por número y nombre real de la actividad.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Validar que el archivo .bib canónico sea derecho-administrativo-y-control.bib según contexto local."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes específicas solo si fueron consultadas o proporcionadas.",
    "No inventar referencias para llenar bibliografía.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, medio y URL o archivo local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar formato institucional de citación antes de estandarizar entregables. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a nodos no equivalentes.",
    "Conservar estrategia union-dedupe lossless en fusiones futuras.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Preservar alerta institucional sobre respuestas no estructuradas.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Separar ADN editorial transversal de doctrina local no verificada."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar consigna textual de cada actividad antes de producir entregables.",
    "Confirmar si existe formato institucional obligatorio de citas para Derecho.",
    "Confirmar convención final del archivo o carpeta de referencias.",
    "Verificar si el año de consulta del sitio UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir son artefactos de generación. [supuesto]",
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Validar si derecho-administrativo-y-control.bib es el único .bib canónico local.",
    "Confirmar rúbricas específicas para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana o unidad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez innecesaria.",
        "Aplicado a la práctica profesional.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Normalización estructurada antes de propagación.",
        "Supuestos marcados de forma visible.",
        "No invención de fuentes.",
        "Respeto del programa analítico local.",
        "Consistencia entre README, LaTeX y bibliografía."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Coursecode local: LDE-S6B1.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Control administrativo.",
      "Criterio jurídico aplicable.",
      "Conclusión transferible.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en entregables coherentes.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Vincular control administrativo con práctica profesional.",
      "Producir conclusiones jurídicas transferibles.",
      "Evitar propagación de memoria no estructurada o no verificable.",
      "Proteger identidad curricular local sin importar reglas doctrinales ajenas."
    ],
    "style_markers": [
      "Abrir con problema delimitado.",
      "Declarar objetivo puntual.",
      "Distinguir conceptos de normas y doctrina.",
      "Citar fuentes verificables.",
      "Marcar [supuesto] cuando falte evidencia local.",
      "Argumentar con postura propia.",
      "Cerrar con aplicación profesional.",
      "Usar nombres canónicos de materia y archivos.",
      "Evitar redacción heredada literal entre materias no equivalentes.",
      "Corregir placeholders antes de compilar o publicar."
    ],
    "argumentative_patterns": [
      "Problema jurídico → objetivo → conceptos → marco normativo → análisis propio → conclusión.",
      "Consigna local → tipo de producto → estructura requerida → evidencia → cierre.",
      "Fuente verificable → afirmación sustentada → criterio jurídico aplicable.",
      "Regla heredada → verificación local → adopción conservadora.",
      "Dato no visible → marca [supuesto] → pregunta abierta.",
      "Control administrativo → práctica profesional → conclusión transferible.",
      "README local → plantilla LaTeX → archivo .bib → compilación validada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular local",
        "Problema jurídico",
        "Conceptos jurídicos",
        "Marco normativo",
        "Doctrina verificable",
        "Evidencia académica",
        "Análisis propio",
        "Postura argumentada",
        "Control administrativo",
        "Práctica profesional",
        "Conclusión transferible",
        "Integridad académica",
        "Normalización estructurada",
        "JSON parseable",
        "Archivo BibTeX local",
        "Plantilla LaTeX local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor, trazabilidad y fuentes verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho administrativo y control",
          "kind": "develops",
          "justification": "La materia pertenece al trayecto curricular local documentado."
        },
        {
          "source": "Malla curricular local",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local declara semestre, bloque, tipo y créditos con fuente curricular."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura académica requiere un problema delimitado."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La aplicación profesional debe derivar de fundamentos jurídicos verificables."
        },
        {
          "source": "Doctrina verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La argumentación académica se fortalece con fuentes consultables."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia debe orientar criterios aplicables a la administración pública y su control."
        },
        {
          "source": "Práctica profesional",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "El cierre debe traducir el análisis en criterio jurídico útil."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación segura requiere salida estructurada y validable."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La bibliografía local permite verificar citas y evitar fuentes inventadas."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Identidad UnADM",
          "kind": "supports",
          "justification": "La plantilla conserva metadatos, portada y formato institucional."
        },
        {
          "source": "Reglas transversales de Filosofía del Derecho",
          "target": "Estructura editorial local",
          "kind": "supports",
          "justification": "Solo se transfieren patrones estables de problema, evidencia, análisis y cierre."
        },
        {
          "source": "Contenidos doctrinales no verificados",
          "target": "Derecho administrativo y control",
          "kind": "contrasts",
          "justification": "No deben importarse contenidos sustantivos ajenos sin confirmación local."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: productos como reportes, presentaciones y visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documenttitle base de Derecho administrativo y control.",
        "Plantilla LaTeX local: documentsubtitle Actividad X.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: Figura docente Nombre por definir.",
        "Memoria institucional heredada: salida no JSON parseable desde Codex.",
        "Memoria origen transversal: normalización obligatoria antes de propagación.",
        "Memoria origen transversal: no inventar fuentes y citar evidencia verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6 refuerza sincronización transversal conservadora.",
      "Se preservan reglas locales de Derecho administrativo y control.",
      "Se integran solo patrones editoriales estables del origen.",
      "Se excluye doctrina específica de Filosofía del Derecho no verificada en destino.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se normalizan reglas hacia frases accionables.",
      "Se corrigen relaciones del grafo hacia tipos permitidos.",
      "Se refuerza trazabilidad entre afirmación, cita y .bib local.",
      "Se mantiene alerta por Codex y GPT-Pro como fuentes provisionales.",
      "Se abren vacíos locales sin inventar fuentes ni consignas."
    ]
  }
}