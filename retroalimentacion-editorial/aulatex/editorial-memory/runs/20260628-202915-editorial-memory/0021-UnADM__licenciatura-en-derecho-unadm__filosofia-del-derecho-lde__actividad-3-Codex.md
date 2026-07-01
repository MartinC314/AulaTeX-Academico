{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 con deduplicacion lossless.",
    "Se preserva ADN UnADM: identidad institucional, integridad academica, citas verificables y cierre juridico propio.",
    "Se mantiene regla dura de normalizacion: sin JSON parseable no hay propagacion recursiva.",
    "Se transfieren solo patrones reutilizables de estructura, calidad y argumentacion; no redaccion ni conclusiones especificas.",
    "Se conserva politica de supuestos para toda falta de consigna local en actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Usar secuencia minima: problema, conceptos y fuentes, analisis propio, cierre.",
    "Separar marco normativo o doctrinal cuando aplique.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin eliminar reglas utiles previas.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva de actividad-1.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o consigna de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivo canonicos desde README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo entradas realmente citadas en actividad-3.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar compresion por union y deduplicacion, sin recorte semantico.",
    "Propagar a nodos hermanos solo reglas generales y patrones reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo cuando existan incidencias previas de parseo.",
    "Si falta consigna textual, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si la bibliografia depurada de Semana 7 aplica a actividad-3 [supuesto].",
    "Confirmar archivo .tex principal de actividad-3."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada obligatoria."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Garantizar consistencia editorial y trazabilidad de fuentes entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion con evidencia y cita.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo inicial -> desarrollo coherente -> cierre consistente."
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
        "Politica de supuestos"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
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
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, conclusion juridica.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas en identidad, estructura, calidad y bibliografia.",
      "Ciclo 2: preservadas reglas utiles previas sin regresion.",
      "Ciclo 2: refuerzo lateral controlado por analogia, sin traslado de contenido especifico de actividad-1.",
      "Ciclo 2: se mantiene uso condicionado de bibliografia clean por falta de consigna local confirmada."
    ]
  }
}