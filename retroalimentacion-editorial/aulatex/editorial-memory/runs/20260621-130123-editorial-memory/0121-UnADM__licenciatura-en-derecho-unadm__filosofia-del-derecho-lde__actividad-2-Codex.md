{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 por patrones reutilizables.",
    "Se preservan reglas institucionales UnADM, estructura editorial y control de calidad sin recorte.",
    "Se refuerza deduplicacion lossless y normalizacion obligatoria antes de propagacion recursiva.",
    "Se evita copiar conclusiones o bibliografia exclusiva de actividad-1 al nodo hermano.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar toda afirmacion con fuente verificable o marca de supuesto.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico [supuesto], no reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo identidad, estructura, calidad y patrones argumentativos.",
    "Evitar propagar contenido tematico exclusivo de una actividad.",
    "Aplicar union-dedupe como compresion lossless en cada ciclo.",
    "Registrar como provisional toda regla basada en fuente no verificada."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si existe estilo de citacion institucional obligatorio.",
    "Confirmar nombre canonico final del .bib de asignatura por tokens no expandidos.",
    "Confirmar si actividad-2 requiere bibliografia propia o reutiliza parcial del .bib general."
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
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Asegurar coherencia entre consigna, evidencia y argumentacion.",
      "Preservar continuidad editorial entre actividades sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales trazables.",
      "Cierre juridico con criterio propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
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
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono y finalidad comun entre actividades."
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
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM y pauta editorial con conclusion juridica.",
        "Programa analitico fija proposito y ejes de trabajo transferibles.",
        "Regla estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se mantiene herencia valida de actividad-1 sin copia literal de contenido especifico.",
      "Ciclo 9: se refuerza gate de normalizacion para entradas no estructuradas.",
      "Ciclo 9: se consolidan patrones reutilizables de identidad, estructura, calidad y trazabilidad.",
      "Ciclo 9: se preserva compresion lossless por deduplicacion."
    ]
  }
}