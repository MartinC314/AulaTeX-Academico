{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM, ejes editoriales y control de normalización JSON.",
    "Se aplica deduplicación lossless sin recortar reglas útiles previas.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento, evidencia y transferencia profesional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía exclusiva de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar revisión manual extra en memorias con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de fijar rutas finales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "No copiar redacción literal, conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Confirmar enunciado específico de la Actividad 5.",
    "Confirmar rúbrica de evaluación de la Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si bibliografía de Semana 7 aplica a Actividad 5 o requiere selección nueva."
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
      "Transformar planeación semanal en productos académicos trazables y útiles.",
      "Asegurar coherencia entre problema, evidencia, análisis y cierre jurídico.",
      "Preservar continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Postura propia sustentada.",
      "Uso explícito de supuestos cuando falte información."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura -> transferencia práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Producto alineado a consigna"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, integridad y orientación del producto."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez argumentativa requiere respaldo verificable."
        },
        {
          "source": "Producto alineado a consigna",
          "target": "Ejes editoriales troncales",
          "kind": "develops",
          "justification": "Concreta los ejes según la actividad específica."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-producto-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y obliga gate de estructura.",
        "Supuesto: falta consigna completa de Actividad 5 en contexto visible."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas preservando contenido útil.",
      "Se reforzó control de parseo JSON como condición de propagación.",
      "Se consolidó separación entre bibliografía base y bibliografía específica de actividad.",
      "Se evitó transferir conclusiones y fuentes exclusivas de Actividad 1."
    ]
  }
}