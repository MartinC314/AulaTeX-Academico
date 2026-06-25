{
  "summary": [
    "Sincronizacion transversal consolidada entre actividad origen y materia destino con estrategia conservadora.",
    "Se preserva ADN UnADM y se transfieren solo abstracciones editoriales estables.",
    "Se mantiene regla critica: no propagar memoria no estructurada sin normalizacion previa.",
    "Se refuerza nucleo reusable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica.",
    "Se conserva contexto curricular local del destino: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Se mantiene correccion pendiente de placeholders y rutas corruptas en README y programa analitico. [supuesto hasta aplicar fix]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear entregables al contexto curricular local verificado.",
    "Conservar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno/matricula de plantilla sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear formato final al producto solicitado en planeacion o rubrica.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar transferir contenido tematico de Filosofia del Derecho sin pertinencia local. [supuesto]",
    "Registrar vacios de informacion como preguntas abiertas, no como hechos.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de guardar o propagar.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Exigir respaldo o etiqueta [supuesto] en afirmaciones no verificadas.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre actividad, consigna y tipo de entregable."
  ],
  "latex_rules": [
    "Mantener espanol academico con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Conservar claves BibTeX estables para evitar rupturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README/programa antes de reutilizar plantillas.",
    "Verificar nombres canonicos de archivos de reporte, presentacion y referencias antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normatividad verificable.",
    "Agregar solo fuentes consultables y pertinentes a cada actividad.",
    "No inventar referencias bibliograficas.",
    "Mantener metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de pasar quality gates.",
    "Transferir entre nodos no equivalentes solo reglas abstractas y reusables.",
    "Evitar redaccion literal y contenido tematico dependiente de actividad origen.",
    "Aplicar compresion lossless por union-dedupe y sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar correccion definitiva de nombres corruptos en README (reporte/referencias).",
    "Confirmar sustitucion definitiva de placeholders Slug en README y programa analitico.",
    "Confirmar vigencia de datos de autoria en plantilla local. [supuesto]",
    "Confirmar si coursecode LDE-S3B1 debe mostrarse en todos los entregables.",
    "Confirmar rubricas oficiales por actividad para calibrar profundidad argumentativa."
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
      "Problema juridico o social bien delimitado.",
      "Conceptos y normas pertinentes al caso.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para practica juridica.",
      "Sostener consistencia editorial y tecnica en toda la materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco teorico y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte evidencia.",
      "Cierre con implicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problematizar.",
      "Fundamentar con norma/doctrina/evidencia.",
      "Analizar con criterio propio.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion de memoria JSON",
        "Consistencia tecnica LaTeX/BibTeX",
        "Nucleo editorial de cinco ejes"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion de memoria JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusion juridica aplicable",
          "kind": "supports",
          "justification": "La validez argumentativa depende de respaldo verificable."
        },
        {
          "source": "Consistencia tecnica LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de trazabilidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional fija tono, rigor y formato."
        },
        {
          "source": "Nucleo editorial de cinco ejes",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Provee plantilla transversal reusable entre actividades."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo local derechos-de-la-persona-y-familia.bib.",
        "Regla institucional heredada: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion aplicada sin eliminar reglas utiles previas.",
      "Ciclo 4: se reforzo gate JSON parseable como condicion de propagacion.",
      "Ciclo 4: se transfirio nucleo argumentativo estable desde nodo transversal sin arrastre tematico literal.",
      "Ciclo 4: se mantuvieron pendientes tecnicos locales como preguntas abiertas."
    ]
  }
}