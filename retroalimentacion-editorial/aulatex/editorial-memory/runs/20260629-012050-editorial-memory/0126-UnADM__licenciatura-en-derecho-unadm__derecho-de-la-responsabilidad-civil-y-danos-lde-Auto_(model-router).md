```json
{
  "summary": [
    "Se consolida un cerebro editorial mínimo para la materia Derecho de la responsabilidad civil y daños.",
    "Se sincronizan abstracciones editoriales estables desde Filosofía del Derecho sin transferir contenido temático.",
    "Se refuerza identidad institucional UnADM y patrón argumentativo reusable.",
    "Se preserva estrategia conservadora con normalización obligatoria y control de no regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto de Licenciatura en Derecho y materia de responsabilidad civil y daños.",
    "Aplicar ubicación curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Marcar como supuesto cualquier dato no confirmado por guía o documento oficial.",
    "Tratar memorias heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Alinear todo producto a: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Mantener separación explícita entre reporte, presentación, programa analítico y bibliografía.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Formular un problema jurídico que active la responsabilidad civil y el daño.",
    "Integrar normas, doctrina y datos pertinentes a la materia.",
    "Exigir postura argumentada del estudiante; evitar descripciones puras.",
    "Cerrar con conclusión jurídica y transferencia a la práctica profesional.",
    "No arrastrar contenido temático de otras materias si no es compatible."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Verificar que toda afirmación jurídica tenga fuente o se marque como análisis propio.",
    "Aplicar control de no regresión sobre reglas útiles previas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar y validar plantillas antes de compilar.",
    "Verificar nombres reales de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material jurídico verificable.",
    "Agregar fuentes específicas de cada actividad al .bib local de la materia.",
    "No inventar referencias; registrar preguntas abiertas si falta una fuente.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Mantener alerta de normalización manual por antecedentes técnicos.",
    "Preservar estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final de nombres de archivos: danos vs daños.",
    "Verificar si el código de curso LDE-S6B1 es oficial.",
    "Completar y validar la plantilla .tex truncada antes de uso extensivo."
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
        "Ubicación curricular verificable."
      ]
    },
    "essence": [
      "Problema jurídico como eje de análisis.",
      "Fundamento normativo y doctrinal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Identidad institucional UnADM."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, evidencia y transferencia profesional.",
      "Convertir planeación semanal en entregables estructurados.",
      "Garantizar coherencia editorial transversal entre materias."
    ],
    "style_markers": [
      "Frases cortas y secciones explícitas.",
      "Supuestos siempre marcados.",
      "Citas trazables al .bib local.",
      "Prioridad al contexto local del nodo destino."
    ],
    "argumentative_patterns": [
      "Planteamiento del problema.",
      "Marco conceptual y normativo.",
      "Análisis crítico con postura propia.",
      "Cierre con criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Responsabilidad civil",
        "Daño",
        "Fundamento normativo",
        "Análisis propio",
        "Conclusión jurídica",
        "Normalización estructurada"
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
          "justification": "El análisis se construye desde una cuestión delimitada."
        },
        {
          "source": "Fundamento normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión válida requiere soporte jurídico verificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación editorial",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico locales.",
        "Bibliografía institucional UnADM.",
        "Reglas heredadas consolidadas del nodo origen."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles previas sin regresión.",
      "Se refuerza patrón editorial estable y reusable.",
      "Se evita transferencia temática inaplicable.",
      "Se consolida sincronización transversal conservadora."
    ]
  }
}
```