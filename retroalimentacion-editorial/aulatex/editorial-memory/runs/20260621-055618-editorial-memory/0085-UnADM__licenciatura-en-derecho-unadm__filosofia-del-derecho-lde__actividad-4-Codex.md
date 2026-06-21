{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren solo patrones reutilizables desde Actividad 1, sin copiar contenido especifico.",
    "Supuesto: la consigna local detallada de Actividad 4 sigue no visible."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega a UnADM y Licenciatura en Derecho.",
    "Usar Filosofia del Derecho como marco disciplinar explicito.",
    "Mantener carpeta de asignatura como entrada canonica.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar formato final al tipo de entrega pedido en Actividad 4.",
    "No trasladar conclusiones especificas de Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Validar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves BibTeX ya activas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local.",
    "Supuesto: filosofia-del-derecho-clean.bib fue creado para Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Aplicar union-dedupe para evitar regresiones.",
    "No propagar bibliografia exclusiva de un hermano a otro sin confirmacion.",
    "Transferir patrones de argumentacion, no redaccion literal.",
    "Mantener bandera de normalizacion manual en ciclos con salida defectuosa."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y rubrica.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si aplica bibliografia de interpretacion juridica o se requiere otra.",
    "Supuesto: los nombres de archivo en README incluyen tokens no resueltos."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
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
      "Transformar planeacion semanal en entregables con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y calidad formal en cada actividad.",
      "Preservar continuidad institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explicita para afirmaciones sustantivas.",
      "Supuestos marcados cuando falte dato local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Fijar postura argumentada.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
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
          "justification": "La pauta local exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia verificable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico: cinco ejes de trabajo transferibles.",
        "Antecedentes: salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 85: deduplicacion de reglas repetidas en destino.",
      "Ciclo 85: refuerzo de gates JSON y normalizacion estructurada.",
      "Ciclo 85: transferencia lateral de patrones sin copiar conclusiones de Actividad 1.",
      "Ciclo 85: mantenimiento de supuestos abiertos por falta de consigna local completa."
    ]
  }
}