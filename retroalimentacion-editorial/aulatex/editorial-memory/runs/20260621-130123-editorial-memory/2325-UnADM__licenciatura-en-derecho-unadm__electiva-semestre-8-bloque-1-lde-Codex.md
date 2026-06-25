{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora entre nodos no equivalentes.",
    "Se preservan reglas institucionales, estructura reusable, calidad y trazabilidad sin traslado tematico literal.",
    "Se refuerza control de placeholders y nombres corruptos detectados en README y programa.",
    "Se mantiene normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Supuesto: el destino carece de consigna de actividad concreta; se mantiene cerebro editorial minimo de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Marcar como supuesto todo dato no visible o no confirmado localmente.",
    "No renombrar asignatura ni codigo provisional LDE-S8B1 sin confirmacion oficial.",
    "Mantener autor y matricula de plantilla mientras no exista instruccion institucional valida.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular cada producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizacion aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar correspondencia del producto con la consigna activa.",
    "Corregir placeholders y caracteres corruptos en rutas y nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte y presentacion de la materia.",
    "Conservar clase article en spanish y letterpaper oneside salvo instruccion local distinta.",
    "Mantener coherencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Completar campos pendientes de portada antes de entrega final.",
    "Usar codificacion compatible con español y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; incluir solo obras consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables: identidad, estructura, gates y grafo conceptual.",
    "No propagar metadatos especificos de materia a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Priorizar control de JSON parseable y trazabilidad de fuentes en saltos recursivos.",
    "Cuando falte consigna local, propagar reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura electiva y codigo definitivo.",
    "Confirmar figura docente para completar plantilla.",
    "Confirmar si existe consigna activa para fijar tipo de producto por actividad.",
    "Confirmar correccion definitiva de placeholders Slug en README y programa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Verificable y sobrio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Preservar identidad institucional y calidad editorial transversal.",
      "Evitar perdida de reglas utiles mediante deduplicacion sin recorte."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Supuestos etiquetados.",
      "Cierre juridico transferible."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
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
          "justification": "Define tono y formato minimo de productos."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay control confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "supports",
          "justification": "Reduce errores de rutas y nombres en artefactos."
        }
      ],
      "evidence": [
        "README del destino con placeholders Slug y nombres corruptos.",
        "Programa analitico con ejes editoriales estables.",
        "Archivo .bib local con fuentes institucionales base.",
        "Plantilla .tex con campos pendientes explicitos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 10: reforzadas reglas transversales de identidad, estructura, calidad y bibliografia.",
      "Ciclo 10: mantenida separacion entre abstracciones estables y contenido tematico local.",
      "Ciclo 10: persisten supuestos abiertos por falta de consigna especifica verificable."
    ]
  }
}