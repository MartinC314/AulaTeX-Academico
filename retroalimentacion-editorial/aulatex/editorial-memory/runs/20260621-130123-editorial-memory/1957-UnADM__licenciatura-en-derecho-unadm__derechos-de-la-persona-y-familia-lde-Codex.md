{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Derechos de la persona y familia.",
    "Se preserva el núcleo editorial estable: problema, conceptos y normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene la regla crítica de normalización: no propagar salidas no estructuradas ni JSON inválido.",
    "Se consolida la identidad UnADM y el contexto curricular local del destino.",
    "Se refuerza la corrección de placeholders y rutas corruptas en README y programa analítico como requisito operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar nombre canónico de asignatura: Derechos de la persona y familia.",
    "Alinear contenido al contexto local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No modificar datos de alumno o matrícula sin verificación local. [supuesto vigencia]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusión.",
    "Alinear la entrega al producto solicitado por la planeación o rúbrica vigente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rúbrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar resumen descriptivo puro.",
    "Evitar texto genérico; vincular cada argumento al problema jurídico planteado.",
    "No trasladar contenido temático de otra materia sin validación de pertinencia. [supuesto]",
    "Registrar vacíos de contexto en preguntas abiertas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa del esquema antes de guardar memoria.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar coherencia entre consigna, producto solicitado y artefacto final.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar documentclass article en español, letterpaper y oneside salvo consigna distinta.",
    "Mantener codificación correcta para acentos y caracteres en español en .tex y .bib.",
    "Usar títulos, subtítulos, asignatura y código de curso coherentes con la actividad.",
    "Compilar sin errores críticos, sin referencias rotas y sin placeholders sin resolver.",
    "Corregir tokens dinámicos tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar consistencia de nombres de archivo: reporte y carpeta de referencias."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Conservar y reutilizar fuentes institucionales base ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "No inventar referencias; marcar faltantes como pendiente.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redacción literal y contenido temático no equivalente.",
    "Mantener estrategia progresiva y conservadora sin regresión de reglas útiles."
  ],
  "open_questions": [
    "Confirmar si el dato de alumno y matrícula de la plantilla sigue vigente. [supuesto]",
    "Confirmar si LDE-S3B1 debe aparecer en todos los productos evaluables.",
    "Confirmar rúbricas activas por actividad en la materia destino.",
    "Validar corrección definitiva de rutas corruptas en README (reporte/referencias).",
    "Validar sustitución definitiva del placeholder de .bib en README y programa analítico."
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
      "Problema jurídico o social como punto de partida.",
      "Fundamentación con conceptos, normas y doctrina pertinentes.",
      "Análisis propio sustentado con evidencia.",
      "Cierre con conclusión jurídica aplicable.",
      "Normalización estructurada antes de toda propagación."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre consigna, argumentación y resultado.",
      "Preservar calidad jurídica y trazabilidad técnica editorial."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separación nítida entre marco conceptual y postura propia.",
      "Etiquetado explícito de [supuesto] cuando falte confirmación documental."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma y doctrina.",
      "Analizar con criterio propio.",
      "Concluir con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización JSON",
        "Consistencia LaTeX/BibTeX",
        "Problema-conceptos-evidencia-análisis-conclusión"
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
          "justification": "El marco institucional fija tono, formato y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay trazabilidad reutilizable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y pérdidas de respaldo."
        },
        {
          "source": "Problema-conceptos-evidencia-análisis-conclusión",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "Define el patrón reusable de redacción académica jurídica."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analítico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib con fuentes institucionales base.",
        "Regla consolidada: bloquear propagación ante JSON inválido.",
        "Hallazgo operativo: placeholders de slug y rutas corruptas requieren corrección previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se transfieren abstracciones estables sin arrastre temático de Filosofía del Derecho.",
      "Ciclo 6: se preservan reglas previas útiles y se eliminan duplicados semánticos.",
      "Ciclo 6: se refuerza gate de normalización estructurada como condición de propagación recursiva.",
      "Ciclo 6: se mantiene ADN editorial UnADM con enfoque jurídico aplicado y verificable."
    ]
  }
}