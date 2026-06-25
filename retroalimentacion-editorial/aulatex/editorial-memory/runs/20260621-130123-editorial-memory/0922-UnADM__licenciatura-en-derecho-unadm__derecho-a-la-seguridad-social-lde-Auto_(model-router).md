```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad origen hacia materia destino sin mezclar contenido tematico.",
    "Se refuerza patron transversal UnADM: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "La compresion aplicada es union-dedupe lossless, sin regresion de reglas utiles.",
    "La materia destino consolida un cerebro editorial minimo, coherente y propagable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo producto.",
    "Usar datos curriculares oficiales del destino; marcar cualquier variacion como [supuesto].",
    "No transferir redaccion literal entre nodos no equivalentes.",
    "Conservar trazabilidad de reglas heredadas y fuentes provisionales."
  ],
  "structure_rules": [
    "Alinear entregas a ejes reutilizables: problema, marco, analisis, evidencia y conclusion.",
    "Tomar README y programa analitico del destino como canon local.",
    "Usar estructura minima verificable antes de propagar.",
    "Separar claramente marco normativo y analisis propio."
  ],
  "activity_rules": [
    "Definir objetivo y problema juridico desde el inicio.",
    "Incluir postura academica propia sustentada.",
    "Cerrar con conclusion juridica transferible.",
    "Ajustar formato al producto solicitado en la planeacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Confirmar respaldo o marca [supuesto] en toda afirmacion relevante.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Validar que la compresion sea union-dedupe sin perdida."
  ],
  "latex_rules": [
    "Mantener plantilla base del destino y solo personalizar campos variables.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar codificacion correcta en español."
  ],
  "bibliography_rules": [
    "Usar archivo .bib local del destino como fuente central.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos minimos verificables.",
    "Validar correspondencia entre citas en texto y BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferencia de contenido tematico entre materias distintas.",
    "Reforzar reglas de identidad, estructura y calidad en nodos laterales.",
    "Aplicar normalizacion manual si se detectan salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar norma de citacion juridica requerida por la materia destino [supuesto].",
    "Verificar consignas especificas de actividades locales antes de profundizar.",
    "Confirmar vigencia de fuentes provisionales heredadas [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Normalizacion estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Respeto a semestre y bloque oficiales",
        "Uso de programa analitico como guia"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Marco normativo verificable",
      "Evidencia relevante",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Crear productos academicos juridicos claros, verificables y reutilizables.",
      "Garantizar coherencia editorial transversal entre materias UnADM."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separacion visible de secciones",
      "Uso explicito de etiquetas [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitacion del problema",
      "Exposicion del marco normativo",
      "Contraste de evidencia",
      "Fijacion de postura propia",
      "Conclusion aplicada"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
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
          "justification": "El analisis requiere una pregunta juridica clara."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende del fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen estructura y proposito.",
        "Bibliografia local confirma base normativa verificable."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patron editorial comun sin mezclar contenidos tematicos.",
      "Se preserva identidad UnADM y control de calidad institucional.",
      "Se consolida cerebro editorial minimo propagable."
    ]
  }
}
```