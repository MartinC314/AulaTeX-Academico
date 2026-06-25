{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se refuerza compresión lossless por unión y deduplicación.",
    "Se mantiene separación entre abstracciones editoriales y contenido temático local.",
    "Se conserva alerta técnica local: salidas no estructuradas, rutas truncadas y placeholders."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de la materia como entrada canónica.",
    "Marcar como supuesto cualquier dato no confirmado en consigna o guía oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No fijar como oficial el código LDE-S6B1 sin respaldo documental explícito.",
    "No cambiar la convención local danos/daños sin validación documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto con la planeación semanal y la consigna vigente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib."
  ],
  "activity_rules": [
    "Formular un problema jurídico activador de la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir análisis propio de contenido descriptivo.",
    "Evitar arrastre temático literal desde materias no equivalentes.",
    "Transferir solo patrones argumentativos y reglas editoriales estables.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que afirmaciones jurídicas tengan fuente o marca de análisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles previas.",
    "Detectar y corregir placeholders sin resolver y rutas truncadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Corregir nombres truncados en README y artefactos referenciados.",
    "Completar plantilla .tex truncada en authortable antes de uso productivo. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar vacíos de referencia como pregunta abierta."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y transversales.",
    "Evitar propagar redacción literal o contenido temático de origen no equivalente.",
    "Mantener normalización manual en ciclos con antecedentes de salida no estructurada.",
    "Propagar gates de calidad y grafo conceptual antes que detalles de actividad puntual.",
    "Conservar compresión lossless por unión-dedupe en cada ciclo."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final danos/daños en todo el árbol documental.",
    "Confirmar oficialidad del código de curso LDE-S6B1.",
    "Resolver definitivamente placeholders Slug en README y programa analítico.",
    "Validar y reparar truncamientos de nombres de archivo en README.",
    "Completar bloque authortable de la plantilla .tex local."
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
        "Normalización estructurada previa a propagación.",
        "Entrada canónica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho de la responsabilidad civil y daños. [convención local pendiente]",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico definido.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Calidad estructural verificable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar evidencia jurídica y criterio propio.",
      "Mantener continuidad editorial entre nodos sin mezclar temáticas."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia documental.",
      "Secciones funcionales y verificables.",
      "Cierre con utilidad profesional.",
      "Separación estricta entre reglas editoriales y contenido temático."
    ],
    "argumentative_patterns": [
      "Problema breve y contextualizado.",
      "Marco conceptual y normativo con citas.",
      "Análisis propio con contraste.",
      "Conclusión aplicada a práctica jurídica."
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La estructura parseable evita ambigüedad y pérdida de reglas."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento normativo y doctrinal."
        },
        {
          "source": "Daño",
          "target": "Responsabilidad civil",
          "kind": "depends_on",
          "justification": "El eje de la materia vincula imputación y efectos del daño."
        }
      ],
      "evidence": [
        "README local: ubicación curricular, pauta editorial y estructura de carpeta.",
        "Programa analítico local: propósito y ejes de trabajo.",
        ".bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local truncada en authortable. [supuesto técnico confirmado por lectura parcial]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicación completa de reglas repetidas y variantes ortográficas.",
      "Ciclo 18: se preservan todas las reglas útiles previas sin recorte semántico.",
      "Ciclo 18: se refuerza transferencia transversal de abstracciones estables.",
      "Ciclo 18: se mantienen vacíos locales abiertos sin inventar fuentes ni datos."
    ]
  }
}