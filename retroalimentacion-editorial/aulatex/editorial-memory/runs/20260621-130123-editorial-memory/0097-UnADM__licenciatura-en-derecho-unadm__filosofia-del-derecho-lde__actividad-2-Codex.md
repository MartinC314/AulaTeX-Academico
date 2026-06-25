{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 sin copiar contenidos exclusivos.",
    "Se mantiene compresion lossless por union y deduplicacion de reglas reutilizables.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva normalizacion obligatoria antes de propagacion recursiva.",
    "Se corrigen ambiguedades locales con marca de supuesto cuando falte consigna."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de actividad-2 antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Evitar entrega solo descriptiva; incluir postura argumentada propia.",
    "Sustentar cada afirmacion sustantiva con fuente verificable o marca de supuesto.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "Reutilizar solo patrones editoriales del nodo hermano, no redaccion ni conclusiones especificas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir, deduplicar y reforzar."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como contexto base.",
    "Registrar fuentes especificas de actividad-2 en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico de semana especifica (supuesto) y no como reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON, estructura y deduplicacion.",
    "Aplicar estrategia progresiva por analogia controlada entre nodos hermanos.",
    "Transferir solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "Si reaparecen salidas no estructuradas, normalizar manualmente antes de reutilizar.",
    "Mantener historial de provisionalidad de fuentes heredadas hasta verificacion local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, producto y formato de entrega.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar si existe estilo de citacion institucional obligatorio. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del .bib de asignatura ante token Slug sin expandir.",
    "Confirmar si bibliografia de interpretacion juridica aplica realmente a actividad-2. [supuesto]"
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y transferencia profesional.",
      "Sostener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales trazables.",
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
        "Normalizacion de salidas",
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
          "justification": "Son patrones reutilizables desde nodo hermano."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico fija proposito y ejes transferibles.",
        "Regla valida heredada: bloquear propagacion sin JSON parseable.",
        "Contexto local muestra token Slug sin expandir; requiere normalizacion tecnica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se refuerza transferencia lateral sin copia literal.",
      "Ciclo 3: se preservan reglas utiles previas y se eliminan duplicados semanticos.",
      "Ciclo 3: se mantiene caracter provisional en datos no confirmados.",
      "Ciclo 3: se prioriza consistencia entre estructura editorial y control bibliografico."
    ]
  }
}