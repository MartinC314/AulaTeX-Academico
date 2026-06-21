{
  "summary": [
    "Se consolida refuerzo lateral para actividad-3 con deduplicacion lossless y sin regresion.",
    "Se preservan reglas nucleares: identidad UnADM, estructura argumentativa y control de calidad JSON.",
    "Se transfieren solo patrones reutilizables desde actividad-1, sin copiar conclusiones ni bibliografia exclusiva.",
    "Se mantiene politica de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir consigna, semana ni formato de actividad-3 sin evidencia local.",
    "Heredar reglas validas de actividad-1 sin copiar redaccion literal ni conclusiones especificas."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas en actividad-3.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica (Semana 7) y su uso en actividad-3 depende de coincidencia tematica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a nodos hermanos reglas generales de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresion por union y deduplicacion lossless en cada ciclo.",
    "Conservar trazabilidad de incidencias de parseo como control editorial, no como evidencia academica."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3 (reporte, presentacion u otro).",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si la bibliografia depurada de Semana 7 aplica o se requiere .bib especifico."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Normalizacion estructurada obligatoria antes de propagar."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar coherencia entre objetivo, desarrollo argumentativo y cierre juridico.",
      "Preservar memoria editorial reutilizable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y orden logico.",
      "Afirmacion con evidencia y cita.",
      "Supuestos marcados cuando falte dato local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo explicito -> desarrollo alineado -> cierre verificable."
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
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
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
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion confiable de reglas argumentativas."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de la delimitacion del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: se reforzo transferencia lateral controlada desde actividad-1 a actividad-3.",
      "Ciclo 73: se eliminaron duplicados semanticos sin recorte de reglas utiles.",
      "Ciclo 73: se mantuvieron supuestos abiertos donde falta consigna local verificable."
    ]
  }
}