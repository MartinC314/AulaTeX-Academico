```json
{
  "summary": [
    "Se consolida cerebro editorial de materia con identidad UnADM para Derecho de la Contratación Internacional.",
    "Se heredan solo abstracciones editoriales estables desde actividad no equivalente.",
    "Se refuerza normalización estructurada, compresión union-dedupe y gates de calidad.",
    "Se mantiene trazabilidad y advertencia histórica de incidentes JSON."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura y coursecode local cuando aplique.",
    "Marcar como supuesto cualquier dato no confirmado por planeación oficial.",
    "Conservar trazabilidad del nodo origen y de fuentes provisionales.",
    "No propagar redacción literal entre nodos no equivalentes."
  ],
  "structure_rules": [
    "Alinear toda entrega al eje reusable: problema, conceptos/normas, análisis propio, conclusión.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Transformar planeación semanal en el producto solicitado.",
    "Agregar fuentes específicas de actividad al .bib local.",
    "No eliminar reglas útiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Identificar el problema jurídico que activa la actividad.",
    "Sustentar afirmaciones con norma, doctrina o evidencia verificable.",
    "Diferenciar resumen descriptivo y postura propia.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Declarar límites del análisis cuando falten datos."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Confirmar respaldo de toda afirmación normativa.",
    "Verificar consistencia entre README, programa y plantillas.",
    "Normalizar manualmente herencias de ciclos tempranos si reaparecen."
  ],
  "latex_rules": [
    "Mantener plantilla base article en español y letterpaper.",
    "Conservar macros institucionales; no sustituir por texto libre.",
    "Completar títulos y metadatos de actividad.",
    "Evitar paquetes o cambios de clase sin justificación verificable.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el BibTeX local de la materia como repositorio principal.",
    "No inventar fuentes; registrar solo documentos consultables.",
    "Priorizar fuentes institucionales y jurídicas aplicables.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas no consultadas en la actividad destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos.",
    "Aplicar deduplicación semántica por regla, no por recorte.",
    "No sobrescribir reglas locales más específicas.",
    "Conservar avisos de incidentes hasta su resolución."
  ],
  "open_questions": [
    "Confirmar planeación oficial y formatos por tipo de actividad.",
    "Definir formato uniforme de citas jurídicas.",
    "Resolver placeholders y rutas corruptas en README y programa.",
    "Confirmar resolución definitiva del incidente JSON histórico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": ["Formal académico", "Claro", "Argumentativo"],
      "institutional": ["Alineación UnADM", "Integridad académica", "Citas verificables"],
      "curricular": ["Licenciatura en Derecho", "Semestre 6, Bloque 2", "Transferencia profesional"]
    },
    "essence": [
      "Problema jurídico como detonante.",
      "Marco normativo y doctrinal verificable.",
      "Análisis propio con criterio jurídico.",
      "Conclusión transferible a la práctica."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento y transferencia profesional."
    ],
    "style_markers": [
      "Supuestos explícitos.",
      "Separación clara entre descripción y postura.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema → marco normativo → evidencia → análisis → conclusión.",
      "Afirmación jurídica → fuente → interpretación propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica",
        "Normalización estructurada",
        "Compresión lossless",
        "Trazabilidad de herencia"
      ],
      "citations": ["unadmMallaDerecho2024", "unadmSitioWeb"],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se activa por la pregunta jurídica central."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión debe sostenerse en norma y doctrina."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia.",
        "BibTeX local institucional.",
        "Registros de incidentes JSON y gates activos."
      ]
    },
    "reinforcement_log": [
      "Se preservan ejes editoriales transferibles.",
      "Se refuerzan gates de calidad y normalización.",
      "Se mantiene identidad UnADM sin regresión."
    ]
  }
}
```