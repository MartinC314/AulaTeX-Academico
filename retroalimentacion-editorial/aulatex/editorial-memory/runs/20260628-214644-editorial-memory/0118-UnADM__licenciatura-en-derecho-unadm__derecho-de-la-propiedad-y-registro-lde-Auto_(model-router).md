{
  "summary": [
    "Materia destino consolidada con identidad UnADM verificada.",
    "Sincronización transversal aplicada de forma progresiva y conservadora.",
    "Se preservan reglas locales de Derecho de la propiedad y registro.",
    "Se transfieren solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, fuentes, análisis propio y cierre jurídico.",
    "Se mantiene normalización obligatoria antes de propagar salidas no estructuradas.",
    "Ubicación curricular local verificada: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "La carpeta de la materia funciona como punto de entrada canónico.",
    "Bibliografía local inicial: sitio institucional UnADM y malla curricular de Derecho.",
    "Persisten vacíos locales sobre rúbrica, figura docente y productos por actividad."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de México.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Marcar como provisional toda regla heredada desde otro programa académico.",
    "Conservar ubicación institucional local si la plantilla la exige: Roma Norte, Ciudad de México.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular."
  ],
  "structure_rules": [
    "Alinear entregables con reporte, presentación, bibliografía y referencias locales.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir problema, fundamento, análisis y conclusión jurídica transferible.",
    "Transformar la planeación semanal en el producto solicitado por la consigna.",
    "Vincular el desarrollo con propiedad y registro cuando corresponda.",
    "Cerrar con conclusión aplicable a la práctica profesional.",
    "Verificar nombres de archivos del README antes de automatizar rutas.",
    "Resolver tokens corruptos del README con el slug local verificado.",
    "Usar derecho-de-la-propiedad-y-registro.bib como bibliografía local canónica."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad.",
    "Relacionar el contenido con propiedad, registro o derechos reales cuando aplique.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular cada actividad con el producto solicitado por la planeación.",
    "Evitar extrapolar fuentes de otras semanas sin validación.",
    "No transferir fuentes específicas de Filosofía del Derecho al destino sin pertinencia local.",
    "Marcar supuestos cuando falte consigna, rúbrica o fuente obligatoria.",
    "Cerrar cada actividad con criterio jurídico propio y sustentado."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo BibTeX.",
    "Confirmar que cada fuente citada exista en BibTeX o repositorio local.",
    "Confirmar que la conclusión responda al problema planteado.",
    "Confirmar correspondencia entre consigna, producto y estructura editorial.",
    "Revisar que no existan placeholders sin resolver.",
    "Revisar sintaxis LaTeX de la tabla de autor antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instrucción distinta.",
    "Completar metadatos académicos antes de compilar.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Evitar placeholders en portada y tabla de autor.",
    "Corregir Figura docente antes de entrega.",
    "Conservar matrícula ES2611202040 en tabla de autor salvo instrucción distinta.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instrucción distinta.",
    "Usar codificación y acentos correctos en español.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar compilación después de modificar portada, bibliografía o rutas.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-propiedad-y-registro.bib para fuentes específicas.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Agregar fuentes específicas de cada actividad en el BibTeX local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar unadmSitioWeb para el sitio institucional consultado.",
    "Conservar unadmMallaDerecho2024 para la malla curricular local.",
    "Incluir datos de consulta o archivo local cuando aplique.",
    "Validar que las claves citadas existan antes de compilar.",
    "No asumir bibliografía de Filosofía del Derecho como pertinente para propiedad y registro."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar identidad UnADM solo a nodos que compartan institución.",
    "Propagar reglas curriculares locales solo dentro de esta materia.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "Evitar transferir redacción literal desde actividades de otra asignatura.",
    "No propagar datos locales de archivo si no existen en el nodo receptor.",
    "Mantener compresión union-dedupe sin eliminar reglas útiles previas.",
    "Aplicar normalización manual a salidas no JSON antes de reutilizarlas.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia local.",
    "Reutilizar gates institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Revisar antecedentes no estructurados de Codex y GPT-Pro antes de nuevos ciclos."
  ],
  "open_questions": [
    "Confirmar rúbrica formal de evaluación de la materia.",
    "Confirmar estilo de citación jurídica requerido por la figura docente.",
    "Confirmar figura docente para sustituir placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto.",
    "Confirmar fuentes jurídicas específicas de propiedad y registro para actividades futuras.",
    "Confirmar nombres reales de archivos del README ante tokens corruptos.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Confirmar si existen actividades con bibliografía obligatoria distinta del BibTeX local.",
    "Supuesto: falta consigna textual de actividades específicas del destino.",
    "Supuesto: falta rúbrica docente específica del destino."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica en carpeta de asignatura.",
        "Normalización obligatoria antes de propagar.",
        "Supuestos explícitos cuando falte evidencia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Código local: LDE-S7B1.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Fundamento jurídico verificable.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Propiedad y registro como anclaje disciplinar.",
      "Integridad académica con trazabilidad.",
      "Producto alineado con la planeación semanal.",
      "Compresión editorial por unión y deduplicación."
    ],
    "reason_for_being": [
      "Orientar productos académicos claros y verificables.",
      "Transformar planeación semanal en entregables jurídicos.",
      "Integrar problema, conceptos, fuentes, análisis y cierre.",
      "Formar criterio jurídico aplicado a propiedad y registro.",
      "Sostener continuidad editorial entre actividades de la materia.",
      "Permitir propagación segura sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Portada con metadatos UnADM completos.",
      "Nombre exacto de materia en metadatos.",
      "Problema y objetivo visibles al inicio.",
      "Separación entre marco conceptual, fundamento y análisis.",
      "Citas explícitas para afirmaciones relevantes.",
      "Supuestos marcados con claridad.",
      "Conclusión con utilidad profesional.",
      "Evitar resumen sin postura.",
      "Evitar fuentes no verificadas.",
      "Lenguaje jurídico preciso y sobrio."
    ],
    "argumentative_patterns": [
      "Problema delimitado desarrolla análisis propio.",
      "Objetivo puntual guía la estructura.",
      "Conceptos clave preparan el marco normativo.",
      "Normas y doctrina sustentan la interpretación.",
      "Fuentes verificables respaldan afirmaciones.",
      "Contraste de fuentes evita opinión vacía.",
      "Postura estudiantil responde al problema.",
      "Conclusión sintetiza criterio y aplicación práctica.",
      "Propiedad y registro anclan la pertinencia local.",
      "Consigna y planeación determinan el formato final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1.",
        "Materia obligatoria de 8 créditos.",
        "Código LDE-S7B1.",
        "Carpeta de asignatura como entrada canónica.",
        "Problema jurídico o social.",
        "Objetivo puntual.",
        "Conceptos jurídicos clave.",
        "Marco normativo o doctrinal.",
        "Fuentes verificables.",
        "Análisis propio.",
        "Postura académica.",
        "Conclusión jurídica transferible.",
        "Propiedad.",
        "Registro.",
        "Planeación semanal.",
        "Reporte académico.",
        "Presentación académica.",
        "Bibliografía local.",
        "Normalización JSON.",
        "Compresión union-dedupe.",
        "Supuesto editorial.",
        "Placeholder LaTeX.",
        "Token README sin expandir."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM.",
          "target": "Integridad académica con citas verificables.",
          "kind": "supports",
          "justification": "La pauta editorial local exige identidad UnADM, integridad académica y citas verificables."
        },
        {
          "source": "Malla curricular de Derecho.",
          "target": "Semestre 7, bloque 1.",
          "kind": "supports",
          "justification": "El README local registra la ubicación curricular con fuente en la malla curricular."
        },
        {
          "source": "Derecho de la propiedad y registro.",
          "target": "Propiedad.",
          "kind": "develops",
          "justification": "La materia destino exige anclaje disciplinar en propiedad."
        },
        {
          "source": "Derecho de la propiedad y registro.",
          "target": "Registro.",
          "kind": "develops",
          "justification": "La materia destino exige anclaje disciplinar en registro."
        },
        {
          "source": "Problema jurídico o social.",
          "target": "Objetivo puntual.",
          "kind": "develops",
          "justification": "El objetivo delimita la respuesta esperada al problema."
        },
        {
          "source": "Objetivo puntual.",
          "target": "Análisis propio.",
          "kind": "supports",
          "justification": "El análisis se organiza a partir del objetivo declarado."
        },
        {
          "source": "Conceptos jurídicos clave.",
          "target": "Marco normativo o doctrinal.",
          "kind": "depends_on",
          "justification": "El marco requiere categorías conceptuales previamente delimitadas."
        },
        {
          "source": "Fuentes verificables.",
          "target": "Análisis propio.",
          "kind": "supports",
          "justification": "Las fuentes sustentan afirmaciones y reducen opinión no fundada."
        },
        {
          "source": "Análisis propio.",
          "target": "Conclusión jurídica transferible.",
          "kind": "supports",
          "justification": "La conclusión debe derivarse del razonamiento desarrollado."
        },
        {
          "source": "Planeación semanal.",
          "target": "Reporte académico.",
          "kind": "develops",
          "justification": "La planeación puede requerir reporte como producto."
        },
        {
          "source": "Planeación semanal.",
          "target": "Presentación académica.",
          "kind": "develops",
          "justification": "La planeación puede requerir presentación como producto."
        },
        {
          "source": "Bibliografía local.",
          "target": "Fuentes verificables.",
          "kind": "supports",
          "justification": "El BibTeX local concentra fuentes institucionales y específicas."
        },
        {
          "source": "Normalización JSON.",
          "target": "Propagación recursiva.",
          "kind": "supports",
          "justification": "La propagación queda bloqueada si la salida no es parseable."
        },
        {
          "source": "Token README sin expandir.",
          "target": "Placeholder LaTeX.",
          "kind": "contrasts",
          "justification": "Ambos son riesgos editoriales distintos y requieren corrección antes de entrega."
        },
        {
          "source": "Supuesto editorial.",
          "target": "Evidencia local.",
          "kind": "contrasts",
          "justification": "Un dato sin evidencia debe marcarse como supuesto hasta verificación."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: cada actividad conserva identidad UnADM, integridad académica y citas verificables.",
        "README local: conclusión jurídica con criterio propio.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: bibliografía específica en derecho-de-la-propiedad-y-registro.bib.",
        "BibTeX local: unadmSitioWeb.",
        "BibTeX local: unadmMallaDerecho2024.",
        "Plantilla LaTeX local: coursename Derecho de la propiedad y registro.",
        "Plantilla LaTeX local: coursecode LDE-S7B1.",
        "Plantilla LaTeX local: documentsubject Licenciatura en Derecho.",
        "Plantilla LaTeX local: Figura docente pendiente.",
        "Memoria origen: normalizar salidas no estructuradas antes de propagar.",
        "Memoria origen: usar problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria heredada: revisar respuesta no estructurada antes de aplicar aguas abajo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 preserva reglas locales verificadas del destino.",
      "Ciclo 2 deduplica reglas repetidas sin recortar contenido útil.",
      "Ciclo 2 refuerza identidad UnADM compartida.",
      "Ciclo 2 evita transferir fuentes específicas de Filosofía del Derecho.",
      "Ciclo 2 mantiene gates de JSON parseable y normalización manual.",
      "Ciclo 2 ancla el razonamiento a propiedad y registro.",
      "Ciclo 2 conserva vacíos locales como preguntas abiertas.",
      "Ciclo 2 corrige propagación transversal hacia abstracciones estables."
    ]
  }
}