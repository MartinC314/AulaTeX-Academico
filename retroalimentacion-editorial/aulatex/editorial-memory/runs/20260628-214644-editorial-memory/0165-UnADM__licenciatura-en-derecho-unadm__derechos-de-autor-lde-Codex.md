{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor.",
    "Se preservan reglas validas previas sin regresion y con deduplicacion lossless.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantiene herencia Codex y GPT-Pro como provisional [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar README de la materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Mantener integridad academica con citas verificables.",
    "Conservar enfoque juridico con criterio propio en la conclusion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion y bibliografia local.",
    "Normalizar nombres de archivo con slug canonico derechos-de-autor."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin validacion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "Verificar correspondencia exacta entre consigna y tipo de entregable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa para tokens sin expandir y nombres corruptos.",
    "Corregir campos pendientes de plantilla antes de publicar.",
    "Mantener normalizacion manual para herencia de ciclos previos."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo consigna contraria.",
    "Declarar metadatos antes de \\input{template}.",
    "No dejar comandos truncados ni \\usepackage sin argumento.",
    "Mover paquetes al preambulo efectivo si la plantilla lo exige.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar acentos y codificacion consistentes en .tex y .bib.",
    "No propagar datos personales del alumno a otros nodos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales verificables.",
    "Priorizar fuentes institucionales UnADM y normativas aplicables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales estables, no redaccion literal.",
    "Preservar especificidad local de Derechos de autor al recibir reglas transversales.",
    "Evitar regresiones de gates de calidad ya consolidados.",
    "Mantener bandera provisional para herencia Codex y GPT-Pro hasta cierre de validacion."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial definitiva [supuesto].",
    "Confirmar nombre de figura docente para eliminar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe mantenerse fija [supuesto].",
    "Confirmar reemplazo total de tokens $(@{...}.Slug) en README y programa.",
    "Confirmar si la materia requiere artefactos adicionales a reporte y presentacion."
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
        "README como entrada canonica.",
        "Integridad academica con citas verificables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Analisis propio con postura.",
      "Conclusion transferible a practica juridica.",
      "Normalizacion estructurada antes de propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener continuidad editorial transversal sin perder contexto local.",
      "Asegurar calidad tecnica LaTeX y calidad argumentativa juridica."
    ],
    "style_markers": [
      "Frases directas y trazables.",
      "Supuestos explicitamente marcados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Consigna -> desarrollo alineado -> verificacion de producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Calidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de un problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamentos juridicos."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga memoria sin estructura parseable."
        }
      ],
      "evidence": [
        "README de Derechos de autor.",
        "programa-analitico-derechos-de-autor.md.",
        "derechos-de-autor.bib.",
        "Regla consolidada de bloqueo por no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas.",
      "Ciclo 2: incorporacion transversal de ejes estables problema-conceptos-evidencia-analisis-cierre.",
      "Ciclo 2: refuerzo de gates de calidad y normalizacion previa a propagacion.",
      "Ciclo 2: preservacion de advertencias de herencia provisional [supuesto]."
    ]
  }
}