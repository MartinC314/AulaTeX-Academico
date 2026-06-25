{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad no equivalente con transferencia solo de abstracciones estables.",
    "Se preservan reglas utiles previas del destino y se deduplican sin recorte.",
    "Se refuerza ADN UnADM: identidad institucional, estructura argumentativa y trazabilidad.",
    "Se mantiene gate critico: bloquear propagacion sin JSON parseable.",
    "Se confirma contexto local de materia: semestre 6, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho.",
    "Conservar coursecode local LDE-S6B2 cuando aplique plantilla actual.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad del origen heredado por nodo y ciclo."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables.",
    "Corregir rutas, placeholders y nombres corruptos en README y programa antes de reutilizar."
  ],
  "activity_rules": [
    "Identificar problema juridico que activa la actividad.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Diferenciar resumen descriptivo y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "No asumir fuentes de semanas posteriores sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que nombres de archivos en README coincidan con archivos reales.",
    "Mantener incidente historico JSON como activo hasta confirmacion de resolucion."
  ],
  "latex_rules": [
    "Mantener clase article en espanol, letterpaper y oneside cuando aplique.",
    "Conservar macros institucionales de curso y universidad.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "Incluir metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas si no fueron usadas en actividad destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y estructura.",
    "Transferir solo reglas generales estables entre nodos no equivalentes.",
    "No sobrescribir reglas locales mas especificas con reglas transversales.",
    "Aplicar deduplicacion semantica por union-dedupe lossless.",
    "Evitar propagar rutas o artefactos corruptos sin normalizacion previa.",
    "Mantener etiqueta de provisionalidad en herencias no verificadas."
  ],
  "open_questions": [
    "Supuesto: persiste incidencia JSON historica; confirmar estado en ciclo siguiente.",
    "Confirmar formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y visual.",
    "Confirmar si README y programa ya sustituyeron placeholders de slug.",
    "Confirmar rubricas oficiales por actividad para ajustar profundidad argumentativa."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencia editorial entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Asegurar coherencia entre consigna, desarrollo y cierre juridico.",
      "Preservar memoria editorial reusable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion clara entre descripcion y postura propia.",
      "Cierre con criterio juridico aplicable.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Bibliografia verificable",
        "Trazabilidad de herencia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe estar fundada en norma o doctrina."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin recorte destructivo."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma ejes de trabajo reutilizables.",
        "Bib local confirma repositorio canonico de referencias.",
        "Memoria historica confirma incidente de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion semantica completa de reglas repetidas.",
      "Ciclo 18: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 18: refuerzo de gates JSON, estructura y consistencia bib-citas.",
      "Ciclo 18: se mantienen supuestos abiertos por vacios de consigna local."
    ]
  }
}