```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad origen hacia materia destino.",
    "Se preservan reglas institucionales UnADM, estructura reusable y gates de calidad.",
    "La compresión aplicada es lossless por unión y deduplicación semántica.",
    "Se refuerza el cerebro editorial mínimo de la materia destino.",
    "No se transfiere redacción literal ni contenidos específicos de Filosofía del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de la asignatura destino.",
    "Vincular siempre a Licenciatura en Derecho.",
    "Marcar como supuesto todo dato no confirmado por planeación oficial.",
    "Conservar trazabilidad explícita de reglas heredadas.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar esquema base de cinco ejes: problema, conceptos/normas, producto, análisis propio, conclusión.",
    "Usar la carpeta de materia como entrada canónica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar claramente marco normativo/doctrinal y análisis propio.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Identificar el problema jurídico o social que activa la actividad.",
    "Sustentar afirmaciones con norma, doctrina o evidencia verificable.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Declarar límites del análisis cuando falten datos.",
    "Alinear el producto final a la consigna de la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar respaldo o supuesto en toda afirmación.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente herencias de ciclo 1 antes de propagar."
  ],
  "latex_rules": [
    "Conservar plantilla base article en español y formato institucional.",
    "No sustituir macros institucionales por texto libre.",
    "Evitar paquetes o clases no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens o rutas corruptas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el BibTeX local de la materia como repositorio principal.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas si no se usaron en la actividad destino."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Evitar transferir redacción literal o ejemplos específicos.",
    "Mantener avisos de incidentes JSON hasta su resolución.",
    "Aplicar deduplicación semántica sin eliminar reglas útiles."
  ],
  "open_questions": [
    "Confirmar formato uniforme de citas jurídicas para la materia.",
    "Confirmar checklist mínimo por tipo de actividad.",
    "Confirmar planeación oficial específica de actividades.",
    "Confirmar corrección definitiva de placeholders en README y programa."
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
        "Integridad académica",
        "Trazabilidad editorial"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia obligatoria",
        "Transferencia profesional del conocimiento"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco normativo y doctrinal verificable",
      "Análisis propio sustentado",
      "Conclusión jurídica aplicable"
    ],
    "reason_for_being": [
      "Estandarizar productos académicos con rigor jurídico.",
      "Permitir reutilización segura de reglas editoriales.",
      "Facilitar coherencia transversal entre asignaturas."
    ],
    "style_markers": [
      "Frases cortas y funcionales",
      "Secciones explícitas",
      "Supuestos claramente etiquetados",
      "Cierre con aplicación práctica"
    ],
    "argumentative_patterns": [
      "Problema -> marco -> análisis -> conclusión",
      "Afirmación -> evidencia -> inferencia jurídica",
      "Descripción breve -> postura propia sustentada"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo y doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Normalización JSON",
        "Trazabilidad editorial"
      ],
      "citations": [
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis se construye a partir de un problema delimitado."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable permite reutilización auditable."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        "BibTeX local institucional",
        "Reglas heredadas validadas por deduplicación"
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales UnADM.",
      "Se refuerza el esquema de cinco ejes como patrón transversal.",
      "Se mantiene control de supuestos y calidad.",
      "Se evita regresión y copia literal."
    ]
  }
}
```