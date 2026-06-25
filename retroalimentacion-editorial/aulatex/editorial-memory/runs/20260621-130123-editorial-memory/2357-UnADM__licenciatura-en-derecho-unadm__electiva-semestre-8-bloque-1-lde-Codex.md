{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se evita traslado de contenido tematico especifico por no equivalencia de nodos.",
    "Se refuerza normalizacion obligatoria de salidas JSON parseables antes de propagacion.",
    "Se mantiene enfoque conservador con supuestos marcados y vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono formal academico, claro y juridicamente preciso.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes de otras semanas o materias sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Corregir placeholders y literales corruptos en README y programa antes de entrega.",
    "Confirmar existencia de rutas y archivos citados antes de usarlos como fuente."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reporte y presentacion.",
    "Usar codificacion compatible con espanol y acentos correctos.",
    "Mantener consistencia entre documenttitle, documentsubtitle, coursename y coursecode.",
    "Completar campos pendientes de portada antes de entrega final.",
    "Evitar tokens sin expandir tipo $(@{...}.Slug) en archivos finales.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local de materia.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni metadatos especificos de actividad origen.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Si falta consigna local, mantener cerebro editorial minimo y abrir pendientes."
  ],
  "open_questions": [
    "[Supuesto] Creditos oficiales de la electiva no visibles en README.",
    "[Supuesto] Nombre oficial definitivo de la electiva pendiente de confirmacion.",
    "[Supuesto] Figura docente en portada sigue sin nombre confirmado.",
    "Confirmar si todas las actividades de la materia usan mismo .bib o .bib por actividad.",
    "Confirmar si presentacion comparte exactamente los mismos metadatos de portada."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Verificable y sobrio",
        "Conservador ante datos no confirmados"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de materia como entrada canonica",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y fuentes pertinentes",
      "Producto alineado a planeacion",
      "Analisis propio argumentado",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos claros, verificables y utiles para practica juridica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Cierre juridico aplicable",
      "Supuestos visibles cuando falte evidencia"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia verificable -> inferencia juridica",
      "Descripcion breve -> posicion critica -> implicacion practica"
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
          "justification": "Define tono, formato y criterios de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con respaldo verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Permite propagacion confiable sin perdida estructural."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "develops",
          "justification": "Reduce errores tecnicos y mejora consistencia documental."
        }
      ],
      "evidence": [
        "README del destino muestra tokens Slug sin expandir.",
        "Programa analitico del destino confirma ejes editoriales estables.",
        "Bib local contiene fuentes institucionales base verificables.",
        "Plantilla LaTeX del destino incluye campos pendientes en portada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se consolida transferencia transversal conservadora sin mover contenido tematico especifico.",
      "Ciclo 18: se refuerza gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 18: se mantiene union-dedupe lossless y sin eliminacion de reglas utiles previas."
    ]
  }
}