{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde Actividad 1 de Filosofia del Derecho hacia la materia Historia del Derecho en Mexico.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y control de calidad JSON.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos.",
    "Se refuerza cerebro editorial minimo del destino con deduplicacion lossless y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico [supuesto: acentuacion pendiente de validacion institucional].",
    "Conservar marco curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Aplicar los cinco ejes editoriales en cada entrega."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No asumir fuentes o instrucciones de semanas distintas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa del esquema editorial antes de propagar.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantillas locales de reporte o presentacion segun consigna.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir placeholders o tokens de Slug sin expandir antes de compilar o automatizar.",
    "Verificar nombres de archivo del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Evitar arrastrar bibliografia tematica de otras materias sin consulta efectiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar datos curriculares especificos de esta materia a materias laterales.",
    "Mantener alerta historica de salidas no parseables en niveles superiores.",
    "Si falta consigna local, propagar solo reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial del nombre de materia: Mexico o México.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo interno de plantilla.",
    "Definir figura docente oficial para plantillas.",
    "Confirmar fuente operativa definitiva para reemplazar referencias provisionales a motores.",
    "Corregir definitivamente errores de render en README (eporte, eferencias) [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Validacion estructural previa a toda propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes y verificables.",
      "Preservar identidad institucional y calidad argumentativa en cada actividad.",
      "Habilitar reutilizacion segura de reglas editoriales entre nodos."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Citas explicitas.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema y objetivo al inicio.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado en evidencia.",
      "Conclusion practica y juridicamente aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto"
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
          "justification": "La identidad institucional exige verificabilidad y forma academica."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan objetivo, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La integridad depende de fuentes consultables y metadatos minimos."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "No transferencia tematica literal",
          "kind": "contrasts",
          "justification": "Se comparten patrones editoriales, no contenido doctrinal de otra materia."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local con cinco ejes.",
        "Archivo .bib local con fuentes institucionales.",
        "Historial de salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerza union-dedupe sin regresion.",
      "Ciclo 20: se transfiere solo abstraccion estable desde nodo actividad transversal.",
      "Ciclo 20: se mantiene gate duro de JSON parseable.",
      "Ciclo 20: se preserva regla de marcar supuestos y no inventar fuentes."
    ]
  }
}