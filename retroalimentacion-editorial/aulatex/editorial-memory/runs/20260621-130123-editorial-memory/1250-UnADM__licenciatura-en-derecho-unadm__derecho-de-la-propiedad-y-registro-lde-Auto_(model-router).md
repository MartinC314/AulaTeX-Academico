{
  "summary": [
    "Se consolida cerebro editorial de materia para Derecho de la propiedad y registro.",
    "Se conserva identidad UnADM verificada en contexto local.",
    "Se integra sincronización transversal desde Filosofía del Derecho solo como abstracciones estables.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene estrategia progresiva, conservadora y sin regresión.",
    "Se preserva normalización obligatoria antes de propagar memorias no estructuradas.",
    "La materia destino tiene ubicación curricular verificada: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "La carpeta de la materia funciona como punto de entrada canónico."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada, tono y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar nombre institucional: Universidad Abierta y a Distancia de México.",
    "Usar la carpeta de la materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Usar ubicación institucional local si la plantilla lo exige: Roma Norte, Ciudad de México."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentación, bibliografía y referencias.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir problema, conceptos o normas, análisis propio y conclusión jurídica transferible.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según consigna.",
    "Alinear cada producto con la planeación semanal y la consigna específica.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Mantener consistencia con semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas.",
    "Supuesto: nombres de archivo en README contienen tokens o caracteres corruptos; resolver con slug derecho-de-la-propiedad-y-registro."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad antes del desarrollo.",
    "Relacionar el contenido con propiedad y registro cuando aplique.",
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
    "Revisar toda respuesta no estructurada heredada antes de reutilizarla.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que cada fuente citada exista en BibTeX o en repositorio local.",
    "Confirmar que no existan placeholders sin resolver.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Revisar sintaxis LaTeX de authortable antes de compilar."
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
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar compilación después de modificar portada, bibliografía o rutas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia: derecho-de-la-propiedad-y-registro.bib.",
    "Agregar fuentes específicas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos mínimos de consulta o archivo local cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local.",
    "Validar consistencia entre citas en texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Propagar identidad UnADM a nodos laterales solo si comparten institución.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Evitar transferir redacción literal entre materias distintas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Mantener compresión por unión y deduplicación sin eliminar reglas útiles previas.",
    "Aplicar normalización manual si se reutiliza memoria heredada no estructurada.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 2 necesita revisión de antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar rúbrica formal de evaluación para esta materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres de archivo reales del README ante tokens o caracteres corruptos.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Supuesto: faltan consignas locales detalladas por actividad.",
    "Supuesto: falta rúbrica local detallada por actividad.",
    "Supuesto: falta bibliografía específica de propiedad y registro más allá de fuentes institucionales."
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Postura académica argumentada.",
      "Conclusión jurídica transferible.",
      "Trazabilidad bibliográfica.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derecho con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales según consigna.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Evitar entregas meramente descriptivas.",
      "Producir conclusiones útiles para la práctica jurídica en propiedad y registro."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin referencias inventadas.",
      "Sin placeholders al cierre.",
      "Nombre exacto de materia en metadatos.",
      "Identidad UnADM visible en portada.",
      "Conclusión con criterio propio.",
      "Citas trazables al .bib local.",
      "Rutas verificadas antes de compilar."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco conceptual al marco normativo.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a la postura jurídica.",
      "De la postura a una conclusión aplicable.",
      "Objetivo puntual antes del desarrollo.",
      "Producto alineado con planeación y consigna.",
      "Cierre jurídico transferible a la práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho de la propiedad y registro",
        "Semestre 7 bloque 1",
        "LDE-S7B1",
        "Punto de entrada canónico",
        "Problema jurídico",
        "Conceptos clave",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Propagación recursiva",
        "Compresión union-dedupe",
        "Fuentes provisionales",
        "Tokens de ruta sin resolver",
        "Plantilla LaTeX local",
        "Bibliografía local"
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
          "justification": "El README identifica la materia dentro del programa de Derecho."
        },
        {
          "source": "Semestre 7 bloque 1",
          "target": "Derecho de la propiedad y registro",
          "kind": "develops",
          "justification": "La ubicación curricular local sitúa la materia en semestre 7, bloque 1."
        },
        {
          "source": "Punto de entrada canónico",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "La carpeta de asignatura organiza reglas, plantillas, bibliografía y programa analítico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo/doctrinal",
          "kind": "supports",
          "justification": "Los conceptos delimitan las normas y doctrinas pertinentes."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe estar sustentada en fuentes consultables y razonamiento propio."
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
          "source": "Compresión union-dedupe",
          "target": "Sin regresión editorial",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin recorte sustantivo."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Supuestos explícitos",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas no verificadas deben marcarse hasta confirmación local."
        },
        {
          "source": "Tokens de ruta sin resolver",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "Los tokens corruptos impiden rutas confiables si no se corrigen antes de compilar."
        },
        {
          "source": "Bibliografía local",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "El archivo derecho-de-la-propiedad-y-registro.bib concentra fuentes base y específicas."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: ubicación curricular semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: propósito de transformar planeación semanal en productos académicos.",
        "Programa analítico local: ejes de trabajo con problema, conceptos, producto, análisis propio y conclusión.",
        "BibTeX local: clave unadmSitioWeb para sitio institucional UnADM.",
        "BibTeX local: clave unadmMallaDerecho2024 para malla curricular de Derecho.",
        "Plantilla .tex local: coursename Derecho de la propiedad y registro.",
        "Plantilla .tex local: coursecode LDE-S7B1.",
        "Plantilla .tex local: documentsubject Licenciatura en Derecho.",
        "Plantilla .tex local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Plantilla .tex local: campo Figura docente pendiente.",
        "Origen transversal: ejes editoriales problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria heredada: salida no JSON parseable requiere normalización manual antes de reutilizarse."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5 conserva reglas locales verificadas de Derecho de la propiedad y registro.",
      "Ciclo 5 deduplica reglas repetidas sin eliminar contenido útil.",
      "Ciclo 5 transfiere solo abstracciones editoriales estables desde Filosofía del Derecho.",
      "Ciclo 5 evita transferir fuentes doctrinales específicas no pertinentes al destino.",
      "Ciclo 5 refuerza gates de JSON parseable, trazabilidad bibliográfica y ausencia de placeholders.",
      "Ciclo 5 normaliza relaciones del grafo a supports, contrasts, depends_on y develops.",
      "Ciclo 5 mantiene abiertos vacíos locales sobre rúbrica, figura docente, producto y fuentes específicas."
    ]
  }
}