{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless y sin copiar contenido específico de Actividad 1.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de la asignatura.",
    "Se refuerza validación JSON estricta por antecedentes de salidas no parseables.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local verificable.",
    "Se conserva que la carpeta de asignatura es entrada canónica documental."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Vincular explícitamente la actividad a Filosofía del Derecho.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a la planeación semanal y a la consigna de Actividad 4.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar el tipo de producto solicitado en Actividad 4 antes de fijar formato.",
    "No arrastrar conclusiones específicas de Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) antes de referenciar archivos.",
    "Verificar nombres reales de archivos en README por posibles caracteres dañados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad temática; validar pertinencia antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no redacción literal.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión y deduplicación semántica en cada ciclo.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 es reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del .bib de la asignatura tras resolver token Slug.",
    "Confirmar si se reutiliza bibliografía existente o se requiere .bib incremental específico."
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos verificables.",
      "Sostener claridad argumentativa con fundamento jurídico.",
      "Asegurar transferencia profesional en el cierre."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Sostener cada afirmación con cita explícita.",
      "Marcar supuestos cuando falte evidencia local.",
      "Mantener estructura seccionada y trazable."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de la actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, conceptos, análisis y cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión debe derivar de evidencia y argumentación."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija cinco ejes de trabajo reutilizables.",
        "Antecedentes de salida no parseable justifican gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 39: refuerzo lateral desde hermano Actividad 1 a Actividad 4.",
      "Se consolidaron reglas compartidas de identidad, estructura, calidad y trazabilidad.",
      "Se evitó transferir bibliografía o conclusiones exclusivas de Actividad 1.",
      "Se preservó compresión lossless por unión-deduplicación sin recorte."
    ]
  }
}