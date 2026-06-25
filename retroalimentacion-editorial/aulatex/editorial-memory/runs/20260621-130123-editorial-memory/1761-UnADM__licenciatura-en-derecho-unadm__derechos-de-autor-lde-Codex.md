{
  "summary": [
    "Consolidar cerebro editorial minimo para Derechos de autor con identidad UnADM.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Preservar regla de normalizacion estructurada antes de propagar.",
    "Transferir solo abstracciones estables entre materias no equivalentes.",
    "Marcar como provisional toda herencia no verificada localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta validacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Corregir tokens de plantilla no resueltos en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar al .bib local solo fuentes realmente usadas por actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico para tokens sin expandir y caracteres anomalos.",
    "Detectar y corregir campos pendientes como Nombre por definir."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "No dejar comandos truncados como usepackage sin argumento.",
    "Mover paquetes al preambulo valido segun la plantilla.",
    "No propagar datos personales del alumno a otros nodos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar derechos-de-autor.bib como archivo canonico local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir lateralmente solo reglas genericas de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal o contenido tematico propio de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual en ciclo 1 para herencia provisional.",
    "Evitar regresiones y conservar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion de Derechos de autor.",
    "Confirmar productos exactos por actividad en planeacion semanal.",
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Confirmar reemplazo de Figura docente en portada.",
    "Supuesto: la ubicacion Roma Norte, Ciudad de Mexico puede ser plantilla; validar si debe mantenerse.",
    "Confirmar correccion definitiva de rutas eporte y eferencias en README."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y transferencia profesional.",
      "Estandarizar calidad editorial sin perder contexto local."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y trazables.",
      "Mantener consistencia entre portada, contenido y referencias."
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
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
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
          "justification": "La postura argumentada permite cierre profesional util."
        }
      ],
      "evidence": [
        "README de Derechos de autor define identidad y ubicacion curricular.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte semantico.",
      "Se transfirieron solo abstracciones estables desde nodo transversal.",
      "Se conservaron controles de JSON parseable y normalizacion manual ciclo 1.",
      "Se abrieron vacios locales sin inventar fuentes ni consignas."
    ]
  }
}