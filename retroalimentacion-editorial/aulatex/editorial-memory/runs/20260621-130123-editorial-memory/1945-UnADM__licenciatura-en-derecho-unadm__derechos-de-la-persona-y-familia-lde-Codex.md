{
  "summary": [
    "Sincronización transversal consolidada con estrategia conservadora y sin regresión.",
    "Se preserva núcleo editorial estable: problema, conceptos y normas, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica: bloquear propagación de salidas no JSON parseable y normalizar antes de reutilizar.",
    "Se refuerza identidad UnADM y contexto curricular local del destino sin arrastrar contenido temático específico de Filosofía del Derecho.",
    "Se corrige a nivel de memoria el uso de abstractions reutilizables para materia destino no equivalente.",
    "Se mantiene alerta operativa por placeholders y rutas corruptas en README/programa analítico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar nombre canónico exacto: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No modificar datos de alumno o matrícula sin verificación local. [supuesto vigencia]"
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: marco conceptual-normativo, análisis propio y cierre.",
    "Alinear desarrollo con consigna, rúbrica y producto solicitado.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener trazabilidad explícita entre pregunta guía, desarrollo y conclusión."
  ],
  "activity_rules": [
    "Identificar primero consigna, rúbrica y producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar transferir contenido temático de otra materia sin validación de pertinencia. [supuesto]",
    "Registrar como pendientes los vacíos de contexto local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa del esquema de memoria antes de guardar.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones no verificadas.",
    "Verificar coherencia entre consigna, rúbrica, producto y artefacto final.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener español académico con acentos correctos en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar consistencia de nombres de archivo, slug y rutas antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analítico.",
    "No copiar bloques LaTeX completos en memoria; guardar solo reglas operativas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar solo fuentes pertinentes a cada actividad.",
    "No inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y gates de calidad.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar propagar redacción literal o contenido temático local de otra asignatura.",
    "Aplicar compresión lossless por unión-deduplicación sin recorte.",
    "Si reaparece salida no estructurada, forzar normalización manual antes de propagar."
  ],
  "open_questions": [
    "Confirmar vigencia de datos de alumno y matrícula en plantilla local. [supuesto]",
    "Confirmar figura docente vigente para metadatos finales.",
    "Confirmar si LDE-S3B1 debe figurar en todos los entregables.",
    "Confirmar corrección definitiva de rutas corruptas en README (reporte/referencias).",
    "Confirmar sustitución definitiva del placeholder de slug .bib en README y programa analítico.",
    "Confirmar plantillas obligatorias por tipo de actividad en esta materia."
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
      "Problema jurídico relevante.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos sólidos.",
      "Garantizar trazabilidad entre consigna, argumentación y cierre.",
      "Preservar calidad técnica y verificabilidad en LaTeX/BibTeX."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separación clara entre marco conceptual y postura propia.",
      "Etiquetado explícito de [supuesto] cuando falte evidencia documental.",
      "Consistencia terminológica jurídica."
    ],
    "argumentative_patterns": [
      "Problematizar.",
      "Fundamentar con norma/doctrina/evidencia.",
      "Analizar con criterio propio.",
      "Concluir con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización de memoria JSON",
        "Consistencia técnica LaTeX y BibTeX",
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
          "justification": "La identidad define tono, formato y exigencia de rigor."
        },
        {
          "source": "Normalización de memoria JSON",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización confiable."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez argumentativa depende de respaldo verificable."
        },
        {
          "source": "Consistencia técnica LaTeX y BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y pérdida de trazabilidad."
        },
        {
          "source": "Producto alineado a consigna",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La forma del entregable condiciona la organización del argumento."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analítico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla heredada validada: no reutilizar salidas no estructuradas sin normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicación completa de reglas repetidas sin pérdida semántica.",
      "Ciclo 3: se mantiene gate de JSON parseable como bloqueo duro.",
      "Ciclo 3: se transfiere solo abstracción editorial estable desde nodo transversal no equivalente.",
      "Ciclo 3: se preservan supuestos abiertos para contexto local no confirmado."
    ]
  }
}