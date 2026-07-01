{
  "summary": [
    "Se refuerza sincronizacion transversal conservadora entre actividad y materia sin trasladar contenido doctrinal especifico.",
    "Se preserva compresion lossless por union-dedupe y sin regresion.",
    "Se mantiene gate critico: no propagar salidas no estructuradas o JSON no parseable.",
    "Se consolidan ejes estables reutilizables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se confirma alineacion curricular local del destino: semestre 6, bloque 1, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y programa analitico local.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Corregir tokens sin expandir en README/programa por slug literal derecho-administrativo-y-control. [supuesto]"
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Separar reglas editoriales generales de contenido sustantivo heredado de otras materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Detener propagacion ante respuesta no estructurada o campos criticos vacios.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla en español y formato letterpaper segun base local.",
    "Completar metadatos institucionales y academicos antes de compilar.",
    "Reemplazar Actividad X por numero y nombre real de actividad.",
    "Sustituir Figura docente: Nombre por definir por dato oficial antes de entrega.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre afirmaciones y referencias citadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni doctrina especifica sin verificacion local.",
    "Preservar reglas institucionales de calidad en niveles superiores y laterales.",
    "Aplicar normalizacion manual cuando la fuente heredada sea provisional."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la figura docente en plantilla .tex.",
    "Confirmar si existe formato de citacion obligatorio adicional en la materia.",
    "Confirmar si el año de consulta del sitio UnADM se mantiene en 2026. [supuesto]",
    "Confirmar convencion final para carpeta de referencias local.",
    "Confirmar correccion definitiva de artefactos de tokens y nombres corruptos en README/programa. [supuesto]"
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
        "Normalizacion estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho administrativo y control."
      ]
    },
    "essence": [
      "Resolver problemas juridicos con base conceptual y normativa.",
      "Demostrar analisis propio sustentado en evidencia.",
      "Entregar productos alineados a planeacion semanal.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial de entregables academicos en LaTeX.",
      "Asegurar coherencia entre identidad institucional, argumentacion y evidencia.",
      "Permitir propagacion segura de reglas reutilizables entre nodos."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones visibles y ordenadas.",
      "Marcado explicito de [supuesto] cuando falte evidencia.",
      "Cierre con criterio juridico transferible."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> interpretacion juridica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Planeacion semanal",
        "Control administrativo"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo."
        },
        {
          "source": "Planeacion semanal",
          "target": "Tipo de producto",
          "kind": "depends_on",
          "justification": "La consigna define formato de entrega."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio juridico se fundamenta en fuentes pertinentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento."
        }
      ],
      "evidence": [
        "README de materia y programa analitico local.",
        "Archivo derecho-administrativo-y-control.bib.",
        "Plantilla reporte-derecho-administrativo-y-control.tex.",
        "Regla institucional historica: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolida transferencia transversal de reglas estables sin mover doctrina especifica.",
      "Ciclo 2: se refuerza gate de parseo JSON y normalizacion previa como regla no negociable.",
      "Ciclo 2: se mantiene union-dedupe lossless con eliminacion de duplicados semanticos."
    ]
  }
}