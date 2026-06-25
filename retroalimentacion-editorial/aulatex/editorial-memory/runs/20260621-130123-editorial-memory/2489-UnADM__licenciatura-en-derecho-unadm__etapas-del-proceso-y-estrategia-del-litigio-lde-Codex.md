{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, validacion JSON y compresion union-dedupe sin regresion.",
    "Se transfiere solo abstraccion reusable; no se transfiere redaccion literal ni detalles exclusivos de Actividad 1.",
    "Se refuerza control de fuentes provisionales y marcacion explicita de [supuesto].",
    "Se mantiene cerebro editorial minimo de materia con base en README, programa analitico, .bib y plantilla .tex locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica editorial.",
    "Sostener tono academico-juridico formal, claro y argumentativo.",
    "Exigir postura propia sustentada; evitar texto meramente descriptivo.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre la estructura al producto solicitado en planeacion semanal.",
    "Aplicar cinco ejes editoriales: problema, conceptos, producto, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Verificar consigna especifica antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Integrar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir fuentes de otras semanas o materias como pertinentes por defecto.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Aplicar fusion por union-dedupe sin eliminar reglas utiles previas.",
    "Revisar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que cada afirmacion factual tenga fuente o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar salidas no estructuradas antes de reutilizarlas aguas abajo.",
    "Evitar contradicciones con reglas institucionales ya vigentes."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base de nuevas entregas.",
    "Conservar macros institucionales de portada y curso.",
    "Mantener compatibilidad con espanol y letterpaper segun plantilla.",
    "No eliminar campos de portada; completar segun actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README o rutas antes de referenciar archivos.",
    "Corregir nombres corruptos de archivos detectados en README. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Conservar fuentes institucionales base ya registradas y agregar solo fuentes realmente usadas.",
    "No inventar referencias; usar obras verificables y consultables.",
    "Mantener metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas abstractas y estables.",
    "No propagar metadatos ni artefactos exclusivos de Actividad 1.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener trazabilidad de fuentes provisionales en notas tecnicas.",
    "Aplicar estrategia progresiva: primero validar JSON, luego fusionar, luego propagar.",
    "Aplicar estrategia conservadora: ante duda, conservar regla util existente."
  ],
  "open_questions": [
    "Confirmar si documentauthor es fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica exigido por docente o asignatura.",
    "Confirmar correccion final de nombres de archivo con caracteres corruptos en README. [supuesto]",
    "Confirmar si existe checklist institucional diferenciado por tipo de producto."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Fundamento conceptual y normativo.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada para memoria persistente."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y reutilizables.",
      "Asegurar continuidad editorial entre actividades y materia sin perder contexto local.",
      "Garantizar calidad verificable antes de cualquier propagacion recursiva."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Afirmacion con evidencia y cierre practico.",
      "Marcacion explicita de [supuesto] cuando falte dato."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo puntual -> desarrollo rubricado -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Union-dedupe sin regresion",
        "Concluson juridica transferible",
        "Fuentes verificables",
        "Supuestos marcados"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay fusion confiable."
        },
        {
          "source": "Union-dedupe sin regresion",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles y evita perdida de conocimiento."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad del producto academico",
          "kind": "develops",
          "justification": "Estandariza estructura y profundidad argumentativa."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce afirmaciones sin respaldo."
        },
        {
          "source": "Supuestos marcados",
          "target": "Transparencia editorial",
          "kind": "supports",
          "justification": "Distingue hechos verificados de inferencias."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        ".bib local: fuentes institucionales base verificables.",
        "Plantilla .tex local: macros institucionales y metadatos de curso."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completada sin recorte semantico.",
      "Ciclo 7: reforzada regla de transferencia por abstracciones entre nodos no equivalentes.",
      "Ciclo 7: mantenidos gates de JSON parseable y no regresion como bloqueo duro.",
      "Ciclo 7: preservada separacion entre fuentes provisionales y autoridad academica.",
      "Ciclo 7: consolidado ADN editorial transversal con enfoque juridico aplicado."
    ]
  }
}