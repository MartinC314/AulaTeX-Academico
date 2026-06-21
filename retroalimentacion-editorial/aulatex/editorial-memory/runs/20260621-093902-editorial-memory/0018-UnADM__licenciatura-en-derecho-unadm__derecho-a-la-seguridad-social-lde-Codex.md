{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas utiles del destino y se incorporan abstracciones estables del origen.",
    "Se refuerza patron editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene separacion entre reglas generales transferibles y contenido tematico local de seguridad social.",
    "Se conserva control institucional: normalizacion obligatoria y bloqueo de propagacion sin JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin recorte.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de origen cuando una regla sea provisional [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; exigir argumentacion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar compresion lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y del curso consistentes en .tex.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivos con marcadores o tokens sin expandir antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "Agregar solo referencias realmente consultables y verificables.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir a laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico de filosofia al destino.",
    "Propagar reglas curriculares especificas solo dentro de la misma materia.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables en ciclos tempranos.",
    "Aplicar normalizacion manual cuando reaparezcan respuestas no estructuradas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue vigente en todos los artefactos [supuesto].",
    "Validar si se requiere plantilla diferenciada por tipo de actividad en semana 1 [supuesto].",
    "Confirmar dato oficial de figura docente para portada cuando exista.",
    "Revisar periodicamente vigencia de URLs normativas en el .bib local."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Producto juridico verificable.",
      "Problema delimitado.",
      "Fundamento normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables academicos solidos y trazables.",
      "Sostener coherencia institucional entre actividades, materia y suite.",
      "Permitir propagacion segura mediante reglas parseables y verificables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Presentar evidencia y contrastarla.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia requiere soporte objetivo."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless necesita estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Evita perdida de reglas nucleares del ADN editorial."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo verificables.",
        "derecho-a-la-seguridad-social.bib contiene base institucional y normativa vigente.",
        "Historial interno reporta salidas no parseables en ciclos tempranos; se mantiene gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion completa de reglas repetidas.",
      "Ciclo 18: transferidas solo abstracciones estables desde nodo transversal no equivalente.",
      "Ciclo 18: preservadas reglas locales de seguridad social sin mezclar contenido tematico de filosofia.",
      "Ciclo 18: reforzados gates de JSON parseable, evidencia verificable y marca [supuesto].",
      "Ciclo 18: mantenida compresion lossless por union-dedupe y politica sin regresion."
    ]
  }
}