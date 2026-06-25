{
  "summary": [
    "Se realiza refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con transferencia de patrones reutilizables.",
    "Se preservan reglas utiles previas del destino y se deduplican sin recorte semantico.",
    "Se consolida ADN comun UnADM: identidad institucional, estructura argumentativa y control de calidad.",
    "Se mantiene bloqueo de propagacion para salidas no parseables y validacion de esquema completo.",
    "Se refuerza trazabilidad de supuestos y fuentes provisionales cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de fuente cuando un ciclo previo no sea parseable."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Integrar evidencia verificable dentro del desarrollo, no solo al final.",
    "Alinear el tipo de producto a la planeacion semanal de Actividad 7.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar afirmaciones sin respaldo documental.",
    "Evitar asumir fuentes de otras semanas o materias sin validacion.",
    "Confirmar que el producto final corresponde a la consigna de Actividad 7."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar propagacion recursiva solo si pasan todas las compuertas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener deduplicacion lossless de entradas equivalentes con politica de alias. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables, no conclusiones ni bibliografia exclusiva del nodo hermano.",
    "Mantener normalizacion manual para ciclos historicos no parseables.",
    "Evitar regresiones: toda regla util previa se conserva.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas.",
    "Registrar en bitacora cada refuerzo lateral aplicado en ciclo 11."
  ],
  "open_questions": [
    "Confirmar consigna exacta y formato requerido en Actividad 7.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana para Actividad 7.",
    "Confirmar politica final de alias BibTeX para claves duplicadas existentes.",
    "Confirmar si el .bib local truncado debe repararse antes de nuevas propagaciones. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 7."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar coherencia entre consigna, desarrollo y cierre.",
      "Preservar identidad institucional y trazabilidad editorial en cada ciclo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados cuando aplique.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y norma aplicable.",
      "Contrastar posturas con evidencia.",
      "Fijar postura propia fundamentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica profesional juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de etica-y-moral-juridica-lde",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento del estudiante parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva del analisis y evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual estructura la argumentacion de la asignatura."
        },
        {
          "source": "Moral",
          "target": "Practica profesional juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral orienta criterios de actuacion profesional."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local confirma ejes: problema, conceptos, producto, analisis, conclusion.",
        "Memoria origen aporta patron transversal de estructura argumentativa y control de supuestos.",
        "Memoria destino valida compuertas de calidad JSON y consistencia .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerza patron transversal de cinco ejes editoriales.",
      "Ciclo 11: se conserva regla dura de bloqueo por JSON no parseable.",
      "Ciclo 11: se integra control explicito de [Supuesto] para datos faltantes.",
      "Ciclo 11: se mantiene compatibilidad LaTeX y normalizacion de tokens Slug.",
      "Ciclo 11: no se transfieren conclusiones especificas ni bibliografia exclusiva de Filosofia del Derecho."
    ]
  }
}