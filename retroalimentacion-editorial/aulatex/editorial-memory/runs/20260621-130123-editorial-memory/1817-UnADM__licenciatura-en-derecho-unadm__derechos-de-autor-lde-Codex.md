{
  "summary": [
    "Se consolida memoria transversal para Derechos de autor con identidad UnADM.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofia del Derecho.",
    "Se mantiene estado provisional para herencias no verificadas (Codex, GPT-Pro).",
    "Se detectan tokens de plantilla y nombres corruptos en README/programa; requieren correccion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: clave local LDE-S5B1 se mantiene vigente."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia local.",
    "Corregir tokens sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al archivo derechos-de-autor.bib.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar consistencia entre portada y datos curriculares locales.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de \\input{template}.",
    "No dejar comandos incompletos como \\usepackage sin argumento.",
    "Mantener paquetes en preambulo efectivo segun plantilla.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y marco juridico aplicable.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar derechos-de-autor.bib como archivo local canonico de la materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales de identidad, estructura y calidad.",
    "No propagar redaccion literal entre nodos no equivalentes.",
    "Mantener bandera de revision manual para herencia de ciclos iniciales.",
    "Evitar regresiones: conservar reglas utiles previas y sumar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar nombre oficial de figura docente para reemplazar marcador pendiente.",
    "Confirmar si LDE-S5B1 es clave oficial estable en toda la suite.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer como ubicacion fija.",
    "Confirmar correccion definitiva de tokens $(@{...}.Slug) a derechos-de-autor.bib.",
    "Confirmar limpieza final de nombres corruptos eporte/eferencias en README."
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
        "Normalizacion estructurada antes de propagar.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y trazables.",
      "Asegurar coherencia entre identidad institucional, argumentacion y evidencia."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y trazables.",
      "Mantener consistencia entre portada, contenido y referencias."
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
        "Propagacion segura",
        "Producto alineado a consigna"
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
          "justification": "Evita heredar salidas no parseables y reduce errores aguas abajo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion debe corresponder a una fuente trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura razonada habilita aplicabilidad profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Producto alineado a consigna",
          "kind": "depends_on",
          "justification": "La forma y metadatos dependen del marco institucional y curricular."
        }
      ],
      "evidence": [
        "README de Derechos de autor confirma ubicacion curricular y entrada canonica.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib aporta base institucional verificable.",
        "Regla historica: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicacion completa de reglas repetidas.",
      "Ciclo 15: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 15: se preservan gates criticos de parseo JSON y trazabilidad de fuentes.",
      "Ciclo 15: se refuerza correccion local de tokens y nombres de archivo corruptos."
    ]
  }
}