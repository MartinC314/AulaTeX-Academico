{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura juridica reusable, calidad verificable y normalizacion JSON.",
    "Se evita transferencia tematica de Filosofia del Derecho por no equivalencia de nodos.",
    "Se refuerza compresion lossless por deduplicacion y sin regresion.",
    "Se mantiene alerta institucional por salidas no estructuradas y se exige normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear contexto curricular local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno o matricula sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: problema, marco conceptual-normativo, analisis propio y conclusion juridica.",
    "Mantener trazabilidad entre consigna, desarrollo y cierre.",
    "Alinear formato final al producto solicitado por planeacion o rubrica."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Mantener conclusion con criterio juridico propio y transferible.",
    "No trasladar contenido tematico del origen sin validar pertinencia local. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna y producto entregable."
  ],
  "latex_rules": [
    "Conservar plantilla base local como punto de partida.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener espanol academico y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir en README y programa analitico para nombre .bib.",
    "Verificar consistencia entre slug, nombres de archivo y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes consultables y pertinentes a cada actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar redaccion literal y contenido tematico no validado.",
    "Si reaparece salida no parseable, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica vigentes de la primera actividad local.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente. [supuesto]",
    "Confirmar si coursecode LDE-S3B1 debe mostrarse en todos los artefactos.",
    "Confirmar correccion definitiva de rutas corruptas en README.",
    "Confirmar sustitucion final del placeholder dinamico del .bib en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada de 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia entre consigna, desarrollo y evaluacion.",
      "Sostener calidad institucional reproducible entre actividades."
    ],
    "style_markers": [
      "Inicio con problema concreto.",
      "Desarrollo por secciones funcionales.",
      "Afirmaciones con cita verificable.",
      "Cierre con criterio juridico propio.",
      "Uso explicito de marca [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna explicita -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad consigna-producto",
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
          "justification": "La identidad institucional exige evidencia, forma y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida se funda en normas y doctrina."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad consigna-producto",
          "kind": "develops",
          "justification": "La estructura formal permite verificar cumplimiento."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla institucional heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion aplicada sin eliminar reglas utiles previas.",
      "Ciclo 2: se reforzaron gates de parseo JSON y normalizacion manual.",
      "Ciclo 2: se preservaron ejes transversales de argumentacion juridica.",
      "Ciclo 2: no se propagaron contenidos tematicos especificos del nodo origen."
    ]
  }
}