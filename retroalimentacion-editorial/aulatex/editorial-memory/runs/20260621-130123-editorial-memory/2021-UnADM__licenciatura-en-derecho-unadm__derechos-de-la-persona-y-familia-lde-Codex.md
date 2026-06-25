{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia la materia destino sin trasladar contenido temático no equivalente.",
    "Se preserva núcleo editorial estable: problema, conceptos y normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene política institucional de normalización: no propagar salidas no estructuradas o no JSON parseable.",
    "Se refuerza identidad local de la materia destino con contexto curricular verificado en README y programa analítico.",
    "Se consolida corrección de placeholders y rutas corruptas como requisito operativo previo a reutilización."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre canónico de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No modificar datos de alumno, matrícula o figura docente sin verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusión.",
    "Alinear cada entrega al producto solicitado por planeación o rúbrica.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rúbrica y tipo de producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Vincular cada argumento al problema jurídico planteado.",
    "No asumir que fuentes de otras semanas o materias aplican automáticamente.",
    "Registrar en preguntas abiertas cualquier vacío de consigna local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa del esquema de memoria.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar correspondencia entre consigna, rúbrica y producto entregable.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar documentclass article en español, letterpaper y oneside salvo consigna distinta.",
    "Mantener metadatos institucionales y académicos completos antes de redactar contenido.",
    "Usar español académico con terminología jurídica consistente.",
    "Compilar sin errores críticos, sin referencias rotas y sin claves faltantes.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar consistencia de nombres de archivo, slug y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar solo fuentes pertinentes a la actividad concreta.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y gates de calidad.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar arrastre de redacción literal o contenido temático específico del origen.",
    "Mantener estrategia progresiva y conservadora: sumar mejoras verificables sin regresión.",
    "Aplicar compresión lossless por unión y deduplicación."
  ],
  "open_questions": [
    "Confirmar si LDE-S3B1 es obligatorio en todos los entregables. [supuesto]",
    "Confirmar vigencia de datos de alumno, matrícula y figura docente en plantilla. [supuesto]",
    "Confirmar formato obligatorio por actividad: reporte, presentación u otro.",
    "Confirmar rúbrica oficial vigente para calibrar profundidad argumentativa.",
    "Validar corrección definitiva de rutas corruptas en README (reporte/referencias).",
    "Validar sustitución definitiva del placeholder de slug .bib en README y programa analítico."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada, 8 créditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar trazabilidad entre consigna, argumentación y cierre jurídico.",
      "Sostener continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Frases directas y comprobables.",
      "Separación nítida entre marco conceptual y postura propia.",
      "Etiquetado explícito de [supuesto] cuando falte confirmación documental."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización JSON",
        "Consistencia LaTeX/BibTeX",
        "Producto alineado a consigna"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "El marco institucional fija tono, forma y estándar de argumentación."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusión depende del sustento verificable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y pérdida de trazabilidad."
        },
        {
          "source": "Producto alineado a consigna",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La estructura se ajusta al entregable requerido por actividad."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analítico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib con fuentes institucionales base.",
        "Regla institucional heredada: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura funcional completa.",
      "Se preservaron gates críticos de parseo JSON y normalización manual.",
      "Se reforzó transferencia transversal por abstracciones estables, no por contenido temático.",
      "Se mantuvieron supuestos abiertos donde falta consigna o validación local."
    ]
  }
}