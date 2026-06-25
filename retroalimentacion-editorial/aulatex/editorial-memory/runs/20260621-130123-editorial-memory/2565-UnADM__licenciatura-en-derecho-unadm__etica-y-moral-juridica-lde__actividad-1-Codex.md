{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas institucionales, estructurales, de calidad y trazabilidad ya validas.",
    "Se refuerza el eje comun UnADM: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se elimina ruido de contingencia no vigente porque el origen actual si es JSON parseable.",
    "Se mantienen solo patrones reutilizables; no se copian conclusiones ni bibliografia exclusiva del origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Registrar ruta de origen y destino en cada consolidacion.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Responder y almacenar memoria solo en JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; unir y deduplicar.",
    "Aplicar compresion lossless por deduplicacion, no por recorte.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto final coincide con la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1.",
    "Integrar fundamento juridico, evidencia y transferencia profesional en cada producto."
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
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar claves bibliograficas duplicadas sin perder informacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Transferir solo patrones reutilizables; no copiar redaccion ni cierre tematico de otra asignatura.",
    "Si falta consigna textual local, propagar estructura base y abrir preguntas.",
    "Mantener bitacora de incidencias de parseo por ciclo solo cuando ocurran."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio canonico de deduplicacion para pares de claves .bib equivalentes.",
    "Confirmar si hay fuentes obligatorias de semana no reflejadas en etica-y-moral-juridica.bib."
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
      "Convertir planeacion semanal en entregables academicos rigurosos.",
      "Sostener continuidad editorial entre actividades y asignaturas afines.",
      "Garantizar trazabilidad, verificabilidad y calidad formal en LaTeX."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados.",
      "Cierre juridico con postura propia."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a norma o doctrina.",
      "De evidencia a analisis propio.",
      "Del analisis a conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Etica",
        "Moral",
        "Practica profesional juridica"
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
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada debe basarse en fuentes y no en opinion aislada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento del estudiante."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es transversal en la asignatura destino. [Supuesto]"
        }
      ],
      "evidence": [
        "README de la asignatura destino.",
        "Programa analitico editorial de Etica y Moral juridica.",
        "Archivo etica-y-moral-juridica.bib con claves duplicadas detectables.",
        "Memoria origen parseable con reglas institucionales y de calidad reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se reemplaza contingencia por consolidacion verificable desde origen parseable.",
      "Ciclo 4: se deduplican reglas repetidas y se preserva cobertura funcional completa.",
      "Ciclo 4: se refuerza transferencia lateral controlada sin copiar contenido tematico exclusivo."
    ]
  }
}