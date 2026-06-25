{
  "summary": [
    "Sincronizacion transversal ciclo 4 aplicada con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM, estructura reusable y gates de calidad.",
    "Se transfieren solo abstracciones estables desde actividad no equivalente.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza normalizacion de placeholders y control de JSON parseable.",
    "Supuesto: destino sigue sin consigna tematica local por actividad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Mantener carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos o fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar programa analitico como guia de reporte, presentacion o producto visual."
  ],
  "activity_rules": [
    "Vincular el producto a un problema juridico delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes de otras semanas sin evidencia local.",
    "No transferir redaccion literal entre nodos no equivalentes.",
    "Aplicar solo patrones argumentativos y editoriales estables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizacion recursiva.",
    "Confirmar trazabilidad de cada afirmacion con cita o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Verificar correspondencia entre producto entregable y consigna local.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Evitar regresiones: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia.",
    "Usar codificacion en espanol con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa.",
    "Completar campos pendientes de portada antes de entrega.",
    "Mantener consistencia entre documenttitle, documentsubtitle, coursename y coursecode."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; solo fuentes consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar correspondencia entre citas en texto y entradas del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar metadatos particulares de actividad origen al destino materia.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Registrar supuestos abiertos cuando falte contexto local.",
    "Conservar antecedente institucional: salidas no estructuradas requieren normalizacion manual."
  ],
  "open_questions": [
    "Confirmar nombre oficial final de la electiva.",
    "Confirmar creditos oficiales para portada y README.",
    "Confirmar figura docente para plantilla.",
    "Confirmar si existe consigna local de actividades para reglas tematicas adicionales.",
    "Confirmar si el codigo LDE-S8B1 es definitivo o provisional.",
    "Supuesto: los placeholders detectados en README y programa aun requieren correccion final."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Supuestos etiquetados sin ambiguedad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio argumentado.",
      "Cierre juridico transferible.",
      "Trazabilidad y normalizacion editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar consistencia institucional y calidad formal en cada entrega.",
      "Permitir propagacion confiable de reglas editoriales entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables reutilizables.",
      "Postura propia sustentada.",
      "Supuestos marcados.",
      "Conclusion juridica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Descripcion breve -> posicion critica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y estandar minimo de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita contenido meramente descriptivo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay reutilizacion segura."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens sin expandir y rutas corruptas."
        }
      ],
      "evidence": [
        "README local muestra placeholders Slug sin expandir.",
        "Programa analitico conserva ejes editoriales estables reutilizables.",
        ".bib local contiene claves institucionales activas.",
        "Antecedente institucional de salida no parseable exige gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 4: reforzados gates de JSON parseable y trazabilidad de supuestos.",
      "Ciclo 4: transferidas abstracciones estables; excluido contenido tematico no verificable del origen."
    ]
  }
}