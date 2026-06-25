{
  "summary": [
    "Sincronizacion transversal ciclo 10 aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas validas del destino y se agregan abstracciones estables del origen sin recorte.",
    "Se refuerza compresion lossless por union-dedupe y control estricto de no regresion.",
    "Se mantiene prioridad en identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se evita transferencia literal de actividad origen por no equivalencia de nodo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad de origen editorial en cada fusion de memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales y fuera de autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Alinear la estructura al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los cinco ejes del programa analitico.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Exigir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No asumir pertinencia de fuentes de otras semanas o materias sin verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Revisar estructura minima completa antes de fusionar aguas abajo.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que cada afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente salidas heredadas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Conservar macros institucionales: documenttitle, coursename, coursecode, universityname.",
    "Mantener compatibilidad con español y letterpaper definida en plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Corregir nombres de archivo con caracteres corruptos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves institucionales estables: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre nodos no equivalentes.",
    "Priorizar en saltos transversales: identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni metadatos especificos de actividad origen.",
    "Mantener alerta historica: ciclo 1 y herencias no parseables requieren normalizacion manual.",
    "Reforzar en nodos vecinos la regla JSON parseable como prerequisito de fusion."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura. [supuesto]",
    "Confirmar correccion de nombres corruptos en README (reporte/referencias). [supuesto]",
    "Confirmar que coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Definir checklist minimo por tipo de producto: reporte, presentacion y visual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro, verificable y argumentativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Fundamento conceptual y normativo.",
      "Analisis propio con evidencia.",
      "Conclusion juridica transferible.",
      "Memoria persistente con compresion lossless y no regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos solidos.",
      "Garantizar consistencia editorial transversal entre actividades y materia.",
      "Asegurar trazabilidad, verificabilidad y utilidad profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre aplicable a practica juridica.",
      "Marcado explicito de [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay fusion confiable."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo hasta el cierre profesional."
        },
        {
          "source": "Identidad UnADM",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "La persistencia institucional exige conservar reglas utiles previas."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: fuentes institucionales base.",
        "Plantilla tex local: macros y coursecode visibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion semantica completada sin perdida de reglas utiles.",
      "Ciclo 10: se integran abstracciones estables del origen actividad sin copiar literal.",
      "Ciclo 10: se refuerzan gates de JSON parseable, normalizacion y trazabilidad.",
      "Ciclo 10: se preserva identidad curricular local del destino y se marcan supuestos pendientes."
    ]
  }
}