{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analítico y bibliografía local activos.",
    "Contexto local verificado: Garantías constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicación curricular verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Se recibe memoria origen estructurada en este ciclo.",
    "Se conserva alerta histórica: Codex y GPT-Pro generaron salidas no JSON parseables.",
    "Se aplica transferencia transversal conservadora desde Filosofía del Derecho.",
    "Se propagan solo abstracciones editoriales estables.",
    "No se transfiere contenido disciplinar de Filosofía del Derecho sin validación local.",
    "Se refuerzan identidad UnADM, estructura reusable, control de calidad y grafo conceptual.",
    "Se mantiene compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como entrada canónica.",
    "Citar la malla curricular institucional para ubicación curricular.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Marcar como provisional toda regla heredada no validada localmente.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar entre materias sin validación expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir reporte, presentación, programa analítico y referencias.",
    "Preservar el programa analítico como guía editorial de la asignatura.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Mantener referencias-garantias-constitucionales como depósito de fuentes locales.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explícito.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo.",
    "Corregir placeholders generados en README y programa analítico.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Vincular cada afirmación relevante con fuente verificable o norma identificable.",
    "Distinguir hechos, normas, doctrina, datos y opinión propia.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Ajustar formato final a la consigna local.",
    "No asumir fuentes de otra semana o materia.",
    "Cerrar con conclusión aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la entrada no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar congruencia entre portada y datos curriculares locales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Confirmar que las fuentes institucionales correspondan a archivos o enlaces disponibles.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Verificar que no queden placeholders literales en rutas, nombres de archivo o bibliografía."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Preservar coursecode como LDE-S2B1 salvo indicación institucional distinta.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Verificar cierre completo de \\authortable y \\universityname.",
    "Reparar truncamiento detectado cerca de la macro de portada antes de compilar.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener nombres y metadatos sin acentos solo si la plantilla lo requiere técnicamente.",
    "No introducir paquetes nuevos sin necesidad editorial o técnica verificable.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Agregar normas jurídicas con identificador, emisor y fecha cuando sean usadas.",
    "Usar claves BibTeX estables y descriptivas.",
    "Corregir menciones al archivo bibliográfico que usen placeholders generados.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de Filosofía del Derecho corresponde a Garantías constitucionales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas editoriales generales ya validadas.",
    "Propagar controles de identidad, estructura, calidad, LaTeX y bibliografía.",
    "No propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "No trasladar contenidos temáticos entre materias sin validación local.",
    "Etiquetar herencia incompleta con necesidad de normalización manual.",
    "Mantener alerta de JSON no parseable como control institucional.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar estrategia progresiva y conservadora en nodos no equivalentes.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 2 necesita normalización manual si llega fuente no estructurada.",
    "Ciclo 3 necesita normalización manual si se reutiliza herencia incompleta."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Confirmar producto exacto solicitado por cada actividad local.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre de figura docente en plantilla destino.",
    "Confirmar si la fecha debe ser automática con today o fija por entrega.",
    "Confirmar si se requiere formato APA, jurídico mexicano u otro estilo de citación.",
    "Verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Corregir nombres truncados de archivos en README.md.",
    "Reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Supuesto: la herencia institucional no parseable se conserva solo como control de riesgo.",
    "Supuesto: reglas de Filosofía del Derecho se aplican solo como abstracciones editoriales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad entre consigna, fuentes y producto.",
        "Normalización estructurada antes de propagar.",
        "Marcado explícito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Garantías constitucionales.",
        "Semestre 2, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia cita-texto-bib.",
      "Validación local antes de transferencia disciplinar."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Conservar identidad UnADM en productos de Garantías constitucionales.",
      "Asegurar transferencia profesional de la conclusión jurídica."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados de forma explícita.",
      "Separación clara entre norma, doctrina y postura personal.",
      "Cierre con aplicación jurídica concreta.",
      "Metadatos curriculares locales consistentes.",
      "Citas explícitas para afirmaciones relevantes.",
      "No transferencia temática sin validación local.",
      "Corrección preventiva de placeholders y truncamientos."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual antes del desarrollo.",
      "Marco conceptual y normativo delimitado.",
      "Análisis propio sustentado.",
      "Contraste entre fuentes y postura personal cuando proceda.",
      "Conclusión aplicable a práctica jurídica.",
      "Coherencia entre pregunta guía, desarrollo y cierre.",
      "Ajuste estricto al producto pedido por la consigna."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Garantías constitucionales",
        "Ubicación curricular local",
        "Integridad académica",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Conceptos jurídicos pertinentes",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Consistencia cita-texto-bib",
        "Bibliografía local",
        "Normalización estructurada",
        "Propagación recursiva conservadora",
        "Fuente heredada provisional",
        "Placeholder generado",
        "Truncamiento LaTeX"
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
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Metadatos de portada",
          "kind": "supports",
          "justification": "Los datos curriculares verifican semestre, bloque, tipo y créditos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica debe apoyarse en fuentes verificables."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Cada cita debe corresponder con una entrada bibliográfica local."
        },
        {
          "source": "Bibliografía local",
          "target": "Fuentes específicas de actividad",
          "kind": "develops",
          "justification": "El archivo .bib local se amplía por actividad."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva conservadora",
          "kind": "supports",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Fuente heredada provisional",
          "target": "Fuente local verificada",
          "kind": "contrasts",
          "justification": "La herencia no validada no equivale a evidencia local."
        },
        {
          "source": "Placeholder generado",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir rompen rutas y referencias."
        },
        {
          "source": "Truncamiento LaTeX",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "El texto truncado puede dejar macros abiertas."
        }
      ],
      "evidence": [
        "README.md local declara materia, ubicación curricular y pauta editorial.",
        "programa-analitico-garantias-constitucionales.md define propósito y ejes de trabajo.",
        "garantias-constitucionales.bib contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte-garantias-constitucionales.tex contiene plantilla base y metadatos locales.",
        "README.md local muestra nombres truncados y token $(@{...}.Slug).",
        "Plantilla LaTeX local muestra truncamiento cerca de \\unive.",
        "Memoria origen aporta patrón estable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria heredada institucional exige revisar salidas no estructuradas antes de propagarlas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida destino con memoria origen ahora estructurada.",
      "Se deduplican reglas equivalentes sin eliminar controles útiles.",
      "Se preservan datos curriculares locales verificados.",
      "Se refuerza transferencia transversal solo editorial.",
      "Se excluye contenido disciplinar de Filosofía del Derecho no validado localmente.",
      "Se mantiene alerta histórica de Codex y GPT-Pro como riesgo de normalización.",
      "Se refuerza control de placeholders en README y programa analítico.",
      "Se refuerza reparación de truncamiento en plantilla LaTeX.",
      "Se preservan claves bibliográficas locales verificadas.",
      "Se actualiza grafo conceptual con relaciones permitidas y evidencia local."
    ]
  }
}