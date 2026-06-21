{
  "summary": [
    "Memoria local canonizada por union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificable.",
    "Se mantiene normalizacion JSON obligatoria antes de propagar.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva TEX reconstruible y reglas de compilacion estables.",
    "Se mantiene distincion entre bibliografia base y bibliografia especifica por actividad.",
    "Se refuerza control de supuestos cuando falte consigna textual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib segun Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 (interpretacion juridica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentacion u otro formato principal.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografia existente o requiere .bib propio."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico, evidencia y transferencia profesional.",
      "Convertir consignas en entregables con estructura argumentativa verificable."
    ],
    "style_markers": [
      "Enunciar objetivo al inicio.",
      "Separar marco conceptual y marco normativo.",
      "Argumentar con citas y postura propia.",
      "Cerrar con conclusion juridica aplicable.",
      "Marcar supuestos de forma explicita."
    ],
    "argumentative_patterns": [
      "Problema inicial -> conceptos clave -> evidencia normativa/doctrinal -> analisis propio -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> implicacion practica.",
      "Contraste entre doctrina y caso -> toma de postura sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Problema juridico o social",
        "Analisis critico del fenomeno juridico",
        "Justicia",
        "Fundamentos del derecho",
        "Derecho y moral",
        "Hermenutica e interpretacion juridica",
        "Argumentacion juridica",
        "Constitucion Politica de los Estados Unidos Mexicanos",
        "Ley General de Victimas"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "El encuadre del problema activa el desarrollo argumentativo de la actividad."
        },
        {
          "source": "Conceptos clave",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura estudiantil requiere base conceptual previa."
        },
        {
          "source": "Constitucion Politica de los Estados Unidos Mexicanos",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre debe anclarse en marco normativo vigente."
        },
        {
          "source": "Hermenutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion da criterios para justificar inferencias juridicas."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "El curso examina tensiones entre validez juridica y valor moral."
        }
      ],
      "evidence": [
        "README.md: identidad institucional, ubicacion curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: proposito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura reconstruible y citas usadas.",
        "filosofia-del-derecho-clean.bib: evidencia de foco en Semana 7 (supuesto para no mezclar con Actividad 1)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 93: deduplicacion completa de reglas repetidas con preservacion semantica.",
      "Ciclo 93: se mantiene artefacto canonico de actividad como reporte.",
      "Ciclo 93: se refuerza distincion entre fuentes verificadas y fuentes provisionales.",
      "Ciclo 93: se preserva compatibilidad con TEX reconstruible y control de claves BibTeX."
    ]
  }
}