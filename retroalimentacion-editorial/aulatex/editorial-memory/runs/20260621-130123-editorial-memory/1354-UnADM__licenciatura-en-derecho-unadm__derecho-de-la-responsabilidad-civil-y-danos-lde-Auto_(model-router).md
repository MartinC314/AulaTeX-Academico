```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde una actividad de Filosofía del Derecho hacia la materia de Responsabilidad Civil y Daños.",
    "La transferencia es transversal, conservadora y sin arrastre temático literal.",
    "Se refuerzan ejes editoriales reutilizables: problema, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene identidad institucional UnADM y control estricto de normalización JSON.",
    "Se consolida cerebro editorial mínimo y verificable para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular confirmado de la materia destino.",
    "Marcar como supuesto cualquier dato no confirmado documentalmente.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "No declarar códigos, nombres o convenciones como oficiales sin fuente."
  ],
  "structure_rules": [
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Estructurar todo producto en: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Formular un problema jurídico alineado a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables o marcar análisis propio.",
    "Incluir postura argumentada; evitar textos solo descriptivos.",
    "No arrastrar contenidos de otras materias si no son compatibles."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas o placeholders.",
    "Aplicar control de no regresión sobre reglas útiles previas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas truncadas antes de compilar.",
    "Verificar nombres canónicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Conservar metadatos mínimos completos.",
    "Usar el .bib local de la materia como repositorio único."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos.",
    "Evitar transferencia de redacción literal o contenido temático puntual.",
    "Aplicar compresión por unión y deduplicación.",
    "Mantener alerta de normalización manual por antecedentes técnicos.",
    "Propagar recursivamente solo tras validación de JSON y estructura."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención definitiva de danos/daños en nombres de archivo.",
    "Validar si el código de curso es oficial.",
    "Completar y verificar plantilla .tex truncada.",
    "Confirmar fuentes obligatorias por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio",
        "Conservador ante datos no verificados",
        "Orientado a práctica profesional"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada previa a propagación",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia obligatoria",
        "Ubicación curricular confirmada por malla institucional"
      ]
    },
    "essence": [
      "Problema jurídico como detonador del análisis",
      "Marco conceptual y normativo verificable",
      "Análisis propio con postura argumentada",
      "Conclusión jurídica aplicable",
      "Transferencia a la práctica profesional"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente de la materia",
      "Garantizar coherencia institucional y académica",
      "Facilitar reutilización segura de estructuras editoriales",
      "Evitar regresiones y errores técnicos en LaTeX y bibliografía"
    ],
    "style_markers": [
      "Declaración explícita de supuestos",
      "Estructura por secciones funcionales",
      "Cierre con utilidad jurídica",
      "Separación clara entre fuente y análisis propio"
    ],
    "argumentative_patterns": [
      "Planteamiento del problema",
      "Exposición de conceptos y normas",
      "Análisis crítico",
      "Conclusión jurídica transferible"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Responsabilidad civil",
        "Daño",
        "Marco normativo",
        "Análisis propio",
        "Conclusión jurídica",
        "Normalización JSON"
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
          "source": "Marco normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La noción de daño es central para configurar la responsabilidad."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Archivo .bib institucional",
        "Plantilla .tex de la materia",
        "Reglas heredadas normalizadas sin regresión"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles del origen sin eliminación.",
      "Se deduplican reglas repetidas por unión semántica.",
      "Se refuerza identidad UnADM y estructura argumentativa reusable.",
      "Se evita traslado temático literal entre nodos no equivalentes."
    ]
  }
}
```