{
  "summary": [
    "Memoria local canonizada con preservacion total y deduplicacion lossless.",
    "Se mantiene identidad UnADM y contexto curricular de Filosofia del Derecho.",
    "Se conservan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza regla de normalizacion: no propagar salidas no estructuradas.",
    "Se mantiene trazabilidad de fuentes provisionales y supuestos pendientes.",
    "Se preserva TEX reconstruible del artefacto de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores corresponden a Actividad 1."
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
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentacion u otro formato principal.",
    "Confirmar rubrica de evaluacion especifica.",
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
      "Estandarizar salidas para asegurar calidad, trazabilidad y propagacion segura."
    ],
    "style_markers": [
      "Marcar supuestos de forma explicita.",
      "Usar secciones con funcion argumentativa clara.",
      "Conectar doctrina, norma y postura propia.",
      "Cerrar con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> delimitacion del objetivo.",
      "Conceptos clave -> marco normativo/doctrinal -> analisis propio.",
      "Evidencia citada -> inferencia juridica -> conclusion transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Problema juridico o social",
        "Conceptos juridicos fundamentales",
        "Marco normativo",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "franzoni_acevedo_ley_2017",
        "rojas_gonzalez_filosofia_derecho_2018",
        "gandara_ley_2015",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta o tension juridica concreta."
        },
        {
          "source": "Conceptos juridicos fundamentales",
          "target": "Marco normativo",
          "kind": "supports",
          "justification": "Los conceptos ordenan la lectura de normas y doctrina."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar de fundamento normativo verificable."
        },
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "develops",
          "justification": "La interpretacion provee criterios para justificar tesis."
        },
        {
          "source": "Derecho y moral",
          "target": "Justicia",
          "kind": "contrasts",
          "justification": "El curso compara enfoques positivistas y iusnaturalistas."
        }
      ],
      "evidence": [
        "README.md: pauta editorial e identidad institucional.",
        "programa-analitico-filosofia-del-derecho.md: proposito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible con 79 bloques.",
        "filosofia-del-derecho-clean.bib: evidencia de foco en Semana 7 (supuesto no extrapolable a Actividad 1)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion integral sin perdida de reglas utiles.",
      "Ciclo 18: canon local consolidado con enfasis en validacion estructural y trazabilidad bibliografica.",
      "Ciclo 18: se preserva artefacto principal reporte-filosofia-del-derecho-Actividad-1."
    ]
  }
}