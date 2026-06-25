{
  "summary": [
    "Memoria transversal consolidada para la materia Electiva Semestre 8 Bloque 2.",
    "Se preserva identidad UnADM con enfoque jurídico y académico.",
    "Se refuerzan ejes reutilizables: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene estrategia conservadora ante datos no confirmados.",
    "Se bloquea propagación de salidas no JSON o no normalizadas.",
    "Se conserva control de placeholders, rutas y nombres de archivo truncados.",
    "El alumno confirmado es Martin Jonathan de la Cruz, matrícula ES2611202040.",
    "La herencia Codex y GPT-Pro se mantiene provisional hasta validación manual.",
    "No se transfiere contenido temático específico de Filosofía del Derecho sin fuente local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos del reporte.",
    "Fijar autor Martin Jonathan de la Cruz y matrícula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] todo dato institucional no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Citar la malla curricular de Derecho como fuente de ubicación curricular cuando se use ese dato."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según consigna.",
    "Alinear la entrega con el producto solicitado por la consigna vigente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y .bib local.",
    "Corregir placeholders de plantillas en nombres de archivo y referencias.",
    "Restaurar nombres truncados en listados, como eporte y eferencias."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir análisis jurídico propio, no solo resumen de fuentes.",
    "Evitar entregas puramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar cada actividad con conclusión aplicable a la práctica jurídica.",
    "No asumir fuentes de otras semanas o materias sin confirmación local.",
    "No trasladar contenido específico de Filosofía del Derecho sin fuente verificable."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar memoria aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizarlos.",
    "Confirmar que toda afirmación tenga respaldo o marca de [supuesto].",
    "Verificar trazabilidad entre afirmaciones, citas en texto y claves BibTeX.",
    "Confirmar que los datos de portada coincidan con la materia destino.",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Validar que el producto final corresponda a la consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia con metadatos institucionales.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Reemplazar Actividad X por el número real de actividad.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Completar figura docente y créditos solo con datos confirmados.",
    "Mantener compatibilidad entre nombres de archivos, recursos y referencias internas.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 solo si sus datos se verifican.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar como [supuesto] cualquier dato bibliográfico no confirmado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y sin ambigüedad.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reutilizable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal o contenido temático local.",
    "Propagar reglas de integridad académica a materias UnADM compatibles.",
    "Etiquetar reglas heredadas de calidad como transversales de institución UnADM.",
    "Mantener compresión por unión y deduplicación sin eliminar reglas útiles.",
    "Mantener etiqueta de herencia provisional hasta revisión manual.",
    "Usar ciclo 1 como etapa de normalización, no como evidencia definitiva.",
    "Propagar la corrección de placeholders como lección transversal de generación.",
    "No propagar datos incompletos de créditos o figura docente."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de la figura docente.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto.",
    "[supuesto] Confirmar consigna y producto exacto de cada actividad.",
    "[supuesto] Confirmar rúbrica de evaluación específica por actividad.",
    "[supuesto] Confirmar fuentes obligatorias de cada semana.",
    "[supuesto] Confirmar política institucional para año y fecha de consulta en @misc del sitio UnADM.",
    "[supuesto] Confirmar si el año 2026 del sitio UnADM en .bib es correcto o placeholder.",
    "[supuesto] Confirmar nombre canónico final del archivo .bib local.",
    "[supuesto] Confirmar si debe existir carpeta referencias-electiva-semestre-8-bloque-2."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Metadatos institucionales consistentes.",
        "Carpeta de materia como entrada canónica.",
        "Control explícito de supuestos.",
        "Normalización estructurada antes de propagar.",
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Electiva Semestre 8 Bloque 2.",
        "Semestre 8.",
        "Bloque 2.",
        "Tipo Electiva.",
        "Código de curso LDE-S8B2.",
        "[supuesto] Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Trazabilidad cita-texto-bib.",
      "Control de supuestos.",
      "Normalización estructurada."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en entregables concretos.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar que cada entrega responda a la consigna vigente.",
      "Proteger la memoria editorial contra errores heredados o no verificables."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explícito.",
      "Secciones ordenadas y reconocibles.",
      "Postura propia respaldada.",
      "Citas verificables.",
      "Cierre con transferencia profesional.",
      "Marcado visible de [supuesto].",
      "Metadatos UnADM consistentes.",
      "Corrección de placeholders antes de entrega.",
      "Lenguaje jurídico claro."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual o normativo -> análisis propio -> conclusión.",
      "Hecho o consigna -> fuente verificable -> razonamiento jurídico -> postura.",
      "Concepto -> norma o doctrina -> aplicación al caso -> implicación profesional.",
      "Dato no confirmado -> marca [supuesto] -> pregunta abierta.",
      "Planeación semanal -> producto solicitado -> estructura editorial -> revisión final.",
      "Evidencia institucional -> ubicación curricular -> metadatos consistentes.",
      "Resumen descriptivo -> contraste crítico -> criterio jurídico propio."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 2",
        "Código LDE-S8B2",
        "Integridad académica",
        "Normalización estructurada",
        "Propagación recursiva segura",
        "Problema jurídico",
        "Objetivo puntual",
        "Marco conceptual",
        "Marco normativo o doctrinal",
        "Análisis jurídico propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Producto solicitado por la planeación",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Fuentes institucionales UnADM",
        "Malla curricular de Derecho",
        "Placeholders sin expandir",
        "Nombres de archivo truncados",
        "Compresión unión-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos institucionales consistentes",
          "kind": "supports",
          "justification": "La portada, el front matter y los documentos locales deben mostrar la misma identidad."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "develops",
          "justification": "La materia destino se ubica dentro del trayecto curricular de Derecho."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la declara como fuente para semestre, bloque y tipo."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables o reglas ambiguas."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones, citas y .bib."
        },
        {
          "source": "Problema jurídico",
          "target": "Objetivo puntual",
          "kind": "develops",
          "justification": "El objetivo delimita la respuesta al problema planteado."
        },
        {
          "source": "Marco conceptual",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "Los conceptos permiten justificar la postura del estudiante."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "Las normas y doctrina sostienen el razonamiento jurídico."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional surge del razonamiento y no del resumen."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Estructura editorial",
          "kind": "depends_on",
          "justification": "La forma final debe ajustarse a la consigna vigente."
        },
        {
          "source": "Placeholders sin expandir",
          "target": "Calidad de entrega",
          "kind": "contrasts",
          "justification": "Los tokens visibles contradicen una entrega final revisada."
        },
        {
          "source": "Nombres de archivo truncados",
          "target": "Trazabilidad documental",
          "kind": "contrasts",
          "justification": "Los nombres incompletos rompen la correspondencia entre README, carpeta y compilación."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin duplicados ni regresiones."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 2, tipo Electiva.",
        "README local: créditos vacíos; requieren confirmación.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: pauta de identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: propósito de transformar planeación semanal en productos académicos.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Contexto local: existen placeholders $(@{...}.Slug) en README y programa.",
        "Contexto local: existen nombres truncados eporte y eferencias en README.",
        "Plantilla LaTeX local: autor Martin Jonathan de la Cruz y matrícula ES2611202040.",
        "Plantilla LaTeX local: figura docente y créditos pendientes.",
        "Herencia institucional: revisar salidas no estructuradas antes de propagarlas.",
        "Origen transversal: normalización JSON, control de supuestos y trazabilidad bibliográfica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14 consolida reglas transversales sin transferir contenido temático específico.",
      "Se deduplican reglas equivalentes de identidad, estructura y calidad.",
      "Se refuerza JSON parseable como condición de propagación.",
      "Se conserva la herencia provisional Codex y GPT-Pro hasta revisión local.",
      "Se integran ejes estables del origen: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
      "Se preservan reglas locales sobre autor, matrícula, código LDE-S8B2 y plantilla base.",
      "Se refuerza corrección de placeholders PowerShell y nombres truncados.",
      "Se mantienen abiertas las preguntas sobre créditos, figura docente, nombre oficial y fechas bibliográficas.",
      "Se normaliza el grafo conceptual con relaciones permitidas y justificación breve.",
      "Se evita inventar fuentes y se conservan solo claves bibliográficas locales verificables."
    ]
  }
}