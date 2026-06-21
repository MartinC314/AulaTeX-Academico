{
  "summary": [
    "Se consolida refuerzo lateral de actividad-1 hacia actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion cuando no hay JSON parseable.",
    "Se refuerza que datos no visibles en consigna se marcan como [supuesto].",
    "Se evita transferir conclusiones especificas o bibliografia exclusiva entre actividades hermanas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna local.",
    "Tratar memorias editoriales heredadas como antecedentes provisionales, no como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Heredar patrones reutilizables de actividad-1 sin copiar redaccion literal.",
    "No trasladar conclusiones especificas de actividad-1 a actividad-3.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o consigna de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no-regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Tomar como [supuesto] que el .bib canonico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en la actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a actividad-3; marcar como [supuesto] hasta confirmar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando existan incidencias de parseo previas.",
    "Aplicar compresion por union y deduplicacion, sin recorte semantico."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3 (reporte, presentacion u otro).",
    "Confirmar rubrica especifica de evaluacion para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si la bibliografia depurada de Semana 7 aplica o no a actividad-3.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura tras resolver token Slug."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos.",
      "Mantener fundamento juridico, evidencia y transferencia profesional.",
      "Asegurar continuidad editorial entre actividades sin contaminar evidencia."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmaciones con evidencia verificable.",
      "Marcado explicito de [supuesto] cuando falte evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
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
        "Bibliografia verificable",
        "Supuestos controlados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor y verificabilidad."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        },
        {
          "source": "Supuestos controlados",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "Evita inventar fuentes o aplicar bibliografia no confirmada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables, conclusion juridica propia.",
        "Programa analitico: ejes de trabajo y proposito editorial.",
        "Regla persistente: bloqueo por falta de JSON parseable.",
        "Nota local: bibliografia clean corresponde a interpretacion juridica (Semana 7)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 40: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 40: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 40: se refuerza transferencia lateral solo de patrones reutilizables.",
      "Ciclo 40: se agrega control explicito de [supuesto] para datos no confirmados."
    ]
  }
}