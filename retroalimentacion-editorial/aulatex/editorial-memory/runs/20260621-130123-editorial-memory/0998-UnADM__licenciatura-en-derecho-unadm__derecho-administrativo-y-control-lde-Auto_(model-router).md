{
  "summary": [
    "Se consolida memoria transversal para Derecho administrativo y control.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se preserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se mantiene ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se evita trasladar doctrina o bibliografía no verificada de otra materia.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta institucional por salidas no JSON parseables.",
    "Se exige normalización estructurada antes de propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redacción académica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Mantener ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular local.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Declarar como provisional toda regla heredada no verificada localmente.",
    "Tratar fuente provisional Codex como no confirmada hasta validación local.",
    "Tratar fuente provisional GPT-Pro como no confirmada hasta validación local.",
    "No trasladar identidad curricular de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Explicitar tipo de producto antes de desarrollar.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar problema, conceptos, normas, doctrina, evidencia, análisis propio y conclusión transferible.",
    "Alinear entregables a la planeación semanal y al programa analítico local.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar índices.",
    "Resolver tokens PowerShell sin expandir por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres espurios en README, como reporte- y referencias-. [supuesto]"
  ],
  "activity_rules": [
    "Verificar producto exacto solicitado por cada actividad.",
    "Identificar si el producto es reporte, presentación o visual.",
    "Vincular cada actividad con control administrativo y práctica profesional.",
    "Incluir postura académica propia del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir conceptos, normas, doctrina y datos utilizados.",
    "Formular criterio jurídico transferible a la práctica profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No omitir conclusión final orientada a aplicación jurídica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados.",
    "No asumir que fuentes de otra semana o materia corresponden a una actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Detener propagación si hay respuesta no estructurada.",
    "Detener propagación si existen campos críticos vacíos.",
    "Normalizar manualmente fuentes provisionales antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar integridad académica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones, citas y bibliografía local.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Revisar que reglas heredadas no contradigan el programa analítico local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Verificar que el producto corresponda a la consigna local de actividad.",
    "Compilar LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español.",
    "Mantener formato letterpaper según archivo base.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos académicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por número y nombre real de la actividad.",
    "Sustituir Nombre por definir por la figura docente oficial antes de entregar.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicación curricular.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes específicas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografía.",
    "No agregar referencias sin evidencia documental.",
    "Conservar metadatos mínimos: autor, título, año, medio y nota de consulta.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de Filosofía del Derecho corresponde a esta materia.",
    "Confirmar nombre canónico final del archivo de referencias si cambia la convención local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido específico de actividad a laterales.",
    "No propagar doctrina de Filosofía del Derecho sin verificación local.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Preservar alerta institucional sobre respuestas no estructuradas.",
    "Aplicar normalización manual cuando la fuente sea provisional.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Confirmar formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convención final del archivo de referencias de la materia.",
    "Verificar si el año de consulta del sitio UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell del README y programa son artefactos de generación. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en el README. [supuesto]",
    "Confirmar productos y rúbricas de actividades locales.",
    "Confirmar fuentes obligatorias por semana o unidad.",
    "Confirmar si se requiere bibliografía separada por actividad."
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
      "Control administrativo.",
      "Marco normativo y doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Criterio jurídico transferible.",
      "Conclusión práctica."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho administrativo y control con claridad, fundamento jurídico y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales verificables.",
      "Conectar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la administración pública y sus mecanismos de control.",
      "Preservar trazabilidad editorial entre programa, README, LaTeX y bibliografía."
    ],
    "style_markers": [
      "Abrir con problema delimitado.",
      "Nombrar el objetivo antes del desarrollo.",
      "Usar secciones explícitas y estables.",
      "Diferenciar norma, doctrina y dato.",
      "Citar solo fuentes verificadas.",
      "Marcar supuestos sin ambigüedad.",
      "Evitar relleno bibliográfico.",
      "Cerrar con conclusión jurídica aplicable.",
      "Mantener lenguaje sobrio y profesional.",
      "Evitar redacción literal heredada de otra materia."
    ],
    "argumentative_patterns": [
      "Problema jurídico → objetivo → marco normativo/doctrinal → análisis propio → conclusión transferible.",
      "Consigna local → producto requerido → estructura adecuada → evidencia → entrega final.",
      "Afirmación jurídica → fuente verificable → interpretación propia → consecuencia práctica.",
      "Concepto administrativo → norma aplicable → mecanismo de control → criterio profesional.",
      "Dato no visible → marca de [supuesto] → verificación pendiente.",
      "Fuente heredada → clasificación provisional → validación local antes de uso."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Integridad académica",
        "Problema jurídico",
        "Conceptos clave",
        "Marco normativo",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Control administrativo",
        "Práctica profesional",
        "Planeación semanal",
        "Programa analítico local",
        "README local",
        "Plantilla LaTeX",
        "Bibliografía local",
        "Normalización estructurada",
        "Propagación recursiva",
        "Fuentes provisionales",
        "Tokens PowerShell sin expandir"
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
          "justification": "La materia pertenece al trayecto curricular local confirmado."
        },
        {
          "source": "Semestre 6 bloque 1",
          "target": "Derecho administrativo y control",
          "kind": "depends_on",
          "justification": "La ubicación curricular se sostiene en la malla local."
        },
        {
          "source": "Programa analítico local",
          "target": "Planeación semanal",
          "kind": "supports",
          "justification": "La planeación debe interpretarse conforme al propósito y ejes del programa."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "La entrega debe adoptar el formato solicitado por la consigna."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis necesita un problema delimitado para evitar resumen descriptivo."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión práctica requiere fundamento jurídico verificable."
        },
        {
          "source": "Doctrina jurídica",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura se fortalece cuando dialoga con fuentes doctrinales verificadas."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La evidencia evita afirmaciones sin respaldo y fuentes inventadas."
        },
        {
          "source": "Control administrativo",
          "target": "Práctica profesional",
          "kind": "develops",
          "justification": "La materia exige aplicación jurídica en contextos administrativos."
        },
        {
          "source": "Bibliografía local",
          "target": "Plantilla LaTeX",
          "kind": "supports",
          "justification": "Las citas del documento deben corresponder al archivo .bib local."
        },
        {
          "source": "README local",
          "target": "Plantilla LaTeX",
          "kind": "supports",
          "justification": "Los nombres de archivos y metadatos deben permanecer consistentes."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido y estructura mínima no debe propagarse memoria."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas requieren verificación antes de consolidarse."
        },
        {
          "source": "Tokens PowerShell sin expandir",
          "target": "Consistencia editorial",
          "kind": "contrasts",
          "justification": "Los placeholders contradicen la trazabilidad de rutas y bibliografía."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: orienta productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: integra problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: bibliografía específica debe agregarse al .bib de la materia.",
        "derecho-administrativo-y-control.bib: contiene unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: contiene unadmMallaDerecho2024.",
        "Plantilla LaTeX local: curso Derecho administrativo y control.",
        "Plantilla LaTeX local: coursecode LDE-S6B1.",
        "Plantilla LaTeX local: documentsubtitle conserva Actividad X.",
        "Plantilla LaTeX local: figura docente aparece como Nombre por definir.",
        "Memoria institucional heredada: hubo salida no JSON parseable desde Codex.",
        "Memoria del destino: se preserva alerta por respuestas no estructuradas.",
        "Memoria transversal: problema, conceptos, evidencia, análisis propio y conclusión jurídica son ejes estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se consolidó destino con estrategia progresiva y conservadora.",
      "Ciclo 8: se deduplicaron reglas repetidas sin eliminar reglas útiles.",
      "Ciclo 8: se conservaron reglas locales de semestre, bloque, tipo y créditos.",
      "Ciclo 8: se reforzó normalización JSON antes de propagación recursiva.",
      "Ciclo 8: se bloquearon transferencias doctrinales no verificadas desde Filosofía del Derecho.",
      "Ciclo 8: se preservaron fuentes locales unadmSitioWeb y unadmMallaDerecho2024.",
      "Ciclo 8: se mantuvo alerta por fuentes provisionales Codex y GPT-Pro.",
      "Ciclo 8: se reforzó coherencia entre README, programa, LaTeX y .bib.",
      "Ciclo 8: se integró grafo conceptual local centrado en control administrativo y práctica profesional."
    ]
  }
}