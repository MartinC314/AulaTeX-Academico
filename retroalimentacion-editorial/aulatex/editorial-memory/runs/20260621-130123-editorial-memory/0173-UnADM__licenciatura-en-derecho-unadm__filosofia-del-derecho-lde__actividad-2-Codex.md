{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral desde actividad-1 sin copiar contenido exclusivo.",
    "Se preservan reglas validas previas con union-dedupe lossless y sin regresion.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas y se exige validacion local."
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
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana ni formato de actividad-2 sin evidencia local.",
    "Diferenciar postura propia, cita textual y parafrasis."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre claves citadas y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas sin migracion completa.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular para contexto.",
    "Registrar fuentes especificas de actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico (supuesto), no reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre hermanos solo patrones reutilizables, no conclusiones ni redaccion literal.",
    "Aplicar normalizacion manual si reaparecen salidas no estructuradas.",
    "Mantener etiquetas de provisionalidad para fuentes heredadas hasta verificacion local.",
    "Evitar regresiones frente a reglas institucionales ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si hay plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion institucional obligatorio (supuesto: no confirmado).",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si actividad-2 requiere bibliografia propia separada."
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
      "Transformar planeacion semanal en productos academicos trazables.",
      "Asegurar fundamento juridico, evidencia y criterio propio.",
      "Habilitar transferencia lateral controlada entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
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
          "source": "Normalizacion estructurada",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay propagacion segura."
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
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico fija proposito y ejes de trabajo transferibles.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: refuerzo lateral aplicado por analogia controlada entre hermanos.",
      "Se mantuvo deduplicacion lossless sin recorte de reglas utiles.",
      "Se excluyo transferencia de conclusiones especificas y bibliografia exclusiva de actividad-1.",
      "Se reforzo control de supuestos para datos no visibles localmente."
    ]
  }
}