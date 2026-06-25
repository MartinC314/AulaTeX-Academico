```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad de Filosofía del Derecho hacia la materia de Responsabilidad Civil y Daños.",
    "La transferencia es transversal y conservadora; no se mueve contenido temático literal.",
    "Se refuerzan identidad UnADM, estructura argumentativa reusable y controles de calidad.",
    "La compresión es lossless por unión y deduplicación.",
    "Se preservan alertas técnicas y supuestos locales del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar Licenciatura en Derecho como marco curricular obligatorio.",
    "Marcar como supuesto todo dato no confirmado por guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al solicitado en la planeación semanal.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Formular un problema jurídico propio del ámbito de la responsabilidad civil y el daño.",
    "Sustentar afirmaciones con fuentes verificables o marcarlas como análisis propio.",
    "Incluir postura argumentada; evitar entregas solo descriptivas.",
    "No arrastrar contenidos filosóficos si no son funcionales al daño o la responsabilidad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Confirmar coherencia entre problema, desarrollo y conclusión.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver.",
    "Completar plantillas antes de compilar; marcar truncamientos como supuesto técnico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos: autor, título, año y fuente.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático puntual.",
    "Normalizar manualmente salidas no estructuradas antes de propagar.",
    "Mantener alertas técnicas como controles editoriales generales.",
    "Respetar estrategia progresiva y conservadora del ciclo."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención definitiva de nombres con 'danos' versus 'daños'.",
    "Validar código de curso LDE-S6B1 con fuente documental.",
    "Completar y verificar la plantilla .tex truncada.",
    "Confirmar rúbricas específicas por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio",
        "Orientado a práctica profesional"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada previa a propagación"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 1, obligatoria, 8 créditos",
        "Asignatura: Derecho de la responsabilidad civil y daños"
      ]
    },
    "essence": [
      "Problema jurídico",
      "Marco normativo y doctrinal",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Responsabilidad civil como eje",
      "Daño como categoría central"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y transferencia profesional.",
      "Transformar planeaciones semanales en reportes y presentaciones estructuradas.",
      "Asegurar coherencia entre identidad institucional y práctica jurídica."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte evidencia",
      "Estructura por secciones funcionales",
      "Cierre con utilidad profesional",
      "Separación estricta entre fuentes y análisis propio"
    ],
    "argumentative_patterns": [
      "Problema inicial breve",
      "Desarrollo conceptual y normativo con fuentes",
      "Análisis propio con contraste de ideas",
      "Conclusión aplicada a casos reales o hipotéticos"
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
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La imputación de responsabilidad se articula a partir de la existencia de un daño."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis se construye sobre una pregunta jurídica claramente formulada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base normativa verificable."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Archivo .bib institucional",
        "Reglas editoriales heredadas y deduplicadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes estables: problema, fuentes, análisis y conclusión.",
      "Se conserva identidad UnADM sin regresión.",
      "Se sincroniza grafo conceptual sin traslado temático literal."
    ]
  }
}
```