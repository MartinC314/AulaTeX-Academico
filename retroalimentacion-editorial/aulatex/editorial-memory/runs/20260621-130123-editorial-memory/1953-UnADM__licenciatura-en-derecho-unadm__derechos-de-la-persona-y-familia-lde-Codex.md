{
  "summary": [
    "Sincronizacion transversal consolidada con compresion union-dedupe sin perdida.",
    "Se preserva ADN editorial UnADM y se evita traslado tematico entre materias no equivalentes.",
    "Se refuerzan ejes estables: problema, conceptos-normas, evidencia, analisis propio, conclusion juridica.",
    "Se mantiene gate critico: no propagar salidas no JSON parseable sin normalizacion.",
    "Se confirma contexto local destino: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Se mantiene correccion operativa pendiente de placeholders y rutas corruptas en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar nombre canonico de materia: Derechos de la persona y familia.",
    "Alinear entregas a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Mantener carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno y matricula sin verificacion local. [supuesto vigencia]"
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado en planeacion o rubrica."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto antes de redactar.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar transferir contenido doctrinal de Filosofia del Derecho sin prueba de pertinencia local. [supuesto]",
    "Registrar vacios de contexto en preguntas abiertas, no rellenarlos con inferencias."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar esquema minimo completo antes de guardar memoria.",
    "Exigir respaldo o marca [supuesto] en afirmaciones no verificadas.",
    "Verificar correspondencia entre consigna y producto entregable.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base local como punto de partida.",
    "Mantener spanish, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes del contenido.",
    "Actualizar documentsubtitle al numero real de actividad.",
    "Corregir nombres/rutas corruptas en README antes de compilar.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Conservar fuentes base institucionales existentes.",
    "Agregar solo fuentes verificables y pertinentes por actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar redaccion literal y contenido tematico dependiente de una actividad puntual.",
    "Aplicar estrategia conservadora: sumar mejoras verificables sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica vigentes de la actividad destino.",
    "Confirmar vigencia de datos de alumno/matricula en plantilla. [supuesto]",
    "Confirmar si codigo LDE-S3B1 es obligatorio en todos los productos.",
    "Validar correccion definitiva de placeholders de .bib en README y programa.",
    "Confirmar formato exigido por actividad: reporte, presentacion u otro."
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
        "Entrada canonica desde carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos con trazabilidad y rigor.",
      "Garantizar coherencia entre consigna, fundamento, analisis y cierre profesional."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte confirmacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma/doctrina/fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX/BibTeX",
        "Nucleo editorial de cinco ejes"
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
          "justification": "La identidad institucional fija tono, formato y exigencia academica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de soporte."
        },
        {
          "source": "Nucleo editorial de cinco ejes",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Define secuencia reusable para actividades distintas."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 5: se conserva gate de no propagar salidas no parseables.",
      "Ciclo 5: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 5: se mantiene separacion entre identidad editorial y contenido tematico de origen."
    ]
  }
}