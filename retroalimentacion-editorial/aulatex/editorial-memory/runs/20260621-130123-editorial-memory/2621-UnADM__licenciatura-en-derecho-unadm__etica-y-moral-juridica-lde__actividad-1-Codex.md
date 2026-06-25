{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas institucionales, estructurales y de calidad reutilizables.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se mantiene enfoque editorial: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se corrige contingencia previa: si el origen tiene JSON parseable, ya no marcar ausencia total. [Supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar trazabilidad de consolidacion con ruta origen, destino y ciclo."
  ],
  "structure_rules": [
    "Responder y almacenar solo JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; unir y deduplicar.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear entregable al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar usar fuentes de semanas posteriores sin validacion de consigna.",
    "Confirmar que el producto final corresponde a Actividad 1.",
    "Integrar fundamento juridico, evidencia y transferencia profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin etiqueta [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar deduplicacion semantica sin perder reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar claves .bib duplicadas sin perder informacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Aplicar refuerzo lateral sin perder especificidad local del destino.",
    "Si faltan datos locales, dejar pregunta abierta en vez de inventar contenido.",
    "Conservar historial de contingencias de parseo como trazabilidad operativa."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar formato requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio canonico para fusion de claves bibliograficas duplicadas.",
    "Confirmar si existen fuentes obligatorias de semana no incorporadas al .bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo ante dilemas etico-juridicos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion JSON antes de propagacion.",
        "Trazabilidad de fuentes y consolidaciones."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar calidad editorial consistente entre actividades y asignaturas hermanas.",
      "Preservar memoria util sin recortes y con deduplicacion lossless."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados.",
      "Citas verificables con cierre juridico propio."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a la norma o doctrina.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Etica",
        "Moral"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "huerta2000etica",
        "ronquillo2018etica",
        "prieto2009favor"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe derivar de fuentes y razonamiento."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El desarrollo argumentativo parte del problema planteado."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Distincion transversal de la asignatura destino. [Supuesto]"
        }
      ],
      "evidence": [
        "README de la asignatura destino con pauta editorial e identidad institucional.",
        "Programa analitico con ejes de trabajo y proposito de realizacion.",
        "Archivo etica-y-moral-juridica.bib con fuentes locales y duplicados detectables.",
        "Memoria origen parseable con reglas estructurales y de calidad reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se integra refuerzo lateral verificable desde origen con deduplicacion semantica.",
      "Ciclo 18: se mantiene regla de bloqueo por JSON invalido.",
      "Ciclo 18: se preserva ADN argumentativo comun entre nodos de Derecho UnADM.",
      "Ciclo 18: no se transfieren conclusiones especificas ni bibliografia exclusiva del hermano."
    ]
  }
}