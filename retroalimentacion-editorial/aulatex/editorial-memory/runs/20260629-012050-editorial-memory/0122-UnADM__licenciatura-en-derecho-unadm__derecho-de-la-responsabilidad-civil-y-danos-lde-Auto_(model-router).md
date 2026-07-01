```json
{
  "summary": [
    "Sincronización transversal conservadora aplicada desde actividad de Filosofía del Derecho hacia materia de Responsabilidad Civil y Daños.",
    "Se preservan reglas institucionales UnADM, estructura reusable y gates de calidad.",
    "Se transfiere patrón editorial estable sin contenido temático no equivalente.",
    "Se refuerza normalización estructurada y control técnico en ciclo 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Aplicar contexto local del destino antes que metadatos heredados.",
    "Marcar como supuesto todo dato no confirmado por documentos oficiales.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "No declarar códigos o convenciones como oficiales sin confirmación documental."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Alinear todo producto a: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Mantener separación explícita entre reporte, presentación, programa analítico y bibliografía.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables o marcarlas como análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar reglas heredadas solo si son compatibles con la materia destino.",
    "Evitar arrastrar contenido temático no aplicable."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Verificar correspondencia con la consigna o planeación semanal.",
    "Control de no regresión sobre reglas útiles previas.",
    "Detectar y corregir truncamientos, rutas rotas y placeholders."
  ],
  "latex_rules": [
    "Usar codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar compilación sin errores críticos.",
    "Completar plantillas truncadas antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Priorizar fuentes institucionales UnADM y material jurídico verificable."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Aplicar compresión por unión y deduplicación, sin recorte semántico.",
    "En ciclo 1, aplicar normalización manual por antecedentes técnicos.",
    "Evitar transferir redacción literal o contenido temático específico."
  ],
  "open_questions": [
    "Confirmar guías oficiales de formato por actividad en la materia destino.",
    "Confirmar convención final de nombres con 'danos/daños'.",
    "Validar código de curso y plantillas locales antes de declararlos oficiales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Asignaturas UnADM",
        "Ubicación curricular verificable"
      ]
    },
    "essence": [
      "Problema jurídico como eje",
      "Fundamento normativo y doctrinal",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reusable.",
      "Asegurar coherencia académica transversal.",
      "Garantizar calidad y trazabilidad en productos LaTeX."
    ],
    "style_markers": [
      "Secciones explícitas",
      "Frases directas",
      "Supuestos siempre marcados",
      "Citas trazables al .bib"
    ],
    "argumentative_patterns": [
      "Planteamiento del problema",
      "Marco conceptual y normativo",
      "Análisis crítico con postura propia",
      "Cierre con criterio jurídico aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Fundamento normativo",
        "Análisis propio",
        "Conclusión jurídica",
        "Normalización estructurada",
        "Responsabilidad civil y daños"
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
          "justification": "El análisis se construye desde una pregunta guía delimitada."
        },
        {
          "source": "Fundamento normativo",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión requiere soporte verificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Bib local institucional",
        "Memoria de origen validada"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas útiles previas sin regresión.",
      "Se refuerza patrón editorial transversal.",
      "Se evita contaminación temática entre nodos no equivalentes."
    ]
  }
}
```