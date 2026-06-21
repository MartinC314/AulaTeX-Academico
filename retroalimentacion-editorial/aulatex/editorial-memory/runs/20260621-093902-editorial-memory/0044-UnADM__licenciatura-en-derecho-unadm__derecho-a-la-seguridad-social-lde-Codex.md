{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin perdida.",
    "Se preserva ADN UnADM y estructura por ejes verificables.",
    "Se refuerza gate critico: no propagar salidas no JSON parseable.",
    "Se mantiene separacion entre reglas estables y contenido tematico local del destino.",
    "Se consolida patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, norma, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente toda salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener compatibilidad tecnica; evitar comandos no estandar sin justificacion.",
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo si aparecen tokens o marcadores corruptos.",
    "Mantener estructura minima: portada, desarrollo, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias.",
    "Agregar solo fuentes consultables con metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables a nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Propagar transversalmente identidad, estructura reusable y gates de calidad.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos tempranos.",
    "Aplicar compresion lossless por union-dedupe en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia destino [supuesto].",
    "Confirmar si la plantilla de Actividad 1 del destino ya es canon operativo local [supuesto].",
    "Confirmar si persiste vigencia de reglas provisionales heredadas de nodos no juridicos [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Producto juridico verificable orientado a consigna.",
      "Problema delimitado con fundamento normativo.",
      "Evidencia verificable y analisis propio.",
      "Cierre con utilidad profesional."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos consistentes, verificables y reutilizables.",
      "Preservar memoria editorial persistente sin regresion entre ciclos.",
      "Permitir propagacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de reglas provisionales."
    ],
    "argumentative_patterns": [
      "Problema y objetivo.",
      "Marco normativo/doctrinal.",
      "Contraste de evidencia.",
      "Postura propia sustentada.",
      "Conclusion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "Sin delimitacion del problema no hay analisis juridico pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion lossless exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Problema juridico",
          "kind": "develops",
          "justification": "Define tono, formato y pertinencia academica del desarrollo."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica de archivos y control editorial.",
        "Programa analitico del destino fija proposito y ejes de trabajo juridico.",
        "Bib local del destino confirma base institucional y normativa verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: se transfieren solo abstracciones estables desde actividad de Filosofia hacia materia de Seguridad Social.",
      "Ciclo 44: se conserva regla critica de bloqueo por no JSON parseable.",
      "Ciclo 44: se refuerza patron argumentativo comun sin mezclar contenido tematico no equivalente.",
      "Ciclo 44: se mantiene compresion lossless por union-dedupe y sin regresion."
    ]
  }
}