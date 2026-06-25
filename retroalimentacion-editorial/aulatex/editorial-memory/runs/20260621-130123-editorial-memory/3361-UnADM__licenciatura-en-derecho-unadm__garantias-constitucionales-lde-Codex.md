{
  "summary": [
    "Sincronizacion transversal consolidada con enfoque conservador y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se refuerza compresion lossless por union-dedupe y eliminacion de duplicados textuales.",
    "Se mantiene separacion estricta entre abstraccion editorial y contenido disciplinar.",
    "Se confirma contexto local destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Supuesto: no hay consigna local de actividad especifica en este salto; se conserva cerebro de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado del destino en todo producto.",
    "Conservar coherencia con Licenciatura en Derecho en argumentacion y referencias.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar de Filosofia del Derecho al destino sin validacion expresa.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders o truncamientos en README y archivos de trabajo antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Asegurar correspondencia entre consigna local y tipo de entrega."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar configuracion base de plantilla local salvo requerimiento verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Corregir truncamientos visibles en macros de portada antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Mantener nombres de archivo canonicos del destino.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "No introducir paquetes no estandar sin necesidad editorial o tecnica verificable."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "Mantener entradas institucionales base ya verificadas.",
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar normas juridicas con emisor y fecha cuando se usen."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales validadas.",
    "Evitar mover contenido tematico entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Conservar alerta institucional sobre entradas no parseables como control transversal.",
    "Mantener estrategia progresiva y conservadora en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar figura docente para completar portada.",
    "Confirmar estilo de citacion requerido por la materia.",
    "Confirmar si la fecha debe ser automatica o fija por entrega.",
    "Validar correccion final de truncamientos en reporte y README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Trazabilidad entre consigna, fuentes y producto.",
        "Marcado explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion transferible.",
      "Control estricto de calidad estructural."
    ],
    "reason_for_being": [
      "Estandarizar productos academicos con identidad UnADM y validez juridica verificable.",
      "Permitir propagacion segura por abstracciones editoriales estables entre nodos transversales."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Separacion entre norma y opinion.",
      "Cierre con aplicacion profesional concreta.",
      "Supuestos etiquetados de forma explicita."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Analisis propio con evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib",
        "Propagacion transversal conservadora"
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
          "justification": "La identidad exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe estar sustentada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo documental."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo bibliografico local con base institucional.",
        "Reglas heredadas deduplicadas sin regresion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 5: refuerzo de gate JSON parseable como bloqueo transversal.",
      "Ciclo 5: mantenimiento de estrategia no disciplinar para salto transversal.",
      "Ciclo 5: adicion de correccion de tokens Slug sin expandir como regla LaTeX operativa."
    ]
  }
}