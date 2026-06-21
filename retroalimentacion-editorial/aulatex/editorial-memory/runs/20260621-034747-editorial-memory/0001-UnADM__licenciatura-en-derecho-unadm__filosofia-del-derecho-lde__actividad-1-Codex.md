{
  "summary": [
    "Memoria local canonizada sin pérdida por unión y deduplicación.",
    "Se mantiene identidad UnADM y encuadre curricular verificable.",
    "Se preserva regla crítica: no propagar salidas no estructuradas sin normalización.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva trazabilidad LaTeX reconstruible del artefacto de Actividad 1."
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
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar solo reglas generales cuando falte consigna textual."
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
        "Integridad académica y citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y transferencia profesional.",
      "Asegurar que cada entrega conserve identidad institucional y cierre argumentativo propio."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones jurídicas claras.",
      "Uso explícito de fuentes verificables.",
      "Marcado de supuestos cuando falte evidencia local.",
      "Cierre con conclusión aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo/doctrinal -> análisis propio -> conclusión.",
      "Afirmación jurídica -> evidencia citada -> interpretación -> postura personal.",
      "Consigna -> producto esperado -> verificación final de correspondencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Problema jurídico o social",
        "Marco normativo y doctrinal",
        "Análisis crítico del fenómeno jurídico",
        "Conclusión jurídica transferible",
        "Hermenéutica e interpretación jurídica",
        "Derecho y moral"
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
          "justification": "El encuadre del problema activa el desarrollo argumentativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "depends_on",
          "justification": "El análisis propio exige sustento normativo y doctrinal verificable."
        },
        {
          "source": "Análisis crítico del fenómeno jurídico",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión deriva del razonamiento y no de un resumen descriptivo."
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Derecho y moral",
          "kind": "contrasts",
          "justification": "Permite discutir límites entre validez normativa y justificación ética."
        }
      ],
      "evidence": [
        "README.md y programa-analitico-filosofia-del-derecho.md validan identidad, ubicación curricular y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex confirma fuente reconstruible y claves citadas activas.",
        "filosofia-del-derecho-clean.bib documenta alcance Semana 7; no se asume para Actividad 1."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron variantes ortográficas y acentuación sin perder contenido normativo.",
      "Se preservó la regla de bloqueo por JSON no parseable como compuerta principal.",
      "Se mantuvo la trazabilidad de fuentes locales y supuestos explícitos.",
      "Se reforzó la compatibilidad entre reglas editoriales y flujo LaTeX/.bib."
    ]
  }
}