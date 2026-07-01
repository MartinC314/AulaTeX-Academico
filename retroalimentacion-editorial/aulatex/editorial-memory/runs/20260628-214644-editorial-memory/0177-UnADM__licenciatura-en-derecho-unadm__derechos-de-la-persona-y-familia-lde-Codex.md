{
  "summary": [
    "Se consolida un cerebro editorial minimo para materia destino con identidad UnADM.",
    "Se preservan reglas estables transversales: normalizacion, estructura juridica y calidad verificable.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico propio de Filosofia del Derecho sin validar pertinencia.",
    "Se refuerza sincronizacion transversal por abstracciones: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva alerta institucional por salidas no JSON parseable y se exige normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear contexto curricular local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por planeacion o consigna.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Vincular argumentos al problema juridico planteado.",
    "Registrar vacios de contexto en preguntas abiertas en lugar de suponer.",
    "No trasladar contenido disciplinar especifico del origen sin prueba de pertinencia local. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar cualquier salida no estructurada antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Mantener compilacion sin errores criticos ni referencias rotas.",
    "Usar espanol academico con acentos y codificacion consistentes.",
    "Conservar claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders de slug sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README antes de referenciar en .tex."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo fuentes realmente consultables y pertinentes a cada actividad.",
    "No inventar referencias bibliograficas.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo reglas estables y reutilizables entre nodos transversales.",
    "Priorizar identidad, gates de calidad, estructura y grafo conceptual general.",
    "Evitar propagar redaccion literal o contenidos tematicos no homologos.",
    "Aplicar compresion lossless por union-deduplicacion sin regresion.",
    "Si destino carece de contexto de actividad, mantener cerebro minimo y abrir vacios."
  ],
  "open_questions": [
    "Confirmar consignas y rubricas reales de actividades de la materia destino.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente. [supuesto]",
    "Confirmar correccion definitiva de nombres corruptos en README.",
    "Confirmar sustitucion definitiva del placeholder de slug .bib en README y programa analitico.",
    "Confirmar si coursecode LDE-S3B1 debe figurar en todos los productos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada de 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Orientar productos academicos con fundamento juridico, evidencia y transferencia profesional.",
      "Convertir planeacion semanal en entregables claros, trazables y evaluables."
    ],
    "style_markers": [
      "Inicio con problema concreto.",
      "Desarrollo por secciones funcionales.",
      "Citas verificables y postura propia.",
      "Cierre con criterio juridico."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna explicita -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
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
          "justification": "La identidad institucional exige evidencia y formato verificable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de un problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento normativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad consigna-producto",
          "target": "Calidad evaluable",
          "kind": "develops",
          "justification": "Permite verificar cumplimiento real de actividad."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo .bib local con fuentes institucionales base."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se transfirieron solo abstracciones estables entre nodos transversales.",
      "Se evitaron fuentes inventadas y contenidos tematicos no verificables del origen.",
      "Se reforzaron gates de calidad y normalizacion como condicion de propagacion.",
      "Se establecio ADN editorial minimo reconstructible para siguientes ciclos."
    ]
  }
}