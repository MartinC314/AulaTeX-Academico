```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad de Filosofía del Derecho hacia la materia de Responsabilidad Civil y Daños.",
    "La transferencia es transversal, conservadora y sin arrastre temático literal.",
    "Se refuerzan identidad UnADM, estructura argumentativa reusable y controles de calidad.",
    "La compresión aplicada es lossless por unión y deduplicación.",
    "El destino mantiene cerebro editorial mínimo y coherente con su contexto curricular."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto de Licenciatura en Derecho.",
    "Alinear toda entrega a la materia de Derecho de la responsabilidad civil y daños.",
    "Marcar como supuesto cualquier dato no confirmado por guía o fuente institucional.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "No declarar oficial ningún código, convención o nombre sin respaldo documental.",
    "Usar la carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico.",
    "Separar secciones funcionales: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al solicitado en la planeación semanal.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y bibliografía.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Formular un problema jurídico vinculado a responsabilidad civil y daño.",
    "Integrar conceptos, normas y doctrina pertinentes a la actividad.",
    "Incluir análisis propio y postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "No arrastrar contenido temático de otras materias si no es compatible.",
    "Separar claramente fundamento jurídico, evidencia y opinión académica.",
    "Incluir transferencia práctica en el cierre."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar que toda afirmación jurídica tenga fuente o esté marcada como análisis propio.",
    "Aplicar control de no regresión sobre reglas útiles heredadas.",
    "Detectar y corregir rutas truncadas, placeholders y caracteres rotos.",
    "Validar metadatos curriculares contra la malla institucional local."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en archivos .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas truncadas antes de compilar.",
    "Verificar coherencia entre metadatos del documento y la materia.",
    "Resolver tokens interpolados antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de cada actividad en el .bib local de la materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de redacción literal o contenido temático específico.",
    "Propagar reglas solo después de validación estructural.",
    "Mantener alertas técnicas como controles editoriales generales.",
    "Aplicar normalización manual en ciclos con antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención definitiva de nombres con danos/daños.",
    "Validar si el código de curso LDE-S6B1 es oficial.",
    "Completar y validar la plantilla LaTeX truncada.",
    "Confirmar rúbricas específicas de evaluación por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio",
        "Conservador ante datos no verificados",
        "Orientado a la práctica profesional"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica y citas verificables",
        "Normalización estructurada previa a propagación",
        "Entrada canónica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 1, obligatoria, 8 créditos",
        "Asignatura: Derecho de la responsabilidad civil y daños",
        "Ubicación curricular validada por malla institucional"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco conceptual y normativo verificable",
      "Análisis propio del estudiante",
      "Conclusión jurídica aplicable",
      "Transferencia a la práctica profesional",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente de la materia.",
      "Garantizar coherencia, calidad y transferibilidad de los productos académicos.",
      "Permitir propagación transversal sin pérdida de identidad ni rigor."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falta evidencia",
      "Estructura por secciones claras",
      "Cierre con criterio jurídico propio",
      "Separación estricta entre hechos, fuentes y opinión"
    ],
    "argumentative_patterns": [
      "Problema jurídico breve y contextualizado",
      "Exposición conceptual y normativa con fuentes",
      "Análisis crítico propio",
      "Conclusión jurídica aplicada y transferible"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad académica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis se construye a partir de una pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa y doctrinal."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La responsabilidad se articula a partir de la noción jurídica de daño."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "El marco institucional exige rigor y citas verificables."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Malla curricular institucional UnADM",
        "Plantillas LaTeX de la materia",
        "Reglas editoriales heredadas sin regresión"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes estables: problema, fuentes, análisis y conclusión.",
      "Se conserva identidad UnADM sin arrastre temático.",
      "Se mantienen controles estrictos de normalización y calidad.",
      "Se habilita propagación transversal segura entre nodos."
    ]
  }
}
```