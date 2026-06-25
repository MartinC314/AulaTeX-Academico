{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad no equivalente con reglas estables y sin recorte.",
    "Se preserva identidad UnADM, estructura base de entrega y cierre juridico transferible.",
    "Se mantiene gate duro: bloquear propagacion si la salida no es JSON parseable.",
    "Se refuerza normalizacion de placeholders y rutas corruptas en README y programa analitico.",
    "Se conserva compresion lossless por union-dedupe y trazabilidad de herencia provisional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular toda entrega a Licenciatura en Derecho y contexto local de semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad explicita del origen transversal: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, evidencia, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "No eliminar reglas utiles previas; solo agregar mejoras verificables."
  ],
  "activity_rules": [
    "Identificar el problema juridico que activa la actividad.",
    "Diferenciar resumen descriptivo y postura propia.",
    "Sustentar cada afirmacion relevante con fuente verificable y cita explicita.",
    "Vincular argumentos con norma, doctrina, jurisprudencia o dato verificable segun consigna.",
    "Declarar limites del analisis cuando falten datos.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Verificar consistencia entre README, programa analitico y archivos reales.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside cuando aplique la plantilla actual.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Usar coursename y universitydepartment con el nombre exacto de la materia.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes a la actividad.",
    "Agregar solo fuentes efectivamente usadas en la entrega destino.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Incluir metadatos minimos: autor, titulo, anio, fuente y URL o editorial.",
    "Incluir fecha de consulta en recursos web o mutables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenidos tematicos especificos de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No sobrescribir reglas locales mas especificas con reglas generales heredadas.",
    "Mantener incidente historico de no-JSON como alerta activa hasta cierre verificado."
  ],
  "open_questions": [
    "Supuesto: la incidencia de JSON no parseable sigue activa; confirmar cierre en este ciclo.",
    "Confirmar formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Confirmar correccion definitiva de entradas corruptas en README y programa.",
    "Confirmar si existe rubrica oficial por actividad en esta materia."
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
      "Analisis propio no meramente descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Garantizar coherencia entre consigna, desarrollo argumentativo y cierre profesional.",
      "Preservar memoria editorial reutilizable con trazabilidad y control de calidad."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion clara entre descripcion y postura propia.",
      "Cierre con criterio juridico aplicable.",
      "Normalizacion estructurada obligatoria antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia local canonica"
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
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Es gate institucional de bloqueo."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige fundamento verificable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin regresion."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Bib local existente como repositorio canonico.",
        "Historial de incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se deduplicaron reglas repetidas sin perdida semantica.",
      "Ciclo 3: se reforzo gate JSON parseable como condicion de propagacion.",
      "Ciclo 3: se transfirieron solo abstracciones estables desde nodo transversal.",
      "Ciclo 3: se mantuvo alerta sobre placeholders de slug y rutas corruptas.",
      "Ciclo 3: se preservo identidad UnADM y estructura argumentativa base."
    ]
  }
}