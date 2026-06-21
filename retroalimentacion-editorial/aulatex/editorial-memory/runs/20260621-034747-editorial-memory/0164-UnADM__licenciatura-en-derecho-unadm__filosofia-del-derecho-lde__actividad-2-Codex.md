{
  "summary": [
    "Se consolida refuerzo lateral de actividad-1 a actividad-2 con deduplicacion lossless.",
    "Se preservan reglas validas previas y se eliminan solo duplicados.",
    "Se refuerza identidad UnADM, estructura argumentativa y control de supuestos.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se evita transferencia de conclusiones o bibliografia exclusiva de un hermano.",
    "Se integra verificacion de tokens Slug sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica y cierre con criterio juridico propio."
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
    "Ajustar actividad-2 solo a la instruccion docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar fuentes de hermeneutica o interpretacion juridica solo si la consigna lo requiere [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; aplicar union y deduplicacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles entre .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar rutas y nombres de archivos antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como contexto base.",
    "Registrar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Mantener etiqueta de herencia provisional cuando el origen fue no estructurado.",
    "Aplicar normalizacion manual en ciclos con entradas heredadas defectuosas.",
    "Registrar refuerzos por analogia controlada sin sobreajuste tematico."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion institucional obligatorio [supuesto: no confirmado].",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato principal.",
    "Confirmar si las fuentes de interpretacion juridica aplican a actividad-2 o solo a semana 7."
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
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Asegurar fundamento juridico y evidencia verificable.",
      "Sostener continuidad editorial entre actividades sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Postura propia explicita.",
      "Marcado de supuestos.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> respaldo -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
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
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Token Slug sin expandir detectado en README y programa analitico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 64: union-dedupe de reglas de actividad-1 y actividad-2 sin recorte semantico.",
      "Ciclo 64: se refuerza control de supuestos para datos no visibles.",
      "Ciclo 64: se mantiene prohibicion de copiar contenido exclusivo entre hermanos.",
      "Ciclo 64: se consolida verificacion de consistencia .tex/.bib y de nombres canonicos.",
      "Ciclo 64: se preserva memoria de normalizacion manual por herencia no estructurada."
    ]
  }
}