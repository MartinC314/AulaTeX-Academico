{
  "summary": [
    "Memoria de materia consolidada para Electiva Semestre 8 Bloque 1.",
    "Sincronización transversal aplicada desde Filosofía del Derecho con estrategia conservadora.",
    "Se preserva identidad institucional UnADM.",
    "Se refuerzan estructura jurídica, trazabilidad y cierre profesional.",
    "Se evita trasladar contenido temático de Filosofía del Derecho sin evidencia local.",
    "Se conserva antecedente de salidas no estructuradas como riesgo editorial.",
    "Se mantiene unión-dedupe lossless sin regresión de reglas útiles.",
    "Se incorporan reglas verificables del destino sobre placeholders, rutas y bibliografía local.",
    "Supuesto: el destino no tiene consigna de actividad específica.",
    "Supuesto: el nombre oficial de la electiva puede requerir confirmación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro y verificable.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Conservar autor y matrícula definidos en plantilla base.",
    "Marcar como supuesto todo dato no visible o no confirmado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Reconocer fuente provisional heredada: Codex desde ingeniería en sistemas computacionales.",
    "Reconocer fuente provisional heredada: GPT-Pro desde Actividad 1.",
    "No trasladar metadatos curriculares de Filosofía del Derecho al destino.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada actividad al programa analítico de la materia.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Incluir conclusión jurídica transferible a la práctica profesional.",
    "Conservar README, programa analítico, reporte, presentación, bibliografía y referencias.",
    "Usar el programa analítico como guía editorial de productos académicos."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio.",
    "Vincular el producto con un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y análisis propio del estudiante.",
    "Incluir postura académica sustentada.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna local.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo verificable.",
    "Cerrar con postura jurídica aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de entrega.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en español.",
    "Conservar documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de universidad sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y archivos finales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar entrada unadmSitioWeb si fue consultada.",
    "Conservar entrada unadmMallaDerecho2024 sin renombrar.",
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Agregar fuentes doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Usar claves BibTeX estables y descriptivas.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar contenido temático de Filosofía del Derecho sin evidencia local.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificación de JSON parseable a nodos superiores.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Registrar ciclos previos como antecedente de normalización manual.",
    "Crear cerebro editorial mínimo cuando falte contexto local."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva.",
    "Confirmar nombre de figura docente para la plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar código oficial de la asignatura frente al provisional LDE-S8B1.",
    "Confirmar consigna específica de cada actividad.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si presentacion-electiva-semestre-8-bloque-1.tex comparte reglas de portada.",
    "Corregir en README nombres de archivo con caracteres faltantes.",
    "Corregir en README tokens de generador sin expandir.",
    "Confirmar carpeta de referencias local.",
    "Supuesto: falta insumo temático verificable para reglas específicas de actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Sobrio ante datos no confirmados.",
        "Conservador en inferencias."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de fuentes.",
      "Normalización JSON.",
      "Control de placeholders editoriales.",
      "Conservadurismo transversal entre nodos no equivalentes."
    ],
    "reason_for_being": [
      "Orientar productos académicos jurídicos con claridad, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Servir como cerebro editorial persistente de la materia.",
      "Evitar inferencias temáticas sin soporte local.",
      "Mantener continuidad institucional sin perder reglas útiles."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones estables y reutilizables.",
      "Marco normativo o doctrinal cuando aplique.",
      "Postura propia sustentada.",
      "Citas verificables.",
      "Supuestos etiquetados.",
      "Cierre jurídico transferible.",
      "Metadatos consistentes.",
      "Placeholders resueltos antes de entrega."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto solicitado -> criterios de cumplimiento.",
      "Dato no confirmado -> marca de supuesto -> verificación pendiente.",
      "Fuente base -> fuente específica -> cita explícita.",
      "Regla institucional -> aplicación local -> control de calidad."
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
        "Control de placeholders editoriales.",
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
          "justification": "La plantilla local fija universidad, carrera, autor y metadatos."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "develops",
          "justification": "El README ubica la materia dentro de la carrera."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 8 bloque 1 tipo Electiva",
          "kind": "supports",
          "justification": "El README cita la malla curricular como fuente de ubicación."
        },
        {
          "source": "Código provisional LDE-S8B1",
          "target": "Confirmación oficial pendiente",
          "kind": "depends_on",
          "justification": "La plantilla usa el código, pero no se aporta fuente oficial distinta."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio del estudiante",
          "kind": "supports",
          "justification": "El encuadre del problema dirige la argumentación."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Los conceptos se precisan con normas, doctrina o datos."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Calidad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias inventadas."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local concentra fuentes institucionales y futuras fuentes específicas."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Resolver tokens y rutas corruptas reduce errores de compilación."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo se transfieren abstracciones editoriales estables."
        },
        {
          "source": "Supuestos editoriales",
          "target": "Confirmación local",
          "kind": "depends_on",
          "justification": "Todo dato no visible requiere verificación antes de fijarse como regla."
        }
      ],
      "evidence": [
        "README del destino declara materia de la Licenciatura en Derecho de la UnADM.",
        "README del destino ubica semestre 8, bloque 1 y tipo Electiva.",
        "README del destino deja créditos vacíos.",
        "README del destino cita UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README del destino contiene nombres corruptos de reporte y referencias.",
        "README del destino contiene token $(@{...}.Slug) sin expandir.",
        "Programa analítico del destino define propósito de productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico del destino fija ejes: problema, conceptos, producto, análisis propio y conclusión.",
        "Archivo .bib local contiene unadmSitioWeb.",
        "Archivo .bib local contiene unadmMallaDerecho2024.",
        "Plantilla LaTeX local define autor Martin Jonathan de la Cruz.",
        "Plantilla LaTeX local define matrícula ES2611202040.",
        "Plantilla LaTeX local usa curso Electiva Semestre 8 Bloque 1.",
        "Plantilla LaTeX local usa código LDE-S8B1.",
        "Plantilla LaTeX local deja figura docente por definir.",
        "Plantilla LaTeX local deja créditos vacíos.",
        "Memoria heredada registra salida sin JSON parseable desde Codex.",
        "Memoria actual registra salida sin JSON parseable desde GPT-Pro.",
        "Origen aporta estructura reusable: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Regla de transferencia exige compartir solo abstracciones estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17 consolida sincronización transversal conservadora.",
      "Se preservan reglas institucionales UnADM del destino.",
      "Se refuerza la estructura problema-conceptos-producto-análisis-conclusión.",
      "Se incorpora del origen solo la abstracción editorial reusable.",
      "Se excluye contenido temático específico de Filosofía del Derecho.",
      "Se mantienen citas locales verificables: unadmSitioWeb y unadmMallaDerecho2024.",
      "Se refuerza bloqueo por JSON no parseable.",
      "Se refuerza validación entre citas en texto y archivo .bib.",
      "Se refuerza control de placeholders y caracteres corruptos.",
      "Se conservan vacíos locales como preguntas abiertas."
    ]
  }
}