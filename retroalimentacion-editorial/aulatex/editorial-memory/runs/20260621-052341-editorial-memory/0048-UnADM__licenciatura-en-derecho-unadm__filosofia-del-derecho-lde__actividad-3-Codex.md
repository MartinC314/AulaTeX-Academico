{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1 sin copiar contenido especifico.",
    "Se preserva identidad UnADM y contexto curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza normalizacion estructurada obligatoria y bloqueo de propagacion sin JSON parseable.",
    "Se mantienen ejes editoriales estables: problema, conceptos y fuentes, analisis propio, conclusion juridica transferible.",
    "Se conserva politica de supuestos para datos no visibles en consigna local.",
    "Se mantiene deduplicacion lossless y no regresion de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear toda entrega con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Respetar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedentes provisionales, no como fuentes academicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Alinear estructura al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables desde actividad hermana.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva de otra actividad.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar regla de no regresion: no eliminar reglas utiles previas.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves usadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas y nombres anomalo solo con verificacion local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni citas.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar al .bib solo referencias realmente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica; validar aplicacion en actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales y patrones estables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar union-deduplicacion lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando haya antecedente de parseo fallido.",
    "Reforzar conexiones entre identidad institucional, calidad y patron argumentativo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar bibliografia obligatoria de actividad-3.",
    "Confirmar si aplica bibliografia depurada de Semana 7 a actividad-3.",
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Disciplina editorial verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico valido.",
      "Asegurar fundamento juridico, evidencia y criterio propio.",
      "Garantizar consistencia institucional y tecnica en LaTeX."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones clave.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
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
          "justification": "La pauta institucional exige citas verificables y forma academica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad editorial confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis surge de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura requiere respaldo documental comprobable."
        },
        {
          "source": "Supuestos controlados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Etiquetar incertidumbre evita afirmar datos no verificados."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Contexto local: token Slug sin expandir detectado en README/programa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 48: consolidacion lateral sin perdida por deduplicacion.",
      "Se preservaron reglas institucionales, estructurales, de calidad, LaTeX y bibliografia.",
      "Se excluyo transferencia de conclusiones especificas y bibliografia exclusiva entre hermanos.",
      "Se reforzo control de supuestos por ausencia de consigna local de actividad-3.",
      "Se mantuvo no regresion y propagacion recursiva condicionada a parseo valido."
    ]
  }
}