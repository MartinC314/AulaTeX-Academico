{
  "summary": [
    "Memoria local consolidada en ciclo 3 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se mantiene normalización JSON obligatoria antes de propagar.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva TEX reconstruible y continuidad de claves de cita."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y no a Actividad 1."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalización manual al reutilizar salidas no estructuradas de ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografía existente o requiere .bib propio."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Uso de conceptos, normas y doctrina pertinente.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar fundamento jurídico, evidencia verificable y criterio propio.",
      "Mantener trazabilidad editorial y técnica del nodo."
    ],
    "style_markers": [
      "Abrir con encuadre del problema.",
      "Desarrollar por secciones explícitas.",
      "Citar fuentes en cada afirmación sustantiva.",
      "Marcar supuestos cuando falte dato de consigna.",
      "Cerrar con conclusión jurídica aplicada."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> análisis propio -> conclusión.",
      "Pregunta guía -> desarrollo con evidencia -> postura -> cierre coherente.",
      "Descripción breve -> evaluación crítica -> transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Fundamentos del derecho",
        "Justicia",
        "Derecho y moral",
        "Análisis crítico del fenómeno jurídico",
        "Constitución y marco de derechos",
        "Víctimas y acceso a justicia"
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
        "gandara_ley_2015"
      ],
      "relations": [
        {
          "source": "Problema jurídico o social",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "supports",
          "justification": "El encuadre inicial activa el razonamiento jurídico del desarrollo."
        },
        {
          "source": "Conceptos y doctrina",
          "target": "Postura argumentada del estudiante",
          "kind": "depends_on",
          "justification": "La postura debe fundarse en marco conceptual verificable."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere sustento normativo explícito."
        },
        {
          "source": "Filosofia-del-derecho-clean.bib",
          "target": "Actividad 1",
          "kind": "contrasts",
          "justification": "Archivo identificado como Semana 7; uso en Actividad 1 queda como supuesto."
        },
        {
          "source": "README y programa analítico",
          "target": "Reglas editoriales locales",
          "kind": "develops",
          "justification": "Ambos documentos fijan identidad, ejes y forma de entrega."
        }
      ],
      "evidence": [
        "README.md de asignatura con pauta editorial y ubicación curricular.",
        "programa-analitico-filosofia-del-derecho.md con propósito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex como fuente reconstruible.",
        "Listado de claves citadas en tex_primary."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortográficas.",
      "Se preservaron reglas útiles sin recorte semántico.",
      "Se mantuvieron supuestos explícitos sobre consigna y .bib canónico.",
      "Se reforzó conexión entre estructura argumentativa y control de calidad.",
      "Se confirmó continuidad del ADN editorial del mismo nodo en ciclo 3."
    ]
  }
}