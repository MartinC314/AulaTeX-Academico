{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral desde actividad-1 por patrones reutilizables.",
    "Se preserva identidad UnADM y contexto curricular sin copiar contenido exclusivo del hermano.",
    "Se refuerza normalizacion obligatoria y compresion lossless por union-dedupe.",
    "Se mantienen ejes editoriales troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conservan fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar asumir tema, semana o formato sin evidencia local.",
    "Ajustar actividad-2 a la instruccion docente vigente."
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
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener compatibilidad entre claves citadas y entradas bibliograficas.",
    "No renombrar claves BibTeX ya citadas sin necesidad editorial.",
    "Evitar comandos no estandar sin justificacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base.",
    "Registrar fuentes especificas de actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complemento tematico y no reemplazo automatico del .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir entre hermanos solo identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar copiar redaccion literal, conclusiones especificas o bibliografia exclusiva de otro nodo.",
    "Aplicar analogia controlada: reutilizar patron, no contenido tematico cerrado.",
    "Registrar ciclos con incidencias de normalizacion manual si reaparecen salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones solicitada por docente.",
    "Confirmar estilo de citacion institucional obligatorio. [Supuesto: no confirmado]",
    "Confirmar nombre canonico final del archivo .bib de asignatura.",
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
      "Problema juridico o social activa el trabajo.",
      "Conceptos y fuentes respaldan el desarrollo.",
      "Analisis propio evita resumen pasivo.",
      "Conclusion juridica aporta transferencia profesional.",
      "Normalizacion estructurada habilita propagacion segura."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminar contenido especifico.",
      "Preservar memoria institucional util y trazable ciclo a ciclo."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos.",
      "Trazabilidad cita-bibliografia."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
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
          "justification": "Define tono, proposito y coherencia entre actividades."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion confiable."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite auditar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Se reutilizan como patron comun sin copiar contenido especifico."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico define proposito y ejes de trabajo transferibles.",
        "Regla valida heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: refuerzo lateral aplicado con deduplicacion lossless.",
      "Se preservaron reglas utiles previas sin recorte.",
      "Se eliminaron duplicados semanticos en formulacion, no en cobertura.",
      "Se mantuvo caracter provisional de fuentes no verificadas.",
      "Se reforzo la frontera: transferir patrones, no conclusiones ni bibliografia exclusiva."
    ]
  }
}