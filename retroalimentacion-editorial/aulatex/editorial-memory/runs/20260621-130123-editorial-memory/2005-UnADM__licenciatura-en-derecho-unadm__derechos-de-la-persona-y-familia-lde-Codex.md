{
  "summary": [
    "Se consolida sincronización transversal conservadora desde actividad origen hacia materia destino sin arrastre temático no equivalente.",
    "Se preserva núcleo editorial estable: problema, conceptos-normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene regla crítica de normalización: no propagar salidas no JSON parseable.",
    "Se refuerza identidad UnADM y contexto curricular local del destino como fuente primaria.",
    "Se incorpora corrección operativa de placeholders y rutas corruptas en README y programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, formato y metadatos.",
    "Usar nombre canónico de asignatura: Derechos de la persona y familia.",
    "Alinear a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Usar carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No modificar datos de alumno y matrícula sin verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: marco conceptual-normativo, análisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusión.",
    "Alinear el formato final al producto solicitado en planeación o rúbrica.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rúbrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar transferencia literal de contenidos de Filosofía del Derecho al destino.",
    "Registrar vacíos de contexto en preguntas abiertas.",
    "No asumir fuentes de semanas o materias distintas sin validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de guardar memoria.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar coherencia entre consigna, producto y estructura de entrega.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener español académico con acentos correctos en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Conservar claves BibTeX estables.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivo canónicos antes de compilar.",
    "Actualizar documentsubtitle al número real de actividad.",
    "Conservar article, letterpaper y oneside salvo consigna distinta."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Priorizar fuentes institucionales UnADM y normativa verificable.",
    "Agregar solo fuentes pertinentes a la actividad concreta.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras pasar gates de JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Evitar propagar redacción literal o contenido temático específico del origen.",
    "Mantener estrategia progresiva y conservadora sin regresión."
  ],
  "open_questions": [
    "Confirmar si el dato de figura docente ya está definido. [supuesto]",
    "Confirmar vigencia de datos de alumno y matrícula en plantilla. [supuesto]",
    "Confirmar si LDE-S3B1 debe mostrarse en todos los entregables.",
    "Confirmar producto obligatorio por actividad cuando exista consigna local.",
    "Validar corrección definitiva de nombres corruptos en README (reporte/referencias).",
    "Validar sustitución definitiva de placeholders de slug .bib."
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
        "Entrada canónica desde carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada, 8 créditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problematizar, fundamentar, analizar y concluir con utilidad jurídica.",
      "Sostener cada afirmación con evidencia verificable.",
      "Conservar consistencia técnica entre narrativa, LaTeX y BibTeX."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar transferencia profesional del razonamiento jurídico.",
      "Preservar memoria editorial reutilizable sin pérdida."
    ],
    "style_markers": [
      "Frases cortas y verificables.",
      "Separación clara entre marco conceptual y postura propia.",
      "Etiquetado explícito de [supuesto] cuando falte confirmación."
    ],
    "argumentative_patterns": [
      "Iniciar con problema jurídico concreto.",
      "Fundamentar con norma, doctrina o fuente institucional.",
      "Desarrollar análisis propio con criterio jurídico.",
      "Cerrar con conclusión transferible a práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización JSON de memoria",
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
          "justification": "El marco institucional define tono y forma de argumentar."
        },
        {
          "source": "Normalización JSON de memoria",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez del cierre depende del sustento verificable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita citas rotas y pérdida de trazabilidad."
        },
        {
          "source": "Producto alineado a consigna",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La consigna determina profundidad y formato del argumento."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analítico de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib con fuentes institucionales base.",
        "Regla heredada validada: no reutilizar salidas no estructuradas sin normalizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicación lossless aplicada sobre reglas repetidas del origen y destino.",
      "Ciclo 18: se preservan reglas útiles previas y se evita regresión.",
      "Ciclo 18: se transfiere solo abstracción editorial estable por relación transversal.",
      "Ciclo 18: se mantiene alerta histórica de salidas no JSON parseable como gate permanente."
    ]
  }
}