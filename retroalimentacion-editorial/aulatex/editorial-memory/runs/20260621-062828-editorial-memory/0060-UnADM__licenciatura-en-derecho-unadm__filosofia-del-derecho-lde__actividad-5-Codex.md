{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM y ubicacion curricular oficial de Filosofia del Derecho.",
    "Se consolida regla de normalizacion JSON parseable como condicion de propagacion recursiva.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se agrega control lateral: transferir patrones reutilizables y no conclusiones ni bibliografia exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales y no como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia en cada bloque argumentativo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido en la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante y evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin validar pertinencia.",
    "Si falta dato operativo, declarar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna y no solo a ejes generales.",
    "Aplicar revision manual extra en memoria con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otro contexto tematico y requiere validacion previa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y verificadas.",
    "Aplicar union y deduplicacion lossless; no recortar reglas utiles.",
    "Evitar transferencia literal de conclusiones o redaccion entre hermanos.",
    "Preservar bandera historica de riesgo por salidas no parseables.",
    "Cuando falte consigna local, propagar plantilla estructural y preguntas abiertas.",
    "Reforzar conexiones concepto-regla-calidad antes que contenido puntual."
  ],
  "open_questions": [
    "Confirmar enunciado textual y rubrica especifica de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si bibliografia de Semana 7 es pertinente para Actividad 5.",
    "Confirmar fuentes obligatorias definidas por la semana de Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico delimita el trabajo.",
      "Conceptos y marco normativo sostienen el analisis.",
      "Evidencia verificable legitima inferencias.",
      "Postura propia evita descripcion vacia.",
      "Conclusion juridica debe ser transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico evaluable.",
      "Mantener continuidad institucional sin perder ajuste a cada consigna.",
      "Asegurar trazabilidad entre instruccion, argumentacion y evidencia."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y trazables.",
      "Supuestos explicitados cuando faltan datos.",
      "Cierre juridico aplicable.",
      "Control de estructura JSON antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> postura propia.",
      "Regla general -> aplicacion al caso -> limite o supuesto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalizacion JSON",
        "Consistencia cita-bib",
        "Transferencia lateral controlada"
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
          "justification": "El marco institucional fija tono, integridad y finalidad del producto."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion confiable."
        },
        {
          "source": "Consistencia cita-bib",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "La evidencia verificable sostiene el analisis y la conclusion."
        },
        {
          "source": "Transferencia lateral controlada",
          "target": "Identidad UnADM",
          "kind": "develops",
          "justification": "Permite continuidad entre hermanos sin contaminar con contenido especifico."
        }
      ],
      "evidence": [
        "README fija identidad UnADM y criterio de conclusion juridica.",
        "Programa analitico define ejes de problema, conceptos, fuentes, analisis y cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene gate de estructura.",
        "Contexto local muestra tokens sin expandir en nombres; se conserva regla de saneamiento."
      ]
    },
    "reinforcement_log": [
      "Ciclo 60: deduplicacion integral aplicada sin perdida de reglas utiles.",
      "Ciclo 60: se refuerza transferencia por patrones y se bloquea copia de conclusiones hermanas.",
      "Ciclo 60: se mantiene control estricto de JSON parseable previo a propagacion recursiva.",
      "Ciclo 60: se retiene incertidumbre local como preguntas abiertas y supuestos marcados."
    ]
  }
}