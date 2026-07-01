{
  "summary": [
    "Se sincroniza memoria transversal con reglas editoriales estables y verificadas para Garantias constitucionales.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza normalizacion estructurada y compresion lossless por union-dedupe sin regresion.",
    "Se mantiene separacion entre control editorial transferible y contenido disciplinar no equivalente.",
    "Se crea cerebro editorial minimo en ADN con foco en estructura, calidad y trazabilidad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar contenido disciplinar de Filosofia del Derecho sin validacion expresa en Garantias constitucionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear el producto a la planeacion semanal y a la consigna de actividad.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir conceptos, normas, doctrina, datos y postura personal.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Completar campos de plantilla antes de entrega: actividad, figura docente y fecha.",
    "Corregir truncamientos y placeholders en README, programa analitico y portada LaTeX.",
    "Verificar cierre completo de macros de portada antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar entradas base locales: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales validadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de nodos no equivalentes.",
    "Mantener alerta institucional de riesgo cuando exista herencia no estructurada.",
    "Si falta contexto local en nodos hijos, inicializar cerebro editorial minimo y abrir vacios."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades locales de Garantias constitucionales.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar formato de citacion exigido en la materia destino.",
    "Confirmar y reparar truncamiento detectado en reporte-garantias-constitucionales.tex.",
    "Confirmar reemplazo de tokens $(@{...}.Slug) en README y programa analitico."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Asegurar trazabilidad editorial entre consigna, fuentes, argumento y cierre."
    ],
    "style_markers": [
      "Explicitar objetivo al inicio.",
      "Mantener secciones funcionales y consistentes.",
      "Marcar supuestos de forma visible.",
      "Evitar afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia/cita -> interpretacion -> implicacion juridica.",
      "Consigna -> desarrollo alineado -> verificacion de cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "JSON parseable",
        "Compresion union-dedupe",
        "Bibliografia verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema activa el razonamiento y la postura argumentada."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre depende del sustento normativo y doctrinal."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin formato valido no hay transferencia segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin recorte ni duplicados."
        }
      ],
      "evidence": [
        "README de Garantias constitucionales: pauta editorial y ubicacion curricular.",
        "Programa analitico: ejes de trabajo y proposito editorial.",
        "garantias-constitucionales.bib: base institucional local.",
        "Regla institucional heredada: bloquear si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se preservaron todas las utiles.",
      "Se reforzaron quality gates como nucleo transversal entre nodos no equivalentes.",
      "Se aislo contenido disciplinar de Filosofia del Derecho para evitar contaminacion tematica.",
      "Se consolido ADN editorial minimo del destino con foco en estructura reusable y trazabilidad.",
      "Se mantienen supuestos abiertos donde falta consigna local verificable."
    ]
  }
}