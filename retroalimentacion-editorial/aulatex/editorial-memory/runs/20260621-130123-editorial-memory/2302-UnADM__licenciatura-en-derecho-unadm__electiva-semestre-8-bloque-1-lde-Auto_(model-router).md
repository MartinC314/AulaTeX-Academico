{
  "summary": [
    "Materia Electiva S8 B1 consolidada como cerebro editorial UnADM.",
    "Sincronización transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas útiles del destino y herencia institucional.",
    "Se transfieren solo abstracciones estables desde Filosofía del Derecho.",
    "Se evita trasladar contenido temático no verificable entre nodos no equivalentes.",
    "Se refuerzan ejes reutilizables: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene control estricto de JSON parseable antes de propagar.",
    "Se registran placeholders y literales corruptos detectados en README y programa local.",
    "Supuesto: la electiva no tiene nombre oficial distinto al provisional local.",
    "Supuesto: créditos y figura docente siguen pendientes de confirmación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redacción académica.",
    "Usar tono jurídico formal, claro, sobrio y verificable.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Evitar renombrar la asignatura sin fuente institucional local.",
    "Conservar autor y matrícula definidos en plantilla base.",
    "Marcar como supuesto todo dato no visible o no confirmado localmente.",
    "Tratar memorias heredadas Codex y GPT-Pro como provisionales hasta validación local.",
    "No eliminar reglas heredadas útiles; extender solo con evidencia verificable.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Alinear cada actividad al programa analítico local.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar README, programa analítico, plantillas, bibliografía y referencias locales.",
    "Evitar redacción literal heredada de materias no equivalentes."
  ],
  "activity_rules": [
    "Vincular el producto con un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No extrapolar fuentes de otras semanas sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin consigna verificable.",
    "Cerrar con postura académica sustentada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de compilar.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, especialmente créditos y figura docente.",
    "Verificar que el producto corresponda a la consigna local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en español.",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Evitar placeholders de automatización como $(@{...}.Slug) en archivos finales.",
    "Resolver tokens sin expandir en README y programa analítico.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Mantener notas de consulta y ruta cuando la fuente sea local.",
    "Agregar doctrina, normativa o jurisprudencia solo cuando la actividad lo requiera.",
    "Distinguir bibliografía base y bibliografía específica de actividad.",
    "Validar correspondencia entre citas en texto y entradas BibTeX.",
    "No asumir bibliografía de Filosofía del Derecho como propia de esta electiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Compartir solo abstracciones editoriales entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar contenidos temáticos sin consigna local verificable.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar control de placeholders a nodos con README generado.",
    "Registrar ciclos con salida no estructurada como normalización manual reutilizable."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva si difiere del usado localmente.",
    "Confirmar código oficial frente al provisional LDE-S8B1.",
    "Confirmar créditos oficiales para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar rúbrica y consigna de cada actividad local.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si presentación local comparte reglas de portada del reporte.",
    "Corregir en README nombres corruptos de reporte y referencias.",
    "Corregir en README y programa el token $(@{...}.Slug).",
    "Confirmar si existe carpeta referencias-electiva-semestre-8-bloque-1.",
    "Supuesto: falta insumo temático específico de la electiva.",
    "Supuesto: la malla curricular local respalda semestre, bloque y tipo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Sobrio en inferencias.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Portada consistente con plantilla local.",
        "Supuestos etiquetados sin ambigüedad.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8.",
        "Bloque 1.",
        "Tipo Electiva.",
        "Código provisional LDE-S8B1.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Estructura argumentativa jurídica.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de fuentes.",
      "Control de placeholders editoriales.",
      "Normalización JSON para propagación confiable."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la electiva con claridad y fundamento jurídico.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Proteger la identidad UnADM durante la generación editorial.",
      "Evitar inferencias no verificadas en una materia con contexto local incompleto.",
      "Mantener una memoria reutilizable sin pérdida por deduplicación."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre jurídico breve.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Citas verificables.",
      "Supuestos etiquetados.",
      "Metadatos curriculares consistentes.",
      "Cierre jurídico transferible.",
      "Lenguaje académico sin adornos innecesarios.",
      "Conservadurismo ante fuentes heredadas."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto solicitado -> criterios de cumplimiento.",
      "Fuente institucional -> dato curricular -> metadato de portada.",
      "Dato no confirmado -> marca de supuesto -> pregunta abierta.",
      "Norma o doctrina -> aplicación al caso -> postura del estudiante.",
      "Evidencia local -> regla editorial -> propagación controlada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Electiva Semestre 8 Bloque 1.",
        "Código provisional LDE-S8B1.",
        "Problema jurídico o social.",
        "Conceptos jurídicos pertinentes.",
        "Marco normativo o doctrinal.",
        "Producto solicitado por planeación.",
        "Análisis propio del estudiante.",
        "Conclusión jurídica transferible.",
        "Trazabilidad de fuentes.",
        "Bibliografía local.",
        "Normalización JSON.",
        "Control de placeholders.",
        "Compilación LaTeX estable.",
        "Supuestos editoriales.",
        "Propagación transversal conservadora."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Portada consistente",
          "kind": "supports",
          "justification": "La plantilla local exige metadatos institucionales coherentes."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "develops",
          "justification": "El README local ubica la materia dentro de la licenciatura."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 8 bloque 1 tipo Electiva",
          "kind": "supports",
          "justification": "El README cita la malla curricular como fuente de ubicación."
        },
        {
          "source": "Código provisional LDE-S8B1",
          "target": "Confirmación oficial",
          "kind": "depends_on",
          "justification": "La plantilla lo usa mientras no exista código institucional distinto."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio del estudiante",
          "kind": "supports",
          "justification": "El encuadre delimita la postura argumentada."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos orientan la selección de fuentes aplicables."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias inventadas."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local concentra fuentes institucionales y específicas."
        },
        {
          "source": "Control de placeholders",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Tokens sin expandir y rutas corruptas pueden romper referencias."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "La reutilización confiable requiere salida estructurada y parseable."
        },
        {
          "source": "Supuestos editoriales",
          "target": "Datos curriculares no confirmados",
          "kind": "supports",
          "justification": "Créditos, figura docente y nombre oficial requieren validación."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo comparten abstracciones editoriales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 1, tipo Electiva.",
        "README local: créditos vacíos.",
        "README local: fuente malla-curricular-derecho-unadm.pdf.",
        "README local: nombres corruptos eporte y eferencias.",
        "README local: token $(@{...}.Slug) sin expandir.",
        "Programa local: productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa local: ejes problema, conceptos, producto, análisis propio y conclusión.",
        "Programa local: bibliografía específica debe agregarse al .bib local.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla local: autor Martin Jonathan de la Cruz.",
        "Plantilla local: matrícula ES2611202040.",
        "Plantilla local: figura docente por definir.",
        "Plantilla local: curso Electiva Semestre 8 Bloque 1.",
        "Plantilla local: código LDE-S8B1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4 conserva reglas útiles previas sin regresión.",
      "Ciclo 4 deduplica frases equivalentes sin recortar contenido válido.",
      "Ciclo 4 refuerza identidad UnADM y estructura jurídica reusable.",
      "Ciclo 4 evita trasladar bibliografía temática de Filosofía del Derecho.",
      "Ciclo 4 mantiene solo abstracciones transversales entre nodos no equivalentes.",
      "Ciclo 4 refuerza control de JSON parseable para propagación recursiva.",
      "Ciclo 4 refuerza revisión de placeholders y literales corruptos locales.",
      "Ciclo 4 conserva preguntas abiertas sobre créditos, código y figura docente.",
      "Ciclo 4 integra grafo conceptual con relaciones justificadas y evidencia local.",
      "Ciclo 4 mantiene enfoque progresivo, conservador y verificable."
    ]
  }
}