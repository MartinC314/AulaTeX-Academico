{
  "summary": [
    "Se refuerza actividad-2 con transferencia lateral de patrones reutilizables desde actividad-1.",
    "Se conserva compresion lossless por union y deduplicacion sin recorte.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar conclusiones, redaccion literal y bibliografia exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion sustantiva con fuente verificable o marca de supuesto.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas heredadas no estructuradas.",
    "Validar consistencia entre citas en texto y .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y archivos referenciados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y marco juridico verificable.",
    "Agregar fuentes especificas de actividad-2 al .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico [supuesto: no sustituye automaticamente el .bib canonico]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones generales entre hermanos; no contenido especifico.",
    "Mantener historial de fuentes provisionales como antecedente, no como verdad final.",
    "Aplicar deduplicacion semantica para evitar variantes repetidas.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar estilo de citacion obligatorio institucional.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug en README.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social como detonante.",
      "Conceptos y fuentes pertinentes con respaldo.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar trazabilidad entre afirmaciones, citas y bibliografia.",
      "Sostener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
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
          "justification": "Permite auditar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla historica valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: union-dedupe de reglas de actividad-1 hacia actividad-2 sin copiar contenido exclusivo.",
      "Ciclo 41: refuerzo de compuertas de calidad y normalizacion previa a propagacion recursiva.",
      "Ciclo 41: conservacion de supuestos abiertos cuando no hay consigna local verificable."
    ]
  }
}