{
  "summary": [
    "Se consolida memoria transversal para Derechos de autor con identidad UnADM.",
    "Se preserva compresion lossless por union y deduplicacion sin regresion.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se mantiene herencia Codex y GPT-Pro como provisional hasta validacion local.",
    "Se detectan y priorizan correcciones locales verificables en README y preambulo LaTeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir datos personales del alumno a nodos distintos."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion y bibliografia de materia.",
    "Corregir tokens de plantilla no resueltos en README y programa analitico.",
    "Corregir nombres de archivo corruptos en estructura publicada."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar al .bib local solo fuentes realmente usadas por actividad.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico por tokens sin expandir y caracteres anomalos.",
    "Corregir campos pendientes de plantilla como 'Nombre por definir' antes de version final."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de cargar plantilla segun convencion local.",
    "No dejar comandos incompletos como \\usepackage sin argumento.",
    "Mover o ajustar paquetes segun orden requerido por plantilla para evitar errores.",
    "Compilar sin errores criticos, sin referencias rotas y sin paquetes truncados.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta cuando la fuente sea web.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Conservar derechos-de-autor.bib como archivo canonico local [supuesto verificado por contexto local]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas por JSON y estructura.",
    "En saltos transversales, transferir identidad, gates de calidad y patrones argumentativos reutilizables.",
    "No propagar redaccion literal ni contenido tematico exclusivo de Filosofia del Derecho.",
    "Mantener advertencia de herencia provisional Codex/GPT-Pro hasta validacion documental local.",
    "Aplicar estrategia conservadora: agregar solo mejoras verificables y sin borrar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial estable para toda la suite.",
    "Confirmar nombre de figura docente para reemplazar marcador pendiente.",
    "Confirmar si la ubicacion institucional en portada debe permanecer fija.",
    "Confirmar orden correcto de carga de paquetes respecto a \\input{template} en esta plantilla.",
    "Confirmar retiro o permanencia de advertencias Codex/GPT-Pro tras validacion local completa."
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
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor."
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
      "Convertir planeacion semanal en productos academicos claros, trazables y utiles para practica juridica.",
      "Sostener un cerebro editorial estable, reusable y seguro entre nodos."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Estructura funcional por secciones trazables.",
      "Coherencia entre portada, desarrollo y referencias."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "Reduce herencia de salidas no parseables y evita regresiones."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion debe enlazar con fuente trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada permite aplicacion profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La consistencia institucional exige respaldo academico comprobable."
        }
      ],
      "evidence": [
        "README local confirma ubicacion curricular y entrada canonica.",
        "Programa analitico local fija eje problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectaron tokens sin expandir y nombres de archivo corruptos en README/programa.",
        "Se detecto comando \\usepackage incompleto en reporte-derechos-de-autor.tex."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicacion total de reglas repetidas en memoria origen y destino.",
      "Ciclo 17: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 17: refuerzo de gates JSON, supuestos y trazabilidad bibliografica.",
      "Ciclo 17: incorporacion de mejoras verificables locales sin eliminar reglas utiles previas."
    ]
  }
}