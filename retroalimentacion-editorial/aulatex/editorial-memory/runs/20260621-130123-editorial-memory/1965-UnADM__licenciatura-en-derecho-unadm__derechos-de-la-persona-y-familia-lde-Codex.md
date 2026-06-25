{
  "summary": [
    "Sincronizacion transversal ciclo 8 completada con estrategia conservadora y sin regresion.",
    "Se preserva nucleo editorial comun: problema, conceptos-normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica de normalizacion: no propagar salidas no JSON parseable.",
    "Se refuerza identidad local de destino: UnADM, Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Se consolida correccion operativa de placeholders y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Conservar contexto curricular local verificado: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Mantener carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en marco conceptual-normativo, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear el contenido al producto solicitado en la planeacion o rubrica.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "No transferir contenido tematico de otra materia sin validacion de pertinencia. [supuesto]",
    "Registrar vacios de contexto en preguntas abiertas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de guardar o propagar.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar correspondencia entre consigna, rubrica y producto final.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders de slug y rutas corruptas antes de compilar."
  ],
  "latex_rules": [
    "Usar plantilla base local como punto de partida.",
    "Mantener documentclass article en espanol, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes del contenido.",
    "Actualizar documentsubtitle al numero real de actividad.",
    "Conservar acentos y codificacion correcta en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Conservar fuentes institucionales base ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a cada actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como [supuesto] cualquier referencia pendiente de verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar arrastre de redaccion literal o contenido tematico no transversal.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica vigentes de la actividad local a editar.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente. [supuesto]",
    "Confirmar si el codigo LDE-S3B1 es obligatorio en todos los entregables.",
    "Validar correccion definitiva de rutas corruptas en README.",
    "Validar sustitucion definitiva del placeholder de .bib en README y programa analitico."
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
        "Carpeta de materia como entrada canonica."
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
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para practica juridica.",
      "Asegurar coherencia entre consigna, argumentacion y cierre."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco y postura propia.",
      "Etiquetado explicito de [supuesto].",
      "Consistencia terminologica juridica."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX-BibTeX",
        "Trazabilidad consigna-desarrollo-conclusion"
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
          "justification": "El marco institucional fija tono, formato y rigor."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad consigna-desarrollo-conclusion",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion segura ni auditable."
        },
        {
          "source": "Consistencia LaTeX-BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de verificabilidad."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El sustento verificable fortalece la conclusion juridica."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla transversal heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 8: se conservaron todas las reglas utiles previas sin recorte funcional.",
      "Ciclo 8: se agrego refuerzo transversal de quality gates y grafo conceptual.",
      "Ciclo 8: no se transfirio contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo."
    ]
  }
}