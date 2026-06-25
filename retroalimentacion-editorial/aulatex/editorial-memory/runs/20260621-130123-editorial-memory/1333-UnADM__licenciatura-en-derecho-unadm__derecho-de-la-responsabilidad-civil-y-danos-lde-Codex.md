{
  "summary": [
    "Se consolida sincronización transversal ciclo 4 sin regresión.",
    "Se preservan reglas institucionales UnADM y normalización JSON obligatoria.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y grafo conceptual.",
    "Se mantiene contexto local verificado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Se refuerzan alertas locales verificadas: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta [supuesto técnico]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Mantener enfoque de Licenciatura en Derecho y materia de responsabilidad civil y daños.",
    "Marcar como supuesto todo dato no confirmado en consigna o guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "No declarar oficial el código LDE-S6B1 sin respaldo documental [supuesto].",
    "No cambiar la convención local danos/daños sin confirmación documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto a la planeación semanal y consigna vigente.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y bibliografía .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Formular problema jurídico pertinente a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Separar fundamento jurídico, evidencia y postura académica.",
    "Incluir criterio propio del estudiante; evitar entregas solo descriptivas.",
    "No arrastrar contenido temático de origen si no aplica al nodo destino.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmación jurídica tenga fuente o marca de análisis propio/supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles heredadas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de compilar."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivo contra README y programa analítico.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Completar plantilla local truncada en authortable antes de compilar [supuesto técnico]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar fuente curricular local: malla-curricular-derecho-unadm.pdf."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo reglas estables no dependientes de una actividad puntual.",
    "Reutilizar gates institucionales de calidad sin reducir especificidad local.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Conservar alertas técnicas como controles editoriales generales, no como contenido temático.",
    "Mantener normalización manual en nodos con antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato por actividad para esta materia.",
    "Confirmar convención definitiva de nombres con danos/daños en todo el árbol.",
    "Confirmar si LDE-S6B1 es código oficial o temporal [supuesto].",
    "Corregir en README y programa analítico rutas truncadas detectadas.",
    "Confirmar resolución final del placeholder de nombre .bib en documentos locales.",
    "Validar cierre técnico de authortable en plantilla .tex local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derecho de la responsabilidad civil y daños.",
        "Fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico activador.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Identidad institucional verificable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos claros, fundados y aplicables.",
      "Asegurar trazabilidad entre consigna, evidencia, análisis y cierre profesional."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia documental.",
      "Secciones funcionales y verificables.",
      "Cierre con utilidad práctica profesional.",
      "Sin literalidad heredada entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema breve y contextualizado.",
      "Marco conceptual y normativo con citas.",
      "Análisis propio con contraste.",
      "Conclusión jurídica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad académica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita propagación de salidas ambiguas o no auditables."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis depende de una pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La responsabilidad civil se articula sobre la noción jurídica de daño."
        }
      ],
      "evidence": [
        "README local: pauta editorial e identidad institucional.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "Archivo .bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local truncada en authortable [supuesto técnico]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicación completa de reglas repetidas y preservación sin recorte semántico.",
      "Ciclo 4: transferencia transversal restringida a abstracciones estables.",
      "Ciclo 4: refuerzo de gates de parseo JSON y normalización previa.",
      "Ciclo 4: mantenimiento de alertas locales técnicas como controles persistentes."
    ]
  }
}