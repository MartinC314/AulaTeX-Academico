{
  "summary": [
    "Se consolida sincronizacion transversal en materia destino con compresion lossless por union-dedupe.",
    "Se preservan reglas utiles previas y se refuerzan solo abstracciones estables transferibles.",
    "Se mantiene incidente historico de salidas no JSON parseables como gate institucional activo.",
    "Se confirma contexto local de la materia: semestre 6, bloque 2, obligatoria, 8 creditos [verificado en README].",
    "Se refuerza normalizacion de placeholders y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto curricular local.",
    "Usar carpeta de materia como entrada canonica.",
    "Conservar trazabilidad de reglas heredadas y su estado de verificacion.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Estructurar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Identificar problema juridico que activa la actividad.",
    "Diferenciar resumen descriptivo y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular argumentos con norma, doctrina o evidencia aplicable.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar correspondencia entre producto entregado y consigna local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que nombres de archivos en README coincidan con archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside cuando aplique plantilla local.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad real.",
    "Usar \\coursename y \\universitydepartment con el nombre exacto de la asignatura.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente usadas en la actividad destino.",
    "Incluir metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o mutables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Preservar reglas locales mas especificas del destino sobre reglas generales heredadas.",
    "Mantener union-dedupe lossless y evitar regresiones en ciclos posteriores."
  ],
  "open_questions": [
    "Confirmar si la incidencia de JSON no parseable ya quedo resuelta en este ciclo.",
    "Definir formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y visual.",
    "Confirmar planeacion oficial especifica de actividades de esta asignatura.",
    "Supuesto: debe corregirse placeholder de BibTeX en README y programa analitico."
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
        "Semestre 6, bloque 2, obligatoria, 8 creditos [verificado].",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Marco conceptual y normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Garantizar consistencia institucional, metodologica y tecnica en cada entrega."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion nitida entre descripcion y postura propia.",
      "Cierre con criterio juridico transferible.",
      "Trazabilidad de fuentes y reglas heredadas."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Trazabilidad de herencia",
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
          "justification": "El encuadre institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Compresion lossless por deduplicacion",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida previa."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se construye a partir de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe estar respaldada por norma, doctrina o evidencia."
        },
        {
          "source": "Trazabilidad de herencia",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Permite auditar reglas heredadas y evitar regresiones."
        }
      ],
      "evidence": [
        "README de materia confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico define proposito y ejes editoriales reutilizables.",
        "Bib local confirma repositorio canonico de referencias.",
        "Registros historicos confirman incidente de salida no JSON parseable.",
        "Se detectan placeholders $(@{...}.Slug) y rutas corruptas que requieren normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se preservan reglas previas utiles sin eliminacion.",
      "Ciclo 7: se deduplican variantes semanticas repetidas en listas nucleares.",
      "Ciclo 7: se transfiere desde actividad no equivalente solo abstraccion estable.",
      "Ciclo 7: se evita transferir contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 7: se refuerzan gates de JSON, estructura y trazabilidad."
    ]
  }
}