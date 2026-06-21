{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1 sin copiar contenido especifico.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales nucleares de la asignatura.",
    "Se mantiene regla de normalizacion estructurada y bloqueo de propagacion sin JSON parseable.",
    "Se refuerza deduplicacion lossless por union de reglas equivalentes sin recorte semantico.",
    "Se mantiene politica de supuestos para datos no visibles en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes provisionales, no como fuentes academicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna, usar estructura base y etiquetar [supuesto]."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad hermana sin eliminar reglas utiles previas.",
    "No copiar redaccion literal, conclusiones concretas ni bibliografia exclusiva del hermano.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Validar esquema minimo completo antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "Aplicar no-regresion: no borrar reglas utiles previas.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres solo con verificacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales pertinentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Registrar en .bib solo entradas efectivamente citadas por la actividad.",
    "Distinguir bibliografia base de asignatura y bibliografia especifica por actividad.",
    "[supuesto] filosofia-del-derecho-clean.bib parece orientado a Semana 7; confirmar aplicabilidad en actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables institucionales, estructurales y de calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando exista historial de parseo defectuoso.",
    "Aplicar union+dedupe lossless en cada ciclo para evitar duplicados sin perder reglas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar tipo de producto requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar archivo .tex principal canonico para actividad-3.",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug."
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar consistencia editorial y trazabilidad de fuentes en cada actividad.",
      "Sostener continuidad entre actividades sin contaminar con contenido no verificado."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Marcado explicito de [supuesto] cuando falte evidencia local.",
      "Cierre juridico aplicable a practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion juridica.",
      "Objetivo claro antes del desarrollo.",
      "Coherencia interna entre consigna, desarrollo y cierre.",
      "Evitar descripcion plana; privilegiar argumentacion sustentada."
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
          "justification": "El analisis se construye sobre un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y pauta editorial base.",
        "Programa analitico confirma ejes de trabajo y proposito de realizacion.",
        "Historial de ciclos confirma regla de bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 34: deduplicacion lossless aplicada sin regresion.",
      "Ciclo 34: se refuerzan reglas institucionales y de calidad transferibles entre hermanos.",
      "Ciclo 34: se preserva politica de supuestos y no invencion de fuentes.",
      "Ciclo 34: se mantiene separacion entre memoria editorial y evidencia academica."
    ]
  }
}