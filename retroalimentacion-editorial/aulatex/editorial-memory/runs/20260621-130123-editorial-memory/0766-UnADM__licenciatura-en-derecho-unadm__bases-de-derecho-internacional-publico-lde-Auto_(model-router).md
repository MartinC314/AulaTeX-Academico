{
  "summary": [
    "Materia destino consolidada con identidad UnADM y contexto curricular local.",
    "Asignatura destino: Bases de derecho internacional publico.",
    "Ubicacion local verificada: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Plantilla base, programa analitico y bibliografia local definidos.",
    "Se preservan reglas transversales estables del origen sin trasladar contenido tematico de Filosofia del Derecho.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva incidencia historica de salidas no parseables desde Codex y GPT-Pro.",
    "Se mantiene compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar al alumno registrado en plantilla si no hay instruccion local que lo sustituya.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Citar la malla curricular de Derecho solo como fuente de ubicacion curricular."
  ],
  "structure_rules": [
    "Mantener el programa analitico como guia editorial de actividades.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar cada entrega con problema, conceptos, marco normativo o doctrinal, fuentes, analisis propio y cierre.",
    "Transformar la planeacion semanal en el producto academico solicitado.",
    "Distinguir reporte, presentacion y productos visuales segun consigna.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir hechos, argumentos, normas y criterio propio."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Verificar que el producto corresponda a la consigna vigente.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Integrar normas, doctrina o datos pertinentes cuando correspondan.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No sustituir faltantes por invenciones.",
    "Ajustar profundidad argumentativa a la rubrica local cuando exista."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar correspondencia entre instrucciones de actividad y programa analitico.",
    "Bloquear afirmaciones sin respaldo documental, normativo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Verificar que README, programa analitico, .bib y plantillas locales coincidan.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Mantener auditoria de parseo JSON antes de nueva propagacion."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para productos de presentacion.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir titulo, subtitulo y subject coherentes con la actividad en curso.",
    "No cambiar la estructura base de portada sin instruccion editorial.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar entradas BibTeX especificas solo cuando la fuente exista y sea verificable.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Validar que las claves citadas existan en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que bibliografia de otra materia corresponde a esta asignatura."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "Mantener compresion union-dedupe con criterio lossless.",
    "No propagar supuestos como reglas definitivas.",
    "No trasladar contenido tematico especifico de Filosofia del Derecho al destino.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar correcciones locales solo despues de verificar archivos afectados.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "Conservar incidencias historicas de salida no estructurada detectadas en ciclos previos.",
    "Aplicar normalizacion estructurada obligatoria antes de propagacion lateral o descendente."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad local antes de redactar.",
    "Confirmar producto exacto solicitado: reporte, presentacion, mapa u otro formato.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si se normaliza el nombre editorial con acento: publico frente a publico.",
    "Revisar nombres en README con caracteres anomalos.",
    "Corregir tokens sin expandir en README y programa analitico.",
    "Reparar el corte del entorno tabular en el archivo de reporte .tex.",
    "Confirmar nombre canonico final del archivo .bib local.",
    "Confirmar alcance de la carpeta referencias-bases-de-derecho-internacional-publico."
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
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Codigo local: LDE-S4B1.",
        "Usar solo contexto curricular verificado del destino.",
        "No mezclar contexto curricular de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Consigna de actividad como eje rector.",
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Consistencia cita-bibliografia.",
      "Normalizacion JSON previa a propagacion.",
      "Conservacion del contexto local frente a transferencias transversales."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Asegurar que cada entrega responda a la consigna local.",
      "Sostener integridad academica mediante fuentes verificables.",
      "Convertir el cierre en criterio juridico aplicable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Encuadre breve del problema juridico o social.",
      "Secciones funcionales y no redundantes.",
      "Terminologia juridica precisa.",
      "Supuestos siempre etiquetados.",
      "Citas verificables antes de afirmaciones fuertes.",
      "Postura propia diferenciada del resumen.",
      "Cierre con criterio juridico aplicable.",
      "Metadatos locales consistentes.",
      "Sin traslado literal de redaccion entre materias."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> analisis -> conclusion.",
      "Consigna -> objetivo -> desarrollo alineado -> verificacion final.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Hechos -> normas aplicables -> razonamiento juridico -> consecuencia.",
      "Fuente institucional -> ubicacion curricular -> alcance editorial.",
      "Pendiente detectado -> marca de supuesto -> pregunta abierta.",
      "Evidencia verificable -> cita explicita -> bibliografia local.",
      "Conclusion juridica -> transferencia a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Bases de derecho internacional publico",
        "Licenciatura en Derecho",
        "Semestre 4 bloque 1",
        "Codigo LDE-S4B1",
        "Consigna de actividad",
        "Planeacion semanal",
        "Producto academico solicitado",
        "Problema juridico o social",
        "Conceptos juridicos",
        "Marco normativo",
        "Doctrina juridica",
        "Evidencia verificable",
        "Analisis propio",
        "Postura academica",
        "Conclusion juridica transferible",
        "Integridad academica",
        "Consistencia cita-bibliografia",
        "Bibliografia local",
        "Normalizacion JSON",
        "Propagacion recursiva",
        "Procedencia provisional",
        "No mezcla curricular entre materias",
        "README local",
        "Programa analitico local",
        "Plantilla LaTeX local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "README local",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "El README define la materia como parte de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "README local",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "El README lista semestre, bloque, tipo y creditos."
        },
        {
          "source": "unadmMallaDerecho2024",
          "target": "Semestre 4 bloque 1",
          "kind": "supports",
          "justification": "La malla curricular local se conserva como fuente institucional de ubicacion."
        },
        {
          "source": "Programa analitico local",
          "target": "Planeacion semanal",
          "kind": "develops",
          "justification": "El programa analitico orienta la transformacion de la planeacion en productos academicos."
        },
        {
          "source": "Consigna de actividad",
          "target": "Producto academico solicitado",
          "kind": "depends_on",
          "justification": "El formato de entrega depende de lo pedido en la consigna."
        },
        {
          "source": "Producto academico solicitado",
          "target": "Plantilla LaTeX local",
          "kind": "depends_on",
          "justification": "La seleccion entre reporte y presentacion depende del producto requerido."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis debe responder al problema planteado."
        },
        {
          "source": "Conceptos juridicos",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Los conceptos delimitan el razonamiento juridico."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento juridico verificable."
        },
        {
          "source": "Doctrina juridica",
          "target": "Postura academica",
          "kind": "supports",
          "justification": "La doctrina ayuda a justificar la posicion del estudiante."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las afirmaciones documentadas reducen riesgo de invencion."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las claves citadas deben existir en el .bib local."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Procedencia provisional",
          "target": "Identidad institucional UnADM",
          "kind": "contrasts",
          "justification": "Codex y GPT-Pro son trazabilidad, no identidad del entregable."
        },
        {
          "source": "No mezcla curricular entre materias",
          "target": "Bases de derecho internacional publico",
          "kind": "supports",
          "justification": "La materia destino conserva su contexto local frente a transferencias transversales."
        }
      ],
      "evidence": [
        "README.md destino: materia, ubicacion curricular, estructura y pauta editorial.",
        "programa-analitico-bases-de-derecho-internacional-publico.md: encuadre, proposito y ejes de trabajo.",
        "bases-de-derecho-internacional-publico.bib: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte-bases-de-derecho-internacional-publico.tex: plantilla article, metadatos locales y codigo LDE-S4B1.",
        "presentacion-bases-de-derecho-internacional-publico.tex: plantilla local para productos de presentacion.",
        "Memoria heredada institucional: incidencia de salida sin JSON parseable desde Codex.",
        "Memoria actual destino: incidencia de salida sin JSON parseable desde GPT-Pro.",
        "Memoria origen: ejes transversales problema, conceptos, evidencia, analisis propio y conclusion juridica.",
        "Regla de transferencia aplicada: no trasladar contenido tematico especifico entre materias no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se deduplican reglas repetidas sin eliminar contenido util.",
      "Ciclo 16: se preserva identidad curricular local del destino.",
      "Ciclo 16: se incorporan solo abstracciones transversales del origen.",
      "Ciclo 16: se excluye contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 16: se refuerza normalizacion JSON previa a propagacion.",
      "Ciclo 16: se refuerza consistencia cita-bibliografia como gate obligatorio.",
      "Ciclo 16: se mantienen incidencias historicas de salidas no estructuradas.",
      "Ciclo 16: se registran pendientes locales de README, tokens y entorno tabular.",
      "Ciclo 16: se conserva estrategia progresiva y conservadora.",
      "Ciclo 16: se fortalece el grafo conceptual editorial de la materia destino."
    ]
  }
}