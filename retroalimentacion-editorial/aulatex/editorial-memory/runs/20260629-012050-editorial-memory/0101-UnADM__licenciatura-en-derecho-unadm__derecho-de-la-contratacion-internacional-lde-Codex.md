{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad origen hacia materia destino.",
    "Se preserva identidad UnADM, estructura de cinco ejes y compresion lossless por union-dedupe.",
    "Se mantiene incidente historico de salidas no JSON parseable hasta cierre verificado.",
    "Se refuerza normalizacion previa a toda propagacion recursiva.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la contratacion internacional.",
    "Vincular la materia a Licenciatura en Derecho, semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion.",
    "Conservar trazabilidad del origen heredado: filosofia-del-derecho-lde/actividad-1.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables.",
    "Corregir tokens y rutas corruptas del README antes de reutilizacion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar cada afirmacion con norma, doctrina o evidencia verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir el producto solicitado por la actividad.",
    "Declarar limites del analisis cuando falten datos.",
    "No asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que nombres de archivos en README coincidan con archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside cuando aplique plantilla local.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico antes de enlazar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "Mantener metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas del origen si no fueron consultadas en el destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar copiar redaccion literal o contenido tematico especifico del origen.",
    "Mantener union-dedupe lossless y no regresion en ciclos posteriores.",
    "Si falta contexto local, conservar cerebro editorial minimo y declarar vacios."
  ],
  "open_questions": [
    "Confirmar si la incidencia de JSON no parseable ya quedo resuelta en este ciclo.",
    "Confirmar checklist minimo por tipo de entrega: reporte, presentacion, visual.",
    "Definir formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Confirmar si deben corregirse en origen los nombres corruptos de README (reporte/referencias).",
    "Supuesto: el .bib canonico de materia es derecho-de-la-contratacion-internacional.bib; confirmar en plantilla final."
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
        "Trazabilidad editorial de herencias.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar fundamento juridico, evidencia y cierre argumentativo profesional.",
      "Permitir reutilizacion segura entre nodos mediante memoria estructurada."
    ],
    "style_markers": [
      "Frases directas y secciones funcionales.",
      "Supuestos etiquetados de forma explicita.",
      "Cierre con aplicacion profesional concreta.",
      "Sin contenido no estructurado en propagacion."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura propia sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Trazabilidad editorial",
        "Estructura de cinco ejes",
        "Integridad academica",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite auditoria y reutilizacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige formato consistente y citas verificables."
        },
        {
          "source": "Estructura de cinco ejes",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El patron conduce de problema a cierre aplicable."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "El cierre requiere evidencia y fundamento normativo."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: repositorio base existente y verificable.",
        "Historial institucional: incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se conservan todas las utiles sin recorte semantico.",
      "Ciclo 2: se refuerzan gates de parseo JSON y normalizacion previa.",
      "Ciclo 2: se agrega regla transversal de no transferir contenido tematico especifico entre materias no equivalentes.",
      "Ciclo 2: se mantiene trazabilidad de herencia y estado provisional de fuentes no verificadas.",
      "Ciclo 2: se preserva ADN editorial minimo completo del nodo destino."
    ]
  }
}