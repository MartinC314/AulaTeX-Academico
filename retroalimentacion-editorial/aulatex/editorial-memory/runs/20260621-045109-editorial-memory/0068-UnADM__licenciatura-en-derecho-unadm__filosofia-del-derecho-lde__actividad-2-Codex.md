{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 por union-dedupe lossless.",
    "Se preservan reglas validas de identidad UnADM, estructura, calidad y trazabilidad sin recorte.",
    "Se refuerza que solo se transfieren patrones reutilizables entre hermanos, no contenidos exclusivos.",
    "Se mantiene control de fuentes provisionales y marcado explicito de supuestos no verificados.",
    "Se conserva normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y finalidad academica.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica del nodo.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear forma de entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion en español consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivos antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico (supuesto), no reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Aplicar compresion lossless por union y deduplicacion, nunca por recorte.",
    "Evitar regresiones: no eliminar reglas utiles ya validadas.",
    "Transferir entre hermanos solo identidad, estructura, calidad y patrones argumentativos.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si existe rubrica docente especifica para profundidad argumentativa.",
    "Confirmar estilo de citacion obligatorio institucional (supuesto: no confirmado).",
    "Confirmar nombre canonico final del .bib de asignatura ante tokens no expandidos.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato principal."
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
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar fundamento juridico, evidencia y transferencia profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Ejes editoriales troncales",
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
          "justification": "Define tono, formato y proposito comun."
        },
        {
          "source": "Normalizacion estructurada",
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
          "justification": "Se reutilizan como patron entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico define proposito y ejes transferibles.",
        "Regla valida heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 68: se refuerza transferencia lateral por analogia controlada entre hermanos.",
      "Ciclo 68: se conserva union-dedupe lossless sin eliminar reglas utiles previas.",
      "Ciclo 68: se mantiene frontera editorial: patrones si, contenido exclusivo no.",
      "Ciclo 68: se sostienen supuestos abiertos cuando falta evidencia local."
    ]
  }
}