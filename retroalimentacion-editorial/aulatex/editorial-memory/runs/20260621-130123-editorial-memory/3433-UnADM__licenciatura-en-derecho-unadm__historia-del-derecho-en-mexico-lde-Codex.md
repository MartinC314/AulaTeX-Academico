{
  "summary": [
    "Se consolida cerebro editorial minimo y estable para materia destino.",
    "Se preserva identidad UnADM y marco curricular local verificado.",
    "Se transfiere del origen solo abstraccion reusable: cinco ejes y control de calidad.",
    "Se mantiene regla de normalizacion previa ante salidas no JSON parseables.",
    "Se refuerza sincronizacion transversal sin copiar contenido tematico de Filosofia del Derecho.",
    "Se marca como supuesto toda inferencia no visible en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Historia del Derecho en Mexico [supuesto: acentuacion pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre el formato al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar conceptos y fuentes pertinentes al problema planteado.",
    "No mezclar contenido de otras materias sin evidencia local verificable.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del esquema editorial.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte y presentacion como base editable.",
    "Conservar metadatos: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener campos institucionales y tabla de autor; actualizar solo valores de actividad.",
    "Corregir placeholders tipo $(@{...}.Slug) antes de compilar o citar rutas.",
    "Usar codificacion y acentos consistentes en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio canonico local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Registrar trazabilidad con origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas estables de identidad, estructura y calidad.",
    "No propagar datos curriculares especificos de esta materia a otras materias.",
    "Reutilizar patron de cinco ejes con ajuste tematico por asignatura.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Mantener alerta historica de salidas no parseables en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar acentuacion institucional oficial de Mexico/Mexico en nombre de materia.",
    "Confirmar codigo de curso oficial vs codigo local LDE-S1B1.",
    "Definir nombre oficial de figura docente para plantillas.",
    "Corregir definitivamente errores de render en README (eporte/eferencias) [supuesto].",
    "Confirmar si existe rubrica transversal especifica para esta materia."
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
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar fundamento juridico, evidencia y analisis propio en cada entrega.",
      "Sostener continuidad editorial transversal sin contaminar contexto local."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Desarrollar conceptos y marco normativo relevante.",
      "Contrastar evidencia y postura propia.",
      "Concluir con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto"
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
          "justification": "La identidad exige citas verificables y formato institucional."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de metadatos y fuentes consultables."
        }
      ],
      "evidence": [
        "README de materia: identidad, estructura y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida funcional.",
      "Se incorporo abstraccion transversal del origen: cinco ejes + gates de calidad.",
      "Se evitaron transferencias literales de contenido tematico no equivalente.",
      "Se reforzo control de supuestos y no invencion de fuentes.",
      "Se dejo base minima robusta para ciclos siguientes."
    ]
  }
}