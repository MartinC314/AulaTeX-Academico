{
  "summary": [
    "Se mantiene sincronizacion transversal con transferencia solo de abstracciones estables.",
    "Se preservan reglas utiles previas y se aplica deduplicacion semantica lossless.",
    "Se refuerza nucleo editorial UnADM: problema, fundamento, analisis propio y conclusion juridica.",
    "Se conserva gate critico: bloquear propagacion sin JSON parseable.",
    "Se mantiene contexto local verificado: semestre 6, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Conservar coursecode local LDE-S6B2 cuando aplique plantilla actual.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad del origen heredado: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Diferenciar resumen descriptivo de postura propia.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Vincular cada argumento con norma, doctrina o evidencia.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Mantener clase article en espanol, letterpaper y oneside segun plantilla local.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar \\documenttitle y \\documentsubtitle segun actividad.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: README contiene entradas corruptas en nombres de reporte y referencias; normalizar antes de propagar."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio canonico.",
    "Registrar solo fuentes consultables; no inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas por actividad en el .bib local.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas si no fueron usadas en actividad destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales.",
    "Conservar incidente historico JSON hasta confirmar resolucion.",
    "Aplicar union-dedupe lossless en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar si la incidencia de JSON no parseable ya quedo resuelta en este ciclo.",
    "Definir formato uniforme de cita juridica para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar consigna oficial por actividad de la materia para afinar profundidad.",
    "Supuesto: debe corregirse placeholder .Slug en README y programa analitico."
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
      "Problema juridico que activa el analisis.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Postura propia argumentada.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y fundados.",
      "Asegurar transferibilidad profesional del cierre juridico.",
      "Mantener memoria editorial estable, verificable y reutilizable."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion neta entre descripcion y argumentacion propia.",
      "Cierre con criterio juridico operativo.",
      "Trazabilidad de toda regla heredada."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final de coherencia."
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
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige formato institucional y citas verificables."
        },
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
          "justification": "El desarrollo argumentativo nace de una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "El cierre debe sostenerse en norma, doctrina o evidencia."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Permite consolidar memoria sin perder reglas utiles."
        }
      ],
      "evidence": [
        "README de materia con identidad UnADM y ubicacion curricular.",
        "Programa analitico con ejes editoriales reutilizables.",
        "Archivo .bib local con fuentes institucionales base.",
        "Registro historico de incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte de contenido util.",
      "Se conservaron gates institucionales criticos de parseo y estructura.",
      "Se transfirieron patrones argumentativos estables desde nodo no equivalente.",
      "Se evitaron fuentes nuevas no verificadas y redaccion literal del origen.",
      "Se reforzo correccion de placeholders y rutas corruptas como riesgo operativo."
    ]
  }
}