{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se mantiene compresion lossless por union y deduplicacion, sin recorte de reglas utiles.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se preservan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene politica de supuestos para datos no visibles en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin copiar redaccion literal ni conclusiones especificas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o bibliografia de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guia oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizacion."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas y nombres de archivo solo con verificacion local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "No usar memoria editorial como bibliografia academica.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad de interpretacion juridica; confirmar aplicacion a actividad-3."
  ],
  "propagation_hints": [
    "Propagar en recursivo solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar conclusiones especificas ni bibliografia exclusiva entre hermanos.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Mantener bandera de riesgo cuando haya antecedente de salida no estructurada.",
    "Aplicar deduplicacion por union para evitar duplicados semanticos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar si actividad-3 usa bibliografia de Semana 7 o requiere bibliografia propia.",
    "Confirmar archivo .tex principal canonico para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con evidencia y cierre argumentativo.",
      "Garantizar consistencia institucional y trazabilidad de fuentes en cada actividad.",
      "Asegurar transferencia lateral sin contaminar con contenido especifico no verificable."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmaciones con cita verificable.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Politica de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Politica de supuestos",
          "kind": "supports",
          "justification": "La estructura valida facilita marcar incertidumbre sin perder trazabilidad."
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
          "justification": "La conclusion depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "Sin evidencia verificable no hay cierre juridico robusto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables, conclusion juridica propia.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Regla persistente: bloquear propagacion si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 7: reforzada regla de no transferir bibliografia exclusiva entre hermanos.",
      "Ciclo 7: mantenida normalizacion estructurada obligatoria para propagacion recursiva.",
      "Ciclo 7: preservada politica de supuestos ante falta de consigna local."
    ]
  }
}