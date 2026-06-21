{
  "summary": [
    "Memoria local canonizada por union y deduplicacion sin perdida.",
    "Se mantiene identidad UnADM y contexto curricular verificable.",
    "Se conserva normalizacion estructurada obligatoria antes de propagar.",
    "Se preservan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza control de fuentes provisionales y marcado explicito de supuestos.",
    "Se mantiene TEX reconstruible y continuidad de claves BibTeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular Actividad 1 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
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
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 y no define por si solo Actividad 1."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
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
      "Transformar la planeacion semanal en productos academicos con fundamento juridico, evidencia y cierre argumentativo transferible."
    ],
    "style_markers": [
      "Apertura con problema juridico concreto.",
      "Desarrollo por secciones funcionales y trazables.",
      "Uso de fuentes verificables con cita explicita.",
      "Marcado explicito de supuestos cuando falte dato de consigna.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia verificable -> interpretacion juridica.",
      "Coherencia interna entre pregunta guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Problema juridico o social",
        "Fundamentos del derecho",
        "Justicia",
        "Derecho y moral",
        "Analisis critico del fenomeno juridico",
        "Constitucion Politica de los Estados Unidos Mexicanos",
        "Ley General de Victimas",
        "Argumentacion juridica"
      ],
      "citations": [
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "generales_ley_2021",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "supports",
          "justification": "El encuadre del problema activa el desarrollo argumentativo exigido por la actividad."
        },
        {
          "source": "Conceptos, normas y doctrina",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura del estudiante requiere base conceptual y normativa verificable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge de la interpretacion argumentada del caso o tema."
        },
        {
          "source": "Constitucion Politica de los Estados Unidos Mexicanos",
          "target": "Marco normativo",
          "kind": "supports",
          "justification": "Funciona como referencia juridica vigente para sustentar afirmaciones."
        },
        {
          "source": "Ley General de Victimas",
          "target": "Marco normativo",
          "kind": "supports",
          "justification": "Aporta sustento legal tematico cuando el problema aborda derechos de victimas."
        }
      ],
      "evidence": [
        "README.md de asignatura con ubicacion curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md con ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex como fuente TEX reconstruible.",
        "filosofia-del-derecho.bib y claves citadas en tex_primary.",
        "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 segun encabezado local."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes con y sin acentos.",
      "Se preservo el contenido util previo sin recorte semantico.",
      "Se reforzo la trazabilidad entre consigna, estructura y validacion.",
      "Se mantuvo la politica de no inventar fuentes y marcar supuestos.",
      "Se confirmo continuidad de identidad UnADM y del flujo de calidad."
    ]
  }
}