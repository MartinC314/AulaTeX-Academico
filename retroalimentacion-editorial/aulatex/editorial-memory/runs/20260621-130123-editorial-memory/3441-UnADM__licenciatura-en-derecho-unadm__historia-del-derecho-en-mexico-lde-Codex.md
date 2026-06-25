{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia Historia del Derecho en Mexico sin copiar contenido tematico.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y trazabilidad bibliografica.",
    "Se refuerza bloqueo de propagacion ante salida no JSON parseable y normalizacion previa obligatoria.",
    "Se mantiene estrategia conservadora: transferir solo abstracciones reutilizables entre nodos no equivalentes.",
    "Se conserva contexto local verificable del destino: README, programa analitico, plantillas LaTeX y .bib institucional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir datos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Asegurar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Mantener coherencia documental entre README, programa analitico, .tex y .bib.",
    "Aplicar los cinco ejes editoriales como plantilla transversal reusable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema planteado.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Adaptar formato de salida al tipo de producto solicitado: reporte o presentacion.",
    "No asumir que fuentes de semanas o materias distintas aplican automaticamente.",
    "Verificar correspondencia exacta entre consigna local y producto entregado."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizacion recursiva.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union-dedupe, sin recortar reglas utiles previas.",
    "Evitar regresiones editoriales respecto de ciclos anteriores."
  ],
  "latex_rules": [
    "Usar plantillas locales de la materia como base editable.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "Actualizar solo campos variables por actividad; no eliminar campos institucionales.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver placeholders de Slug no expandidos en README y programa antes de automatizar o citar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir trazabilidad de consulta cuando aplique.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva en el destino."
  ],
  "propagation_hints": [
    "Propagar lateral y hacia arriba solo reglas transversales verificables.",
    "Priorizar transferencia de identidad, estructura reusable y gates de calidad.",
    "Evitar transferencia de redaccion literal o conceptos tematicos no comunes.",
    "Mantener alerta historica de salidas no parseables en nodos vecinos.",
    "Reforzar normalizacion temprana en ciclos recursivos.",
    "Si falta consigna local, conservar cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional: Mexico o México en nombre de materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Definir nombre oficial de figura docente para plantillas.",
    "Confirmar fuente operativa definitiva del motor de memoria [supuesto: origen mixto Codex/GPT-Pro].",
    "Corregir saltos de linea anomalos en README (eporte, eferencias) [supuesto de render].",
    "Confirmar reglas locales de citacion requeridas por rubrica de la materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional con voz estudiantil."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible.",
      "Control estructural y verificabilidad."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y verificables.",
      "Preservar continuidad editorial transversal sin contaminar contexto tematico local.",
      "Garantizar calidad tecnica y academica en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales trazables.",
      "Citas explicitas.",
      "Supuestos marcados.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion sustantiva -> evidencia verificable -> interpretacion -> implicacion juridica.",
      "Consigna local como criterio rector de extension y formato."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalizacion JSON",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto",
        "Sincronizacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Estandarizan estructura de cualquier actividad sin copiar contenido tematico."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Sincronizacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad de fuentes sustenta la integridad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia consigna-producto",
          "kind": "develops",
          "justification": "El marco institucional define tono, formato y criterios de entrega."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y entrada canonica.",
        "Programa analitico: cinco ejes y proposito de realizacion.",
        "historia-del-derecho-en-mexico.bib: fuentes institucionales base.",
        "Memoria origen: regla de normalizacion y bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion aplicada sin perdida de reglas utiles.",
      "Ciclo 3: se transfieren solo abstracciones estables entre nodos no equivalentes.",
      "Ciclo 3: se refuerzan gates de calidad y grafo conceptual transversal.",
      "Ciclo 3: se preserva separacion entre contenido tematico de origen y contexto local de destino."
    ]
  }
}