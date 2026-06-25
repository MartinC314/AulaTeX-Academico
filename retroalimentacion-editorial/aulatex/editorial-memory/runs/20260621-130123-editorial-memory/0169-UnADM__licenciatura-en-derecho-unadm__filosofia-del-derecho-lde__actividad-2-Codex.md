{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-2 con deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura editorial y controles de calidad.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagar.",
    "Se mantiene uso de supuestos cuando falte consigna local verificable.",
    "Se evita copiar conclusiones o bibliografia exclusiva de un nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Diferenciar postura propia, cita textual y parafrasis."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir postura argumentada del estudiante."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles con .tex.",
    "No renombrar claves ya citadas sin motivo editorial verificable.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres canonicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas de actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento tematico y no reemplazo automatico del .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal.",
    "Evitar mover conclusiones especificas entre nodos hermanos.",
    "Mantener trazabilidad de cambios por union-dedupe lossless.",
    "Conservar historial de fuentes provisionales como antecedente, no como verdad canonica.",
    "Aplicar refuerzo-lateral por analogia controlada con evidencia local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, producto y semana.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion institucional obligatorio. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug en README.",
    "Confirmar si actividad-2 reutiliza bibliografia existente o requiere curacion propia."
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
      "Producto segun planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Garantizar fundamento juridico, evidencia y postura propia.",
      "Asegurar consistencia editorial entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones trazables.",
      "Cierre con criterio juridico propio.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> ajuste de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Ejes editoriales troncales"
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
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia confiable."
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
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla vigente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se refuerza transferencia lateral por patrones y no por contenido especifico.",
      "Ciclo 21: se mantiene compresion lossless por union y deduplicacion.",
      "Ciclo 21: se preservan reglas utiles previas sin regresion."
    ]
  }
}