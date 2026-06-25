{
  "summary": [
    "Ciclo 9 consolida sincronización transversal hacia Derecho de la propiedad y registro.",
    "Se preserva base institucional UnADM verificada para la materia.",
    "Se conserva ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene política de normalización obligatoria para salidas no JSON.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se conserva estrategia progresiva, conservadora y sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada, tono y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de México.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Registrar ubicación institucional local: Roma Norte, Ciudad de México.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentación, bibliografía y referencias.",
    "Transformar la planeación semanal en productos académicos claros.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir evidencia y fuentes verificables en el desarrollo.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia con semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas.",
    "Supuesto: nombres de archivo en README tienen tokens o caracteres corruptos; resolverlos con el slug derecho-de-la-propiedad-y-registro."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad antes del desarrollo.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "Distinguir problema, fundamento, análisis y cierre argumentativo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular cada actividad con el producto solicitado por la planeación.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada.",
    "Cerrar cada actividad con postura jurídica propia y sustentada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar que cada fuente citada exista en BibTeX o repositorio local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Confirmar que no existan placeholders sin resolver.",
    "Revisar sintaxis LaTeX de authortable antes de compilar.",
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
    "Conservar matrícula del alumno ES2611202040 en tabla de autor salvo instrucción distinta.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instrucción distinta.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico local es derecho-de-la-propiedad-y-registro.bib."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes específicas.",
    "Agregar fuentes específicas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos mínimos de consulta o archivo local cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No reutilizar bibliografía de otra materia sin validación local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Propagar identidad UnADM a nodos laterales solo si comparten institución.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Mantener compresión union-dedupe sin eliminar reglas útiles previas.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 heredado necesita normalización manual si se reutiliza.",
    "Antecedentes Codex y GPT-Pro no parseables siguen como provisionales."
  ],
  "open_questions": [
    "Confirmar si existe rúbrica formal de evaluación para esta materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir el placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres de archivo reales del README ante tokens o caracteres corruptos.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Supuesto: falta consigna local detallada por actividad.",
    "Supuesto: archivo .bib canónico local es derecho-de-la-propiedad-y-registro.bib."
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
        "Entrada canónica por carpeta de asignatura.",
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
      "Problema jurídico.",
      "Marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Postura jurídica sustentada.",
      "Conclusión transferible.",
      "Trazabilidad bibliográfica.",
      "Normalización JSON."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar cada actividad con la práctica jurídica en propiedad y registro.",
      "Preservar un cerebro editorial reutilizable sin perder reglas locales."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin referencias inventadas.",
      "Sin placeholders al cierre.",
      "Portada con metadatos completos.",
      "Cierre jurídico con criterio propio.",
      "Rutas y tokens resueltos antes de compilar.",
      "Citas verificables y consistentes con BibTeX."
    ],
    "argumentative_patterns": [
      "Del problema jurídico al objetivo de actividad.",
      "Del objetivo al marco conceptual.",
      "Del marco conceptual al fundamento normativo o doctrinal.",
      "Del fundamento a la evidencia verificable.",
      "De la evidencia al análisis propio.",
      "Del análisis a una postura jurídica sustentada.",
      "De la postura a una conclusión aplicable.",
      "De la conclusión a la transferencia profesional.",
      "De la consigna al formato final solicitado."
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
        "Marco normativo o doctrinal",
        "Conceptos jurídicos",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Planeación semanal",
        "Reporte académico",
        "Presentación académica",
        "Bibliografía local",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Compilación LaTeX",
        "Metadatos académicos",
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
          "justification": "La pauta institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho de la propiedad y registro",
          "kind": "develops",
          "justification": "La materia pertenece al programa local verificado."
        },
        {
          "source": "Malla curricular de Derecho UnADM",
          "target": "Semestre 7 bloque 1",
          "kind": "supports",
          "justification": "La ubicación curricular local se documenta en README y malla."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo o doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe sustentarse en fuentes y razonamiento."
        },
        {
          "source": "Planeación semanal",
          "target": "Reporte académico",
          "kind": "develops",
          "justification": "La planeación puede transformarse en reporte según consigna."
        },
        {
          "source": "Planeación semanal",
          "target": "Presentación académica",
          "kind": "develops",
          "justification": "La planeación puede transformarse en presentación según consigna."
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
          "source": "Compilación LaTeX",
          "target": "Metadatos académicos",
          "kind": "depends_on",
          "justification": "Portada, autoría y rutas deben resolverse antes de compilar."
        },
        {
          "source": "Propiedad y registro",
          "target": "Problema jurídico",
          "kind": "develops",
          "justification": "Cada actividad debe contextualizar el problema dentro de la materia cuando aplique."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación semanal transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "BibTeX local: unadmSitioWeb.",
        "BibTeX local: unadmMallaDerecho2024.",
        "Plantilla .tex local: coursename Derecho de la propiedad y registro.",
        "Plantilla .tex local: coursecode LDE-S7B1.",
        "Plantilla .tex local: autor y matrícula registrados.",
        "Origen transversal: normalización estructurada obligatoria antes de propagar.",
        "Origen transversal: no inventar fuentes.",
        "Origen transversal: validar consistencia entre citas en texto y archivo .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9 preserva reglas locales verificadas del destino.",
      "Ciclo 9 elimina duplicados semánticos sin recortar reglas útiles.",
      "Ciclo 9 evita transferir conceptos filosóficos específicos no equivalentes.",
      "Ciclo 9 transfiere patrones estables de estructura argumentativa.",
      "Ciclo 9 refuerza calidad institucional, trazabilidad y normalización JSON.",
      "Ciclo 9 conserva metadatos locales de LaTeX por evidencia en plantilla.",
      "Ciclo 9 marca como supuestos los vacíos de consigna, rúbrica y figura docente.",
      "Ciclo 9 mantiene antecedentes no parseables como provisionales.",
      "Ciclo 9 respeta relación transversal entre materias no equivalentes."
    ]
  }
}