{
  "summary": [
    "Base institucional UnADM verificada y aplicable a la materia.",
    "Materia destino: Derecho de la propiedad y registro.",
    "Programa: Licenciatura en Derecho.",
    "Ubicación curricular verificada: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "La carpeta funciona como punto de entrada canónico de la asignatura.",
    "Se consolida sincronización transversal con Filosofía del Derecho.",
    "Se transfieren solo abstracciones editoriales estables.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva estrategia progresiva y conservadora sin regresión.",
    "Existe antecedente institucional con salida no JSON parseable; requiere normalización antes de reutilizarse."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar nivel y programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de México.",
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Registrar ubicación institucional local: Roma Norte, Ciudad de México.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentación, bibliografía y referencias.",
    "Transformar la planeación semanal en productos académicos claros.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar problema, conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia con semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas.",
    "Resolver tokens corruptos del README con el slug local verificado."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad antes del desarrollo.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "Vincular cada actividad con el producto solicitado por la planeación.",
    "Distinguir problema, fundamento, análisis y cierre argumentativo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Evitar afirmaciones jurídicas sin fuente o razonamiento propio.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar formato estructurado antes de propagar a nodos aguas abajo.",
    "Revisar estructura mínima completa antes de aplicar reglas.",
    "Revisar toda respuesta no estructurada heredada antes de reutilizarla.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar que cada fuente citada exista en BibTeX o repositorio local.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Confirmar que no existan placeholders sin resolver.",
    "Revisar sintaxis LaTeX de authortable antes de compilar."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor.",
    "Corregir Figura docente antes de entrega.",
    "Conservar matrícula del alumno ES2611202040 en tabla de autor salvo instrucción distinta.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instrucción distinta.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar compilación después de modificar portada, bibliografía o rutas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo BibTeX local verificado."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes específicas.",
    "Agregar fuentes específicas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir datos mínimos de consulta o archivo local cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Propagar identidad UnADM a nodos laterales solo si comparten institución.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre asignaturas.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Mantener compresión union-dedupe sin eliminar reglas útiles previas.",
    "Aplicar ciclo 1 con normalización manual si se reutiliza memoria heredada.",
    "Aplicar ciclo 2 con revisión de antecedentes no estructurados.",
    "Aplicar ciclo 4 con estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar si existe rúbrica formal de evaluación para esta materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir el placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres de archivo reales del README ante tokens corruptos detectados.",
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
        "Normalización estructurada antes de propagación."
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
      "Normalización JSON.",
      "Pertinencia con propiedad y registro."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicado a propiedad y registro.",
      "Evitar entregas descriptivas sin postura ni fundamento.",
      "Garantizar reutilización editorial segura entre nodos UnADM."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin referencias inventadas.",
      "Sin placeholders al cierre.",
      "Tono institucional UnADM.",
      "Nombre exacto de la materia.",
      "Ubicación curricular explícita.",
      "Cierre con criterio jurídico propio.",
      "Rutas y claves verificadas antes de compilar."
    ],
    "argumentative_patterns": [
      "Del problema al objetivo.",
      "Del objetivo al marco conceptual.",
      "Del marco conceptual al fundamento normativo.",
      "Del fundamento normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis propio a la postura jurídica.",
      "De la postura jurídica a una conclusión aplicable.",
      "De la planeación al producto solicitado.",
      "De la cita verificable a la trazabilidad en .bib.",
      "De la consigna local a la estructura final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho de la propiedad y registro",
        "Semestre 7 bloque 1",
        "LDE-S7B1",
        "Carpeta canónica de asignatura",
        "Planeación semanal",
        "Producto académico",
        "Problema jurídico",
        "Propiedad y registro",
        "Conceptos jurídicos",
        "Normas jurídicas",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión transferible",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Archivo BibTeX local",
        "Normalización JSON",
        "Salida no estructurada",
        "Tokens corruptos en README",
        "Compilación LaTeX"
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
          "justification": "La materia pertenece al programa de Derecho."
        },
        {
          "source": "Semestre 7 bloque 1",
          "target": "Derecho de la propiedad y registro",
          "kind": "supports",
          "justification": "La ubicación curricular local está verificada en README."
        },
        {
          "source": "LDE-S7B1",
          "target": "Metadatos LaTeX",
          "kind": "supports",
          "justification": "El código local debe mantenerse cuando corresponda."
        },
        {
          "source": "Carpeta canónica de asignatura",
          "target": "Archivo BibTeX local",
          "kind": "develops",
          "justification": "La carpeta contiene el .bib local de la materia."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa analítico indica transformar la planeación en productos académicos."
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
          "kind": "supports",
          "justification": "La pertinencia temática debe orientar los problemas de cada actividad."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo o doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La postura del estudiante debe sustentarse en fuentes o razonamiento jurídico."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia entre citas y .bib evita afirmaciones no verificables."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "Las fuentes específicas deben registrarse en el .bib de la materia."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Salida no estructurada",
          "target": "Normalización JSON",
          "kind": "depends_on",
          "justification": "Las salidas heredadas no parseables requieren revisión manual."
        },
        {
          "source": "Tokens corruptos en README",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens y nombres anómalos pueden romper rutas y referencias."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: propósito de transformar planeación en productos académicos.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "BibTeX local: clave unadmSitioWeb.",
        "BibTeX local: clave unadmMallaDerecho2024.",
        "Plantilla .tex local: coursename Derecho de la propiedad y registro.",
        "Plantilla .tex local: coursecode LDE-S7B1.",
        "Plantilla .tex local: documentsubject Licenciatura en Derecho.",
        "Memoria institucional heredada: salida no JSON parseable requiere normalización.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: no inventar referencias.",
        "Memoria origen: sustentar afirmaciones con fuentes verificables y cita explícita."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4 consolida reglas locales ya verificadas.",
      "Ciclo 4 deduplica identidad UnADM sin perder especificidad de la materia.",
      "Ciclo 4 conserva ubicación curricular local del destino.",
      "Ciclo 4 incorpora abstracciones transversales desde Filosofía del Derecho.",
      "Ciclo 4 evita transferir bibliografía específica no pertinente al destino.",
      "Ciclo 4 refuerza normalización JSON como gate de propagación.",
      "Ciclo 4 refuerza estructura problema-marco-evidencia-análisis-cierre.",
      "Ciclo 4 mantiene política de no inventar fuentes.",
      "Ciclo 4 preserva archivo BibTeX local como repositorio canónico.",
      "Ciclo 4 marca vacíos locales como preguntas abiertas."
    ]
  }
}