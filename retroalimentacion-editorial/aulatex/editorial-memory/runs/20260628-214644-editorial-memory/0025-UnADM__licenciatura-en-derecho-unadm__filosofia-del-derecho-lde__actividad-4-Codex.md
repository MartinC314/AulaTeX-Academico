{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con union-dedupe lossless y sin recorte util.",
    "Se preserva identidad UnADM y marco curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto: no propagar si no hay JSON parseable y estructura minima completa.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; no fijar producto final sin confirmacion."
  ],
  "identity_rules": [
    "Mantener tono formal academico con precision juridica.",
    "Alinear toda entrega a UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto pedido por planeacion semanal.",
    "Distinguir hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico a Actividad 4.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con evidencia y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4.",
    "Supuesto: confirmar si el producto es reporte, presentacion u otro formato."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Verificar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre consigna de Actividad 4 y producto generado.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves BibTeX activas sin migracion controlada.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Supuesto: archivo .bib canonico esperado: filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar patrones generales institucionales y de calidad.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva entre hermanos.",
    "Mantener mejoras verificables y evitar regresiones de reglas utiles previas.",
    "Cuando falte dato local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar formato requerido: reporte, presentacion o producto visual.",
    "Confirmar rubrica de evaluacion especifica de Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del .bib ante token Slug no resuelto en README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumento juridico."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales claras.",
      "Cita explicita por afirmacion relevante.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco.",
      "Contrastar fuentes.",
      "Emitir postura propia justificada.",
      "Concluir con aplicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Ejes editoriales de Filosofia del Derecho",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere salida parseable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El flujo problema-evidencia-analisis conduce al cierre profesional."
        }
      ],
      "evidence": [
        "README define identidad, integridad y conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes registran fallas de parseo; se mantiene gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortograficas.",
      "Se preservaron reglas utiles heredadas sin eliminar restricciones validas.",
      "Se evitaron transferencias de contenido especifico entre nodos hermanos.",
      "Se agregaron solo refuerzos verificables desde README y programa analitico."
    ]
  }
}