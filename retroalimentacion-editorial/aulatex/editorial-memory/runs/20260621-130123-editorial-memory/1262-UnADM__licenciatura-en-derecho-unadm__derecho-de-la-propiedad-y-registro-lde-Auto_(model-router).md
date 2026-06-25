{
  "summary": [
    "Se consolida sincronización transversal hacia Derecho de la propiedad y registro.",
    "Se conserva identidad institucional UnADM ya verificada en el nodo destino.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada obligatoria antes de propagar.",
    "Se conserva política de no reutilizar salidas no JSON sin revisión manual.",
    "Se aplica compresión por unión y deduplicación sin eliminar reglas útiles previas."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada, metadatos y tono.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de México.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Registrar ubicación institucional local solo si la plantilla la exige: Roma Norte, Ciudad de México."
  ],
  "structure_rules": [
    "Alinear cada entregable con la estructura local disponible.",
    "Soportar reportes y presentaciones salvo instrucción distinta.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Vincular el desarrollo con propiedad y registro cuando aplique.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia con semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas.",
    "Supuesto: nombres de archivo en README contienen tokens o caracteres corruptos; resolver con slug derecho-de-la-propiedad-y-registro."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad antes del desarrollo.",
    "Verificar que el producto final corresponda a la actividad solicitada.",
    "Relacionar contenido con propiedad y registro cuando aplique.",
    "Distinguir problema, fundamento, análisis y cierre argumentativo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar cada actividad con postura jurídica propia y sustentada.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "No transferir redacción literal de actividades de otra materia.",
    "Usar abstracciones editoriales comunes cuando falte consigna textual."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar toda respuesta no estructurada heredada antes de reutilizarla.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que cada fuente citada exista en BibTeX o repositorio local.",
    "Confirmar que no existan placeholders sin resolver.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Revisar sintaxis LaTeX de la tabla de autor antes de compilar.",
    "Verificar compilación después de modificar portada, bibliografía o rutas.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor.",
    "Corregir campo Figura docente antes de entrega.",
    "Conservar matrícula del alumno ES2611202040 salvo instrucción distinta.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instrucción distinta.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar slug derecho-de-la-propiedad-y-registro para resolver archivo .bib local cuando aplique."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes específicas.",
    "Agregar fuentes específicas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos mínimos de consulta o archivo local cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir bibliografía de Filosofía del Derecho como bibliografía local de Propiedad y Registro."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Compartir identidad UnADM solo con nodos que comparten institución.",
    "Compartir ejes editoriales comunes solo como abstracciones estables.",
    "No propagar datos curriculares locales fuera de la materia destino.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Mantener compresión unión-dedupe sin eliminar reglas útiles previas.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Aplicar normalización manual si se detectan salidas heredadas no estructuradas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar reglas generales cuando falte consigna textual.",
    "Ciclos previos con salida no JSON requieren revisión antes de reutilización."
  ],
  "open_questions": [
    "Confirmar si existe rúbrica formal de evaluación para esta materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres reales de archivo del README ante tokens y caracteres corruptos.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Supuesto: falta rúbrica local detallada por actividad.",
    "Supuesto: falta consigna textual de actividades específicas en el contexto actual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias.",
        "Accionable y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Metadatos institucionales completos.",
        "Entrada canónica por carpeta de asignatura.",
        "Normalización estructurada antes de propagación.",
        "Sin propagación de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S7B1.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Postura académica argumentada.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad bibliográfica.",
      "Normalización JSON."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Vincular la formación jurídica avanzada con problemas de propiedad y registro.",
      "Evitar productos descriptivos sin criterio jurídico propio.",
      "Asegurar entregables verificables, compilables y alineados con la consigna."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre.",
      "Tono institucional UnADM.",
      "Nombre de materia exacto.",
      "Metadatos curriculares consistentes.",
      "Citas explícitas y verificables.",
      "Conclusión jurídica aplicable.",
      "Transferencia profesional al cierre."
    ],
    "argumentative_patterns": [
      "Del problema jurídico al objetivo puntual.",
      "Del objetivo al marco conceptual.",
      "Del marco conceptual al marco normativo o doctrinal.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una postura jurídica sustentada.",
      "De la postura a una conclusión transferible.",
      "De la consigna al formato de entrega.",
      "De la cita verificable a la afirmación académica.",
      "De la revisión de fuentes a la trazabilidad BibTeX."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho de la propiedad y registro",
        "Semestre 7 bloque 1",
        "LDE-S7B1",
        "Problema jurídico",
        "Propiedad y registro",
        "Conceptos jurídicos",
        "Normas jurídicas",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión transferible",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Archivo BibTeX local",
        "Normalización JSON",
        "Plantilla LaTeX local",
        "Planeación semanal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la propiedad y registro",
          "kind": "supports",
          "justification": "El README local define la materia dentro del programa de Derecho."
        },
        {
          "source": "Derecho de la propiedad y registro",
          "target": "Semestre 7 bloque 1",
          "kind": "depends_on",
          "justification": "La ubicación curricular local fija semestre y bloque."
        },
        {
          "source": "Semestre 7 bloque 1",
          "target": "LDE-S7B1",
          "kind": "supports",
          "justification": "El código local resume la ubicación curricular registrada."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Propiedad y registro",
          "target": "Problema jurídico",
          "kind": "develops",
          "justification": "La materia exige contextualizar problemas jurídicos desde su campo específico."
        },
        {
          "source": "Conceptos jurídicos",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos ordenan la lectura de normas y doctrina."
        },
        {
          "source": "Normas jurídicas",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo aplicable."
        },
        {
          "source": "Doctrina jurídica",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La doctrina permite sostener una posición académica propia."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones sustentadas reducen riesgo de inferencias no verificadas."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Archivo BibTeX local",
          "kind": "depends_on",
          "justification": "La consistencia entre citas y .bib permite verificar fuentes."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "La plantilla concentra portada, curso, código y datos académicos."
        },
        {
          "source": "Planeación semanal",
          "target": "Formato de entrega",
          "kind": "develops",
          "justification": "La planeación determina si el producto será reporte, presentación u otro formato."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: ubicación curricular semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "derecho-de-la-propiedad-y-registro.bib: clave unadmSitioWeb existente.",
        "derecho-de-la-propiedad-y-registro.bib: clave unadmMallaDerecho2024 existente.",
        "Plantilla .tex local: coursename Derecho de la propiedad y registro.",
        "Plantilla .tex local: coursecode LDE-S7B1.",
        "Memoria origen: normalización JSON obligatoria antes de propagar.",
        "Memoria origen: no inventar fuentes y marcar supuestos.",
        "Memoria origen: ejes transferibles de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8 conserva reglas locales verificadas del destino.",
      "Ciclo 8 deduplica repeticiones de identidad UnADM y ubicación curricular.",
      "Ciclo 8 transfiere solo abstracciones estables desde Filosofía del Derecho.",
      "Ciclo 8 excluye bibliografía específica de Filosofía del Derecho por no ser local.",
      "Ciclo 8 refuerza normalización JSON como gate de propagación.",
      "Ciclo 8 mantiene alerta sobre salidas no estructuradas de Codex y GPT-Pro.",
      "Ciclo 8 refuerza trazabilidad entre citas, .bib y repositorio local.",
      "Ciclo 8 conserva reglas LaTeX locales sin copiar plantilla completa.",
      "Ciclo 8 mantiene estrategia progresiva, conservadora y sin regresión."
    ]
  }
}