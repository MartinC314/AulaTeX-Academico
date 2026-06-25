{
  "summary": [
    "Se consolida cerebro editorial de materia para Derecho de la propiedad y registro.",
    "Se conserva identidad institucional UnADM verificada.",
    "Se mantiene ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Se sincronizan abstracciones transversales desde Filosofía del Derecho sin importar contenido específico.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva política de normalización obligatoria para salidas no JSON.",
    "Se aplica compresión por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de México.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Registrar ubicación institucional local solo si la plantilla vigente la conserva.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular."
  ],
  "structure_rules": [
    "Alinear entregables con reporte, presentación, bibliografía y referencias locales.",
    "Transformar la planeación semanal en producto académico claro.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Relacionar conceptos, normas, doctrina o datos pertinentes con propiedad y registro.",
    "Incluir evidencia verificable antes de la postura propia.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Verificar nombres de archivos del README antes de automatizar rutas.",
    "Resolver tokens corruptos del README con el slug local verificado.",
    "Adaptar formato final a reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "Distinguir problema, fundamento, análisis y cierre argumentativo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores sin validación de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Ajustar profundidad argumentativa a la rúbrica local cuando exista.",
    "Cerrar cada actividad con criterio jurídico propio y sustentado."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar coherencia entre consigna y pauta editorial de la materia.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar trazabilidad entre citas en texto y archivo BibTeX.",
    "Confirmar que cada fuente citada exista en repositorio local o sea consultable.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Confirmar que no existan placeholders sin resolver.",
    "Revisar sintaxis LaTeX de portada, authortable, bibliografía y rutas.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos obligatorios antes de compilar.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor.",
    "Corregir Figura docente antes de entrega.",
    "Conservar autor y matrícula locales salvo instrucción distinta.",
    "Usar codificación y acentos correctos en español.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens sin expandir en nombres de archivo.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar compilación después de modificar portada, bibliografía o rutas."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo BibTeX local.",
    "Agregar fuentes específicas de la actividad en el BibTeX local.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir datos de consulta o archivo local cuando aplique.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir bibliografía de otra asignatura como fuente local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "No propagar contenido doctrinal específico de Filosofía del Derecho al destino.",
    "Propagar identidad UnADM solo a nodos que compartan institución.",
    "Propagar reglas curriculares locales solo dentro de esta materia.",
    "No propagar datos locales de archivo si no existen en el receptor.",
    "Mantener compresión union-dedupe sin eliminar reglas útiles previas.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Reutilizar gates de calidad institucional sin reducir especificidad local.",
    "Aplicar estrategia progresiva y conservadora en ciclos futuros."
  ],
  "open_questions": [
    "Confirmar rúbrica formal de evaluación de la materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres reales del README ante tokens y caracteres corruptos.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Supuesto: falta consigna local detallada por actividad.",
    "Supuesto: la plantilla local conserva autor y matrícula mientras no exista instrucción contraria.",
    "Supuesto: el archivo BibTeX canónico es derecho-de-la-propiedad-y-registro.bib."
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
      "Postura académica argumentada.",
      "Conclusión jurídica transferible.",
      "Trazabilidad bibliográfica.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conectar la materia con la práctica jurídica de propiedad y registro.",
      "Evitar entregas descriptivas sin criterio jurídico propio.",
      "Garantizar reutilización segura mediante JSON parseable y reglas verificables."
    ],
    "style_markers": [
      "Enunciados breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin afirmaciones sin fuente.",
      "Sin referencias inventadas.",
      "Sin placeholders al cierre.",
      "Tono institucional UnADM.",
      "Nombre exacto de la materia.",
      "Conclusión con transferencia profesional.",
      "Citas rastreables al BibTeX local.",
      "Rutas verificadas antes de compilar."
    ],
    "argumentative_patterns": [
      "Del problema jurídico al objetivo.",
      "Del objetivo a los conceptos clave.",
      "De los conceptos al marco normativo o doctrinal.",
      "Del marco a la evidencia verificable.",
      "De la evidencia al análisis propio.",
      "Del análisis a la postura jurídica.",
      "De la postura a la conclusión aplicable.",
      "De la consigna al producto solicitado.",
      "De la cita al archivo BibTeX.",
      "Del supuesto a la verificación pendiente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho de la propiedad y registro",
        "Semestre 7 bloque 1",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura jurídica",
        "Conclusión transferible",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Planeación semanal",
        "Producto académico",
        "Archivo BibTeX local"
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
          "kind": "develops",
          "justification": "La materia pertenece al programa local verificado."
        },
        {
          "source": "Semestre 7 bloque 1",
          "target": "Derecho de la propiedad y registro",
          "kind": "develops",
          "justification": "La ubicación curricular está indicada en README y programa analítico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Postura jurídica",
          "kind": "supports",
          "justification": "La postura requiere fundamento jurídico o doctrinal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La evidencia evita afirmaciones no sustentadas."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "Las claves locales permiten verificar citas y fuentes."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La consistencia entre texto y BibTeX sostiene la confiabilidad académica."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "La planeación define si el entregable será reporte, presentación o producto visual."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión debe derivar del razonamiento desarrollado."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho de la propiedad y registro",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones editoriales estables entre materias no equivalentes."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica y citas verificables.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "BibTeX local: unadmSitioWeb.",
        "BibTeX local: unadmMallaDerecho2024.",
        "Plantilla local: coursename Derecho de la propiedad y registro.",
        "Plantilla local: coursecode LDE-S7B1.",
        "Memoria origen: normalización estructurada obligatoria antes de propagar.",
        "Memoria origen: ejes editoriales problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15 consolida sincronización transversal con estrategia progresiva y conservadora.",
      "Se preservan reglas locales verificadas del destino.",
      "Se agregan solo abstracciones estables del origen.",
      "Se descarta transferencia de citas y doctrina específicas de Filosofía del Derecho.",
      "Se deduplican formulaciones equivalentes sin recortar reglas útiles.",
      "Se refuerza bloqueo de propagación para salidas no JSON.",
      "Se normalizan reglas de estructura en un patrón reusable.",
      "Se mantiene abierto el contexto local faltante por actividad."
    ]
  }
}