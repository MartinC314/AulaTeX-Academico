{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral reutilizable desde actividad-1.",
    "Se conserva identidad UnADM y contexto curricular sin copiar contenidos exclusivos del hermano.",
    "Se mantiene compresion lossless por union y deduplicacion, sin recorte de reglas utiles.",
    "Se ratifica normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se consolidan ejes editoriales troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener integridad academica con citas verificables y conclusion juridica propia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato del entregable con la planeacion semanal y consigna local.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Diferenciar postura propia, cita textual y parafrasis."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir argumento juridico propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar conceptos y doctrina solo cuando sean pertinentes a la consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Verificar correspondencia exacta entre producto entregado y consigna de actividad-2."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres canonicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y marco juridico verificable.",
    "Registrar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es tematico de Semana 7 y solo aplica si la consigna lo requiere."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "Evitar copiar redaccion literal, conclusiones especificas y bibliografia exclusiva de otro hermano.",
    "Aplicar normalizacion manual cuando reaparezcan salidas no estructuradas.",
    "Mantener historial de fuentes provisionales como antecedente, no como verdad final.",
    "Evitar regresiones frente a reglas institucionales ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar si el estilo de citacion institucional es obligatorio. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug sin expandir.",
    "Confirmar si actividad-2 reutiliza bibliografia existente o requiere seleccion bibliografica propia."
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
      "Transformar planeacion semanal en entregables academicos con fundamento juridico.",
      "Garantizar trazabilidad entre afirmaciones, citas y bibliografia.",
      "Sostener transferencia lateral controlada entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Transferencia lateral controlada",
        "Ejes editoriales troncales"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
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
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, forma y finalidad academica comun."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README define identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico define proposito y ejes de trabajo transferibles.",
        "Regla vigente: bloquear propagacion sin JSON parseable.",
        "Token Slug sin expandir requiere normalizacion de nombres de archivo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: refuerzo lateral aplicado con analogia controlada entre hermanos.",
      "Se preservaron reglas validas previas sin eliminacion.",
      "Se deduplicaron formulaciones redundantes manteniendo cobertura semantica.",
      "Se evitaron traslados de contenido exclusivo de actividad-1.",
      "Se mantuvieron supuestos explicitamente marcados donde faltan datos locales."
    ]
  }
}