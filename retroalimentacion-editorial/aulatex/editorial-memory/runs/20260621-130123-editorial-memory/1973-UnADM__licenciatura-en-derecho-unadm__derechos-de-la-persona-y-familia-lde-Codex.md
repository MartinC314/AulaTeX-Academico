{
  "summary": [
    "Sincronizacion transversal aplicada con compresion lossless por union-dedupe.",
    "Se preserva nucleo editorial estable: problema, conceptos-normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no estructuradas sin normalizacion previa.",
    "Se conserva identidad local del destino: UnADM, Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Se refuerza correccion de placeholders y rutas corruptas en README y programa analitico.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, formato y metadatos.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear productos al contexto local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno, matricula o figura docente sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear el formato final al producto solicitado en planeacion o rubrica."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir pertinencia de fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de guardar.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, rubrica y producto entregado."
  ],
  "latex_rules": [
    "Mantener espanol academico con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar consistencia entre nombre de archivos, slug y referencias.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico.",
    "Conservar plantilla local como base y actualizar subtitulo de Actividad X al numero real."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no transversal.",
    "Mantener estrategia conservadora: sin regresion de reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica especificas de la proxima actividad en la materia destino.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente en plantilla. [supuesto]",
    "Confirmar sustitucion definitiva de placeholders de slug en README y programa analitico.",
    "Confirmar si el codigo LDE-S3B1 es obligatorio en todos los productos.",
    "Confirmar si existe formato institucional obligatorio adicional para presentaciones."
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
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar coherencia entre consigna, argumentacion y cierre."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion clara entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte confirmacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina y fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion de memoria JSON",
        "Consistencia tecnica LaTeX y BibTeX"
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
          "justification": "El marco institucional fija tono y formato de argumentacion."
        },
        {
          "source": "Normalizacion de memoria JSON",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
        },
        {
          "source": "Consistencia tecnica LaTeX y BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de respaldo."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Fortalece la validez de conclusiones juridicas."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla institucional heredada: normalizar antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion completada sin eliminar reglas utiles.",
      "Ciclo 10: se consolidan gates JSON y normalizacion manual previa.",
      "Ciclo 10: se mantiene separacion entre abstracciones transversales y contenido tematico local.",
      "Ciclo 10: se refuerza resolucion de placeholders de slug y rutas corruptas."
    ]
  }
}