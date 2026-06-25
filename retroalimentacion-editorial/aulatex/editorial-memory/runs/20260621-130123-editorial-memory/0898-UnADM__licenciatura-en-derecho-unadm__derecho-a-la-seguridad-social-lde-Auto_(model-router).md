```json
{
  "summary": [
    "Se sincroniza memoria editorial transversal desde actividad no equivalente hacia materia.",
    "Se preservan reglas institucionales UnADM y patron editorial comun reutilizable.",
    "Se refuerza estructura por ejes y control de calidad sin transferir contenido tematico.",
    "La compresion aplicada es union-dedupe, sin perdida ni regresion.",
    "Se consolida cerebro editorial minimo para Derecho a la Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "No mezclar contenido tematico de otras materias; solo abstraer reglas estables.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas provisionales."
  ],
  "structure_rules": [
    "Usar README de la materia como canon estructural.",
    "Alinear todo producto a ejes reutilizables: problema, marco, evidencia, analisis, conclusion.",
    "Separar claramente marco normativo, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social desde el inicio.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura academica propia; evitar solo resumen.",
    "Ajustar formato y alcance al producto solicitado por planeacion.",
    "Relacionar el desarrollo con el campo de seguridad social cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Confirmar coherencia entre objetivo, desarrollo y conclusion.",
    "Verificar respaldo o marca de [supuesto] en afirmaciones relevantes.",
    "Validar correspondencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia; personalizar solo campos variables.",
    "Mantener codificacion correcta en español y compilacion sin errores.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivo y rutas antes de compilar.",
    "Mantener claves BibTeX estables."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "Conservar metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenido tematico.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida para la materia [supuesto].",
    "Verificar si existen consignas especificas de actividades iniciales.",
    "Confirmar nombre oficial de figura docente para plantillas.",
    "Revisar si hay jurisprudencia obligatoria indicada en planeaciones.",
    "Confirmar vigencia de fuentes provisionales heredadas [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Normalizacion estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Uso de datos curriculares oficiales del destino"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables.",
      "Garantizar coherencia editorial transversal entre materias.",
      "Preservar identidad UnADM con calidad academica."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separacion visible entre marco, analisis y cierre",
      "Uso explicito de etiquetas [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
      "Contrastar evidencia",
      "Fijar postura propia sustentada",
      "Concluir con implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicado."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen estructura y proposito.",
        "Archivo .bib local confirma base normativa.",
        "Antecedentes de salida no parseable justifican gates estrictos."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patron comun problema–marco–analisis–conclusion.",
      "Se preserva identidad UnADM sin mezclar contenidos tematicos.",
      "Se mantiene control estricto de estructura y calidad.",
      "Se consolida cerebro editorial minimo y reconstruible."
    ]
  }
}
```