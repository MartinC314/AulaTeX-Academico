{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor con identidad UnADM.",
    "Se preserva compresion lossless por union y deduplicacion sin recorte.",
    "Se mantiene regla critica: no propagar salidas no estructuradas ni no-JSON.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho por relacion transversal.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se confirma necesidad de normalizar tokens de plantilla y nombres corruptos en README/programa.",
    "Se mantiene tratamiento provisional para herencias no verificadas (Codex/GPT-Pro)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sostener enfoque juridico con criterio propio en el cierre."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia local.",
    "Normalizar nombres de archivo con slug de la asignatura.",
    "Corregir tokens sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias como obligatorias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README/programa para corregir marcadores de plantilla y caracteres anómalos.",
    "Detectar y corregir campos pendientes en portada como 'Nombre por definir'."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos antes de cargar plantilla.",
    "Evitar comandos incompletos o paquetes truncados.",
    "No dejar \\usepackage sin argumento.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar citas de actividad en derechos-de-autor.bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas de identidad, estructura y calidad.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual para herencia historica no estructurada.",
    "Evitar regresiones: conservar toda regla util ya vigente en destino.",
    "Cuando falte consigna local, propagar solo abstracciones editoriales estables."
  ],
  "open_questions": [
    "Confirmar nombre oficial de figura docente para portada.",
    "Confirmar si LDE-S5B1 es clave curricular oficial en toda la suite. [supuesto]",
    "Confirmar si 'Roma Norte, Ciudad de Mexico' debe permanecer fijo en metadatos. [supuesto]",
    "Confirmar si la plantilla exige paquetes antes o despues de \\input{template}.",
    "Confirmar limpieza definitiva de tokens $(@{...}.Slug) en README y programa.",
    "Confirmar si herencia Codex/GPT-Pro ya puede cerrarse como verificada localmente."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Garantizar consistencia entre identidad institucional, argumento juridico y soporte bibliografico."
    ],
    "style_markers": [
      "Supuestos marcados de forma explicita.",
      "Secciones funcionales y trazables.",
      "Coherencia entre portada, cuerpo y referencias."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo.",
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
        "Propagacion segura transversal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura transversal",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables o ambiguas."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener fuente trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada permite aplicacion profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion segura transversal",
          "kind": "depends_on",
          "justification": "La reutilizacion entre nodos requiere marco institucional comun."
        }
      ],
      "evidence": [
        "README de Derechos de autor fija ubicacion curricular y pauta editorial.",
        "Programa analitico define ejes problema-conceptos-producto-analisis-cierre.",
        "Regla heredada consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion integral aplicada sin eliminar reglas utiles previas.",
      "Ciclo 22: reforzada transferencia estable transversal desde actividad origen a materia destino.",
      "Ciclo 22: preservada politica de provisionalidad para herencia no verificada.",
      "Ciclo 22: reforzados gates de calidad y grafo conceptual reusable."
    ]
  }
}