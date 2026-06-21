{
  "summary": [
    "Memoria lateral consolidada por union y deduplicacion sin recorte.",
    "Se preserva identidad UnADM y marco curricular verificable para Actividad 4.",
    "Se transfieren solo patrones reutilizables desde Actividad 1: identidad, estructura, calidad y trazabilidad.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Ubicar la actividad en semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No copiar conclusiones especificas de Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna real de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres reales de archivos en README por tokens Slug sin resolver.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar si aplica a Actividad 4 antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local de cada actividad.",
    "Aplicar compresion lossless por union-dedupe en ciclos posteriores.",
    "Preservar reglas utiles previas y evitar regresiones editoriales.",
    "Cuando falte consigna, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del archivo .bib con token Slug resuelto.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere bloque .bib propio."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo-doctrinal pertinente.",
      "Evidencia verificable y trazable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos.",
      "Asegurar fundamento juridico, claridad y transferencia profesional.",
      "Mantener consistencia editorial entre actividades hermanas sin copiar contenido especifico."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y trazables.",
      "Uso visible de supuestos cuando falte evidencia local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problematizar contexto.",
      "Delimitar conceptos y normas aplicables.",
      "Contrastar evidencia con analisis propio.",
      "Sostener postura argumentada.",
      "Concluir con implicacion juridica practica."
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
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden argumentativo reusable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida exige respaldo y analisis."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y exigencia de conclusion juridica propia.",
        "Programa analitico define cinco ejes reutilizables.",
        "Antecedentes de salida no parseable justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortograficas.",
      "Se conservaron reglas utiles previas sin recortes semanticos.",
      "Se eliminaron traslados no permitidos de contenido especifico de Actividad 1.",
      "Se reforzo control de supuestos por falta de consigna local visible.",
      "Se mantuvo estrategia progresiva por analogia controlada entre nodos hermanos."
    ]
  }
}