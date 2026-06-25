{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1 con enfoque conservador.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa reusable y control de calidad estricto.",
    "Se deduplican reglas sin perdida y sin trasladar contenido tematico no verificable entre nodos no equivalentes.",
    "Se refuerza la normalizacion de placeholders y literales corruptos detectados en README y programa analitico del destino.",
    "Se consolida un cerebro editorial minimo de materia con vacios locales marcados como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de entrega final.",
    "Verificar existencia de rutas locales citadas como fuente."
  ],
  "latex_rules": [
    "Mantener plantilla base LaTeX de la materia y su clase actual.",
    "Usar codificacion compatible con espanol y acentos correctos en .tex y .bib.",
    "Mantener consistentes documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Completar campos pendientes de portada antes de entrega.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin caracteres anomalos en rutas.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; incluir solo fuentes consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables: identidad, estructura, calidad y metodo de citas.",
    "Evitar propagar metadatos o redaccion literal especifica entre nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para prevenir regresiones.",
    "Registrar ciclo 1 como normalizacion manual reutilizable cuando falte consigna local.",
    "Priorizar grafo conceptual metodologico sobre contenidos tematicos de una sola actividad."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen vacios; confirmar en fuente institucional.",
    "Supuesto: figura docente aun no confirmada para portada.",
    "Confirmar nombre oficial definitivo de la asignatura y codigo de curso.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Confirmar correccion final de nombres corruptos en README (reporte y referencias).",
    "Confirmar si hay rubrica especifica de evaluacion para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de materia como entrada canonica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8 bloque 1 electiva",
        "Producto academico orientado a transferencia profesional"
      ]
    },
    "essence": [
      "Problema delimitado",
      "Conceptos y fuentes pertinentes",
      "Analisis propio",
      "Conclusion juridica aplicable",
      "Normalizacion estructurada antes de propagar"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables y utiles para practica juridica.",
      "Sostener continuidad editorial entre actividades y materia sin perder trazabilidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables y reutilizables",
      "Postura propia sustentada",
      "Supuestos etiquetados",
      "Cierre juridico transferible"
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
          "justification": "Define tono, formato y criterios minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Calidad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias inventadas."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens sin expandir y rutas corruptas."
        }
      ],
      "evidence": [
        "README del destino con placeholders Slug sin expandir y nombres corruptos.",
        "Programa analitico del destino con ejes editoriales estables y reutilizables.",
        "Archivo .bib local con claves institucionales ya definidas."
      ]
    },
    "reinforcement_log": [
      "Se conservaron reglas utiles previas sin eliminacion.",
      "Se deduplicaron variantes semanticas repetidas.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se evitaron fuentes inventadas y contenido tematico no verificable.",
      "Se reforzo gate de JSON parseable como condicion de propagacion."
    ]
  }
}