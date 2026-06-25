{
  "summary": [
    "Memoria transversal consolidada para Electiva Semestre 8 Bloque 2.",
    "Identidad UnADM preservada para Licenciatura en Derecho.",
    "Estrategia conservadora aplicada por ser salto entre nodos no equivalentes.",
    "Se transfieren solo abstracciones editoriales estables.",
    "No se transfiere contenido temático específico de Filosofía del Derecho sin validación local.",
    "Ejes editoriales vigentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Normalización estructurada obligatoria antes de propagar.",
    "Compresión aplicada por unión y deduplicación.",
    "Alumno confirmado: Martin Jonathan de la Cruz.",
    "Matrícula confirmada: ES2611202040.",
    "Persisten riesgos locales: créditos vacíos, figura docente pendiente, placeholders y nombres truncados.",
    "Herencias no JSON previas se mantienen como provisionales hasta revisión manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Ubicar la materia en semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos.",
    "Fijar autor Martin Jonathan de la Cruz en front matter.",
    "Fijar matrícula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular cuando corresponda.",
    "No propagar datos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según consigna.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y archivo .bib local.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Corregir placeholders de plantillas en nombres de archivo y referencias.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres de archivo literales.",
    "Restaurar nombres truncados en listados, como eporte y eferencias.",
    "Evitar redacción literal heredada de nodos no equivalentes."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Verificar que el producto corresponda a la consigna vigente.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir análisis jurídico propio, no solo resumen de fuentes.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar cada actividad con conclusión aplicable a la práctica jurídica.",
    "No asumir fuentes de otra semana o materia sin confirmación local.",
    "No trasladar contenido específico de Filosofía del Derecho sin fuente verificable y pertinencia local."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de consolidar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclos previos antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Verificar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Validar correspondencia entre producto final y consigna de actividad.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Usar presentacion-electiva-semestre-8-bloque-2.tex como base de presentación cuando corresponda.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Completar figura docente solo con dato confirmado.",
    "Completar créditos solo con dato oficial confirmado.",
    "Mantener compatibilidad de nombres de archivos entre .tex y recursos de la materia.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Usar solo obras realmente consultables.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Marcar como [supuesto] cualquier dato bibliográfico no confirmado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias.",
    "Propagar reglas transversales de integridad académica en ecosistema UnADM.",
    "Etiquetar reglas heredadas de calidad como transversales de institución UnADM.",
    "No propagar contenido temático específico sin validación local.",
    "No propagar datos incompletos de créditos o figura docente.",
    "Mantener etiqueta provisional para herencias no verificadas.",
    "Propagar lección transversal de corregir placeholders y nombres truncados.",
    "Usar ciclos heredados 1 y 2 como etapas de normalización, no como evidencia definitiva.",
    "Mantener compresión por unión y deduplicación sin eliminar reglas útiles previas."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto.",
    "[supuesto] Confirmar fuentes obligatorias de cada actividad.",
    "[supuesto] Confirmar rúbricas de evaluación específicas.",
    "[supuesto] Confirmar productos solicitados por actividad.",
    "[supuesto] Verificar si el sitio institucional UnADM debe citarse con fecha de consulta actualizada.",
    "[supuesto] Confirmar si el año 2026 del sitio UnADM en .bib es dato vigente o placeholder.",
    "[supuesto] Confirmar política institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si se requiere bibliografía adicional local para la electiva.",
    "[supuesto] Confirmar corrección definitiva de README con nombres de archivo sin truncar.",
    "[supuesto] Confirmar eliminación de tokens $(@{...}.Slug) en archivos locales."
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
        "Carpeta de materia como entrada canónica.",
        "Metadatos institucionales consistentes.",
        "Control visible de supuestos.",
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Electiva Semestre 8 Bloque 2.",
        "Semestre 8.",
        "Bloque 2.",
        "Tipo Electiva.",
        "Código LDE-S8B2.",
        "[supuesto] Créditos pendientes de confirmación."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Postura académica argumentada.",
      "Conclusión jurídica transferible.",
      "Trazabilidad cita-texto-bib.",
      "Normalización estructurada.",
      "Control de supuestos.",
      "Corrección de placeholders."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en entregables concretos.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Asegurar identidad UnADM en cada actividad.",
      "Evitar entregas descriptivas sin juicio jurídico.",
      "Proteger la verificabilidad bibliográfica.",
      "Mantener coherencia entre README, programa, LaTeX y .bib.",
      "Permitir propagación transversal segura."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explícito.",
      "Secciones ordenadas.",
      "Conceptos delimitados.",
      "Marco normativo o doctrinal separado.",
      "Postura propia respaldada.",
      "Citas verificables.",
      "Cierre con transferencia profesional.",
      "Marcado explícito de [supuesto].",
      "Metadatos UnADM visibles.",
      "Autor y matrícula confirmados.",
      "Sin placeholders visibles."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> conceptos -> fuentes -> análisis -> conclusión.",
      "Hecho o problema -> norma o doctrina -> interpretación -> postura -> efecto práctico.",
      "Afirmación -> fuente verificable -> razonamiento propio -> cierre jurídico.",
      "Consigna -> producto solicitado -> criterios de entrega -> validación final.",
      "Dato confirmado -> uso directo.",
      "Dato no confirmado -> marca [supuesto] -> pregunta abierta.",
      "Fuente heredada -> validación local -> adopción o descarte.",
      "Error de plantilla -> corrección de ruta -> recompilación."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 2",
        "Código LDE-S8B2",
        "Problema jurídico",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis jurídico propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Trazabilidad cita-texto-bib",
        "Bibliografía local",
        "Malla curricular de Derecho",
        "Normalización estructurada",
        "JSON parseable",
        "Control de supuestos",
        "Compresión unión-dedupe",
        "Placeholders de plantilla",
        "Nombres de archivo truncados",
        "Propagación recursiva segura"
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
          "justification": "La identidad se expresa en portada, curso, autoría y contexto curricular."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "develops",
          "justification": "La materia destino pertenece al trayecto jurídico local."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la señala como fuente institucional de ubicación."
        },
        {
          "source": "Problema jurídico",
          "target": "Objetivo puntual",
          "kind": "develops",
          "justification": "El objetivo delimita el tratamiento del problema."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "El marco requiere conceptos definidos para evitar ambigüedad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "El análisis debe razonar sobre fuentes comprobables."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional surge del razonamiento del estudiante."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y referencias."
        },
        {
          "source": "Bibliografía local",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "supports",
          "justification": "El archivo .bib local centraliza las fuentes usadas."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes."
        },
        {
          "source": "JSON parseable",
          "target": "Normalización estructurada",
          "kind": "supports",
          "justification": "Permite consolidar memoria sin ambigüedad técnica."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Reduce errores heredados antes de aplicar reglas aguas abajo."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Sin regresión editorial",
          "kind": "supports",
          "justification": "Elimina duplicados sin descartar reglas útiles."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Errores de compilación o entrega",
          "kind": "supports",
          "justification": "Tokens visibles rompen coherencia documental y presentación final."
        },
        {
          "source": "Nombres de archivo truncados",
          "target": "Errores de trazabilidad local",
          "kind": "supports",
          "justification": "Listados incorrectos dificultan ubicar artefactos reales."
        },
        {
          "source": "Contenido temático de Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "contrasts",
          "justification": "No debe transferirse sin pertinencia y fuente local verificable."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 2, tipo Electiva.",
        "README local: créditos vacíos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "README local: nombres truncados eporte y eferencias.",
        "README local: token $(@{...}.Slug) visible.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "Archivo .bib local: clave unadmSitioWeb.",
        "Archivo .bib local: clave unadmMallaDerecho2024.",
        "Reporte LaTeX local: autor Martin Jonathan de la Cruz.",
        "Reporte LaTeX local: matrícula ES2611202040.",
        "Reporte LaTeX local: figura docente por definir.",
        "Reporte LaTeX local: créditos vacíos.",
        "Memoria origen: normalización estructurada obligatoria antes de propagar.",
        "Memoria origen: ejes editoriales de problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Memoria origen: no inventar referencias y validar citas contra .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 consolida identidad UnADM del destino sin copiar temática de origen.",
      "Se preservan reglas útiles previas mediante deduplicación.",
      "Se refuerza normalización JSON como gate transversal.",
      "Se refuerza estructura problema-conceptos-fuentes-análisis-conclusión.",
      "Se refuerza postura jurídica propia frente a resumen descriptivo.",
      "Se refuerza trazabilidad entre citas y .bib local.",
      "Se refuerza control de supuestos para créditos y figura docente.",
      "Se refuerza corrección de placeholders PowerShell.",
      "Se refuerza corrección de nombres truncados en README.",
      "Se mantienen fuentes heredadas no verificadas como provisionales.",
      "Se limita propagación a abstracciones editoriales estables.",
      "Se conserva la malla curricular como fuente institucional local."
    ]
  }
}