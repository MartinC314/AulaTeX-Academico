{
  "summary": [
    "Materia destino consolidada con identidad UnADM y contexto local verificado.",
    "Asignatura: Bases de derecho internacional publico.",
    "Contexto curricular local: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se preserva plantilla base, programa analitico y bibliografia local.",
    "Se transfieren solo abstracciones editoriales estables desde el origen transversal.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva la incidencia historica de salidas no parseables.",
    "Se mantiene compresion union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y tono.",
    "Usar nombre local: Bases de derecho internacional publico.",
    "Usar codigo local: LDE-S4B1.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar al alumno registrado en plantilla salvo instruccion local distinta.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "No mezclar metadatos curriculares del origen con el destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Integrar fuentes verificables dentro del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Mantener programa analitico como guia editorial de actividades.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Usar referencias-bases-de-derecho-internacional-publico como repositorio de apoyo."
  ],
  "activity_rules": [
    "Adaptar cada actividad a la consigna local.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas, doctrina y criterio propio.",
    "Incluir postura academica propia, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Integrar normas, doctrina o datos pertinentes cuando correspondan.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No sustituir vacios documentales por invenciones.",
    "Validar que el producto final corresponda al formato solicitado."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagacion si la salida no es estructurada.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar consistencia entre consigna, programa analitico y producto.",
    "Bloquear afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar claves citadas contra bibliografia local.",
    "Validar sintaxis LaTeX antes de cerrar entregables.",
    "Revisar cierre de entornos LaTeX, especialmente tabular.",
    "Verificar README, programa analitico, .bib y plantillas locales.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Conservar auditoria de incidencias no parseables."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex para presentaciones.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "Completar titulo, subtitulo y subject segun la actividad.",
    "No alterar portada institucional sin instruccion editorial.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo para fuentes existentes y consultables.",
    "No inventar referencias.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda cita en texto exista en el .bib local.",
    "No importar bibliografia tematica del origen sin necesidad local verificada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales entre materias no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "No trasladar contenido tematico especifico de Filosofia del Derecho.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Normalizar manualmente memorias heredadas no estructuradas.",
    "Conservar incidencias historicas de salida no parseable.",
    "Propagar correcciones locales solo despues de verificar archivos afectados.",
    "Revalidar contexto curricular en cada nodo destino."
  ],
  "open_questions": [
    "Confirmar consignas locales de actividades especificas.",
    "Confirmar rubricas de evaluacion por actividad.",
    "Confirmar fuentes obligatorias por semana.",
    "Confirmar si se normaliza publico a publico con acento en titulos visibles.",
    "Corregir nombres anomalos en README: reporte y referencias.",
    "Resolver token Slug sin expandir en README y programa analitico.",
    "Reparar cierre incompleto de entorno tabular en reporte .tex.",
    "Confirmar si existen materiales locales adicionales en referencias.",
    "Confirmar criterio de nomenclatura para archivos derivados por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Fuentes provisionales tratadas como trazabilidad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Bases de derecho internacional publico.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Codigo local: LDE-S4B1.",
        "Usar solo contexto curricular verificado del destino.",
        "No mezclar contexto curricular entre materias."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna local como eje rector.",
      "Problema juridico o social inicial.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible.",
      "Consistencia cita-bibliografia.",
      "Normalizacion JSON previa a propagacion.",
      "Estrategia conservadora entre nodos transversales."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos verificables.",
      "Orientar reportes, presentaciones y productos visuales con fundamento juridico.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Evitar entregas descriptivas sin postura juridica.",
      "Asegurar transferencia profesional de la conclusion.",
      "Proteger identidad curricular local ante propagaciones transversales."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Lenguaje juridico claro.",
      "Supuestos siempre etiquetados.",
      "Citas explicitas para afirmaciones sustantivas.",
      "Cierre con criterio juridico aplicable.",
      "Metadatos locales consistentes.",
      "Sin redaccion literal transferida entre materias."
    ],
    "argumentative_patterns": [
      "Consigna -> objetivo -> desarrollo alineado -> verificacion final.",
      "Problema -> conceptos -> norma o doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Hechos -> regla aplicable -> razonamiento -> consecuencia juridica.",
      "Fuente institucional -> ubicacion curricular -> identidad del entregable.",
      "Faltante documental -> marca de pendiente -> no invencion.",
      "Producto solicitado -> formato adecuado -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Bases de derecho internacional publico",
        "Licenciatura en Derecho",
        "Semestre 4 bloque 1",
        "Consigna de actividad",
        "Planeacion semanal",
        "Problema juridico o social",
        "Conceptos juridicos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Postura academica",
        "Conclusion juridica transferible",
        "Bibliografia local",
        "Consistencia cita-bibliografia",
        "Normalizacion JSON",
        "Propagacion recursiva conservadora",
        "Tokens sin expandir",
        "Entornos LaTeX cerrados"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Planeacion semanal",
          "kind": "depends_on",
          "justification": "El formato y alcance dependen del producto solicitado."
        },
        {
          "source": "Planeacion semanal",
          "target": "Producto academico",
          "kind": "develops",
          "justification": "La planeacion se transforma en reporte, presentacion o producto visual."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema activa la interpretacion y la postura del estudiante."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El razonamiento juridico requiere normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida necesita respaldo documental."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La correspondencia entre citas y .bib evita referencias rotas."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Contexto curricular local",
          "target": "Metadatos del entregable",
          "kind": "supports",
          "justification": "README y programa analitico fijan materia, semestre, bloque y creditos."
        },
        {
          "source": "Contenido tematico del origen",
          "target": "Contenido tematico del destino",
          "kind": "contrasts",
          "justification": "La relacion transversal permite estructura, no traslado tematico literal."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Compilacion confiable",
          "kind": "contrasts",
          "justification": "Los tokens residuales generan rutas y referencias inestables."
        },
        {
          "source": "Entornos LaTeX cerrados",
          "target": "Compilacion confiable",
          "kind": "supports",
          "justification": "El cierre correcto de tabular previene errores criticos."
        }
      ],
      "evidence": [
        "README destino: materia de Licenciatura en Derecho de la UnADM.",
        "README destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "README destino: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README destino: carpeta como punto de entrada canonico.",
        "README destino: identidad UnADM, integridad academica y citas verificables.",
        "Programa analitico destino: productos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico destino: proposito de transformar planeacion en reportes, presentaciones y productos visuales.",
        "Programa analitico destino: ejes de problema, conceptos, producto, analisis propio y conclusion.",
        "Bibliografia local: entradas unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla reporte: clase article con spanish, letterpaper y oneside.",
        "Plantilla reporte: coursename Bases de derecho internacional publico.",
        "Plantilla reporte: coursecode LDE-S4B1.",
        "Contexto local: README contiene token Slug sin expandir.",
        "Contexto local: README contiene nombres anomalos de reporte y referencias.",
        "Contexto local: reporte .tex muestra cierre incompleto de tabular."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se consolida memoria destino con estrategia progresiva y conservadora.",
      "Ciclo 14: se deduplican reglas equivalentes sin eliminar reglas utiles.",
      "Ciclo 14: se preserva identidad UnADM y contexto curricular local.",
      "Ciclo 14: se transfiere estructura argumentativa estable desde nodo transversal.",
      "Ciclo 14: se evita traslado tematico de Filosofia del Derecho.",
      "Ciclo 14: se refuerza bloqueo de propagacion sin JSON parseable.",
      "Ciclo 14: se agregan alertas verificables sobre README, tokens y tabular.",
      "Ciclo 14: se mantienen citas locales verificadas unadmSitioWeb y unadmMallaDerecho2024."
    ]
  }
}