{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino sin transferir contenido tematico especifico.",
    "Se preservan reglas utiles previas y se deduplican variantes equivalentes por union lossless.",
    "Se refuerza nucleo estable: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y trazabilidad bibliografica.",
    "Se mantiene alerta historica por salidas no JSON parseables y bloqueo de propagacion cuando aplique.",
    "Se mantiene estado minimo verificable del destino con vacios locales abiertos como preguntas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar la carpeta de materia como entrada canonica del trabajo editorial.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio y conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No mezclar contenido tematico de otras materias sin evidencia local verificable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar salida al tipo de producto solicitado: reporte, presentacion o visual.",
    "Conservar integridad academica en cada actividad.",
    "No asumir que fuentes de semanas o materias distintas aplican automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del esquema editorial antes de propagar.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles previas.",
    "Confirmar que afirmaciones sustantivas tengan respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun el tipo de entrega.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "No eliminar campos institucionales; solo actualizar valores confirmados.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir placeholders o tokens Slug sin expandir en README y programa antes de automatizar o citar.",
    "Revisar nombres de archivo con render anomalo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Incluir trazabilidad minima cuando aplique: origen y fecha de consulta.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar transferencia de identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico especifico del origen.",
    "Mantener alertas de calidad institucional en niveles superiores y laterales.",
    "No propagar datos curriculares especificos de esta materia a materias hermanas.",
    "Si un nodo destino esta vacio, crear cerebro minimo con supuestos marcados y vacios abiertos."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional de Mexico/Mexico en nombre de materia y metadatos.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla [supuesto].",
    "Definir nombre oficial de figura docente para plantillas.",
    "Corregir en README y programa los placeholders Slug no expandidos.",
    "Corregir en README los nombres con salto anomalo (eporte, eferencias) [supuesto de render].",
    "Confirmar fuente operativa definitiva para consolidacion de memoria (Codex/GPT-Pro como provisionales)."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral reusable.",
      "Primero estructura y verificabilidad; despues propagacion.",
      "Postura propia con soporte documental y cierre juridico transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, sustentados y utiles para la practica juridica.",
      "Sostener continuidad editorial entre actividades y materias sin contaminar contexto tematico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explicito.",
      "Bloques funcionales trazables.",
      "Citas verificables en puntos sustantivos.",
      "Marcado explicito de supuestos.",
      "Conclusion con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> conceptos/marco -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre con fuente o supuesto marcado.",
      "Consigna y producto deben corresponder sin desalineaciones."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalizacion JSON",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige verificabilidad y forma academica consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan el desarrollo y evitan entregas desalineadas."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La calidad argumentativa depende de fuentes consultables y metadatos minimos."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Analisis propio y postura academica",
          "kind": "develops",
          "justification": "La estructura obliga a pasar de descripcion a argumentacion."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad institucional.",
        "Programa analitico: proposito y ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional local.",
        "Historial de salidas no parseables: necesidad de gate JSON y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se incorporan abstracciones estables del origen (cinco ejes, gates, supuestos) sin transferir contenido tematico de Filosofia del Derecho.",
      "Ciclo 10: se deduplican reglas repetidas y se conserva no regresion editorial.",
      "Ciclo 10: se refuerza grafo conceptual minimo para propagacion transversal recursiva."
    ]
  }
}