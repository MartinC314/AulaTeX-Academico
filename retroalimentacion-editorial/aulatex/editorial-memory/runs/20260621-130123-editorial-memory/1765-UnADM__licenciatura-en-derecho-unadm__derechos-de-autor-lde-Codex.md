{
  "summary": [
    "Consolidar memoria editorial de materia para Derechos de autor con identidad UnADM.",
    "Mantener compresion lossless por union y deduplicacion sin recorte.",
    "Preservar normalizacion estructurada obligatoria antes de propagar.",
    "Reforzar ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Marcar como provisionales herencias no verificadas localmente (Codex, GPT-Pro).",
    "Corregir deuda local verificable: tokens de plantilla y nombres de archivo corruptos en README y programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como soporte curricular cuando aplique.",
    "Supuesto: LDE-S5B1 es clave local valida hasta confirmacion institucional global."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar programa analitico como marco reusable de estructura.",
    "Normalizar nombres de archivo con slug de asignatura.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres corruptos detectados en estructura (eporte, eferencias)."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local de la materia.",
    "No asumir fuentes de otras semanas sin validacion contra consigna.",
    "Verificar que cada entrega corresponda al producto pedido en la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Detectar y corregir campos pendientes en portada (ejemplo: Nombre por definir).",
    "Auditar README y programa por tokens de plantilla no resueltos."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo consigna contraria.",
    "Declarar metadatos antes de cargar plantilla base.",
    "Mantener tabla de autor completa y sin marcadores pendientes.",
    "No dejar comandos incompletos en preambulo.",
    "No dejar \\usepackage sin argumento.",
    "Mover paquetes al preambulo efectivo segun plantilla.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar acentos y codificacion correctos en .tex y .bib."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Registrar bibliografia especifica por actividad en derechos-de-autor.bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Asegurar correspondencia bidireccional entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Preservar reglas utiles previas sin regresion.",
    "Mantener bandera de normalizacion manual para herencia de ciclos tempranos.",
    "Propagar advertencias sobre Codex y GPT-Pro solo como estado provisional.",
    "Si falta consigna local, propagar solo abstracciones editoriales generales."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial transversal en toda la suite.",
    "Confirmar nombre de figura docente para cerrar marcador en portada.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer fijo en metadatos.",
    "Confirmar orden correcto de carga de paquetes respecto a template en esta plantilla.",
    "Confirmar cierre definitivo de tokens $(@{...}.Slug) en README y programa.",
    "Confirmar continuidad o retiro de herencia provisional Codex/GPT-Pro tras validacion local."
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
        "Carpeta de asignatura como entrada canonica."
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
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener consistencia editorial entre actividades y formatos.",
      "Asegurar transferencia segura de reglas entre nodos no equivalentes."
    ],
    "style_markers": [
      "Supuestos declarados de forma explicita.",
      "Secciones funcionales y trazables.",
      "Consistencia entre portada, desarrollo y bibliografia.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion segura entre nodos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura entre nodos",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
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
          "source": "Identidad institucional UnADM",
          "target": "Propagacion segura entre nodos",
          "kind": "depends_on",
          "justification": "La transferencia transversal mantiene marco institucional comun."
        }
      ],
      "evidence": [
        "README de Derechos de autor define ubicacion curricular y entrada canonica.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene fuentes institucionales base.",
        "Se detectan tokens de plantilla y nombres corruptos que requieren normalizacion local.",
        "En reporte .tex existe comando \\usepackage incompleto al cierre del preambulo."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates de JSON parseable y normalizacion previa.",
      "Se reforzo declaracion de supuestos y provisionalidad de herencias no verificadas.",
      "Se transfirieron solo abstracciones estables desde actividad de otra materia.",
      "Se agregaron mejoras verificables del contexto local (tokens, nombres corruptos, preambulo incompleto)."
    ]
  }
}