{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular verificable.",
    "Se refuerza gate crítico: no propagar sin JSON parseable y estructura mínima.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar contenido específico.",
    "Supuesto: la consigna textual de Actividad 4 no está visible; mantener plantilla base."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio, cierre.",
    "Alinear el producto al formato solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir problema, conceptos, evidencia y análisis propio de forma explícita.",
    "Evitar entrega meramente descriptiva o de resumen.",
    "Sustentar afirmaciones con citas verificables.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: confirmar si la temática local es interpretación jurídica antes de fijar fuentes específicas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación española correctos en .tex y .bib.",
    "Citar solo claves existentes en el .bib.",
    "Mantener claves BibTeX estables; no renombrar claves activas sin migración total.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver o reemplazar tokens tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin reducir especificidad local.",
    "No transferir conclusiones ni redacción literal entre nodos hermanos.",
    "Propagar patrones de estructura, identidad, calidad y trazabilidad de fuentes.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4 y su producto exacto.",
    "Confirmar rúbrica docente específica para profundidad argumentativa.",
    "Confirmar si requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere .bib incremental.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Entrada canónica en carpeta de asignatura",
        "Normalización obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1",
        "Bloque 2",
        "Obligatoria",
        "8 créditos",
        "Asignatura Filosofía del Derecho"
      ]
    },
    "essence": [
      "Problema jurídico o social",
      "Conceptos, normas, doctrina o datos pertinentes",
      "Producto solicitado por planeación",
      "Análisis propio y postura académica",
      "Conclusión transferible a práctica jurídica"
    ],
    "reason_for_being": [
      "Transformar planeación semanal en producto académico trazable",
      "Asegurar fundamento jurídico con evidencia verificable",
      "Conectar estructura argumentativa con aplicación profesional"
    ],
    "style_markers": [
      "Objetivo explícito al inicio",
      "Secciones funcionales con lógica jurídica",
      "Cita explícita por afirmación relevante",
      "Supuestos marcados cuando falte dato local"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Delimitar marco conceptual y normativo",
      "Contrastar fuentes con análisis propio",
      "Emitir postura justificada",
      "Cerrar con conclusión jurídica aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Ejes editoriales de Filosofía del Derecho"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "Define consistencia editorial transversal."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión requiere evidencia y argumentación."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden y cobertura mínima."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico define cinco ejes de trabajo reutilizables.",
        "Historial reporta salidas no parseables; se justifica gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 64: deduplicación de reglas repetidas con preservación semántica.",
      "Ciclo 64: se mantiene política de supuestos para datos no visibles.",
      "Ciclo 64: se refuerza separación entre patrones transferibles y contenido específico de hermano.",
      "Ciclo 64: se mantiene compatibilidad LaTeX/BibTeX y trazabilidad de fuentes."
    ]
  }
}