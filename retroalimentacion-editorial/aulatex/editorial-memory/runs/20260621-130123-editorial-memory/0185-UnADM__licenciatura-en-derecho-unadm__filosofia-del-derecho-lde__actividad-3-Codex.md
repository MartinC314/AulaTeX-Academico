{
  "summary": [
    "Memoria lateral consolidada para actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado.",
    "Se mantienen ejes editoriales: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se mantiene regla critica: no propagar sin JSON parseable y estructura minima valida.",
    "Se evita transferencia de conclusiones o bibliografia exclusiva de actividad-1.",
    "Se marcan como supuesto los datos no confirmados de consigna local en actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Alinear el producto al formato solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables desde actividad-1.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva de hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: conservar reglas utiles previas.",
    "Distinguir fuentes academicas y normativas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles con citas del .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir en nombres de archivo del README y programa analitico.",
    "Verificar rutas y nombres canonicos antes de referenciar artefactos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con consigna y citas de actividad-3 [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales y patrones argumentativos.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo cuando exista antecedente de salida no estructurada.",
    "Aplicar compresion por union y deduplicacion sin recorte semantico.",
    "Priorizar refuerzo lateral de identidad, calidad y estructura."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar bibliografia obligatoria de la semana correspondiente.",
    "Confirmar si aplica bibliografia depurada de interpretacion juridica (Semana 7) [supuesto].",
    "Confirmar archivo .tex principal canonico para actividad-3."
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
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico valido.",
      "Asegurar claridad, fundamento juridico y transferencia profesional.",
      "Sostener trazabilidad entre afirmaciones, citas y conclusion."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Postura propia sustentada.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se activa desde un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 3: refuerzo lateral de patrones reutilizables sin copiar contenido especifico de actividad-1.",
      "Ciclo 3: conservada no regresion en calidad, estructura, LaTeX y bibliografia.",
      "Ciclo 3: mantenidos supuestos abiertos por falta de consigna local verificable."
    ]
  }
}