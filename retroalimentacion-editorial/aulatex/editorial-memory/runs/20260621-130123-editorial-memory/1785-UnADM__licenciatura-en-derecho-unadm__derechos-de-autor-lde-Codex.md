{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor con ADN UnADM.",
    "Se preserva compresion lossless por union y deduplicacion sin recorte.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion recursiva.",
    "Se mantienen como provisionales las herencias no verificadas de Codex y GPT-Pro.",
    "Se transfiere solo abstraccion estable desde Filosofia del Derecho: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado en la planeacion semanal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al BibTeX local de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar y corregir tokens de plantilla no resueltos y nombres de archivo corruptos."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de \\input{template} segun plantilla local.",
    "No dejar comandos incompletos como \\usepackage sin argumento.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales consultables e institucionales o verificables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar y mantener correspondencia biunivoca entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "No transferir redaccion literal ni contenido tematico propio de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual para memorias heredadas de ciclos tempranos.",
    "Propagar advertencia de herencia provisional Codex/GPT-Pro solo como metadato de riesgo.",
    "Evitar regresion: conservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial definitiva de la materia. [supuesto]",
    "Definir valor final de Figura docente en portada.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer fijo en plantillas. [supuesto]",
    "Validar orden correcto de paquetes respecto a \\input{template} en esta plantilla.",
    "Confirmar limpieza completa de tokens $(@{...}.Slug) en README y programa analitico."
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
        "Entrada canonica por carpeta de asignatura.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Sostener consistencia editorial entre actividades, reporte, presentacion y bibliografia."
    ],
    "style_markers": [
      "Supuestos declarados explicitamente.",
      "Secciones funcionales y trazables.",
      "Coherencia entre portada, cuerpo y referencias.",
      "Cierre con implicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Conclusion aplicable al contexto juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Consigna semanal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Consigna semanal",
          "target": "Estructura de entrega",
          "kind": "depends_on",
          "justification": "El formato final debe corresponder al producto solicitado."
        }
      ],
      "evidence": [
        "README de Derechos de autor define ubicacion curricular y pauta institucional.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Reporte actual muestra hallazgos tecnicos: comando \\usepackage incompleto y marcador de Figura docente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se deduplican reglas repetidas y se conserva contenido util sin perdida semantica.",
      "Ciclo 7: se refuerzan gates de JSON parseable y validacion de supuestos.",
      "Ciclo 7: se agrega control transversal de tokens de plantilla no resueltos.",
      "Ciclo 7: se mantiene separacion entre abstraccion editorial estable y contenido tematico local."
    ]
  }
}