{
  "summary": [
    "Se consolida memoria lateral reusable entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM, ejes editoriales y control de calidad con deduplicacion lossless.",
    "Se mantiene normalizacion estructurada y validacion JSON estricta como precondicion de propagacion.",
    "Se refuerza regla de marcar supuestos cuando falte consigna local de Actividad 4.",
    "Se conserva separacion entre bibliografia base de asignatura y bibliografia especifica por actividad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Mantener integridad academica con citas verificables.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir explicitamente problema, conceptos, evidencia y analisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin confirmar pertinencia para Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Verificar nombres reales de archivos en README por posibles caracteres danados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4. [supuesto]",
    "Marcar como pendiente cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos nucleares y relaciones recurrentes.",
    "No transferir redaccion literal, conclusiones concretas ni bibliografia exclusiva de un hermano.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe como metodo de compresion lossless.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y rubrica.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib cuando el token Slug no este resuelto.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a Actividad 4 o solo a Semana 7.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
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
      "Transformar la planeacion semanal en productos academicos con fundamento juridico, evidencia y transferencia profesional.",
      "Asegurar continuidad editorial entre actividades sin perder trazabilidad ni control de calidad."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con logica juridica.",
      "Sostener afirmaciones con cita explicita.",
      "Marcar supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar marco conceptual y normativo.",
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
        "Relacion problema-evidencia-conclusion juridica"
      ],
      "citations": [
        "README.md de asignatura",
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
          "justification": "Los cinco ejes ordenan desarrollo y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo y analisis."
        }
      ],
      "evidence": [
        "README define identidad UnADM, entrada canonica y exigencia de conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes de salida no parseable justifican gate de JSON estricto.",
        "Token Slug sin resolver en README obliga verificacion de nombre .bib. [supuesto]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se reforzo transferencia lateral por patrones, sin copiar contenido especifico de Actividad 1.",
      "Ciclo 8: se deduplicaron reglas repetidas manteniendo cobertura funcional completa.",
      "Ciclo 8: se preservaron reglas de calidad criticas y se mantuvo bloqueo por JSON invalido.",
      "Ciclo 8: se mantuvo separacion entre bibliografia base y bibliografia por actividad."
    ]
  }
}