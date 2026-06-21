{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable sin copiar contenido especifico entre hermanos.",
    "Se mantiene normalizacion estructurada y validacion JSON estricta como puerta obligatoria de propagacion.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se registran supuestos donde falta consigna local de Actividad 4."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineada con UnADM.",
    "Vincular siempre la entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Mantener integridad academica con postura propia sustentada."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto pedido por la planeacion semanal.",
    "Diferenciar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Evitar traslado literal de conclusiones o redaccion de Actividad 1.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: confirmar formato exacto de entrega de Actividad 4 antes de version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar aguas abajo.",
    "Validar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar toda respuesta no estructurada heredada.",
    "Confirmar correspondencia del producto con consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Verificar nombres reales de archivos del README antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) en rutas y nombres antes de cierre editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en .bib de asignatura o incremental validado.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a Semana 7; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables de identidad, estructura y calidad.",
    "Evitar copiar bibliografia exclusiva o conclusiones especificas entre nodos hermanos.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Preservar trazabilidad de supuestos y fuentes provisionales.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por placeholder Slug no resuelto en README.",
    "Confirmar si Actividad 4 usa .bib existente o requiere .bib incremental propio.",
    "Confirmar fuentes obligatorias de semana para no sobreextender bibliografia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica y citas verificables",
        "Entrada canonica en carpeta de asignatura"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos",
        "Asignatura Filosofia del Derecho"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y aplicabilidad profesional.",
      "Sostener continuidad editorial entre actividades sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales claras",
      "Citas trazables",
      "Supuestos etiquetados",
      "Cierre con criterio juridico propio"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Desarrollar conceptos y norma",
      "Contrastar evidencia",
      "Fijar postura razonada",
      "Concluir con transferencia profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica",
        "Consistencia cita-bibliografia"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal y precision juridica",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Validacion JSON estricta",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Hay antecedentes de salidas no parseables en ciclos previos."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de Actividad 4",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan problema, desarrollo y cierre."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere evidencia y analisis propio."
        }
      ],
      "evidence": [
        "README fija identidad, entrada canonica e integridad academica.",
        "Programa analitico define proposito y cinco ejes de trabajo.",
        "Malla curricular respalda ubicacion academica.",
        "Supuesto: consigna especifica de Actividad 4 no visible en contexto actual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: deduplicacion de reglas repetidas en destino sin recorte semantico.",
      "Ciclo 41: se preservan gates de JSON y estructura por riesgo historico de salida no parseable.",
      "Ciclo 41: se transfiere patron argumentativo reusable de Actividad 1 a Actividad 4 sin copiar contenido especifico.",
      "Ciclo 41: se mantiene tratamiento provisional de fuentes heredadas no verificadas."
    ]
  }
}