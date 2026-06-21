{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral de patrones reutilizables desde actividad-1.",
    "Se conserva compresión lossless por unión y deduplicación, sin recorte ni regresión.",
    "Se mantiene normalización obligatoria para salidas no estructuradas antes de propagación recursiva.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita copiar conclusiones o bibliografía exclusiva de actividad-1; solo pasan reglas generales verificables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y propósito académico.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener integridad académica con citas verificables y cierre jurídico propio."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal o consigna docente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Diferenciar postura propia, cita textual y paráfrasis."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Usar fuentes de hermenéutica o argumentación solo si la consigna lo exige [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar rutas y nombres de archivos locales antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Registrar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático, no reemplazo automático [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no redacción literal.",
    "Conservar antecedentes provisionales de fuentes heredadas como histórico, no como base definitiva.",
    "Aplicar normalización manual en ciclos con entradas no estructuradas.",
    "Evitar regresiones respecto de reglas institucionales ya validadas.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto esperado.",
    "Confirmar si existe plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación obligatorio institucional [supuesto: no confirmado].",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si actividad-2 requiere bibliografía propia adicional o reutiliza base existente.",
    "Confirmar corrección de nombres de archivo con caracteres anómalos en README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica y citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables y útiles profesionalmente.",
      "Estandarizar calidad editorial en actividades con base institucional verificable.",
      "Asegurar transferencia lateral controlada entre nodos hermanos sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos.",
      "Correspondencia estricta entre afirmación, cita y referencia."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación propia.",
      "Consigna local -> selección de formato -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Ejes editoriales troncales",
        "Integridad académica",
        "Trazabilidad cita-bibliografía",
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
          "justification": "Define tono, formato y finalidad académica común."
        },
        {
          "source": "Normalización estructurada",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay propagación segura."
        },
        {
          "source": "Trazabilidad cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de cada afirmación."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre actividades hermanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica con criterio propio.",
        "Programa analítico define propósito editorial y ejes de trabajo transferibles.",
        "Regla histórica: bloquear propagación sin JSON parseable.",
        "Regla histórica: normalizar salidas no estructuradas antes de reutilizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 34: se refuerza salto hermano actividad-1 -> actividad-2 con analogía controlada.",
      "Se mantiene política lossless por unión-dedupe y sin eliminación de reglas útiles.",
      "Se depuran duplicados semánticos y se conservan supuestos explícitos.",
      "Se bloquea transferencia de contenidos exclusivos del hermano origen."
    ]
  }
}