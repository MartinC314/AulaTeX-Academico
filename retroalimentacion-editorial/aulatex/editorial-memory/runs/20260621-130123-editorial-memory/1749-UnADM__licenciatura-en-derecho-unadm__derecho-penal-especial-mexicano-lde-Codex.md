{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalización estructurada y cierre jurídico propio.",
    "Se mantiene transferencia por abstracciones editoriales; no se traslada contenido temático de Filosofía del Derecho sin evidencia local.",
    "Se refuerza control técnico: JSON parseable, deduplicación lossless, consistencia cita-bibliografía y corrección de placeholders."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 créditos.",
    "Tomar la carpeta de la materia como entrada canónica.",
    "Conservar autoría real del estudiante y validar matrícula antes de entrega.",
    "No inventar figura docente; marcar pendiente cuando falte dato.",
    "Marcar como supuesto todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Sincronizar README, programa analítico, .tex y .bib por actividad.",
    "Corregir nombres corruptos y placeholders sin alterar el slug canónico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas de la actividad al .bib local antes de versión final.",
    "No asumir que fuentes de otras semanas aplican a la actividad actual.",
    "No trasladar contenido disciplinar del origen sin insumo verificable en el destino."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders o tokens sin expandir antes de compilar.",
    "Compilar LaTeX sin errores críticos ni referencias rotas antes de entrega."
  ],
  "latex_rules": [
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Conservar clase y configuración base aprobada de la materia salvo justificación.",
    "Completar metadatos institucionales y académicos antes de salida final.",
    "Corregir campo truncado Tipo/Créditos en authortable.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente única del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar fuentes específicas por actividad con metadatos mínimos completos.",
    "No inventar referencias ni completar datos sin verificación.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener trazabilidad entre afirmaciones, citas y evidencia documental."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar deduplicación semántica sin recorte de reglas útiles previas.",
    "Conservar bandera de normalización manual para insumos heredados no estructurados.",
    "Compartir abstracciones estables entre nodos no equivalentes; evitar redacción literal.",
    "Si falta contexto local, mantener cerebro mínimo y abrir vacíos explícitos."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna concreta de actividades del destino para fijar plantillas por semana.",
    "Confirmar figura docente real para reemplazar 'Nombre por definir'.",
    "Confirmar si LDE-S2B2 debe mantenerse como código canónico global.",
    "Validar matrícula visible contra fuente institucional local.",
    "Confirmar cierre completo del campo truncado Tipo/Créditos en la plantilla .tex.",
    "Verificar que no queden rutas o nombres con caracteres anómalos en README."
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
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho penal especial mexicano.",
        "Semestre 2, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y norma aplicable.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre identidad institucional, forma editorial y validez jurídica."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Uso explícito de supuestos cuando falten datos.",
      "Cierre con posición jurídica propia sustentada."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Consigna -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliográfica",
        "Conclusión jurídica transferible",
        "Trazabilidad de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, evidencia, análisis y cierre."
        },
        {
          "source": "Integridad bibliográfica",
          "target": "Validez académica",
          "kind": "depends_on",
          "justification": "Requiere citas verificables y correspondencia con .bib."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "La transferencia es editorial transversal, no temática literal."
        },
        {
          "source": "Trazabilidad de supuestos",
          "target": "Control de calidad",
          "kind": "supports",
          "justification": "Reduce afirmaciones sin respaldo documental."
        }
      ],
      "evidence": [
        "README del destino define identidad, ubicación curricular y pauta editorial.",
        "Programa analítico del destino explicita cinco ejes de trabajo.",
        "Archivo .bib local contiene base institucional verificable.",
        "Plantilla .tex muestra campo truncado y dato docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación semántica aplicada sin pérdida.",
      "Ciclo 20: se preservan reglas útiles previas y se evita regresión.",
      "Ciclo 20: se refuerza separación entre transferencia editorial y contenido temático.",
      "Ciclo 20: se mantiene estrategia progresiva y conservadora con vacíos locales abiertos."
    ]
  }
}