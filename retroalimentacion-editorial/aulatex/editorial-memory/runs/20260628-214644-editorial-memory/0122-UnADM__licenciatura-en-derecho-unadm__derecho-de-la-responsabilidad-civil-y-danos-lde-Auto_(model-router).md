```json
{
  "summary": [
    "Se consolida sincronización transversal conservadora desde actividad de Filosofía del Derecho hacia materia de Responsabilidad Civil y Daños.",
    "Se preservan reglas institucionales UnADM y patrón editorial estable reusable.",
    "Se refuerza normalización estructurada, control de calidad y ADN argumentativo.",
    "El destino mantiene cerebro editorial mínimo con contexto local confirmado.",
    "No se transfiere contenido temático específico no equivalente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Aplicar primero el contexto local del destino antes de reglas heredadas.",
    "Marcar como supuesto todo dato no confirmado por documentos oficiales.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "No declarar oficiales códigos o convenciones sin fuente institucional."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Alinear todo producto a: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Mantener separación explícita entre reporte, presentación, programa analítico y .bib.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Formular un problema jurídico pertinente a responsabilidad civil y daños.",
    "Separar fundamento normativo/doctrinal, evidencia y análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar reglas heredadas solo si son compatibles con la materia destino."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Verificar que toda afirmación jurídica tenga fuente o marca de análisis propio.",
    "Aplicar control de no regresión sobre reglas útiles previas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar codificación correcta y acentos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas truncadas antes de compilar.",
    "Verificar nombres de archivos y resolver tokens interpolados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material jurídico verificable.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "En ciclo 1, exigir normalización manual antes de reutilizar.",
    "Propagar recursivamente solo después de pasar quality gates."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final de nombres con 'danos' versus 'daños'.",
    "Confirmar código oficial del curso si aplica.",
    "Validar y completar plantilla LaTeX local truncada.",
    "Confirmar fuentes obligatorias por semana."
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
        "Integridad académica y citas verificables.",
        "Normalización estructurada obligatoria."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la responsabilidad civil y daños.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico como eje articulador.",
      "Fundamento normativo y doctrinal verificable.",
      "Análisis propio con postura argumentada.",
      "Conclusión jurídica transferible.",
      "Identidad institucional UnADM."
    ],
    "reason_for_being": [
      "Orientar productos académicos claros, fundamentados y transferibles.",
      "Transformar la planeación semanal en entregables estructurados.",
      "Garantizar reutilización segura de memoria editorial."
    ],
    "style_markers": [
      "Secciones explícitas y orden lógico.",
      "Supuestos siempre marcados.",
      "Citas trazables al .bib local.",
      "Lenguaje jurídico preciso y sobrio."
    ],
    "argumentative_patterns": [
      "Planteamiento del problema.",
      "Marco conceptual y normativo.",
      "Análisis crítico con criterio propio.",
      "Cierre con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Fundamento normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil y daños",
        "Normalización estructurada",
        "Integridad de citación"
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
          "justification": "El análisis se construye desde una pregunta jurídica delimitada."
        },
        {
          "source": "Fundamento normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere soporte normativo verificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura y JSON válido no hay reutilización segura."
        },
        {
          "source": "Reglas heredadas",
          "target": "Materia destino",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones, no contenido temático específico."
        }
      ],
      "evidence": [
        "README y programa analítico locales.",
        "Bib local institucional.",
        "Memoria origen validada por deduplicación."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales sin regresión.",
      "Se refuerza patrón editorial estable transversal.",
      "Se excluye contenido no equivalente entre materias.",
      "Se mantiene control técnico y de calidad."
    ]
  }
}
```