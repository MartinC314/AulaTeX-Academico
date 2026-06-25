{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y deduplicación sin pérdida.",
    "Se preserva el núcleo editorial estable compartido: problema, conceptos/normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene prioridad institucional: no propagar memoria no estructurada y bloquear salidas no JSON parseables.",
    "Se conserva identidad local del destino: UnADM, Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Se refuerza corrección operativa de placeholders y rutas corruptas en README y programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, formato y metadatos.",
    "Usar nombre canónico de asignatura: Derechos de la persona y familia.",
    "Conservar contexto curricular local verificado: semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No modificar datos de alumno o matrícula sin verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusión.",
    "Alinear cada entrega al producto solicitado por la planeación o rúbrica.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rúbrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar transferir contenido temático literal desde materias no equivalentes.",
    "Transferir solo patrones editoriales estables y reutilizables.",
    "Registrar vacíos de contexto como preguntas abiertas con marca [supuesto] cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de guardar o propagar.",
    "Normalizar respuestas no estructuradas antes de reutilización aguas abajo.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna vigente."
  ],
  "latex_rules": [
    "Mantener español académico con acentos correctos en .tex y .bib.",
    "Compilar sin errores críticos, sin referencias rotas y sin placeholders.",
    "Conservar claves BibTeX estables para evitar roturas de compilación.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar consistencia entre nombres de archivo, slug y referencias antes de compilar.",
    "No introducir comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Agregar solo fuentes realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y gates de calidad.",
    "Mantener compresión union-dedupe sin regresión de reglas útiles previas.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual sobre redacción literal.",
    "Etiquetar como provisionales las reglas heredadas sin verificación local.",
    "Si reaparece salida no estructurada, forzar normalización manual previa."
  ],
  "open_questions": [
    "Confirmar consignas y rúbricas específicas de actividades del destino para ajustar granularidad.",
    "Confirmar vigencia de datos de portada de plantilla (alumno, matrícula, figura docente). [supuesto]",
    "Confirmar resolución definitiva de rutas corruptas en README (reporte/referencias).",
    "Confirmar si LDE-S3B1 es obligatorio en todos los productos o solo en portada.",
    "Confirmar si habrá archivo .bib complementario por actividad o solo uno único por materia."
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
        "Semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problematizar, fundamentar, analizar y concluir con transferencia jurídica.",
      "Rastreabilidad completa entre consigna, evidencia y postura propia.",
      "Estabilidad técnica editorial: JSON válido, LaTeX compilable y bibliografía íntegra."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos sólidos y verificables.",
      "Preservar una memoria editorial reutilizable entre nodos sin arrastre temático indebido."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separación clara entre marco conceptual y postura propia.",
      "Etiquetado explícito de [supuesto] cuando falte verificación documental."
    ],
    "argumentative_patterns": [
      "Encuadre del problema.",
      "Marco conceptual-normativo.",
      "Análisis propio con evidencia.",
      "Conclusión jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización JSON",
        "Consistencia LaTeX/BibTeX",
        "Trazabilidad consigna-desarrollo-conclusión"
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
          "justification": "Define estándar de tono, forma y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad consigna-desarrollo-conclusión",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay propagación confiable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y pérdida de respaldo."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "Sostiene conclusiones jurídicas defendibles."
        },
        {
          "source": "Trazabilidad consigna-desarrollo-conclusión",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "Asegura coherencia entre objetivo y resultado."
        }
      ],
      "evidence": [
        "README local del destino.",
        "Programa analítico local del destino.",
        "Archivo derechos-de-la-persona-y-familia.bib con fuentes institucionales base.",
        "Regla persistente heredada: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se consolidan abstracciones estables transversales sin mover contenido temático de Filosofía del Derecho.",
      "Ciclo 13: se mantiene gate crítico de normalización para salidas no estructuradas.",
      "Ciclo 13: se refuerza núcleo editorial reusable y se deduplican reglas equivalentes.",
      "Ciclo 13: se preservan reglas útiles previas sin regresión."
    ]
  }
}