{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe y sin regresion.",
    "Se transfieren solo abstracciones estables desde actividad origen a materia destino.",
    "Se preserva identidad UnADM y encuadre curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se consolidan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferir redaccion literal o contenido tematico no equivalente entre nodos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como entrada canonica de decisiones editoriales.",
    "No mezclar identidades de otras carreras en entregables de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener estructura reusable para reporte y presentacion sin copiar redaccion literal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra semana o asignatura aplica automaticamente.",
    "Vincular cada actividad con el problema juridico o social que la activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local vigente."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos locales del curso: LDE-S7B2, semestre 7, bloque 2.",
    "Conservar portada academica completa cuando aplique.",
    "Usar article con spanish, letterpaper y oneside salvo instruccion contraria.",
    "No compilar con placeholders sin expandir tipo $(@{...}).",
    "Corregir nombres de archivos rotos en README y programa antes de referenciar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No trasladar bibliografia tematica de Filosofia del Derecho sin verificacion documental local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, estables y no duplicadas.",
    "Separar en propagacion transversal: identidad, estructura, calidad y grafo conceptual.",
    "Evitar transferir contenido tematico especifico entre nodos no equivalentes.",
    "Mantener bandera de normalizacion manual para ciclos con insumos no estructurados.",
    "Aplicar compresion lossless por deduplicacion, no por recorte.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para README y portada.",
    "Corregir placeholders pendientes en README y programa analitico.",
    "Confirmar si year 2026 en unadmSitioWeb se mantiene o migra a solo fecha de consulta.",
    "Confirmar figura docente en plantilla base.",
    "Supuesto: no hay consigna local detallada por actividad; validar formato requerido por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia transversal."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "Trazabilidad entre README, programa, plantillas y .bib."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en productos academicos claros, fundamentados y verificables.",
      "Sostener coherencia institucional y calidad tecnica en LaTeX y bibliografia.",
      "Permitir reutilizacion transversal segura sin contaminar contexto tematico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones trazables y reutilizables.",
      "Supuestos etiquetados cuando falte informacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalizacion estructurada",
        "alineacion con consigna",
        "evidencia verificable",
        "postura argumentada",
        "conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Define limites formales y curriculares del entregable."
        },
        {
          "source": "normalizacion estructurada",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Evita ruido y mejora trazabilidad de decisiones editoriales."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental explicito."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita cierre util para practica juridica."
        },
        {
          "source": "alineacion con consigna",
          "target": "conclusion transferible",
          "kind": "depends_on",
          "justification": "La utilidad practica depende de responder el encargo real."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM, semestre 7, bloque 2 y tipo electiva.",
        "Programa analitico local define ejes de problema, conceptos, producto, analisis y cierre.",
        "Archivo .bib local contiene base institucional verificable.",
        "Memoria origen aporta reglas estables de estructura, calidad y normalizacion parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se consolida transferencia transversal estable sin copiar contenido literal.",
      "Ciclo 20: se preservan reglas utiles previas del destino y del origen por union-dedupe.",
      "Ciclo 20: se refuerzan quality gates de JSON parseable y revision de supuestos.",
      "Ciclo 20: se mantiene estrategia progresiva y conservadora con foco en abstracciones editoriales."
    ]
  }
}