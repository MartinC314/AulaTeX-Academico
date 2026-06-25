{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas institucionales UnADM, normalización JSON y ejes argumentativos reutilizables.",
    "Se refuerzan controles locales verificables: placeholders sin resolver, rutas truncadas y plantilla .tex incompleta [supuesto técnico].",
    "Se transfiere solo abstracción editorial estable; no se transfiere contenido temático literal de Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto de Licenciatura en Derecho y materia de responsabilidad civil y daños.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no confirmado por consigna o guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "No declarar oficial el código de curso LDE-S6B1 sin fuente documental explícita [supuesto].",
    "No alterar la convención local danos/daños sin confirmación documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la planeación semanal y la consigna vigente.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y archivo .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Formular el problema jurídico en clave de responsabilidad civil y daño.",
    "No arrastrar contenido temático de origen cuando no aplique al nodo destino.",
    "Distinguir fundamento jurídico, evidencia y análisis propio."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmación jurídica tenga fuente o marca de análisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver.",
    "Validar compilación LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar metadatos por actividad sin romper identidad institucional.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres truncados de archivos antes de referenciarlos.",
    "Completar la sección authortable truncada antes de compilar [supuesto técnico]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Conservar como base local unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, no contenido temático puntual.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte semántico.",
    "Mantener alertas técnicas como controles generales reutilizables.",
    "Conservar antecedentes de normalización manual en ciclos con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final de nombres con danos versus daños en todo el árbol.",
    "Confirmar si LDE-S6B1 es código oficial o interno [supuesto].",
    "Validar y corregir truncamientos en README de reporte y referencias.",
    "Resolver placeholder del .bib en README y programa analítico.",
    "Confirmar rúbricas específicas por actividad para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
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
      "Problema jurídico claro.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible.",
      "Cumplimiento estricto de consigna y formato."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar fundamento jurídico, evidencia y criterio propio.",
      "Permitir propagación segura por estandarización editorial."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia documental.",
      "Secciones funcionales y verificables.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Planteamiento breve del problema.",
      "Marco conceptual y normativo con citas.",
      "Análisis propio con contraste.",
      "Conclusión jurídica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada JSON",
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
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Normalización estructurada JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Reduce ambigüedad y evita reutilizar salidas inválidas."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "No hay análisis sólido sin pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa y doctrinal."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "El campo de estudio se estructura sobre la noción de daño."
        },
        {
          "source": "Ejes editoriales transversales",
          "target": "Productos semanales",
          "kind": "develops",
          "justification": "La estructura reusable guía reportes y presentaciones sin traslado temático literal."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "Archivo .bib local con fuentes institucionales.",
        "Plantilla .tex local con truncamiento en authortable [supuesto técnico].",
        "Historial de salidas no estructuradas en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicación integral de reglas repetidas.",
      "Ciclo 19: preservación de gates críticos heredados sin recorte.",
      "Ciclo 19: refuerzo de transferencia por abstracciones estables entre nodos no equivalentes.",
      "Ciclo 19: mantenimiento de vacíos locales como preguntas abiertas verificables."
    ]
  }
}