{
  "summary": [
    "Se sincroniza memoria transversal con transferencia estable y sin redaccion literal.",
    "Se conserva compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza normalizacion obligatoria a JSON parseable antes de propagar.",
    "Se preservan ejes editoriales comunes: problema, marco conceptual-normativo, analisis propio y conclusion juridica.",
    "Se mantiene separacion entre reglas institucionales estables y contenido tematico local de cada materia.",
    "Supuesto: el destino sigue sin consigna de actividad concreta y opera con cerebro editorial minimo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Verificar datos personales y figura docente antes de compartir entregables.",
    "No transferir datos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final con producto solicitado por planeacion semanal.",
    "Mantener separacion entre reporte .tex, presentacion .tex y .bib local.",
    "Corregir rutas o nombres rotos en README y programa analitico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Vincular analisis fiscal-tributario con aplicacion profesional concreta.",
    "No asumir fuentes de otras semanas o materias como obligatorias para la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna local.",
    "Revisar placeholders o tokens sin expandir en README, .tex y .bib.",
    "Compilar .tex sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Completar campos de plantilla antes de compilar.",
    "Cerrar todos los entornos LaTeX truncados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivos truncados en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar malla curricular solo para respaldar datos curriculares."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar traslado de contenido tematico especifico de Filosofia al eje fiscal salvo patron metodologico.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar consigna concreta de la siguiente actividad del destino.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar formato de citacion requerido por la asignatura.",
    "Resolver definitivamente nombre de figura docente en plantilla.",
    "Confirmar si autor y matricula deben permanecer en plantillas compartidas.",
    "Supuesto: archivo .bib canonico del destino permanece como derecho-fiscal-y-tributario.bib."
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
        "Trazabilidad de supuestos y fuentes.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Fundamento conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable.",
      "Consistencia tecnica editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar continuidad editorial entre actividades y materias sin perder identidad institucional."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales y cierre profesional.",
      "Sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo delimitado.",
      "Contraste de fuentes con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia tex-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa parte de un conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere sustento normativo."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia tex-bib",
          "kind": "supports",
          "justification": "La integridad academica exige forma y cita consistentes."
        }
      ],
      "evidence": [
        "README de destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y regla bibliografica local.",
        "Archivo .bib local con fuentes institucionales base.",
        "Supuesto: transferencia transversal limitada a patrones metodologicos estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion completa de reglas repetidas.",
      "Ciclo 10: preservacion de reglas utiles previas sin recorte.",
      "Ciclo 10: refuerzo de gates tecnicos JSON y tex-bib.",
      "Ciclo 10: consolidacion de ADN editorial transversal sin contaminar contenido tematico local."
    ]
  }
}