{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM, estructura editorial base y control de calidad de propagación.",
    "Se mantiene compresión lossless por deduplicación semántica y eliminación de ruido duplicado.",
    "Se evita transferir conclusiones específicas y bibliografía exclusiva de un hermano a otro.",
    "Se mantiene el estado de supuestos explícitos donde falta consigna local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmaciones, evidencia y conclusión.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si hay duda de alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar revisión manual extra en memorias con incidentes previos de parseo.",
    "Rechazar reutilización de contenido no estructurado sin normalización."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "No propagar bibliografía exclusiva entre hermanos sin validación de consigna.",
    "Conservar deduplicación semántica sin pérdida de reglas válidas.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 requiere reporte, presentación u otro formato principal.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 es pertinente para Actividad 5."
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
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y cierre argumentativo.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Mantener continuidad editorial entre actividades sin copiar contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos marcados cuando falte información.",
      "Cierre con transferencia a práctica jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterio académico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida debe tener respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema, conceptos, producto, análisis y cierre.",
        "Historial de ciclos: incidentes de parseo obligan gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: consolidación lateral A1->A5 con deduplicación lossless.",
      "Se preservaron reglas institucionales y gates técnicos sin recorte funcional.",
      "Se retiró transferencia de contenido específico no reutilizable entre hermanos.",
      "Se mantuvieron supuestos abiertos por falta de consigna local verificable."
    ]
  }
}