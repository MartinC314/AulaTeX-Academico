{
  "summary": [
    "Se consolida refuerzo lateral de actividad-1 a actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se mantiene regla critica: no propagar sin JSON parseable y estructura minima completa.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, analisis propio, conclusion juridica transferible.",
    "Se mantiene politica de supuestos para datos no visibles en consigna local.",
    "Se conserva distincion entre memoria editorial provisional y evidencia academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas del nodo hermano sin copiar redaccion literal ni conclusiones especificas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guia oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Distinguir fuentes academicas, normativas, jurisprudenciales y antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar al .bib solo entradas efectivamente citadas en actividad-3.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad de Semana 7 y su uso en actividad-3 es condicionado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Propagar a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener compresion por union y deduplicacion lossless.",
    "Conservar bandera de riesgo si reaparece salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 usa bibliografia propia o reutiliza .bib existente.",
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable.",
      "Asegurar fundamento juridico, evidencia y transferencia profesional.",
      "Sostener memoria editorial persistente sin regresiones."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas con orden logico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falta evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
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
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion editorial confiable."
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
        "README confirma identidad UnADM, integridad academica y cierre juridico propio.",
        "Programa analitico define ejes problema-conceptos-fuentes-analisis-conclusion.",
        "Regla persistente valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 37: deduplicacion completa de reglas repetidas por variantes ortograficas.",
      "Ciclo 37: conservadas reglas utiles previas sin eliminacion.",
      "Ciclo 37: reforzada separacion entre evidencia academica y memoria editorial provisional.",
      "Ciclo 37: mantenida transferencia lateral por analogia controlada sin copiar contenido especifico del hermano."
    ]
  }
}