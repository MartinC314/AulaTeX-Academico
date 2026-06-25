{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas institucionales, estructurales y de calidad ya vigentes en destino.",
    "Se agregan mejoras verificables del origen: normalizacion obligatoria, ejes editoriales y control de supuestos.",
    "Se evita transferencia de contenido especifico no reutilizable de la asignatura hermana.",
    "Se mantiene trazabilidad de incidencias de parseo y fuentes provisionales por ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar origen, destino y ciclo en cada consolidacion."
  ],
  "structure_rules": [
    "Responder y guardar memoria solo en JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "No eliminar reglas utiles previas.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas posteriores para Actividad 1.",
    "Confirmar correspondencia exacta entre producto final y consigna local.",
    "Integrar problema, conceptos, evidencia y analisis propio en cada entrega."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin etiqueta [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar deduplicacion semantica sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar claves duplicadas en .bib sin perder informacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva del nodo hermano.",
    "Cuando falten datos locales, conservar estructura base y abrir preguntas.",
    "Mantener registro de ciclos con incidencias de normalizacion manual."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar formato requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar si existe fuente obligatoria de semana no cargada en el .bib.",
    "Definir criterio canonico final para fusionar claves bib duplicadas."
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
        "Normalizacion JSON antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etica y Moral juridica."
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
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Preservar coherencia institucional y trazabilidad editorial entre nodos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos etiquetados.",
      "Secciones explicitas.",
      "Cierre juridico transferible."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a la norma o doctrina.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion juridica."
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
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis argumentado requiere sustento documental."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento del estudiante."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Eje transversal tipico de la asignatura destino. [Supuesto]"
        }
      ],
      "evidence": [
        "README de la asignatura destino.",
        "Programa analitico de Etica y Moral juridica.",
        "Archivo etica-y-moral-juridica.bib con duplicados verificables.",
        "Memoria origen con reglas institucionales y de calidad consolidadas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se transfieren patrones reutilizables sin arrastrar contenido especifico de Filosofia del Derecho.",
      "Ciclo 11: se refuerza gate de JSON parseable y normalizacion previa obligatoria.",
      "Ciclo 11: se consolida eje editorial comun problema-conceptos-evidencia-analisis-conclusion.",
      "Ciclo 11: se mantiene deduplicacion bibliografica como regla operativa local."
    ]
  }
}