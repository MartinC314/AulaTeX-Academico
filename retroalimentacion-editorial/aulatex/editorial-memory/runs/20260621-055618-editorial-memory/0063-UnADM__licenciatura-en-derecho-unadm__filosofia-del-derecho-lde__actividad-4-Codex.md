{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de la asignatura.",
    "Se mantiene regla critica de normalizacion estructurada y JSON parseable antes de propagar.",
    "Se transfieren patrones reutilizables de estructura, calidad y argumentacion sin copiar contenido especifico del hermano origen.",
    "Supuesto: la consigna puntual de Actividad 4 no esta visible; se conserva plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal academico, claro y juridicamente preciso.",
    "Alinear toda entrega con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna real de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica; verificar pertinencia para Actividad 4.",
    "Agregar en el .bib canonico solo fuentes realmente usadas por la actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales reutilizables.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe sin recortar contenido valido.",
    "Si falta consigna local, propagar estructura base y abrir preguntas.",
    "Mantener bandera de normalizacion manual en ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica de Actividad 4.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere bloque nuevo.",
    "Confirmar si los archivos listados con caracteres danados en README tienen nombre corregido."
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
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con postura.",
      "Cierre juridico aplicable.",
      "Trazabilidad editorial verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables argumentativos con rigor juridico.",
      "Asegurar consistencia institucional entre actividades hermanas.",
      "Sostener calidad tecnica de LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y limpias.",
      "Cita explicita en afirmaciones clave.",
      "Supuestos etiquetados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia.",
      "Fijar postura propia.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden argumentativo reutilizable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida depende de evidencia verificable."
        }
      ],
      "evidence": [
        "Pauta editorial del README.",
        "Ejes de trabajo del programa analitico.",
        "Antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 63: deduplicacion de reglas repetidas en identidad, estructura, calidad y LaTeX.",
      "Ciclo 63: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 63: se evita traslado de contenido especifico de Actividad 1 y solo se transfieren patrones.",
      "Ciclo 63: se preservan supuestos abiertos por falta de consigna local completa."
    ]
  }
}