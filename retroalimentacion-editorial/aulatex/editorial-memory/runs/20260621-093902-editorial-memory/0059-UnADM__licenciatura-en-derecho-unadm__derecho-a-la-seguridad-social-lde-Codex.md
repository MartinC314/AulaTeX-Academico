{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes sin mezclar contenido tematico.",
    "Se preserva identidad UnADM y enfoque juridico del destino como prioridad local.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva gate critico: bloquear propagacion si no hay JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar actividad con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener compatibilidad tecnica del proyecto; evitar comandos no estandar sin justificacion.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar solo referencias realmente consultables.",
    "No inventar referencias; marcar faltantes como pendientes [supuesto].",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables entre materias no equivalentes.",
    "No transferir redaccion literal ni contenido tematico de Filosofia del Derecho.",
    "Propagar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Conservar alerta historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si la fuente provisional heredada externa a Derecho sigue vigente [supuesto].",
    "Confirmar datos faltantes de figura docente para portada [supuesto].",
    "Confirmar consigna exacta por actividad antes de fijar tipo de producto.",
    "Confirmar si hay rubrica especifica adicional para profundidad argumentativa [supuesto]."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas con fundamento juridico verificable.",
      "Sostener analisis propio sobre evidencia y norma.",
      "Convertir resultados en conclusiones juridicas transferibles."
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial persistente entre actividades y materia.",
      "Asegurar calidad tecnica, argumentativa y bibliografica sin perdida de memoria util.",
      "Permitir propagacion segura por reglas estables y verificables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiquetado de [supuesto] cuando falte verificacion local.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Problema y objetivo primero.",
      "Marco normativo y doctrinal despues.",
      "Contraste de evidencia verificable.",
      "Postura propia sustentada.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico delimitado",
        "Marco normativo verificable",
        "Evidencia trazable",
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
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion consistente."
        },
        {
          "source": "Marco normativo verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Evita perdida de reglas utiles y elimina duplicados."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino fija proposito y ejes juridicos.",
        "Bib local del destino confirma base institucional y normativa.",
        "Historial institucional conserva alerta por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 59: se transfieren solo abstracciones estables por relacion transversal.",
      "Ciclo 59: se preservan reglas locales de seguridad social sin mezclar contenido de filosofia.",
      "Ciclo 59: se refuerzan gates JSON, trazabilidad de supuestos y control bibliografico.",
      "Ciclo 59: consolidacion lossless por union-dedupe completada sin regresion."
    ]
  }
}