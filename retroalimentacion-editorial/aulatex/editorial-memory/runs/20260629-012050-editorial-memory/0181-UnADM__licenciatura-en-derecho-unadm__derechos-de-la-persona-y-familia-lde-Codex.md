{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia conservadora y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura juridica y control de calidad.",
    "Se transfiere solo abstraccion reusable; no se transfiere contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria ante salidas no estructuradas o no JSON parseable.",
    "Se mantiene cerebro editorial minimo de materia con vacios locales en preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear contexto curricular local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno, matricula o figura docente sin verificacion local. [supuesto]"
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear formato final al producto solicitado por planeacion o rubrica.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "No asumir fuentes de otras semanas o materias como obligatorias para la actividad actual.",
    "Registrar faltantes de contexto local en preguntas abiertas.",
    "Adaptar reglas heredadas solo cuando sean compatibles con la materia destino. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar cualquier salida no estructurada antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia real entre consigna y producto entregable."
  ],
  "latex_rules": [
    "Mantener espanol academico con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Usar plantilla local de reporte o presentacion como base.",
    "Conservar documentclass article, letterpaper y oneside salvo consigna distinta.",
    "Verificar coherencia de titulo, subtitulo, asignatura y codigo local en portada.",
    "Corregir placeholders o tokens sin expandir en README y programa analitico antes de reutilizar.",
    "Mantener nombres de archivo consistentes con slug canonico de la materia."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo fuentes pertinentes a la actividad y realmente consultables.",
    "No inventar referencias bibliograficas.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo reglas abstractas y estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico de otra asignatura.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica vigentes de la actividad destino.",
    "Confirmar si el codigo LDE-S3B1 es obligatorio en todos los entregables.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente de plantilla. [supuesto]",
    "Confirmar sustitucion definitiva de tokens de slug .bib en README y programa analitico.",
    "Confirmar si existe formato institucional obligatorio adicional para presentaciones."
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
        "Normalizacion estructurada previa a propagacion.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos evaluables con trazabilidad y rigor juridico.",
      "Asegurar coherencia entre consigna, argumentacion y cierre profesional.",
      "Preservar identidad UnADM en cualquier formato academico."
    ],
    "style_markers": [
      "Inicio con problema concreto.",
      "Desarrollo por bloques funcionales.",
      "Afirmaciones con respaldo explicito.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna explicita -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad consigna-producto",
        "Bibliografia verificable"
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
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa del problema."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento juridico valido."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad consigna-producto",
          "kind": "develops",
          "justification": "La estructura permite verificar cumplimiento y calidad."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo .bib local con fuentes institucionales base.",
        "Regla estable heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completada sin eliminar reglas utiles previas.",
      "Ciclo 2: se reforzaron quality gates transversales de parseo JSON y normalizacion.",
      "Ciclo 2: se preservo estructura argumentativa reusable sin copiar contenido tematico de origen.",
      "Ciclo 2: se mantuvieron vacios locales como preguntas abiertas para verificacion posterior."
    ]
  }
}