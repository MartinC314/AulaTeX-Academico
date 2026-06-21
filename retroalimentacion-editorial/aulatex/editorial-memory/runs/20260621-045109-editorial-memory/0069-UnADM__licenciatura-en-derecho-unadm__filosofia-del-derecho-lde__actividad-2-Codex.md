{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-2 con deduplicacion lossless.",
    "Se preservan reglas validas de identidad UnADM, estructura argumentativa, calidad y trazabilidad.",
    "Se refuerza que solo se propagan patrones reutilizables, no contenidos exclusivos de un hermano.",
    "Se mantiene normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantiene caracter provisional de fuentes heredadas no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: problema, conceptos y fuentes, desarrollo del producto, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; aplicar union-dedupe lossless."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre claves de cita en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas sin necesidad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar nombres canonicos de archivos por caracteres anomalos en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como contexto base.",
    "Registrar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico del .bib canonico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva de actividad-1.",
    "Mantener sin regresion reglas institucionales ya validadas.",
    "Aplicar normalizacion manual si reaparecen salidas no estructuradas.",
    "Cuando falten datos locales, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si el producto obligatorio es reporte, presentacion u otro formato.",
    "Confirmar rubrica especifica para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si existe estilo de citacion institucional obligatorio [supuesto: no confirmado].",
    "Confirmar si referencias de Semana 7 aplican a actividad-2 o solo como reserva tematica [supuesto]."
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
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con postura academica.",
      "Cierre juridico transferible.",
      "Trazabilidad entre afirmaciones, citas y bibliografia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Preservar coherencia institucional y rigor juridico.",
      "Habilitar propagacion segura entre nodos por patrones estables."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Supuestos marcados de forma explicita.",
      "Conclusion con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> control de calidad final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Normalizacion de salidas",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
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
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
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
          "justification": "Son patrones reutilizables entre actividades hermanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y punto de entrada canonico.",
        "Programa analitico define proposito y ejes de trabajo transferibles.",
        "Regla historica valida: bloquear propagacion sin JSON parseable.",
        "Se aplica union-dedupe lossless sin recorte de reglas utiles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: refuerzo lateral por analogia controlada aplicado.",
      "Se deduplicaron reglas repetidas con preservacion semantica.",
      "Se removio transferencia de contenido especifico no reutilizable de actividad-1.",
      "Se reforzo marcado de supuestos ante vacios de consigna local."
    ]
  }
}