{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral desde actividad-1 sin copiar contenido exclusivo.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y control de calidad ya validados.",
    "Se mantiene compresion lossless por union y deduplicacion, sin recorte.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
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
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el contenido al producto solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar fuentes de hermeneutica o argumentacion solo si la consigna lo requiere."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Verificar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener compatibilidad entre claves de cita en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar nombres canonicos de archivos por caracteres anomalos en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base de contexto.",
    "Registrar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento tematico y no reemplazo automatico del .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos troncales y relaciones recurrentes.",
    "No propagar conclusiones ni bibliografia exclusiva de un hermano a otro.",
    "Aplicar union-dedupe lossless para evitar regresiones.",
    "Mantener registro de herencia provisional cuando el origen fue no estructurado.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si existe plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion obligatorio institucional.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si actividad-2 reutiliza bibliografia existente o requiere .bib propio."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico alineado a consigna.",
      "Garantizar claridad juridica, trazabilidad y criterio propio.",
      "Preservar continuidad editorial entre nodos sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
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
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla historica valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se refuerza transferencia lateral por patrones y no por contenido literal.",
      "Ciclo 20: se mantiene union-dedupe lossless sin eliminar reglas utiles.",
      "Ciclo 20: se consolida control de supuestos para datos no visibles en consigna.",
      "Ciclo 20: se reafirma prioridad de normalizacion estructurada antes de propagacion recursiva."
    ]
  }
}