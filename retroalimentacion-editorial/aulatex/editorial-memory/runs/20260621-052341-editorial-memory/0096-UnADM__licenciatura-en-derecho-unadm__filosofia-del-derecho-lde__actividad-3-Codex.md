{
  "summary": [
    "Se refuerza memoria lateral de actividad-3 con patrones reutilizables de actividad-1.",
    "Se conserva identidad UnADM y contexto curricular validado en README y programa analitico.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se aplica deduplicacion lossless sin eliminar reglas utiles previas.",
    "Se corrige lectura de rutas con tokens y caracteres anommalos del README como incidencia tecnica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin copiar redaccion literal.",
    "No transferir conclusiones especificas ni bibliografia exclusiva del nodo hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Verificar esquema completo antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "Exigir marca de supuesto en datos no verificados.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar renombrar claves bibliograficas sin migracion total.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anommalas del README antes de automatizar referencias. [supuesto]"
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Registrar en .bib solo entradas realmente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a actividad-3 sin confirmacion. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando exista antecedente de parseo fallido.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Escalar incidencias tecnicas de tokens/rutas al nodo de asignatura."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 usa filosofia-del-derecho.bib o requiere .bib dedicado.",
    "Confirmar si bibliografia depurada de Semana 7 aplica o no en actividad-3."
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
      "Evidencia verificable con cita.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico util y verificable.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y forma de entrega."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Afirmaciones con respaldo.",
      "Supuestos marcados.",
      "Cierre juridico aplicable."
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
          "justification": "La pauta institucional exige rigor de citas y formato."
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
          "justification": "El analisis surge de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Incidencia local: tokens Slug sin expandir en archivos de contexto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas en identidad, estructura, calidad y LaTeX.",
      "Se preservaron reglas utiles previas sin recorte semantico.",
      "Se agrego control explicito para tokens sin expandir del README/programa.",
      "Se mantuvo separacion entre evidencia academica y memoria editorial provisional.",
      "Se reforzo transferencia lateral por patrones, no por contenido especifico."
    ]
  }
}