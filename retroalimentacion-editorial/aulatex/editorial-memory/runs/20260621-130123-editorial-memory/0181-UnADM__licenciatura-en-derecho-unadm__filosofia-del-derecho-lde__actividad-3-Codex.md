{
  "summary": [
    "Se consolida memoria lateral para actividad-3 con transferencia de patrones reutilizables desde actividad-1.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales sin copiar conclusiones ni redaccion especifica.",
    "Se mantiene normalizacion estructurada obligatoria y compresion lossless por deduplicacion.",
    "Se refuerza politica de supuestos cuando falta consigna local verificable."
  ],
  "identity_rules": [
    "Mantener tono y formato institucional UnADM.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin eliminar reglas utiles previas.",
    "No asumir consigna, semana o formato de actividad-3 sin evidencia local.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles consolidadas."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib es tematico de Semana 7; validar aplicacion a actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar conclusiones especificas ni bibliografia exclusiva entre nodos hermanos.",
    "Mantener bandera de riesgo si hubo incidencias de parseo en ciclos previos.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si aplica bibliografia de interpretacion juridica (Semana 7) a actividad-3.",
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y orden logico.",
      "Cita verificable en afirmaciones relevantes.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo inicial coherente con cierre final."
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
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
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
          "justification": "La conclusion depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "Pauta editorial del README.",
        "Ejes y proposito del programa analitico.",
        "Regla persistente de bloqueo sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion aplicada sin perdida de reglas utiles.",
      "Ciclo 2: se refuerza transferencia lateral por analogia controlada.",
      "Ciclo 2: se evita importar bibliografia exclusiva no confirmada del nodo hermano.",
      "Ciclo 2: se mantiene politica explicita de supuestos ante faltantes locales."
    ]
  }
}