{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas utiles previas del destino y se agregan patrones reutilizables verificables del origen.",
    "Se refuerza el nucleo editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene obligatoria la normalizacion estructurada y JSON parseable antes de propagacion recursiva.",
    "Se corrige el supuesto previo de ausencia de reglas transferibles: si existen y son verificables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar trazabilidad de origen, destino y ciclo en cada consolidacion."
  ],
  "structure_rules": [
    "Responder y almacenar memoria solo en JSON valido y parseable.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresion lossless por union y deduplicacion, no por recorte.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas posteriores para Actividad 1.",
    "Confirmar que el producto final coincide con la consigna de Actividad 1.",
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
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar claves .bib duplicadas sin perder informacion bibliografica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre nodos laterales solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Conservar reglas institucionales de calidad sin reducir especificidad local.",
    "Si falta consigna textual local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Etica y Moral juridica.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio canonico para fusionar claves duplicadas en etica-y-moral-juridica.bib.",
    "Confirmar si existen fuentes obligatorias de semana no reflejadas en el .bib actual."
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
        "Carpeta de asignatura como entrada canonica.",
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
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad, calidad formal y consistencia editorial entre actividades."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados.",
      "Cierre juridico propio sustentado."
    ],
    "argumentative_patterns": [
      "Del problema al concepto.",
      "Del concepto a la norma o doctrina.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion juridica aplicable."
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada debe derivar de fuentes consultables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "El cierre profesional se construye desde el razonamiento del estudiante."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Eje transversal de la asignatura destino. [Supuesto]"
        }
      ],
      "evidence": [
        "README de la asignatura destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "etica-y-moral-juridica.bib: fuentes base y duplicados observables.",
        "Memoria origen: reglas estructurales, de calidad y trazabilidad transferibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se incorporan reglas transferibles verificables del origen sin copiar contenido especifico.",
      "Ciclo 17: se mantiene contingencia historica de parseo como control operativo, sin bloquear refuerzo editorial.",
      "Ciclo 17: se refuerza deduplicacion semantica y preservacion de reglas utiles previas."
    ]
  }
}