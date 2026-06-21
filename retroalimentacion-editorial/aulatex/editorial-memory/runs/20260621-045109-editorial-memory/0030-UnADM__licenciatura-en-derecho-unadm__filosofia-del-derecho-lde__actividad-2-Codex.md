{
  "summary": [
    "Se refuerza actividad-2 con patrones reutilizables de actividad-1 sin copiar contenido especifico.",
    "Se mantiene identidad UnADM, estructura argumentativa y control de calidad como nucleo estable.",
    "Se conserva compresion lossless por union y deduplicacion, sin recorte de reglas utiles.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas y marcado explicito de supuestos.",
    "Se refuerza la propagacion recursiva solo con JSON valido y estructura minima completa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre afirmaciones y fuentes."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente disponible.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Diferenciar postura propia, cita textual y parafrasis."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Verificar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo con caracteres anomalos en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular para contexto.",
    "Registrar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es tematico y no reemplaza automaticamente el .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar copiar conclusiones o bibliografia exclusiva de otra actividad.",
    "Mantener historial de herencia provisional como antecedente, no como verdad final.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar estilo de citacion obligatorio institucional. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si clean.bib se usa en actividad-2 o solo en semana tematica distinta."
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
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables con fundamento juridico verificable.",
      "Garantizar continuidad editorial estable entre actividades hermanas.",
      "Proteger calidad formal y trazabilidad academica en cada ciclo."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos.",
      "Sin afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Integridad academica",
        "Normalizacion de salidas",
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
          "justification": "Define tono, forma y finalidad comun entre actividades."
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
          "justification": "Permite verificar respaldo real de cada afirmacion."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables y no contenido exclusivo."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM, integridad academica y cierre juridico.",
        "Programa analitico define proposito y ejes transferibles.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Regla persistente: normalizar salida no estructurada antes de reutilizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 30: refuerzo lateral aplicado por analogia controlada entre hermanos.",
      "Se deduplican reglas repetidas de identidad, estructura y calidad.",
      "Se preservan reglas utiles previas sin eliminacion regresiva.",
      "Se evita transferencia de redaccion literal y bibliografia exclusiva de actividad-1."
    ]
  }
}