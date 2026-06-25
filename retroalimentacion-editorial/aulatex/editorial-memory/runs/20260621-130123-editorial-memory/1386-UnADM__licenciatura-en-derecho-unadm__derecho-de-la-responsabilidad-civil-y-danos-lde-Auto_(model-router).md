```json
{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia la materia.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y control de calidad.",
    "La transferencia es abstracta, no temática ni literal.",
    "Se refuerza ADN editorial común: problema, fuentes, análisis propio y conclusión.",
    "Compresión aplicada por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto de Licenciatura en Derecho con enfoque en responsabilidad civil y daños.",
    "Marcar como supuesto cualquier dato no confirmado por guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar la carpeta de la materia como entrada canónica."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la planeación semanal vigente.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Formular un problema jurídico pertinente a la responsabilidad civil.",
    "Sustentar afirmaciones con fuentes verificables o marcarlas como análisis propio.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "No arrastrar contenido temático de otras materias si no es compatible."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Verificar correspondencia entre consigna, desarrollo y conclusión.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar compilación sin errores críticos ni referencias rotas.",
    "Resolver rutas truncadas y placeholders antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos: autor, título, año y fuente.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de cada actividad en el .bib local de la materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Aplicar normalización manual si se detectan salidas no estructuradas.",
    "Mantener alertas técnicas como control editorial general."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Definir convención final de uso: danos vs daños.",
    "Confirmar código oficial del curso si existe.",
    "Validar plantilla .tex por truncamientos antes de reutilizar."
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
        "Integridad académica con citas verificables",
        "Normalización estructurada previa a propagación",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia obligatoria según malla institucional",
        "Ubicación curricular validada por fuente UnADM"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco normativo y doctrinal verificable",
      "Análisis propio con postura argumentada",
      "Conclusión jurídica transferible",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Orientar productos académicos claros, fundados y aplicables.",
      "Garantizar coherencia editorial entre materias de la licenciatura.",
      "Facilitar transferencia metodológica entre nodos curriculares."
    ],
    "style_markers": [
      "Estructura por secciones funcionales.",
      "Declaración explícita de supuestos.",
      "Cierre con utilidad profesional.",
      "Separación clara entre fuente y opinión."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y contextualizado.",
      "Exposición conceptual y normativa con fuentes.",
      "Análisis propio con contraste de ideas.",
      "Conclusión jurídica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño",
        "Identidad institucional UnADM",
        "Normalización estructurada JSON"
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
          "justification": "El análisis se construye sobre una pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa y doctrinal verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La responsabilidad se articula a partir del daño jurídicamente relevante."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "El marco institucional exige citas verificables y formato consistente."
        }
      ],
      "evidence": [
        "README y programa analítico locales.",
        "Archivo .bib institucional.",
        "Plantilla .tex de la materia."
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales estables sin traslado temático literal.",
      "Se mantiene control estricto de normalización y calidad.",
      "No se elimina ninguna regla útil previa."
    ]
  }
}
```