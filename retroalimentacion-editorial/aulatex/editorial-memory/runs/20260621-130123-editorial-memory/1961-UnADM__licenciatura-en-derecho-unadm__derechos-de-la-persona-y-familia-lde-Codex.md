{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin perdida.",
    "Se preserva ADN UnADM y se transfieren solo abstracciones estables no tematicas.",
    "Se refuerza gate critico: no propagar salidas no estructuradas sin normalizacion previa.",
    "Se mantiene nucleo reusable: problema, conceptos-normas, evidencia, analisis propio, conclusion juridica.",
    "Se conserva contexto curricular local del destino y no se altera con datos del origen.",
    "Se consolida correccion de placeholders y rutas corruptas como requisito operativo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, formato y metadatos.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Conservar marco curricular local: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno, matricula o figura docente sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear desarrollo con consigna, rubrica y producto solicitado.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad explicita entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "No transferir contenido tematico de Filosofia del Derecho sin pertinencia validada. [supuesto]",
    "Registrar vacios de consigna en preguntas abiertas antes de propagar reglas dependientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de guardar.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Exigir respaldo verificable o marca [supuesto] en cada afirmacion no confirmada.",
    "Verificar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol, letterpaper y oneside salvo consigna distinta.",
    "Usar plantilla local de reporte/presentacion como base canonica.",
    "Corregir placeholders de slug en README y programa analitico antes de reutilizar.",
    "Corregir nombres de archivo corruptos en README antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Conservar y reutilizar entradas institucionales base ya verificables.",
    "Agregar solo fuentes consultables y pertinentes a cada actividad.",
    "No inventar referencias; declarar faltantes como pendiente.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras pasar quality gates.",
    "Transferir solo reglas estables de identidad, estructura y calidad entre nodos no equivalentes.",
    "Evitar arrastre literal de redaccion o contenidos disciplinares del origen.",
    "Mantener compresion lossless por union-dedupe y sin regresion.",
    "Si reaparece salida no parseable, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consignas y rubricas vigentes de actividades de la materia destino.",
    "Confirmar vigencia de datos de autor en plantilla local. [supuesto]",
    "Confirmar sustitucion definitiva de placeholders de .bib en README y programa analitico.",
    "Confirmar si el codigo LDE-S3B1 debe figurar en todos los entregables.",
    "Confirmar formato obligatorio por actividad: reporte, presentacion u otro."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y trazabilidad.",
      "Sostener consistencia editorial, tecnica y bibliografica en toda la materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte verificacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma/doctrina/fuente.",
      "Analizar con criterio propio.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX-BibTeX",
        "Producto alineado a consigna"
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
          "justification": "El marco institucional define tono y forma del argumento."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Producto alineado a consigna",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Consistencia LaTeX-BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y mantiene trazabilidad."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El analisis y la conclusion requieren respaldo verificable."
        },
        {
          "source": "Producto alineado a consigna",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La forma final depende del tipo de entrega solicitado."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local del destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla heredada estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 7: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 7: se preservan gates institucionales y se evita arrastre tematico del origen.",
      "Ciclo 7: se mantiene base minima robusta para propagacion recursiva."
    ]
  }
}