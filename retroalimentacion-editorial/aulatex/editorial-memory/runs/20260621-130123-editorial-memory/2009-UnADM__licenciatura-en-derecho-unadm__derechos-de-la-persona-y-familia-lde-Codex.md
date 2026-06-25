{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preserva nucleo editorial estable: problema, conceptos y normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no estructuradas sin normalizacion JSON.",
    "Se conserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza correccion de placeholders y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No modificar datos de alumno o matricula sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear siempre el producto al formato solicitado en planeacion o rubrica.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "No trasladar contenido tematico de otra materia sin validar pertinencia. [supuesto]",
    "Registrar pendientes de contexto faltante en preguntas abiertas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de guardar o reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, rubrica y producto entregado."
  ],
  "latex_rules": [
    "Conservar plantilla base local como punto de partida.",
    "Mantener documentclass article en spanish, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes del contenido.",
    "Actualizar documentsubtitle al numero real de actividad.",
    "Usar espanol academico con acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README (reporte y referencias)."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes pertinentes a la actividad y realmente consultables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener coherencia de claves BibTeX para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no transversal.",
    "Mantener compresion por union-dedupe sin regresion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar rubricas vigentes por actividad en la materia destino.",
    "Confirmar si coursecode LDE-S3B1 es obligatorio en todos los productos.",
    "Confirmar vigencia de datos de alumno y figura docente en plantilla. [supuesto]",
    "Validar correccion definitiva de rutas y nombres corruptos en README.",
    "Validar sustitucion definitiva del placeholder de slug .bib en README y programa analitico."
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
      "Resolver problemas juridicos con fundamento verificable.",
      "Integrar conceptos, normas y doctrina con analisis propio.",
      "Cerrar con criterio juridico aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y solidos.",
      "Sostener calidad editorial y tecnica en LaTeX y BibTeX.",
      "Permitir propagacion segura entre nodos por reglas estables."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion clara entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] cuando falte confirmacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o evidencia.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Consistencia LaTeX y BibTeX",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional define tono, forma y exigencia academica."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere sustento verificable."
        },
        {
          "source": "Consistencia LaTeX y BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de trazabilidad."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Una secuencia problema-fundamento-analisis produce cierre aplicable."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla persistente institucional: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolida transferencia transversal sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 19: se deduplican reglas repetidas y se preservan reglas utiles previas.",
      "Ciclo 19: se refuerzan gates de JSON, supuestos y coherencia cita-bib.",
      "Ciclo 19: se mantiene foco operativo en correccion de placeholders y rutas corruptas."
    ]
  }
}