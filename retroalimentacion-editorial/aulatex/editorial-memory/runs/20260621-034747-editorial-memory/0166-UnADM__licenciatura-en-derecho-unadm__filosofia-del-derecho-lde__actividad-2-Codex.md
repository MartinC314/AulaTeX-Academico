{
  "summary": [
    "Se refuerza memoria lateral de actividad-2 con patrones reutilizables validados en actividad-1.",
    "Se mantiene compresion lossless por union y deduplicacion sin recortar reglas utiles.",
    "Se conserva identidad UnADM, estructura canonica y control de supuestos como nucleo persistente.",
    "Se evita transferir conclusiones especificas o bibliografia exclusiva de un hermano sin consigna local.",
    "Se mantiene bloqueo de propagacion cuando no exista JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y finalidad academica.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con citas verificables y cierre juridico propio."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre afirmaciones, citas y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Sustentar cada afirmacion sustantiva con fuente verificable o marca de supuesto.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "Diferenciar con claridad postura propia, cita textual y parafrasis.",
    "Ajustar la entrega a la instruccion docente disponible."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar nombre canonico del .bib de asignatura antes de citarlo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre hermanos solo patrones reutilizables, no redaccion literal.",
    "Mantener etiquetas de fuente provisional como historial hasta verificacion local.",
    "Aplicar normalizacion manual cuando reaparezcan entradas no estructuradas.",
    "Evitar regresiones frente a reglas institucionales ya validadas.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si el producto es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si existe estilo de citacion institucional obligatorio [supuesto: no confirmado].",
    "Confirmar si las fuentes de interpretacion juridica aplican a actividad-2 [supuesto]."
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
        "Integridad academica y citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables y argumentados.",
      "Garantizar transferencia profesional con fundamento juridico verificable.",
      "Preservar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre juridico propio.",
      "Consistencia cita-bibliografia."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> analisis propio -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> control de calidad final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Ejes editoriales troncales",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y proposito comun entre actividades."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones recurrentes reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y cierre juridico propio.",
        "Programa analitico define proposito y cinco ejes de trabajo transferibles.",
        "Regla historica valida: bloquear propagacion sin JSON parseable.",
        "Token Slug sin expandir en README/programa exige verificacion de nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 66: se preservan reglas vigentes y se deduplican sin perdida.",
      "Ciclo 66: se refuerza no transferencia de contenido exclusivo entre hermanos.",
      "Ciclo 66: se mantiene control de supuestos como barrera anti-invencion.",
      "Ciclo 66: se consolida prioridad de estructura, calidad y trazabilidad."
    ]
  }
}