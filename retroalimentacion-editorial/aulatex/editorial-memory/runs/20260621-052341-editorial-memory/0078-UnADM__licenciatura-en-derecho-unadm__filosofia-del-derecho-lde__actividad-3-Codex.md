{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar sin JSON parseable y sin estructura minima completa.",
    "Se mantiene deduplicacion lossless por union de reglas sin recorte de contenido util.",
    "Se marca como supuesto toda inferencia no confirmada por consigna local de Actividad 3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de evaluacion.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y etiquetar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad hermana sin copiar redaccion literal.",
    "No transferir conclusiones especificas ni bibliografia exclusiva de otra actividad.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente cualquier memoria no estructurada antes de reutilizarla."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivo en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Registrar en .bib solo fuentes citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No usar memoria editorial como bibliografia academica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar propagar contenido tematico puntual no confirmado en nodo destino.",
    "Conservar bandera de riesgo cuando exista historial de parseo defectuoso.",
    "Aplicar compresion lossless por union y deduplicacion en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica de Actividad 3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si bibliografia depurada de Semana 7 aplica o no a Actividad 3 [supuesto].",
    "Confirmar archivo .tex principal canonico para Actividad 3."
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
      "Problema juridico o social como punto de partida.",
      "Conceptos y fuentes pertinentes como soporte.",
      "Analisis propio como nucleo del aprendizaje.",
      "Conclusion juridica transferible a practica profesional.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia entre objetivo, evidencia y postura juridica.",
      "Sostener continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Afirmaciones con cita verificable.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo consistente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Estructura minima editorial",
        "Integridad academica",
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
        "filosofia-del-derecho-clean.bib [uso condicionado, supuesto]"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Estructura minima editorial",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "Ordenar secciones evita entregas descriptivas."
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
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 78: deduplicacion lossless aplicada sin eliminar reglas utiles.",
      "Ciclo 78: se refuerza transferencia lateral de patrones, no de contenido especifico.",
      "Ciclo 78: se mantiene politica de supuestos y no invencion de fuentes.",
      "Ciclo 78: se preserva compuerta de calidad de parseo JSON como requisito duro."
    ]
  }
}