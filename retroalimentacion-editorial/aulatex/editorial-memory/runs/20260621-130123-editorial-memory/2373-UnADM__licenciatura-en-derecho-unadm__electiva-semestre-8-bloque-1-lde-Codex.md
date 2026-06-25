{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa reusable y control de calidad estricto.",
    "Se transfieren solo abstracciones estables desde actividad no equivalente.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se refuerza correccion de placeholders y literales corruptos detectados en README y programa analitico.",
    "Supuesto: faltan datos oficiales de creditos y figura docente en destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional LDE-S8B1 sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en secuencia: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenido tematico de otras materias sin evidencia local.",
    "No asumir fuentes de semanas posteriores sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders de automatizacion y caracteres corruptos en nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte y presentacion de la materia.",
    "Mantener clase article con spanish, letterpaper, oneside salvo instruccion oficial distinta.",
    "Conservar consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Usar codificacion compatible con espanol y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "No dejar tokens sin expandir tipo $(@{...}.Slug) en README, programa o entregables."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM para contexto curricular.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales y superiores solo reglas abstractas estables.",
    "No propagar metadatos locales de esta electiva a materias no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Reutilizar gates institucionales de JSON, trazabilidad y no invencion de fuentes.",
    "Si falta consigna local, propagar solo estructura, identidad y calidad; dejar vacios como supuestos."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de figura docente.",
    "Confirmar si LDE-S8B1 es codigo oficial o provisional.",
    "Confirmar si existe nombre oficial distinto para la asignatura.",
    "Confirmar que todos los nombres de archivo en README quedaron normalizados."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Claro y verificable",
        "Sobrio ante datos no confirmados"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos, normas, doctrina o datos pertinentes",
      "Producto solicitado por planeacion",
      "Analisis propio con postura academica",
      "Conclusion juridica transferible",
      "Normalizacion estructurada previa a propagacion"
    ],
    "reason_for_being": [
      "Estandarizar entregables academicos con trazabilidad y criterio juridico.",
      "Asegurar calidad reutilizable entre nodos sin contaminar contexto tematico.",
      "Preservar memoria editorial util sin regresiones."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Supuestos marcados",
      "Cierre con implicacion practica"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia verificable -> inferencia juridica",
      "Descripcion breve -> posicion critica -> transferencia profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y criterio de cierre."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Evita errores por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Conduce de problema a implicacion practica."
        }
      ],
      "evidence": [
        "README local muestra placeholders Slug sin expandir y literales corruptos.",
        "Programa analitico local define ejes estables reutilizables.",
        "Archivo .bib local contiene fuentes institucionales base verificables.",
        "Plantilla .tex local conserva metadatos curriculares y campos pendientes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: dedupe semantico aplicado sin eliminar reglas utiles previas.",
      "Ciclo 22: reforzado gate de JSON parseable y estructura minima.",
      "Ciclo 22: reforzada separacion entre abstracciones transferibles y contenido tematico local.",
      "Ciclo 22: mantenido estado provisional de datos no confirmados (creditos, figura docente, codigo oficial)."
    ]
  }
}