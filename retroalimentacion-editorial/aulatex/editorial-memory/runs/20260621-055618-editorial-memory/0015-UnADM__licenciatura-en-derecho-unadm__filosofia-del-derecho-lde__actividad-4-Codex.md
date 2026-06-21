{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial común.",
    "Se transfieren patrones reutilizables sin copiar redacción ni conclusiones de Actividad 1.",
    "Se mantiene normalización estructurada y validación JSON estricta como puerta de propagación.",
    "Supuesto: la consigna local completa de Actividad 4 no está visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear la entrega a Licenciatura en Derecho y Filosofía del Derecho.",
    "Respetar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, evidencia y postura propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía exclusiva de otra actividad sin validar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre consigna de Actividad 4 y producto entregado.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificación española correctos en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y no aplica por defecto a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales estables en nodos hermanos.",
    "Evitar regresiones: no eliminar reglas útiles previas verificadas.",
    "Transferir patrones, no contenido específico de otra actividad.",
    "Mantener banderas de normalización manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar tipo de producto exigido: reporte, presentación u otro.",
    "Confirmar rúbrica y criterios de evaluación específicos.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canónico final del archivo .bib en el repositorio."
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeación.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con fundamento jurídico.",
      "Garantizar trazabilidad entre problema, evidencia y conclusión.",
      "Sostener identidad institucional y calidad técnica de entrega."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Postura personal argumentada.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables y consistentes."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura justificada.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige coherencia institucional."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de la actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden de desarrollo y cierre."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión válida requiere evidencia trazable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica y exigencia de conclusión jurídica.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Historial de salidas no parseables: necesidad de gate JSON estricto.",
        "Token Slug sin resolver en README/programa: necesidad de verificación de nombres."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: refuerzo lateral hermano A1->A4 aplicado.",
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se preservaron gates críticos de parseo y estructura.",
      "Se evitó transferencia de conclusiones o bibliografía exclusiva de A1.",
      "Se añadieron supuestos explícitos donde faltan datos locales."
    ]
  }
}