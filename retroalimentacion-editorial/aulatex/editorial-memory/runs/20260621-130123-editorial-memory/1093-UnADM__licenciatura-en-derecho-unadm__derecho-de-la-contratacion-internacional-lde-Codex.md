{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad no equivalente con transferencia por abstracciones estables.",
    "Se preserva identidad UnADM, estructura editorial reusable y compresion lossless por union-dedupe.",
    "Se refuerza gate de bloqueo por JSON no parseable y normalizacion previa obligatoria.",
    "Se mantiene contexto local verificado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se agrega control de placeholders y rutas corruptas en README y programa analitico como mejora verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Conservar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad del origen heredado: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables.",
    "Normalizar nombres de archivo y placeholders antes de reutilizar rutas."
  ],
  "activity_rules": [
    "Identificar el problema juridico que activa la actividad.",
    "Sustentar afirmaciones con norma, doctrina o evidencia verificable.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos.",
    "No trasladar fuentes de otra materia sin verificacion de pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que README, programa y archivos reales coincidan en nombres y rutas."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside en plantilla actual.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad.",
    "Usar \\coursename y \\universitydepartment con el nombre exacto de la materia.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "Incluir metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas que no fueron usadas en la actividad destino."
  ],
  "propagation_hints": [
    "Propagar solo reglas editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico especifico de Filosofia del Derecho.",
    "Mantener etiqueta de incidente historico JSON hasta confirmar cierre.",
    "Aplicar union-dedupe semantico sin recorte destructivo en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar si la incidencia JSON no parseable ya quedo resuelta en este ciclo. [supuesto]",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y visual.",
    "Confirmar planeacion oficial de actividades de la materia para afinar reglas locales.",
    "Confirmar correccion final de placeholders Slug y rutas corruptas en README/programa."
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
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Asegurar consistencia institucional, trazabilidad y calidad tecnica en LaTeX/BibTeX."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion clara entre descripcion y postura propia.",
      "Cierre con criterio juridico transferible.",
      "Trazabilidad de reglas heredadas."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna -> producto alineado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
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
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "La reutilizacion segura depende de salida valida."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido se bloquea propagacion."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo verificable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin perder historial."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo .bib local canonico existente.",
        "Registro historico de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura total.",
      "Se transfirieron solo abstracciones estables desde el origen transversal.",
      "Se excluyeron contenidos tematicos especificos de Filosofia del Derecho no aplicables al destino.",
      "Se reforzo control de placeholders Slug y rutas corruptas como mejora verificable.",
      "Se mantuvo estrategia progresiva y conservadora sin regresion."
    ]
  }
}