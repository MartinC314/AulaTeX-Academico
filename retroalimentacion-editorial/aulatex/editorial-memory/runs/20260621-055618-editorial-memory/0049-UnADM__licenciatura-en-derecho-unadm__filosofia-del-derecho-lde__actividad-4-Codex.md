{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con union-dedupe lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales transferibles.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se mantienen reglas de estructura, calidad, LaTeX y bibliografia sin copiar contenido especifico de Actividad 1.",
    "Supuesto: la consigna textual de Actividad 4 no esta visible; se conserva plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos o normas, evidencia y analisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: confirmar formato final solicitado (reporte, presentacion u otro)."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol consistentes en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Verificar nombres reales de archivos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib puede ser tematico; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones ni redaccion literal de hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para compresion lossless sin recorte semantico.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar rubrica de evaluacion especifica de la semana.",
    "Confirmar si el producto requerido es reporte, presentacion o formato mixto.",
    "Confirmar nombre canonico final del archivo .bib por token Slug no resuelto.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o requiere .bib propio."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y consistencia institucional en cada actividad."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con logica juridica.",
      "Sostener afirmaciones con cita explicita.",
      "Marcar supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
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
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen secuencia de desarrollo y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia y analisis."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica, citas verificables y conclusion juridica.",
        "Programa analitico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de ciclos: salidas no parseables requieren gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortograficas.",
      "Se conservaron reglas utiles heredadas sin recorte funcional.",
      "Se reforzo control de supuestos por falta de consigna local visible.",
      "Se excluyo transferencia de conclusiones especificas y bibliografia exclusiva del hermano."
    ]
  }
}