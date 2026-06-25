{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas institucionales, estructurales, de calidad y argumentacion reutilizables.",
    "Se mantiene normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar conclusiones especificas y bibliografia exclusiva del nodo origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar trazabilidad de consolidacion con origen, destino y ciclo."
  ],
  "structure_rules": [
    "Responder y guardar memoria en JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto final coincide con la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1.",
    "Integrar fundamento juridico, evidencia y transferencia profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin etiqueta [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar deduplicacion semantica sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Registrar fuentes especificas por actividad en etica-y-moral-juridica.bib.",
    "Distinguir bibliografia base y bibliografia especifica de actividad.",
    "Deduplicar claves .bib duplicadas sin perder informacion bibliografica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal del hermano.",
    "Aplicar analogia controlada: conservar forma argumentativa y ajustar contenido local.",
    "Mantener reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio canonico para fusionar claves BibTeX duplicadas locales.",
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
        "Normalizacion JSON obligatoria antes de propagacion.",
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
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Mantener coherencia entre identidad institucional, calidad formal y utilidad profesional."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados como [Supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a la norma o doctrina.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion aplicable."
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe derivar de fuentes y razonamiento."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Eje transversal de la asignatura destino. [Supuesto]"
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La argumentacion parte del problema y culmina en postura."
        }
      ],
      "evidence": [
        "README de la asignatura destino.",
        "Programa analitico de la asignatura destino.",
        "Archivo etica-y-moral-juridica.bib con duplicados verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se transfieren patrones generales del origen sin copiar contenido especifico.",
      "Ciclo 22: se refuerza compresion lossless por union y deduplicacion.",
      "Ciclo 22: se mantiene bloqueo de propagacion ante JSON invalido."
    ]
  }
}