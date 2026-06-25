```json
{
  "summary": [
    "Se refuerza el cerebro editorial de la materia con abstracciones estables heredadas.",
    "Sincronización transversal aplicada sin traslado temático literal.",
    "Se preservan reglas útiles previas y se deduplican por unión.",
    "Se consolida estructura argumentativa reusable UnADM.",
    "Se mantiene estrategia progresiva y conservadora en ciclo 2."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado por guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "No declarar oficiales códigos o convenciones sin fuente documental."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Separar secciones funcionales: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear siempre el producto con la planeación semanal.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y bibliografía.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Formular un problema jurídico propio del daño o la responsabilidad civil.",
    "Sustentar afirmaciones con fuentes verificables o marcar análisis propio.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No arrastrar contenido temático incompatible desde otras materias."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas o placeholders.",
    "Aplicar control estricto de no regresión de reglas útiles."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas truncadas antes de compilar.",
    "Verificar nombres de archivos y rutas antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Registrar fuentes locales en el .bib canónico de la materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener alertas técnicas como controles editoriales generales."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención final de nombres con danos/daños.",
    "Verificar carácter oficial del código de curso.",
    "Completar y validar plantilla .tex local.",
    "Confirmar fuentes obligatorias por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica y citas verificables",
        "Entrada canónica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 1, obligatoria, 8 créditos",
        "Asignatura de responsabilidad civil y daños"
      ]
    },
    "essence": [
      "Problema jurídico como eje",
      "Marco normativo y doctrinal verificable",
      "Análisis propio argumentado",
      "Conclusión jurídica transferible",
      "Identidad institucional consistente"
    ],
    "reason_for_being": [
      "Orientar productos académicos claros y transferibles",
      "Garantizar integridad académica y estructura reusable",
      "Facilitar propagación segura entre nodos"
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia",
      "Secciones funcionales y verificables",
      "Cierre con utilidad profesional",
      "Normalización estructurada obligatoria"
    ],
    "argumentative_patterns": [
      "Problema inicial breve",
      "Fundamentación normativa y doctrinal",
      "Análisis crítico propio",
      "Conclusión aplicada"
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Responsabilidad civil",
        "Daño",
        "Marco normativo",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Identidad institucional UnADM"
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
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La responsabilidad se articula a partir de la noción de daño."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Archivo .bib institucional",
        "Plantilla .tex local con incidencias técnicas marcadas como supuesto"
      ]
    },
    "reinforcement_log": [
      "Se integran ejes editoriales estables desde Filosofía del Derecho.",
      "No se transfiere contenido temático literal.",
      "Se mantiene compresión lossless por deduplicación.",
      "Ciclo 2 conserva reglas útiles sin regresión."
    ]
  }
}
```