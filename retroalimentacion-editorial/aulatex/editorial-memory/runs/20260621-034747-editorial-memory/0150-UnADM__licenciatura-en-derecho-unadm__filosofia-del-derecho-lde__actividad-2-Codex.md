{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas validas por union-dedupe lossless sin recorte.",
    "Se refuerza ADN editorial UnADM: identidad, estructura argumentativa, trazabilidad y cierre juridico propio.",
    "Se mantiene bloqueo de propagacion ante salidas no parseables y normalizacion previa obligatoria.",
    "Se evita copiar contenidos exclusivos del hermano; solo se transfieren patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y finalidad academica.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar rutas y nombres de archivos antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base de contexto.",
    "Agregar fuentes especificas de la actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y aplica solo si la consigna lo requiere."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "Evitar pasar conclusiones especificas, redaccion literal o bibliografia exclusiva de otra actividad.",
    "Mantener normalizacion manual cuando reaparezcan entradas heredadas no estructuradas.",
    "Reforzar sin regresion reglas institucionales y de calidad ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto solicitado.",
    "Confirmar plantilla obligatoria de secciones definida por el docente.",
    "Confirmar estilo de citacion institucional obligatorio. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del archivo .bib de asignatura.",
    "Confirmar si actividad-2 usa bibliografia propia o reutiliza parcialmente la existente."
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
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Normalizacion y trazabilidad editorial."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables.",
      "Asegurar consistencia entre identidad institucional, argumentacion y evidencia.",
      "Garantizar transferencia lateral segura entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre juridico con criterio propio."
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
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables para nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico fija proposito y ejes de trabajo.",
        "Regla vigente: bloquear propagacion sin JSON parseable.",
        "Transferencia hermano-a-hermano limitada a patrones reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 50: deduplicacion integral aplicada sin perdida.",
      "Ciclo 50: se mantienen reglas historicas de normalizacion obligatoria.",
      "Ciclo 50: se refuerza separacion entre patron reusable y contenido especifico de actividad-1.",
      "Ciclo 50: se preserva caracter provisional de fuentes heredadas no verificadas."
    ]
  }
}