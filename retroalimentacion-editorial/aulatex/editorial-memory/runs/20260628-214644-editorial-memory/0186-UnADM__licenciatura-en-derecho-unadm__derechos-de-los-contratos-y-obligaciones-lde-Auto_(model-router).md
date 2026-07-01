```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal UnADM desde actividad hacia materia no equivalente.",
    "Se preservan reglas estables: identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "La transferencia es abstracta, conservadora y sin redaccion literal.",
    "Se refuerza compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo producto.",
    "Marcar como [supuesto] cualquier dato no confirmado localmente.",
    "Tratar herencias Codex o GPT-Pro como provisionales hasta verificacion.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "No mezclar identidad de materias distintas sin adaptacion disciplinar."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Explicitar postura academica propia con fundamento juridico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o traslados literales entre materias.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Marcar supuestos cuando falte consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar español academico con acentos correctos en .tex y .bib.",
    "Mantener metadatos institucionales completos antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y normas verificables.",
    "Separar bibliografia base de fuentes especificas por actividad.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Declarar [supuesto] si una referencia no esta disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Aplicar lateralmente tras validar compatibilidad disciplinar.",
    "Evitar transferir redaccion literal o ejemplos casuisticos.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Propagar hacia arriba solo reglas institucionales y de calidad."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion juridica obligatoria en la materia.",
    "Definir formato minimo de conclusion juridica por actividad.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
    "Precisar uso esperado de legislacion federal o local segun actividad.",
    "Confirmar nombre canonico final del archivo .bib."
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
        "Integridad academica y citas verificables",
        "Carpeta como entrada canonica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre y bloque verificados por materia",
        "Asignatura definida por carpeta"
      ]
    },
    "essence": [
      "Problema juridico como punto de partida",
      "Marco conceptual y normativo verificable",
      "Analisis propio argumentado",
      "Conclusion juridica transferible",
      "Identidad institucional UnADM"
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos estructurados.",
      "Asegurar claridad, fundamento juridico y utilidad profesional.",
      "Servir como cerebro editorial persistente y reusable."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Supuestos explicitados",
      "Cierre con utilidad profesional",
      "Trazabilidad entre objetivo, evidencia y conclusion"
    ],
    "argumentative_patterns": [
      "Problema inicial definido",
      "Fundamentacion normativa o doctrinal",
      "Analisis critico propio",
      "Conclusion aplicada a la practica juridica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema juridico",
        "Marco normativo y doctrinal",
        "Analisis argumentativo",
        "Conclusion transferible",
        "Contratos",
        "Obligaciones",
        "Identidad institucional UnADM"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis argumentativo",
          "kind": "develops",
          "justification": "El analisis deriva de un conflicto definido."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion debe apoyarse en fundamento verificable."
        },
        {
          "source": "Contratos",
          "target": "Obligaciones",
          "kind": "depends_on",
          "justification": "Categorias nucleares articuladas en la materia."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige citas y rigor verificable."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia.",
        "Bibliografia institucional UnADM.",
        "Reglas editoriales consolidadas por union-dedupe."
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas utiles previas sin eliminacion.",
      "Se reforzo normalizacion estructurada previa a propagacion.",
      "Se consolido grafo conceptual transversal aplicable a LDE."
    ]
  }
}
```