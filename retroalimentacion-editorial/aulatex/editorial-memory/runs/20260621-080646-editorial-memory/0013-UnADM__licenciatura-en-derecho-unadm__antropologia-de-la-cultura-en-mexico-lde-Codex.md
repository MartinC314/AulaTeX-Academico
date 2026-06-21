{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura canonica y control de calidad.",
    "Se incorporan del origen solo abstracciones reutilizables: objetivo puntual, evidencia verificable, postura propia y coherencia entre pregunta, desarrollo y cierre.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se mantiene alerta por salidas no JSON parseable en historico y se exige normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar nombre oficial de materia: Antropologia de la cultura en Mexico.",
    "Usar clave LDE-S4B2 salvo instruccion institucional distinta.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias operativas.",
    "Resolver placeholders y tokens dinamicos en rutas y nombres antes de usar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica juridica.",
    "Evitar puentes forzados: conectar analisis cultural con implicaciones juridicas de forma explicita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Verificar consistencia entre metadatos del documento y malla curricular local.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local.",
    "Confirmar que no queden tokens sin resolver en README, programa, .tex y rutas."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename, documentsubject y universityname coherentes con la materia.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni caracteres anomalos en rutas."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes de cada actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia cuando se use archivo local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales, no redaccion literal.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Mantener compresion lossless por union-dedupe.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "No transferir metadatos curriculares especificos de una materia a otra."
  ],
  "open_questions": [
    "Supuesto: falta estandar unico de citacion para toda la licenciatura; confirmar formato oficial.",
    "Supuesto: confirmar si la conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave operativa local.",
    "Confirmar si hay rubrica transversal que exija extension o tipo de evidencia minima por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Mantener coherencia institucional y calidad tecnica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion.",
      "Pregunta guia -> desarrollo -> respuesta final coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "La reutilizacion segura requiere estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana validez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige honestidad y trazabilidad."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma ejes problema, conceptos, evidencia, analisis y cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Historico registra incidencias por salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se reforzo gate de JSON parseable como condicion de propagacion.",
      "Ciclo 13: se agrego objetivo puntual como patron transversal estable.",
      "Ciclo 13: se mantuvo regla de supuestos marcados para datos no visibles.",
      "Ciclo 13: se excluyeron contenidos tematicos exclusivos de Filosofia del Derecho.",
      "Ciclo 13: se preservo union-dedupe lossless sin eliminar reglas utiles."
    ]
  }
}