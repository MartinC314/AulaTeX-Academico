{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe.",
    "Se preservan reglas locales de Derecho a la Seguridad Social sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron estable reutilizable: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compuerta critica: no propagar si salida no es JSON parseable.",
    "Se conserva trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Relacionar el contenido con seguridad social cuando corresponda al destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion sea lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "No asumir reutilizacion automatica de .bib de otras materias."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Mantener bandera historica de riesgo por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta interna [supuesto].",
    "Confirmar norma de citacion requerida en la materia (APA, institucional o juridica mexicana) [supuesto].",
    "Confirmar si todas las plantillas de Actividad 1 del destino ya existen y son canon.",
    "Confirmar si persiste alguna fuente provisional heredada de nodos no juridicos [supuesto]."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas en productos juridicos verificables.",
      "Sostener cada entrega en problema, fundamento, evidencia, analisis y cierre.",
      "Preservar identidad institucional y trazabilidad editorial.",
      "Comprimir sin perder reglas utiles ni contexto operativo."
    ],
    "reason_for_being": [
      "Convertir planeaciones en entregables evaluables y compilables.",
      "Garantizar coherencia transversal entre calidad editorial y rigor juridico.",
      "Evitar regresiones al consolidar memoria persistente."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y conclusion.",
      "Etiquetado visible de [supuesto] cuando falte verificacion.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico delimitado",
        "Marco normativo verificable",
        "Evidencia con cita explicita",
        "Analisis propio argumentado",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion lossless por union-dedupe"
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
          "source": "Problema juridico delimitado",
          "target": "Analisis propio argumentado",
          "kind": "depends_on",
          "justification": "Sin pregunta clara no hay analisis juridico coherente."
        },
        {
          "source": "Marco normativo verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal comprobable."
        },
        {
          "source": "Evidencia con cita explicita",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad protege calidad institucional."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion lossless por union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin recorte."
        }
      ],
      "evidence": [
        "README local define estructura canonica y archivos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial previo confirma necesidad de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 70: se reforzo patron transversal estable sin transferir contenido tematico de origen.",
      "Ciclo 70: se mantuvo gate de JSON parseable como condicion de propagacion.",
      "Ciclo 70: se consolidaron reglas de trazabilidad con etiqueta [supuesto].",
      "Ciclo 70: se preservo prioridad del .bib local del destino."
    ]
  }
}