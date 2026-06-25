{
  "summary": [
    "Se refuerza memoria lateral entre asignaturas sin copiar contenidos especificos.",
    "Se conserva identidad UnADM y ubicacion curricular comun verificable.",
    "Se consolida patron transversal: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla operativa: no propagar salidas no parseables sin normalizacion.",
    "Se agregan mejoras verificables locales: token Slug sin expandir en README/programa y entrada .bib truncada.",
    "Se aplica compresion lossless por deduplicacion sin eliminar reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar con [Supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sostener integridad academica con citas verificables y postura propia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar que el tipo de producto corresponda a la consigna de Actividad 6.",
    "Traducir el analisis a implicaciones juridicas aplicables cuando proceda.",
    "No reutilizar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en cada fusion.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Exigir trazabilidad de supuestos y evidencias antes de cerrar ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte y presentacion de la asignatura.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar metadatos sin respaldo.",
    "Conservar metadatos minimos: autor/editor, titulo, anio y fuente/editorial o URL.",
    "Deduplicar entradas equivalentes con clave canonica sin perder trazabilidad.",
    "Marcar y bloquear uso operativo de entradas truncadas hasta su curacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y verificadas.",
    "Transferir patrones reutilizables, no redaccion literal ni bibliografia exclusiva.",
    "Mantener analogia controlada: estructura y calidad primero, contenido despues.",
    "Conservar historial de fallas de parseo como contexto, no como base operativa.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas.",
    "Evitar regresiones de calidad al fusionar nodos laterales."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato de entrega exigido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Definir criterio formal de clave canonica para deduplicar .bib.",
    "[Supuesto] Verificar cierre completo de la entrada sierraUniversidadNacional1910 en .bib local.",
    "Confirmar si Actividad 6 requiere fuentes obligatorias adicionales de semana."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social como disparador.",
      "Conceptos y marco normativo con evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Control de calidad estructural y bibliografico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos.",
      "Asegurar consistencia editorial transversal entre asignaturas afines.",
      "Preservar memoria util sin perder trazabilidad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y estables.",
      "Afirmacion con evidencia y cita.",
      "Cierre con criterio juridico propio.",
      "Uso explicito de [Supuesto] cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo -> desarrollo coherente -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Deduplicacion bibliografica canonica",
        "Token Slug sin expandir",
        "Entrada .bib truncada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial local exige ambas de forma conjunta."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El programa analitico define el problema como eje de desarrollo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion debe derivar del razonamiento y evidencia."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida se bloquea reutilizacion segura."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce errores de cita y preserva trazabilidad."
        },
        {
          "source": "Token Slug sin expandir",
          "target": "Calidad de compilacion",
          "kind": "contrasts",
          "justification": "Puede romper referencias de archivos si no se corrige."
        }
      ],
      "evidence": [
        "README: identidad UnADM, punto de entrada canonico, conclusion con criterio propio.",
        "Programa analitico: cinco ejes editoriales transversales.",
        ".bib local: duplicados verificables y entrada truncada en sierraUniversidadNacional1910.",
        "Historial: multiples salidas no parseables; normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se transfieren patrones reutilizables desde Filosofia del Derecho a Etica y Moral juridica.",
      "Ciclo 8: se preservan reglas previas utiles y se eliminan duplicados semanticos.",
      "Ciclo 8: se refuerzan compuertas de calidad parseable y trazabilidad de supuestos.",
      "Ciclo 8: se agregan hallazgos verificables locales sin inventar fuentes."
    ]
  }
}