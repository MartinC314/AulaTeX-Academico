{
  "summary": [
    "Se consolida transferencia lateral desde Actividad 1 a Actividad 4 por patrones reutilizables.",
    "Se preserva identidad UnADM y marco curricular verificable sin copiar contenido específico.",
    "Se refuerza normalización estructurada y validación JSON estricta antes de propagar.",
    "Se mantiene flujo editorial base: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: la consigna textual de Actividad 4 no está visible; se conserva estructura base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Sostener integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analítico de la asignatura.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que bibliografía de otras semanas aplica sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Citar en el .tex solo claves existentes en el .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna de Actividad 4 coincide con su tema."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre actividades hermanas.",
    "Evitar copiar redacción literal, conclusiones específicas y bibliografía exclusiva de otro nodo.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar deduplicación lossless por unión semántica y normalización ortográfica.",
    "Mantener bandera de normalización manual para ciclos con salidas históricas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios de evaluación.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a interpretación jurídica; confirmar aplicabilidad a Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 4."
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
        "Carpeta de asignatura como entrada canónica.",
        "Normalización obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos jurídicos con fundamento y trazabilidad.",
      "Asegurar coherencia entre consigna, desarrollo argumentativo y cierre profesional."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con lógica jurídica.",
      "Sostener afirmaciones con cita explícita.",
      "Marcar supuestos cuando falte evidencia local.",
      "Mantener cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Construir marco conceptual y normativo.",
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
        "Integridad académica",
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
          "justification": "La pauta editorial local exige alineación institucional explícita."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan el desarrollo y el cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La postura final requiere respaldo verificable."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, entrada canónica y criterio jurídico propio.",
        "Programa analítico define propósito editorial y cinco ejes reutilizables.",
        "Historial de salidas no parseables justifica gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 92: deduplicación ortográfica y semántica aplicada sin recorte de reglas útiles.",
      "Ciclo 92: refuerzo lateral entre hermanos limitado a patrones transferibles.",
      "Ciclo 92: se mantiene separación entre patrones generales y contenido específico de actividad."
    ]
  }
}