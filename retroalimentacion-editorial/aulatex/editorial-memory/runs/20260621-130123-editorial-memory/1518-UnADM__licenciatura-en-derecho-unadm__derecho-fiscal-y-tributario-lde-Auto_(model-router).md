{
  "summary": [
    "Ciclo 6 consolida memoria transversal sin regresión.",
    "Se preserva identidad UnADM y contexto de Licenciatura en Derecho.",
    "Se mantiene compresión por unión y deduplicación.",
    "Se normalizan reglas heredadas antes de propagarlas.",
    "Se transfiere solo ADN editorial estable desde Filosofía del Derecho.",
    "No se transfiere bibliografía temática de Filosofía como obligatoria.",
    "El destino conserva enfoque fiscal y tributario local.",
    "Se refuerzan calidad, trazabilidad, estructura y consistencia LaTeX-BibTeX."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en portada, tono y contexto.",
    "Usar materia destino: Derecho fiscal y tributario.",
    "Usar semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar clave local LDE-S6B1 cuando aplique.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Tratar Codex, GPT-Pro y Auto heredados como provisionales.",
    "Verificar datos personales antes de entrega final.",
    "Verificar figura docente antes de entrega final.",
    "Verificar autor base y matrícula antes de compartir."
  ],
  "structure_rules": [
    "Usar README de la materia como punto de entrada canónico.",
    "Usar programa analítico como guía editorial local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo, análisis propio y cierre.",
    "Alinear cada entrega con la planeación semanal.",
    "Alinear el producto final con la consigna.",
    "Mantener separación entre reporte, presentación y bibliografía local.",
    "Conservar estructura local: reporte, presentación, bibliografía, programa y referencias.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Corregir rutas truncadas o rotas en README antes de publicar.",
    "Resolver slug dinámico del archivo .bib en README y programa analítico."
  ],
  "activity_rules": [
    "Incluir problema jurídico o social explícito al inicio.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Desarrollar el producto solicitado por la planeación.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Vincular argumentos fiscales y tributarios con aplicación profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otra materia como obligatorias del destino.",
    "Marcar como supuesto cualquier insumo no confirmado por consigna local."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo.",
    "Confirmar que todo supuesto esté marcado.",
    "Verificar consistencia entre portada y programa analítico.",
    "Confirmar semestre, bloque, tipo y créditos contra malla local.",
    "Revisar que no existan placeholders sin resolver.",
    "Comprobar que toda cita usada tenga entrada .bib verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar integridad del .tex antes de compilar.",
    "Cerrar correctamente entornos LaTeX truncados.",
    "Corregir rutas con caracteres anómalos antes de publicar."
  ],
  "latex_rules": [
    "Completar campos pendientes de plantilla antes de compilar.",
    "Mantener variables institucionales y de curso consistentes.",
    "Usar español y formato carta según plantilla base.",
    "Actualizar título, subtítulo y actividad en cada entrega.",
    "Conservar portada institucional con UnADM y Licenciatura en Derecho.",
    "Sustituir placeholders generados por expresiones de plantilla.",
    "Corregir bloque authortable truncado antes de compilar.",
    "Cerrar todos los entornos tabular y document.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo Slug en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en derecho-fiscal-y-tributario.bib.",
    "Priorizar fuentes institucionales UnADM.",
    "Priorizar normas jurídicas verificables.",
    "Agregar doctrina, legislación o jurisprudencia solo si la actividad lo exige.",
    "No inventar referencias.",
    "Usar solo obras consultables.",
    "Marcar fuente pendiente cuando falte dato verificable.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar unadmSitioWeb cuando sea pertinente.",
    "Usar unadmMallaDerecho2024 solo para datos curriculares.",
    "No trasladar bibliografía temática de Filosofía al destino sin consigna fiscal."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No propagar datos específicos de Derecho fiscal a materias no equivalentes.",
    "No propagar redacción literal de Filosofía del Derecho.",
    "Reutilizar identidad UnADM y gates de calidad institucional.",
    "Mantener unión-dedupe como método de compresión.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si la entrada heredada es ambigua.",
    "Priorizar mejoras verificables del contexto local antes de lateralizar.",
    "Ciclo 6 requiere trazabilidad de supuestos si se reutiliza."
  ],
  "open_questions": [
    "Confirmar figura docente en plantilla.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar formato de citación requerido por la asignatura.",
    "Confirmar bibliografía fiscal base adicional para la materia.",
    "Confirmar fuentes obligatorias por actividad.",
    "Resolver expresiones PowerShell sin expandir en README y programa analítico.",
    "Corregir rutas truncadas en README para reporte y referencias.",
    "Cerrar correctamente authortable y documento LaTeX del reporte.",
    "Supuesto: el archivo .bib local canónico es derecho-fiscal-y-tributario.bib.",
    "Confirmar si la herencia institucional desde ingeniería sigue vigente para Derecho."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Sobrio y profesional.",
        "Argumentativo con criterio propio.",
        "Orientado a evidencia verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Portada institucional consistente.",
        "Carpeta de asignatura como entrada canónica.",
        "Supuestos etiquetados y trazables.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1.",
        "Obligatoria, 8 créditos.",
        "Clave local LDE-S6B1.",
        "Ubicación curricular respaldada por malla institucional."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social inicial.",
      "Conceptos, normas y datos pertinentes.",
      "Fundamento jurídico verificable.",
      "Análisis propio con postura académica.",
      "Aplicación profesional fiscal y tributaria.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex, .bib y README.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho fiscal y tributario.",
      "Transformar planeación semanal en entregables verificables.",
      "Integrar problema, fuentes, análisis y cierre argumentativo.",
      "Conectar el marco normativo con práctica profesional.",
      "Evitar resúmenes sin postura jurídica.",
      "Preservar trazabilidad institucional y bibliográfica."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Citas verificables y entradas .bib consistentes.",
      "Secciones funcionales y ordenadas.",
      "Cierre jurídico con implicación práctica.",
      "Sin contenido de relleno descriptivo.",
      "Sin bibliografía inventada.",
      "Sin placeholders visibles en entrega final.",
      "Sin redacción literal transferida entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Plantear problema jurídico concreto.",
      "Definir objetivo puntual.",
      "Delimitar conceptos clave.",
      "Ubicar marco normativo o doctrinal.",
      "Contrastar fuentes verificables.",
      "Construir postura propia del estudiante.",
      "Aplicar el argumento al contexto fiscal-tributario.",
      "Cerrar con conclusión profesional transferible.",
      "Comprobar coherencia entre pregunta, desarrollo y conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho fiscal y tributario",
        "Semestre 6 bloque 1",
        "Problema jurídico",
        "Marco normativo",
        "Conceptos fiscales y tributarios",
        "Evidencia verificable",
        "Cita explícita",
        "Análisis propio",
        "Postura académica",
        "Aplicación profesional",
        "Conclusión transferible",
        "Bibliografía local",
        "Consistencia .tex/.bib",
        "Normalización JSON",
        "Propagación recursiva",
        "Supuesto etiquetado"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho fiscal y tributario",
          "kind": "develops",
          "justification": "El README ubica la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "unadmMallaDerecho2024",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "La malla curricular local respalda la ubicación curricular."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura académica requiere un conflicto o pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica necesita fundamento normativo explícito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Cita explícita",
          "kind": "supports",
          "justification": "La trazabilidad exige correspondencia entre afirmación y fuente."
        },
        {
          "source": "Bibliografía local",
          "target": "Consistencia .tex/.bib",
          "kind": "supports",
          "justification": "Toda cita del documento debe existir en el archivo bibliográfico local."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia segura requiere estructura parseable."
        },
        {
          "source": "Supuesto etiquetado",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Los datos no confirmados deben distinguirse de los datos verificados."
        },
        {
          "source": "Actividad de Filosofía del Derecho",
          "target": "Derecho fiscal y tributario",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo comparten abstracciones editoriales."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: conservar identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "derecho-fiscal-y-tributario.bib: contiene unadmSitioWeb.",
        "derecho-fiscal-y-tributario.bib: contiene unadmMallaDerecho2024.",
        "Reporte local: plantilla base con curso Derecho fiscal y tributario y clave LDE-S6B1.",
        "Reporte local: authortable aparece truncado y requiere corrección.",
        "Origen transversal: aporta patrón problema-conceptos-evidencia-análisis-cierre.",
        "Supuesto: no se transfiere bibliografía temática de Filosofía como obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6 preserva reglas útiles previas sin recorte.",
      "Se deduplican reglas repetidas por equivalencia semántica.",
      "Se refuerza identidad local del destino.",
      "Se conserva contexto curricular verificado por README.",
      "Se mantiene advertencia sobre fuentes heredadas provisionales.",
      "Se agrega transferencia transversal solo metodológica.",
      "Se bloquea traslado de citas filosóficas no exigidas por consigna fiscal.",
      "Se refuerza gate de JSON parseable.",
      "Se refuerza gate de consistencia .tex/.bib.",
      "Se refuerza corrección de rutas, slugs y authortable truncado."
    ]
  }
}