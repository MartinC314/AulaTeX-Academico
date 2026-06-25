{
  "summary": [
    "Se refuerza identidad UnADM y ejes editoriales por unión-dedupe sin recorte.",
    "Se transfiere patrón estructural: problema, conceptos/marco, análisis propio y cierre.",
    "Se endurecen compuertas de calidad: JSON parseable, citas verificables y marcado de supuestos.",
    "Se alinean reglas LaTeX: claves BibTeX estables, acentos correctos y tokens Slug resueltos.",
    "Se distingue bibliografía base vs específica de actividad; no inventar fuentes.",
    "Se mantiene validación curricular: semestre 1, bloque 2, obligatoria, 8 créditos (fuente malla curricular).",
    "Se dejan preguntas abiertas sobre consigna y .bib canónico para Actividad 4."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Ubicar la asignatura en semestre 1, bloque 2, obligatoria, 8 créditos (fuente: malla-curricular-derecho-unadm.pdf).",
    "Usar la carpeta de la asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico con postura propia sustentada.",
    "Tratar memoria heredada no verificada como provisional hasta validación local.",
    "Marcar como supuesto cualquier dato no visible en la consigna."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Vincular cada entrega con los ejes del programa analítico.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Redactar con claridad, fundamento jurídico y evidencia verificable."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico de la asignatura.",
    "Incluir explícitamente el problema jurídico o social que activa la entrega.",
    "Integrar conceptos, normas, doctrina o datos pertinentes según consigna.",
    "Desarrollar análisis propio y postura argumentada antes de la conclusión.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Comprobar que toda cita tenga referencia bibliográfica verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar instrucciones específicas de la actividad antes de redactar (marcar supuestos).",
    "No propagar reglas dudosas sin marcarlas como supuesto.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Citar en el .tex solo claves existentes en el .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos listados en README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico (supuesto hasta confirmar nombres reales)."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No inventar referencias; usar solo obras consultables con metadatos mínimos.",
    "Conservar autor, título, año y fuente/editorial o URL en cada entrada.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con las claves del .tex (supuesto hasta validar para Actividad 4)."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si hay salidas no estructuradas en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas; usar unión-dedupe.",
    "Propagar solo reglas generales cuando falte consigna textual local."
  ],
  "open_questions": [
    "Confirmar consigna específica de Actividad 4: producto, extensión y criterios de evaluación.",
    "Determinar si Actividad 4 corresponde a interpretación jurídica u otro tema.",
    "Confirmar el nombre canónico del archivo .bib de la asignatura (plantilla Slug sin resolver en README).",
    "Verificar si existe rúbrica docente adicional no incluida en README/programa analítico.",
    "Definir si se usará .bib limpio existente o uno incremental para Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica y citas verificables",
        "Entrada canónica en carpeta de la asignatura",
        "Normalización estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2",
        "Obligatoria, 8 créditos",
        "Asignatura: Filosofía del Derecho"
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura",
      "Conceptos, normas, doctrina o datos pertinentes",
      "Producto solicitado por la planeación",
      "Análisis propio y postura académica",
      "Conclusión transferible a la práctica jurídica",
      "Integridad académica y verificabilidad",
      "Normalización y trazabilidad documental"
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento y transferencia profesional",
      "Asegurar relación clara entre problema, evidencia y conclusión jurídica",
      "Establecer una estructura reusable y evaluable para actividades de la asignatura"
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo",
      "Separar secciones funcionales con lógica jurídica",
      "Sostener afirmaciones con cita explícita",
      "Marcar supuestos cuando falte evidencia local",
      "Concluir con criterio propio aplicable a la práctica"
    ],
    "argumentative_patterns": [
      "Plantear el problema inicial con contexto",
      "Desarrollar marco conceptual y normativo",
      "Contrastar fuentes con análisis propio",
      "Emitir postura justificada",
      "Cerrar con conclusión jurídica aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON",
        "Relación problema-evidencia-conclusión",
        "Bibliografía base vs específica",
        "Claves BibTeX estables",
        "Tokens Slug en README"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "supports",
          "justification": "Los ejes definen el orden lógico del análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no se permite reutilización segura."
        },
        {
          "source": "Bibliografía base vs específica",
          "target": "Claves BibTeX estables",
          "kind": "supports",
          "justification": "La separación favorece trazabilidad y evita roturas de compilación."
        },
        {
          "source": "Tokens Slug en README",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Resolver plantillas asegura rutas y nombres correctos antes de compilar."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y conclusión jurídica con criterio propio",
        "Programa analítico: cinco ejes de trabajo reutilizables",
        "Malla curricular: ubicación en semestre 1, bloque 2, obligatoria, 8 créditos"
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: Refuerzo lateral desde actividad-1 a actividad-4 por unión-dedupe de patrones institucionales, estructurales, de calidad y bibliográficos.",
      "Ciclo 5: Se agrega gate de consistencia citas .tex/.bib y estabilidad de claves BibTeX.",
      "Ciclo 5: Se consolida regla de resolver tokens Slug en README/programa antes de compilar.",
      "Ciclo 5: Se mantienen preguntas abiertas para consigna y .bib canónico de Actividad 4."
    ]
  }
}