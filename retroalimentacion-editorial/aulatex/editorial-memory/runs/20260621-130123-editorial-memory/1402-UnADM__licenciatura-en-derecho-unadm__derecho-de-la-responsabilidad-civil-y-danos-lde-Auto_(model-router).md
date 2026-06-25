```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad de Filosofía del Derecho hacia materia de Responsabilidad Civil y Daños.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa reusable y gates de calidad.",
    "La transferencia es abstracta, no temática; no se arrastra contenido doctrinal específico.",
    "Se refuerza normalización JSON, identidad institucional y control de supuestos.",
    "Compresión aplicada por unión y deduplicación sin pérdida semántica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular confirmado de la materia destino.",
    "Marcar explícitamente como supuesto todo dato no confirmado por guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "Usar la carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear siempre el producto con la planeación y consigna vigentes."
  ],
  "activity_rules": [
    "Formular un problema jurídico pertinente a la responsabilidad civil y el daño.",
    "Integrar conceptos, normas y doctrina solo si son compatibles con la materia.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento jurídico, evidencia y análisis propio.",
    "No arrastrar contenido temático de asignaturas origen si no aplica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar que toda afirmación tenga fuente o esté marcada como análisis propio.",
    "Aplicar control de no regresión sobre reglas útiles heredadas.",
    "Detectar y corregir rutas truncadas y placeholders antes de compilar o propagar."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas truncadas antes de compilar.",
    "Verificar nombres de archivos y resolver tokens interpolados."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica.",
    "Registrar vacíos bibliográficos como preguntas abiertas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático puntual.",
    "Propagar recursivamente solo después de validación JSON y estructural.",
    "Mantener alertas técnicas como reglas editoriales generales.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención definitiva de danos/daños en todo el árbol.",
    "Validar código de curso oficial con fuente institucional.",
    "Completar y verificar plantilla LaTeX local truncada.",
    "Confirmar fuentes obligatorias por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio",
        "Conservador ante datos no verificados"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica y citas verificables",
        "Normalización estructurada obligatoria antes de propagación"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia obligatoria según malla institucional",
        "Ubicación curricular validada por fuente UnADM"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco conceptual y normativo verificable",
      "Análisis propio con postura académica",
      "Conclusión jurídica transferible",
      "Utilidad profesional del producto académico"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente para productos académicos en LaTeX.",
      "Garantizar coherencia institucional, calidad argumentativa y reutilización segura.",
      "Facilitar sincronización transversal entre asignaturas sin pérdida de identidad."
    ],
    "style_markers": [
      "Declaración explícita de supuestos",
      "Estructura seccional clara y repetible",
      "Cierre aplicado a la práctica jurídica",
      "Separación estricta entre fuente y análisis propio"
    ],
    "argumentative_patterns": [
      "Problema inicial contextualizado",
      "Desarrollo conceptual y normativo con fuentes",
      "Análisis crítico del estudiante",
      "Conclusión jurídica aplicada"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño"
      ],
      "citations": [
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
          "justification": "La conclusión requiere base normativa verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La noción de daño articula la responsabilidad civil."
        }
      ],
      "evidence": [
        "Programa analítico local",
        "README institucional",
        "Malla curricular UnADM"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales estables sin arrastre temático.",
      "Se mantiene control estricto de normalización JSON.",
      "No se eliminan reglas útiles previas; solo se deduplican.",
      "Se consolida identidad UnADM como núcleo persistente."
    ]
  }
}
```