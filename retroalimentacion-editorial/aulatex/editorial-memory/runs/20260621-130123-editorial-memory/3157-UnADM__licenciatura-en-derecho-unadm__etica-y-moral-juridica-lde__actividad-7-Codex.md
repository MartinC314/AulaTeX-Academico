{
  "summary": [
    "Se consolida transferencia lateral reutilizable desde Filosofia del Derecho hacia Etica y Moral juridica sin copiar contenido especifico.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales comunes con deduplicacion lossless.",
    "Se refuerza control de calidad: JSON parseable, esquema completo, supuestos marcados y trazabilidad de fuentes.",
    "Se mantiene regla de no propagar salidas no estructuradas sin normalizacion previa.",
    "Se agrega mejora verificable local: resolver tokens Slug sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar conclusiones tematicas de Filosofia del Derecho a Etica y Moral juridica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal de Actividad 7.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener estructura base cuando falte consigna detallada."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de otras semanas o materias sin validacion.",
    "Confirmar que el producto final corresponde a la consigna de Actividad 7.",
    "Diferenciar analisis etico-moral de simple resumen historico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Revisar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar propagacion recursiva solo despues de pasar todas las compuertas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para no romper compilaciones existentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir caracteres anomalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener deduplicacion lossless: no borrar duplicados BibTeX sin politica de alias validada [Supuesto]."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo reglas generales reutilizables.",
    "No copiar redaccion literal ni bibliografia exclusiva del nodo hermano.",
    "Si falta consigna local, propagar plantilla estructural y abrir preguntas.",
    "Mantener trazabilidad de ciclo y fuente provisional cuando aplique [Supuesto].",
    "Aplicar normalizacion manual en nodos con historial de salida no parseable."
  ],
  "open_questions": [
    "Confirmar consigna exacta y formato de entrega de Actividad 7.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar politica local de alias para claves BibTeX duplicadas.",
    "Confirmar si se normalizaran los errores de texto en README (lineas con caracteres truncados).",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 7."
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
        "Validacion estructural previa a propagacion."
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
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Sostener continuidad editorial entre actividades sin perder especificidad local.",
      "Proteger integridad estructural y trazabilidad en propagacion recursiva."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco.",
      "Contrastar con evidencia.",
      "Fijar postura del estudiante.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico-social",
        "Analisis propio",
        "Conclusion transferible",
        "Etica",
        "Moral"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico-social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte del problema planteado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar del analisis y evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es nucleo recurrente en la asignatura."
        }
      ],
      "evidence": [
        "README de la asignatura con ubicacion curricular verificable.",
        "Programa analitico con proposito y ejes de trabajo.",
        "Bibliografia local con duplicados observables en claves BibTeX."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerzan patrones transversales reutilizables sin traslado de contenido especifico.",
      "Ciclo 20: se conserva bloqueo por no-JSON y normalizacion obligatoria.",
      "Ciclo 20: se agrega mejora verificable de higiene editorial sobre tokens Slug sin expandir."
    ]
  }
}