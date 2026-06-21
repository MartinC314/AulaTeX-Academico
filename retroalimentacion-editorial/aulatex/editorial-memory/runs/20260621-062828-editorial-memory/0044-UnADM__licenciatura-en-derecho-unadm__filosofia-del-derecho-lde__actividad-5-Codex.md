{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM, ejes editoriales y control de calidad estructural.",
    "Se aplica deduplicacion lossless y se eliminan repeticiones semanticas.",
    "Se mantiene regla de no propagar contenido no parseable sin normalizacion.",
    "Supuesto: falta consigna local completa de Actividad 5; se preserva estructura base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad y precision.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia juridica.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si falta alcance o formato en la consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con incidentes historicos de parseo.",
    "Verificar que el producto responda al problema y no solo resuma conceptos."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y requiere validacion de pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones especificas entre hermanos.",
    "Evitar regresiones: conservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar normalizacion manual si un nodo vecino trae salida no estructurada.",
    "Mantener bandera de riesgo historico por incidentes de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar formato requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografia de Semana 7 aplica a Actividad 5 o requiere set propio."
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en entregables academicos solidos.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y trazables.",
      "Postura propia sustentada.",
      "Supuestos marcados de forma explicita.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia del resultado a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalizacion JSON",
        "Consistencia cita-.bib",
        "Bibliografia base vs bibliografia especifica",
        "Supuestos explicitos"
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
          "justification": "La identidad institucional fija tono, rigor y forma del producto."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez argumentativa depende de evidencia trazable."
        },
        {
          "source": "Bibliografia base vs bibliografia especifica",
          "target": "Actividad 5",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la especifica responde a la consigna concreta."
        },
        {
          "source": "Supuestos explicitos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita invenciones cuando faltan datos locales."
        }
      ],
      "evidence": [
        "README: pauta editorial y entrada canonica de asignatura.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial: incidentes de parseo no JSON obligan gate de normalizacion.",
        "Comentario en clean.bib indica alcance de Semana 7 y exige verificacion de pertinencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: deduplicacion semantica aplicada sin perder reglas validas.",
      "Ciclo 44: se preservan reglas institucionales, de estructura, calidad y LaTeX.",
      "Ciclo 44: se refuerza transferencia lateral por patrones, sin copiar conclusiones ni bibliografia exclusiva.",
      "Ciclo 44: se mantienen preguntas abiertas donde faltan datos locales verificables."
    ]
  }
}