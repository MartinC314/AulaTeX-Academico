{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalización estructurada y cierre jurídico propio.",
    "Se refuerza compresión lossless por unión-deduplicación sin recorte semántico.",
    "Se mantiene bloqueo de propagación para salidas no JSON parseable.",
    "Se agrega corrección prioritaria de placeholders y campos truncados detectados en README, programa analítico y plantilla TeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 créditos.",
    "Tomar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar autoría real del estudiante y validar matrícula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Sincronizar README, programa analítico, .tex y .bib por actividad.",
    "Corregir nombres corruptos y tokens sin resolver sin alterar el slug canónico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No transferir contenido temático de Filosofía del Derecho sin evidencia local verificable."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca de supuesto para toda afirmación.",
    "Validar correspondencia 1:1 entre citas en texto y archivo .bib.",
    "Detectar y corregir placeholders, tokens sin expandir y campos truncados antes de compilar."
  ],
  "latex_rules": [
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliográfico local canónico.",
    "Completar campo truncado Tipo/Créditos en la tabla de autoría.",
    "Verificar nombres de archivos antes de referenciarlos en el documento."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente única del entregable.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar entradas específicas por actividad solo con datos verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable y quality gates sobre contenido disciplinar.",
    "Mantener bandera activa de normalización manual para insumos heredados no estructurados.",
    "Propagar a laterales correcciones de placeholders, slugs y campos truncados.",
    "Evitar regresiones: no eliminar reglas útiles previas ya validadas."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna textual de actividades locales del destino; confirmar producto exacto por semana.",
    "Confirmar nombre final de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 debe fijarse como código definitivo global.",
    "Verificar que autor y matrícula visibles correspondan al estudiante real.",
    "Confirmar que no queden rutas con caracteres anómalos en README/estructura TeX."
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
      "Problema jurídico concreto.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Trazabilidad editorial verificable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Garantizar coherencia entre identidad institucional, método argumentativo y evidencia."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Secciones funcionales y explícitas.",
      "Marcado visible de supuestos.",
      "Cierre con posición jurídica propia."
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
        "Sincronización README-programa-.tex-.bib"
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
          "justification": "Ordena problema, fundamento, análisis y cierre."
        },
        {
          "source": "Integridad bibliográfica",
          "target": "Validez académica",
          "kind": "depends_on",
          "justification": "Exige cita verificable y correspondencia con .bib."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia transversal limitada a abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README del destino confirma ubicación curricular y pauta editorial.",
        "Programa analítico del destino fija cinco ejes de trabajo.",
        "Archivo derecho-penal-especial-mexicano.bib contiene base institucional verificable.",
        "Plantilla .tex muestra campo truncado y requiere corrección previa a entrega."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 13: se preserva gate de JSON parseable como condición de propagación.",
      "Ciclo 13: se refuerza política de no traslado temático entre nodos no equivalentes.",
      "Ciclo 13: se elevan a prioridad operativa correcciones de tokens y campos truncados."
    ]
  }
}