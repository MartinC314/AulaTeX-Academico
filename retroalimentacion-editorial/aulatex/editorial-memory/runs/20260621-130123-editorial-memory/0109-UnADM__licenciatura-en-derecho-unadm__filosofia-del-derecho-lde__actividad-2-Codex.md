{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas validas previas por union y deduplicacion lossless.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar contenido exclusivo de un hermano; solo se transfieren patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Redactar con enfoque academico-juridico y transferencia a practica profesional.",
    "Incluir conclusion juridica con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar fuentes de hermeneutica o argumentacion solo si la consigna lo requiere."
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
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre claves de cita del .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Confirmar nombre canonico del .bib de asignatura; supuesto actual: filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base de contexto.",
    "Agregar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico; supuesto: orientado a Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir entre hermanos solo patrones reutilizables, no conclusiones especificas.",
    "Mantener union-dedupe lossless para evitar regresiones.",
    "Registrar como provisionales los bloques heredados de origen no estructurado.",
    "Aplicar refuerzo lateral en identidad, estructura, calidad, conceptos y relaciones recurrentes."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar si existe estilo de citacion institucional obligatorio.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si actividad-2 reutiliza bibliografia existente o requiere .bib especifico."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar fundamento juridico, evidencia y cierre argumentativo transferible.",
      "Preservar continuidad editorial entre actividades hermanas sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre juridico con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Ejes editoriales troncales",
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
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Guian la construccion del producto sin copiar contenido de actividad 1."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico define proposito y ejes transferibles.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se reforzo transferencia lateral por analogia controlada.",
      "Ciclo 6: se deduplicaron reglas repetidas sin recortar informacion util.",
      "Ciclo 6: se mantuvo caracter provisional de fuentes heredadas no verificadas.",
      "Ciclo 6: se preservo frontera entre patrones reutilizables y contenido especifico de hermano."
    ]
  }
}