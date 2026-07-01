{
  "summary": [
    "Se consolida actividad-2 con refuerzo lateral desde actividad-1 por patrones reutilizables.",
    "Se preserva identidad UnADM, ejes editoriales y control de calidad sin recorte.",
    "Se mantiene normalizacion obligatoria de salidas no estructuradas antes de propagacion.",
    "Se evita traslado de conclusiones o bibliografia exclusiva de actividad-1.",
    "Se refuerza compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad de origen provisional Codex y GPT-Pro como antecedente historico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente disponible.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Usar fuentes de hermeneutica o argumentacion solo si la consigna lo exige."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion sustantiva.",
    "Validar consistencia entre citas en texto y .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Normalizar respuestas heredadas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves citadas en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas sin necesidad.",
    "Usar acentos y codificacion espanola correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base.",
    "Agregar fuentes especificas de actividad-2 en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones institucionales y argumentativos.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva entre actividades.",
    "Aplicar union-dedupe como compresion lossless.",
    "Registrar ciclo 2 con normalizacion manual si reaparecen salidas no estructuradas.",
    "Mantener reglas validadas sin regresion."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2 (tema, semana y producto).",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion obligatorio institucional [supuesto: no confirmado].",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato.",
    "Confirmar fuentes obligatorias locales de la semana correspondiente."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables con fundamento juridico y evidencia.",
      "Preservar consistencia editorial entre actividades hermanas sin contaminar contenido especifico.",
      "Garantizar trazabilidad entre afirmaciones, citas y bibliografia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
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
        "Integridad academica",
        "Normalizacion estructurada",
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
          "justification": "Fija tono, formato y finalidad comun entre actividades."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin salida valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo real de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Son patrones reutilizables en nodo hermano."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico define ejes de trabajo y proposito editorial.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Transferencia actual respeta no copiar contenido exclusivo del hermano."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza normalizacion previa a propagacion recursiva.",
      "Ciclo 2: se consolidan ejes troncales como invariantes del nodo.",
      "Ciclo 2: se mantiene herencia valida y se etiqueta lo provisional.",
      "Ciclo 2: se depuran duplicados semanticos sin perdida de reglas."
    ]
  }
}