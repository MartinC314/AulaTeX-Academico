{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin copiar contenido especifico de Actividad 1.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales comunes de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta antes de toda propagacion recursiva.",
    "Se mantiene regla de marcar supuestos cuando la consigna local no sea visible."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineados con UnADM.",
    "Vincular la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "No trasladar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en el .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura, calidad y trazabilidad.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva de un hermano.",
    "Aplicar union-dedupe sin regresion de reglas utiles previas.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en lugar de inventar.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto exacto.",
    "Confirmar rubrica y criterios de evaluacion especificos de Actividad 4.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra semana; confirmar si aplica a Actividad 4."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia verificable.",
      "Asegurar trazabilidad editorial entre actividades sin perdida de reglas nucleares."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar hechos, conceptos, argumentos y postura personal.",
      "Sostener cada afirmacion con cita o supuesto marcado.",
      "Cierre con criterio juridico propio aplicable."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Contraste de fuentes con analisis propio.",
      "Postura justificada.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional constante."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Definen orden de construccion argumentativa reutilizable."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia y analisis."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y exigencia de conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate de JSON estricto.",
        "Token Slug sin resolver en README exige verificacion de nombres de archivo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: deduplicacion de reglas repetidas con conservacion total de contenido util.",
      "Ciclo 43: refuerzo lateral de patrones transferibles sin copiar resultados especificos del hermano.",
      "Ciclo 43: mantenimiento de supuestos abiertos donde falta evidencia local verificable."
    ]
  }
}