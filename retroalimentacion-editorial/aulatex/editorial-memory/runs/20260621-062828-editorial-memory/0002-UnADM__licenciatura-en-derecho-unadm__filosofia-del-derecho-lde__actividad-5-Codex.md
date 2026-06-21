{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 con deduplicación lossless y sin recorte de reglas útiles.",
    "Se preserva identidad UnADM y ubicación curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada obligatoria: no propagar si no hay JSON parseable.",
    "Se estabilizan ejes editoriales reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se aplica transferencia controlada: no copiar conclusiones específicas ni bibliografía exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte consigna o rúbrica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 5.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "Evitar regresiones: conservar reglas útiles previas y agregar solo mejoras verificables.",
    "No propagar como académicas fuentes no verificadas de memoria técnica.",
    "Cuando falte dato local, propagar plantilla base más preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar enunciado textual de la Actividad 5.",
    "Confirmar rúbrica específica de evaluación de la Actividad 5.",
    "Confirmar si el producto es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica total o parcialmente a Actividad 5."
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
      "Problema jurídico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con cita.",
      "Análisis propio con inferencia jurídica.",
      "Conclusión transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Mantener continuidad editorial entre actividades hermanas sin copiar contenido específico.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre inicial breve y funcional.",
      "Secciones con propósito analítico claro.",
      "Uso explícito de supuestos cuando falta información.",
      "Cierre con postura propia sustentada."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a contexto profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Ejes editoriales troncales",
        "Consistencia cita-.bib",
        "Producto alineado a consigna",
        "Supuesto explícito"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Producto alineado a consigna",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterio de cierre."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "La secuencia problema-conceptos-evidencia habilita postura jurídica."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La trazabilidad bibliográfica sostiene validez argumentativa."
        },
        {
          "source": "Supuesto explícito",
          "target": "Riesgo de invención",
          "kind": "contrasts",
          "justification": "Declarar supuestos reduce afirmaciones no verificadas."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, fuentes, análisis propio y cierre.",
        "Historial de parseo: obligación de gate estructural antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicación aplicada en reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 2: se conserva regla crítica de bloqueo por JSON no parseable.",
      "Ciclo 2: se refuerza separación entre bibliografía base y bibliografía específica de actividad.",
      "Ciclo 2: se mantiene transferencia por analogía controlada entre nodos hermanos."
    ]
  }
}