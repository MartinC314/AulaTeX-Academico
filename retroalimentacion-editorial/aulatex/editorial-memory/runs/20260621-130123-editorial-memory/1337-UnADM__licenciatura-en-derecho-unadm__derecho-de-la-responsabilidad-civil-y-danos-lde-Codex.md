{
  "summary": [
    "Se consolida sincronizacion transversal sin traslado tematico literal desde Filosofia del Derecho.",
    "Se preservan reglas utiles previas del destino y del marco institucional UnADM sin regresion.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conservan alertas tecnicas locales verificadas: JSON no parseable historico, placeholders y truncamientos en README/.tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o guia oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo LDE-S6B1 sin fuente documental explicita [supuesto].",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Alinear el producto con la planeacion semanal y la consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib."
  ],
  "activity_rules": [
    "Formular problema juridico pertinente a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir analisis propio de afirmaciones factuales o normativas.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "No arrastrar contenido tematico del origen si no aplica al nodo destino.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion juridica tenga respaldo o marca de supuesto.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombre canonico del .bib local antes de citarlo.",
    "Completar plantilla .tex truncada en authortable antes de compilar [supuesto tecnico confirmado por contexto]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Si falta fuente, registrar vacio en preguntas abiertas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico puntual del origen.",
    "Mantener compresion lossless por union-dedupe sin recorte semantico.",
    "Conservar alerta de normalizacion manual por antecedentes de salida no estructurada en ciclos previos."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de esta materia.",
    "Confirmar si LDE-S6B1 es codigo oficial o interno [supuesto vigente].",
    "Confirmar convencion final danos/daños en todo el arbol de archivos.",
    "Corregir en README rutas truncadas de reporte y referencias.",
    "Resolver placeholders Slug en README y programa analitico.",
    "Completar y validar la seccion authortable truncada en la plantilla .tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la responsabilidad civil y danos."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio diferenciado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables y utiles para la practica juridica.",
      "Preservar consistencia editorial institucional en todos los artefactos de la materia."
    ],
    "style_markers": [
      "Supuestos marcados de forma explicita.",
      "Secciones funcionales y reutilizables.",
      "Cierre con utilidad profesional.",
      "Control estricto de trazabilidad documental."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Conceptos y normas con fuentes.",
      "Analisis propio con criterio.",
      "Conclusion juridica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad academica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor de citas y formato."
        },
        {
          "source": "Normalizacion estructurada JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de memoria ambigua o no verificable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "El campo material de la asignatura articula ambos conceptos."
        },
        {
          "source": "Ejes editoriales estables",
          "target": "Productos semanales",
          "kind": "develops",
          "justification": "La estructura reusable orienta reportes y presentaciones."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con entradas institucionales.",
        "Incidencias locales verificadas de placeholder y truncamiento [supuesto tecnico en .tex]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas y preservacion sin recorte.",
      "Ciclo 5: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 5: refuerzo de gates JSON, trazabilidad bibliografica y control de supuestos.",
      "Ciclo 5: se mantiene alerta tecnica local sin convertir supuestos en hechos."
    ]
  }
}