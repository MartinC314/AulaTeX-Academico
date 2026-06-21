{
  "summary": [
    "Se mantiene memoria de materia con identidad UnADM y enfoque juridico verificable.",
    "Se refuerza patron transversal estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva control de normalizacion: no propagar si no hay JSON parseable.",
    "Se aplica compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se preserva especificidad local de Seguridad Social sin importar contenido tematico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No propagar datos personales de plantilla a nodos laterales [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, conceptos y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o etiqueta [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin perdida."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta de español en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas corruptas.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Normalizar nombres de archivo cuando existan marcadores o tokens sin expandir.",
    "Mantener metadatos institucionales consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar nuevas fuentes solo cuando la consigna lo exija y se puedan verificar."
  ],
  "propagation_hints": [
    "Propagar a laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener bandera historica: ciclo 1 con salida no parseable requiere cautela.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo recursivo."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o solo operativo [supuesto].",
    "Confirmar figura docente oficial para completar portada cuando aplique.",
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
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas con base juridica verificable.",
      "Unir problema, fundamento, evidencia, analisis y cierre profesional.",
      "Preservar memoria util sin duplicados ni regresiones."
    ],
    "reason_for_being": [
      "Garantizar entregas academicas consistentes, trazables y compilables.",
      "Convertir planeaciones en productos juridicos evaluables.",
      "Sostener sincronizacion transversal sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y conclusion.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia pertinente.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
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
          "justification": "Sin delimitacion del problema no hay analisis defendible."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite conservar reglas utiles sin perdida."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes juridicos de trabajo.",
        "derecho-a-la-seguridad-social.bib confirma base institucional y normativa vigente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 25: se reforzo patron transversal estable sin mover contenido tematico entre materias no equivalentes.",
      "Ciclo 25: se mantuvieron gates de JSON parseable y normalizacion previa como condicion de propagacion.",
      "Ciclo 25: se consolido ADN minimo reconstruible con foco en identidad, estructura, calidad y trazabilidad."
    ]
  }
}