{
  "summary": [
    "Materia destino consolidada con cerebro editorial mínimo y memoria local activa.",
    "Contexto local verificado: Garantías constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicación curricular verificada: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Se transfiere solo abstracción editorial estable desde Filosofía del Derecho.",
    "No se transfiere contenido disciplinar de Filosofía del Derecho sin validación local.",
    "Se conserva alerta institucional sobre salidas heredadas no estructuradas.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "La estrategia sigue siendo progresiva y conservadora."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos locales: Garantías constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo obligatoria y 8 créditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas desde Codex y GPT-Pro como provisionales.",
    "No trasladar contenido disciplinar entre materias sin validación expresa.",
    "Citar la malla curricular solo para ubicación curricular verificada."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía.",
    "Usar nombres locales verificados de reporte, presentación y archivo .bib.",
    "Preservar el programa analítico como guía editorial de la asignatura.",
    "Mantener referencias-garantias-constitucionales como depósito de fuentes locales.",
    "Corregir nombres truncados en README antes de usarlo como índice operativo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social claro desde la introducción.",
    "Vincular cada afirmación relevante con fuente verificable o norma identificable.",
    "Distinguir conceptos, normas, doctrina, datos y postura personal.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliográfico.",
    "Adaptar profundidad y formato a la consigna local de cada actividad.",
    "No asumir fuentes de otra materia como fuentes de Garantías constitucionales.",
    "Cerrar con aplicación jurídica concreta."
  ],
  "quality_gates": [
    "Bloquear propagación automática si la entrada no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar memoria aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar congruencia entre portada y datos curriculares locales.",
    "Confirmar que toda cita usada tenga entrada bibliográfica local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar que el producto corresponda a la consigna de actividad.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Eliminar placeholders literales en rutas, nombres de archivo y bibliografía.",
    "Confirmar disponibilidad de fuentes institucionales citadas.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en español, letterpaper y oneside según plantilla.",
    "Completar actividad, figura docente y fecha antes de entregar.",
    "Mantener tabla de autor con matrícula, semestre, bloque, tipo y créditos correctos.",
    "Preservar coursecode como LDE-S2B1 salvo indicación institucional distinta.",
    "Reparar truncamiento cerca de la portada antes de compilar.",
    "Verificar cierre completo de authortable y universityname.",
    "Usar codificación y acentos correctos en español.",
    "Mantener nombres sin acentos solo si la plantilla lo exige técnicamente.",
    "No introducir paquetes nuevos sin necesidad editorial o técnica verificable.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo Slug en README y programa analítico.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en garantias-constitucionales.bib.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar normas jurídicas con identificador, emisor y fecha cuando sean usadas.",
    "Incluir nota de consulta o procedencia en fuentes institucionales o locales.",
    "Usar claves BibTeX estables y descriptivas.",
    "Corregir menciones al archivo bibliográfico que usen placeholders generados.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a materias laterales solo reglas editoriales generales validadas.",
    "No propagar datos curriculares específicos fuera de Garantías constitucionales.",
    "No trasladar contenidos temáticos entre materias sin validación expresa.",
    "Mantener alerta de JSON no parseable como control institucional.",
    "Aplicar normalización manual si llega herencia incompleta.",
    "Reutilizar controles de identidad, estructura, calidad, LaTeX y bibliografía.",
    "Conservar especificidad local al recibir reglas transversales.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclos heredados con salida no estructurada requieren normalización manual."
  ],
  "open_questions": [
    "Falta confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Falta definir nombre de figura docente en la plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar placeholder bibliográfico en README.md y programa analítico.",
    "Falta confirmar si la fecha debe ser automática con today o fija por entrega.",
    "Falta validar si se requiere APA, formato jurídico mexicano u otro estilo de citación.",
    "Supuesto: la herencia institucional no estructurada se conserva solo como control de riesgo.",
    "Supuesto: las reglas de Filosofía del Derecho aplican solo como patrones editoriales generales."
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
        "Marcado explícito de supuestos.",
        "Separación entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantías constitucionales.",
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Marco normativo verificable.",
      "Análisis propio con postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia cita-texto-bib.",
      "Conservadurismo ante herencia no equivalente."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Garantías constitucionales con claridad y fundamento.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, fuentes, análisis propio y cierre argumentativo.",
      "Garantizar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener una memoria editorial reutilizable sin importar el formato de entrega."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados explícitamente.",
      "Distinción clara entre norma, doctrina, hechos y opinión.",
      "Cierre con aplicación jurídica concreta.",
      "Metadatos curriculares locales consistentes.",
      "Citas explícitas y bibliografía local sincronizada.",
      "Sin contenido disciplinar importado sin validación local.",
      "Sin placeholders visibles en productos finales."
    ],
    "argumentative_patterns": [
      "Plantear problema jurídico o social.",
      "Delimitar objetivo de la actividad.",
      "Definir conceptos clave.",
      "Identificar marco normativo o doctrinal.",
      "Relacionar fuentes con el problema.",
      "Desarrollar análisis propio sustentado.",
      "Contrastar postura personal con evidencia verificable.",
      "Cerrar con conclusión jurídica aplicable.",
      "Revisar coherencia entre pregunta, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Garantías constitucionales",
        "Ubicación curricular local",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Postura académica",
        "Conclusión transferible",
        "Consistencia cita-texto-bib",
        "Normalización estructurada",
        "Propagación transversal conservadora",
        "Marcado de supuestos",
        "Plantilla LaTeX local",
        "Bibliografía local"
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
          "justification": "Los datos de semestre, bloque, tipo y créditos deben reflejarse en la plantilla."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis necesita un conflicto o pregunta delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere sustento legal o doctrinal verificable."
        },
        {
          "source": "Fuentes verificables",
          "target": "Consistencia cita-texto-bib",
          "kind": "supports",
          "justification": "Cada cita debe corresponder a una entrada bibliográfica local."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Marcado de supuestos",
          "target": "Control de riesgo editorial",
          "kind": "supports",
          "justification": "Los datos no visibles en consigna requieren tratamiento provisional."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Producto académico final",
          "kind": "develops",
          "justification": "La plantilla materializa portada, metadatos y formato de entrega."
        },
        {
          "source": "Bibliografía local",
          "target": "Producto académico final",
          "kind": "supports",
          "justification": "El archivo .bib sostiene la evidencia citada en el documento."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Garantías constitucionales",
          "kind": "contrasts",
          "justification": "La relación es transversal, no equivalente; solo se comparten patrones editoriales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 2, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Bib local: unadmSitioWeb como fuente institucional.",
        "Bib local: unadmMallaDerecho2024 como fuente de malla curricular.",
        "Plantilla local: coursecode LDE-S2B1.",
        "Plantilla local: figura docente por definir.",
        "Plantilla local: truncamiento visible cerca de universityname.",
        "Memoria origen: normalización estructurada antes de propagar.",
        "Memoria origen: no inventar fuentes y validar cita-texto-bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12 consolida destino con unión-dedupe sin recorte útil.",
      "Se preservan reglas locales verificadas de Garantías constitucionales.",
      "Se incorporan solo abstracciones editoriales estables del origen.",
      "Se excluyen citas y conceptos disciplinares de Filosofía del Derecho.",
      "Se refuerza bloqueo por JSON no parseable.",
      "Se refuerza consistencia entre consigna, fuentes, análisis y conclusión.",
      "Se refuerza reparación de truncamientos y placeholders locales.",
      "Se mantiene estrategia progresiva, conservadora y transversal."
    ]
  }
}