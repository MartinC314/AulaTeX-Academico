```json
{
  "summary": [
    "Se consolida cerebro editorial mínimo para materia destino con sincronización transversal.",
    "Se preservan reglas institucionales UnADM y ejes editoriales comunes.",
    "Se transfieren solo abstracciones estables desde actividad origen.",
    "Se evita transferencia de contenido temático específico de Filosofía del Derecho.",
    "Se refuerza normalización estructurada y validación JSON como prerrequisito.",
    "La compresión se realiza por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo artefacto.",
    "Conservar adscripción a Licenciatura en Derecho.",
    "Usar nombre oficial de la materia destino.",
    "Respetar ubicación curricular local confirmada.",
    "Marcar como supuesto todo dato heredado no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No transferir metadatos curriculares de otra asignatura."
  ],
  "structure_rules": [
    "Usar README de la materia como entrada canónica.",
    "Alinear todo producto a ejes: problema, conceptos, evidencia, análisis, conclusión.",
    "Separar claramente reporte, presentación y bibliografía.",
    "Usar programa analítico como guía editorial.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar siempre con conclusión transferible a la práctica jurídica."
  ],
  "activity_rules": [
    "Iniciar cada actividad con encuadre del problema jurídico o social.",
    "Integrar conceptos culturales y jurídicos pertinentes con puente argumentativo.",
    "Distinguir evidencia, interpretación y postura personal.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
    "Relacionar el producto con la planeación semanal."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar consistencia entre metadatos y malla curricular local.",
    "No aceptar afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar existencia y uso correcto del .bib local.",
    "Normalizar manualmente salidas no estructuradas en ciclos tempranos."
  ],
  "latex_rules": [
    "Usar plantilla base .tex de la materia destino.",
    "Mantener configuración en español y codificación correcta.",
    "No cambiar clase o formato sin justificación académica.",
    "Actualizar títulos y subtítulos por actividad.",
    "Resolver tokens dinámicos antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes verificables y consultables.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales.",
    "Conservar metadatos mínimos completos.",
    "Distinguir bibliografía base de bibliografía específica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas.",
    "Compartir solo abstracciones editoriales estables entre nodos transversales.",
    "Etiquetar como provisional toda regla heredada de otra disciplina.",
    "Registrar alertas de parseo como memoria reutilizable.",
    "Evitar regresiones respecto a reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de evaluación de la materia destino.",
    "Confirmar si todas las actividades requieren conclusión jurídica explícita.",
    "Confirmar estándar único de citas para la licenciatura.",
    "Confirmar fuentes base oficiales adicionales de la asignatura.",
    "Confirmar nombre canónico definitivo del archivo .bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y preciso",
        "Argumentativo con criterio propio",
        "Sensible al contexto cultural mexicano"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Trazabilidad de fuentes",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia obligatoria",
        "Ubicación curricular verificada",
        "Coherencia con programa analítico"
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida",
      "Conceptos pertinentes al contexto mexicano",
      "Evidencia verificable",
      "Análisis propio del estudiante",
      "Conclusión transferible a la práctica jurídica"
    ],
    "reason_for_being": [
      "Orientar productos académicos claros y transferibles",
      "Asegurar coherencia institucional y editorial",
      "Facilitar sincronización transversal sin pérdida de reglas"
    ],
    "style_markers": [
      "Objetivo explícito",
      "Secciones funcionales",
      "Supuestos marcados",
      "Cierre con valor profesional"
    ],
    "argumentative_patterns": [
      "Problema → conceptos → evidencia → análisis → conclusión",
      "Afirmación → fuente → interpretación propia",
      "Coherencia entre pregunta y respuesta final"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Normalización estructurada",
        "Validación JSON"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas y trazabilidad."
        },
        {
          "source": "Validación JSON",
          "target": "Normalización estructurada",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay propagación confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El criterio personal se legitima con respaldo."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión útil surge del razonamiento."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        "Malla curricular UnADM",
        "Reglas institucionales UnADM heredadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan gates de calidad y validación JSON.",
      "Se consolida patrón argumentativo común entre materias.",
      "Se preserva identidad UnADM sin introducir contenido temático ajeno.",
      "Se mantiene estrategia progresiva y conservadora en ciclo 2."
    ]
  }
}
```