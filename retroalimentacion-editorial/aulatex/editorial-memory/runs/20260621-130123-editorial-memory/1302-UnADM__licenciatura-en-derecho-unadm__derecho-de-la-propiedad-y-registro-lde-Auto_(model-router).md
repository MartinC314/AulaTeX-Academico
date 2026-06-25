{
  "summary": [
    "Se consolida sincronización transversal hacia Derecho de la propiedad y registro.",
    "Se preserva identidad UnADM verificada en el nodo destino.",
    "Se conserva ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene política de normalización obligatoria para salidas no JSON.",
    "Se aplica compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar nombre institucional: Universidad Abierta y a Distancia de México.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Registrar ubicación institucional local solo si la plantilla la exige: Roma Norte, Ciudad de México."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentación, bibliografía y referencias.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Verificar nombres reales de archivos del README antes de automatizar rutas.",
    "Resolver tokens corruptos del README con el slug local verificado."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad.",
    "Vincular cada actividad con el producto solicitado por la planeación.",
    "Distinguir problema, fundamento, análisis y cierre argumentativo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Confirmar que el producto final corresponda a la actividad solicitada.",
    "Cerrar cada actividad con postura jurídica propia y sustentada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que cada fuente citada exista en BibTeX o repositorio local.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Confirmar que no existan placeholders sin resolver.",
    "Revisar sintaxis LaTeX de authortable antes de compilar.",
    "Verificar compilación después de modificar portada, bibliografía o rutas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor.",
    "Corregir Figura docente antes de entrega.",
    "Conservar matrícula del alumno ES2611202040 salvo instrucción distinta.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instrucción distinta.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia.",
    "Agregar fuentes específicas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos de consulta o archivo local cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local.",
    "No transferir citas filosóficas del origen si no fueron consultadas en el destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar identidad UnADM a nodos laterales solo si comparten institución.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Evitar transferir redacción literal desde Filosofía del Derecho.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Mantener estrategia progresiva y conservadora sin regresión.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Ciclo 18 refuerza sincronización transversal sin ampliar fuentes no verificadas."
  ],
  "open_questions": [
    "Confirmar si existe rúbrica formal de evaluación para esta materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres reales de archivo ante tokens corruptos del README.",
    "Confirmar figura docente para sustituir el placeholder local.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Supuesto: falta consigna local detallada por actividad."
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
        "Carpeta de asignatura como entrada canónica.",
        "Metadatos institucionales completos.",
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
      "Postura jurídica argumentada.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad bibliográfica."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en productos académicos claros.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar que cada entrega responda a la consigna local.",
      "Evitar afirmaciones jurídicas sin respaldo verificable."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Citas verificables y consistentes.",
      "Sin referencias inventadas.",
      "Sin placeholders al cierre.",
      "Metadatos locales consistentes.",
      "Conclusión jurídica con criterio propio.",
      "Transversalidad sin transferencia literal."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión aplicable.",
      "De la consigna al producto requerido.",
      "De la fuente verificable a la afirmación jurídica.",
      "De la postura del estudiante a la transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho de la propiedad y registro",
        "Semestre 7 bloque 1",
        "LDE-S7B1",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Conceptos jurídicos pertinentes",
        "Evidencia verificable",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión transferible",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Plantilla LaTeX local",
        "Archivo BibTeX local",
        "Malla curricular de Derecho UnADM",
        "Sitio institucional UnADM"
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
          "justification": "La pauta local exige identidad institucional, citas verificables y criterio propio."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la propiedad y registro",
          "kind": "develops",
          "justification": "La materia pertenece al programa de Derecho según README local."
        },
        {
          "source": "Malla curricular de Derecho UnADM",
          "target": "Semestre 7 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local remite a la malla curricular institucional."
        },
        {
          "source": "Derecho de la propiedad y registro",
          "target": "LDE-S7B1",
          "kind": "supports",
          "justification": "El código local aparece en la plantilla de la materia."
        },
        {
          "source": "Problema jurídico",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El marco debe seleccionarse en función del problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las afirmaciones jurídicas requieren fuentes consultables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El análisis debe construirse sobre fuentes explícitas y no sobre resumen libre."
        },
        {
          "source": "Análisis propio",
          "target": "Postura argumentada",
          "kind": "develops",
          "justification": "La postura del estudiante surge de valorar problema, fuentes y argumentos."
        },
        {
          "source": "Postura argumentada",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "El cierre debe proyectar una consecuencia jurídica aplicable."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia entre texto y .bib evita afirmaciones no verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Metadatos institucionales completos",
          "kind": "depends_on",
          "justification": "La compilación editorial exige portada y campos locales completos."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "El .bib local centraliza fuentes institucionales y fuentes específicas de actividad."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho de la propiedad y registro",
          "kind": "contrasts",
          "justification": "Son materias no equivalentes; solo comparten abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: la carpeta funciona como punto de entrada canónico.",
        "README local: cada actividad debe conservar identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de trabajo basados en problema, conceptos, producto, análisis propio y conclusión.",
        "BibTeX local: clave unadmSitioWeb para sitio institucional.",
        "BibTeX local: clave unadmMallaDerecho2024 para malla curricular.",
        "Plantilla local: coursename Derecho de la propiedad y registro.",
        "Plantilla local: coursecode LDE-S7B1.",
        "Memoria origen: normalización estructurada antes de propagación.",
        "Memoria origen: no inventar fuentes y citar solo referencias consultables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18 deduplica reglas repetidas del destino.",
      "Ciclo 18 conserva reglas locales verificadas.",
      "Ciclo 18 transfiere solo patrones editoriales generales desde Filosofía del Derecho.",
      "Ciclo 18 bloquea transferencia de citas no consultadas en el destino.",
      "Ciclo 18 refuerza normalización JSON como gate recursivo.",
      "Ciclo 18 mantiene estrategia progresiva y conservadora.",
      "Ciclo 18 preserva ADN editorial: problema, fundamento, evidencia, análisis y cierre profesional."
    ]
  }
}