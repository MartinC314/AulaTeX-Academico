{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho (actividad) y Derechos de autor (materia).",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa, evidencia verificable y cierre juridico transferible.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte de reglas utiles.",
    "Se refuerza gate de normalizacion: no propagar salidas no JSON parseable.",
    "Se mantiene herencia previa (Codex, GPT-Pro) como provisional hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener enfoque juridico con criterio propio en la conclusion."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre reporte, presentacion y bibliografia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de cada actividad al .bib local.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir tokens o marcadores de plantilla sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos del documento antes de cargar plantilla.",
    "Evitar comandos incompletos y paquetes truncados en el preambulo.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Supuesto: ajustar orden de paquetes segun requerimientos de template local."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de asignatura y bibliografia especifica por actividad.",
    "Usar derechos-de-autor.bib como contenedor canonico local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni datos personales del alumno.",
    "Mantener bandera de normalizacion manual para herencia de ciclos con salida no estructurada.",
    "Evitar regresiones: conservar toda regla util previa ya validada.",
    "Si falta contexto local, mantener supuestos explicitados y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave curricular oficial en toda la suite. [supuesto]",
    "Confirmar nombre de figura docente para reemplazar marcador pendiente.",
    "Confirmar si la ubicacion institucional en portada debe permanecer fija.",
    "Validar orden correcto de paquetes LaTeX respecto a template.",
    "Confirmar sustitucion definitiva de tokens $(@{...}.Slug) por nombres reales de archivo.",
    "Confirmar rubricas de evaluacion por actividad para calibrar profundidad argumentativa."
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
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables.",
      "Asegurar calidad editorial juridica con estructura reusable.",
      "Sostener memoria persistente sin perdida y sin regresion."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y trazables.",
      "Mantener coherencia entre portada, contenido y referencias.",
      "Normalizar antes de propagar."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion debe tener respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada mejora aplicabilidad profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia editorial transversal",
          "kind": "supports",
          "justification": "Homologa tono y formato entre materias."
        }
      ],
      "evidence": [
        "README de Derechos de autor define ubicacion curricular y pauta editorial.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene fuentes institucionales base.",
        "Se detectaron tokens de plantilla sin expandir en README y programa analitico. [supuesto confirmado por contexto local]",
        "Se detecto comando LaTeX incompleto al final del preambulo. [supuesto confirmado por contexto local]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicadas reglas repetidas y conservadas reglas utiles previas.",
      "Ciclo 4: reforzado gate JSON parseable como bloqueo de propagacion.",
      "Ciclo 4: transferidas solo abstracciones estables desde nodo transversal no equivalente.",
      "Ciclo 4: mantenida marca provisional para herencia Codex y GPT-Pro.",
      "Ciclo 4: ampliado grafo conceptual con relaciones de soporte y desarrollo sin inventar fuentes."
    ]
  }
}