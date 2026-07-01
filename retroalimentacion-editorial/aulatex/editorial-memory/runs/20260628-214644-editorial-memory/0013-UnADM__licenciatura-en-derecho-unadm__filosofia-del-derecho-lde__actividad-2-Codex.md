{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 hacia actividad-2 sin copiar contenido exclusivo.",
    "Se preservan reglas validas previas con union y deduplicacion lossless.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria antes de propagacion recursiva.",
    "Se corrigen supuestos de bibliografia: clean.bib es tematico y no reemplaza automaticamente al .bib canonico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con citas verificables y cierre juridico con criterio propio."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar fuentes de hermeneutica/argumentacion solo si la consigna lo exige."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar respaldo o marca de [supuesto] en cada afirmacion sustantiva.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar rutas y nombres de archivo antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "[supuesto] .bib canonico esperado: filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho.",
    "Registrar fuentes especificas de actividad-2 en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base vs bibliografia especifica de actividad.",
    "[supuesto] filosofia-del-derecho-clean.bib corresponde a tema puntual y funciona como complemento, no reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "Evitar copiar redaccion literal, conclusiones especificas o bibliografia exclusiva entre hermanos.",
    "Mantener etiqueta de herencia provisional cuando el origen fue no estructurado.",
    "Aplicar normalizacion manual si reaparecen salidas no estructuradas en ciclo 2."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si existe estilo de citacion obligatorio institucional.",
    "Confirmar nombre canonico final del archivo .bib en entorno local.",
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
      "Problema juridico o social activa el trabajo.",
      "Conceptos y normas se usan con respaldo.",
      "Producto responde a planeacion semanal.",
      "Analisis propio evita resumen plano.",
      "Cierre juridico transferible a practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener coherencia entre consigna, evidencia y argumento propio.",
      "Asegurar transferencia lateral sin degradar identidad editorial."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Consigna local -> ajuste de formato -> validacion final."
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
          "justification": "Permite verificar respaldo real de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y cierre juridico.",
        "Programa analitico define proposito y ejes transferibles.",
        "Regla historica valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion semantica aplicada sin recorte.",
      "Se removieron duplicados literales y variantes redundantes.",
      "Se reforzo separacion entre reglas generales y datos dependientes de consigna.",
      "Se mantuvo herencia util y se marco incertidumbre con [supuesto]."
    ]
  }
}