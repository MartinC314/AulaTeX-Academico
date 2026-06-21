{
  "summary": [
    "Memoria local canonizada con preservacion total y deduplicacion lossless.",
    "Se mantiene identidad UnADM y ubicacion curricular verificable desde README.",
    "Se mantiene regla de normalizacion estructurada previa a toda propagacion.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva TEX reconstruible de Actividad 1 y control de claves BibTeX estables.",
    "Supuesto: la consigna textual de Actividad 1 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 1."
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
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 (interpretacion juridica)."
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
      "Transformar la planeacion semanal en entregables con fundamento juridico, evidencia y cierre argumentativo.",
      "Asegurar transferencia profesional del analisis academico en Derecho."
    ],
    "style_markers": [
      "Abrir con encuadre del problema.",
      "Desarrollar por secciones explicitas.",
      "Sostener cada afirmacion con evidencia verificable.",
      "Declarar supuestos de forma visible.",
      "Cerrar con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> analisis propio -> conclusion.",
      "Descripcion breve -> contraste de fuentes -> toma de postura -> implicacion practica.",
      "Pregunta guia -> desarrollo consistente -> cierre que responde la pregunta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Objeto de estudio",
        "Principios y normas juridicas",
        "Justicia",
        "Fundamentos del derecho",
        "Analisis critico del fenomeno juridico",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Derechos de victimas"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio y postura academica",
          "kind": "depends_on",
          "justification": "El analisis se activa desde un problema delimitado."
        },
        {
          "source": "Conceptos, normas y doctrina",
          "target": "Conclusion transferible a la practica juridica",
          "kind": "supports",
          "justification": "La conclusion valida requiere base conceptual y normativa."
        },
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "develops",
          "justification": "La interpretacion provee criterios para sostener tesis."
        },
        {
          "source": "Constitucion y leyes vigentes",
          "target": "Postura del estudiante",
          "kind": "supports",
          "justification": "La postura debe justificarse con marco juridico verificable."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicacion curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: proposito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: estructura y claves citadas reconstruibles.",
        "filosofia-del-derecho-clean.bib: evidencia de foco en Semana 7, no equivalente automatico a Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Se elimino duplicidad ortografica y semantica sin perdida de reglas.",
      "Se mantuvieron supuestos explicitamente marcados.",
      "Se preservo compatibilidad con TEX y BibTeX existentes.",
      "Se reforzo patron argumentativo canonico de la actividad.",
      "Se mantuvo criterio de no inventar fuentes y de verificacion local."
    ]
  }
}