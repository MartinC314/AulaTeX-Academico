{
  "summary": [
    "Sincronización transversal conservadora aplicada sin regresión.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control JSON.",
    "Se mantiene separación entre abstracciones editoriales y contenido temático específico.",
    "Se refuerzan alertas técnicas locales verificadas: placeholders, rutas truncadas y .tex incompleto [supuesto técnico].",
    "Compresión lossless realizada por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna o guía oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No fijar como oficial el código LDE-S6B1 sin respaldo documental [supuesto].",
    "No cambiar la convención local danos/daños sin confirmación documental."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib."
  ],
  "activity_rules": [
    "Formular problema jurídico pertinente a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar contenido temático de Filosofía del Derecho si no aporta al objetivo local.",
    "Distinguir análisis propio de afirmaciones fácticas o normativas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que afirmaciones jurídicas tengan fuente o marca de análisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles previas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas truncadas y caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Completar plantilla .tex truncada en authortable antes de compilar [supuesto técnico]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar vacíos de fuentes como preguntas abiertas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redacción o contenido temático puntual de origen.",
    "Mantener alerta de normalización manual por antecedentes de salida no estructurada (ciclos 1, 2 y 3).",
    "Propagar control de placeholders y rutas truncadas como regla técnica general."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato por actividad para esta materia.",
    "Confirmar convención final de nombres con danos/daños en todo el árbol.",
    "Confirmar si LDE-S6B1 es código oficial o interno [supuesto].",
    "Confirmar corrección final de README en entradas truncadas de estructura.",
    "Confirmar resolución del placeholder .Slug en README y programa analítico.",
    "Confirmar cierre completo de authortable en la plantilla .tex."
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
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derecho de la responsabilidad civil y daños [convención local pendiente].",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico relevante.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con criterio.",
      "Conclusión jurídica transferible.",
      "Calidad estructural verificable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos útiles y verificables.",
      "Sostener coherencia institucional y técnica en toda entrega.",
      "Asegurar transferencia profesional del razonamiento jurídico."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia documental.",
      "Secciones funcionales y auditables.",
      "Cierre con utilidad práctica.",
      "Sincronización transversal sin arrastre temático improcedente."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con fuentes.",
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
          "justification": "La identidad institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La estructura parseable evita ambigüedad y errores de propagación."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay razonamiento jurídico enfocado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Daño",
          "target": "Responsabilidad civil",
          "kind": "depends_on",
          "justification": "La materia articula imputación y consecuencias a partir del daño."
        },
        {
          "source": "Estructura argumentativa reusable",
          "target": "Sincronización transversal",
          "kind": "develops",
          "justification": "Permite transferir método sin copiar contenido literal."
        }
      ],
      "evidence": [
        "README local con pauta editorial y ubicación curricular.",
        "Programa analítico local con ejes de trabajo.",
        ".bib local con fuentes institucionales base.",
        "Plantilla .tex local truncada en authortable [supuesto técnico].",
        "Historial de salidas no estructuradas en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicación completa de reglas repetidas.",
      "Ciclo 17: conservación de gates críticos heredados (JSON, normalización, no regresión).",
      "Ciclo 17: refuerzo de estructura argumentativa común entre nodos no equivalentes.",
      "Ciclo 17: preservación de alertas técnicas locales sin convertir supuestos en hechos.",
      "Ciclo 17: consolidación del grafo conceptual transversal para propagación recursiva."
    ]
  }
}