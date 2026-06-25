{
  "summary": [
    "Materia destino consolidada: Historia del Derecho en Mexico, Licenciatura en Derecho UnADM.",
    "Se preserva identidad institucional, marco curricular local y carpeta canónica.",
    "Se transfiere solo abstracción transversal desde Filosofía del Derecho.",
    "Se refuerzan cinco ejes editoriales: problema, conceptos, producto, análisis propio y conclusión.",
    "Se mantiene alerta histórica por salidas no JSON parseables.",
    "Se conserva base local verificable: README, programa analítico, plantilla LaTeX y .bib.",
    "Se evita transferir contenido temático de Filosofía del Derecho sin evidencia local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Usar nombre local: Historia del Derecho en Mexico.",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Marcar como supuesto cualquier dato no visible en documentos locales o consigna.",
    "Tratar antecedentes Codex y GPT-Pro como provisionales hasta confirmación local.",
    "No importar identidad curricular de Filosofía del Derecho al destino."
  ],
  "structure_rules": [
    "Alinear cada entrega a la planeación semanal.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Integrar fuentes, conceptos y datos pertinentes al problema.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar estructura al producto solicitado: reporte, presentación o producto visual.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental.",
    "Corregir placeholders de Slug antes de automatizar referencias o compilación."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Relacionar pregunta guía, desarrollo y conclusión.",
    "Usar conceptos, normas, doctrina o datos pertinentes al tema local.",
    "No mezclar contenido temático de Filosofía del Derecho sin evidencia local verificable.",
    "Actualizar subtítulo y metadatos según número y nombre real de actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa del esquema editorial.",
    "Aplicar unión-dedupe sin recortar reglas útiles previas.",
    "Confirmar que toda afirmación sustantiva tenga soporte o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Revisar render de nombres de archivo en README antes de automatizar.",
    "Resolver placeholders de Slug antes de compilar o citar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para presentaciones.",
    "Conservar metadatos: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener coursecode local LDE-S1B1 como supuesto hasta confirmación oficial.",
    "Conservar universidad, facultad, departamento, imagen institucional y ubicación.",
    "Mantener tabla de autor con alumno, matrícula, figura docente, semestre/bloque y tipo/créditos.",
    "No eliminar campos institucionales.",
    "Actualizar solo valores concretos exigidos por la actividad.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Mantener claves BibTeX estables.",
    "Verificar nombres de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliográfico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas.",
    "No inventar referencias.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Incluir trazabilidad mínima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No propagar bibliografía de Filosofía del Derecho sin consulta efectiva.",
    "Corregir referencias con placeholders de Slug antes de compilar o citar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales transversales verificables.",
    "Reutilizar estructura de cinco ejes con ajuste temático por asignatura.",
    "Propagar validación JSON y normalización temprana a materias hermanas.",
    "No propagar datos curriculares específicos de esta materia a laterales.",
    "No propagar contenido temático de Filosofía del Derecho al destino.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "Normalizar manualmente ciclos previos antes de reutilización automática.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar fuente operativa definitiva para consolidación de memoria.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es código oficial o código local.",
    "Validar acentuación oficial de Mexico/México según lineamiento institucional.",
    "Corregir posibles saltos anómalos en README: eporte y eferencias.",
    "Confirmar producto exacto de cada actividad antes de generar entrega.",
    "Confirmar rúbrica específica de evaluación por actividad.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si la carpeta referencias contiene materiales consultables adicionales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional con voz estudiantil.",
        "Conservador ante inferencias no verificadas."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Portada y metadatos coherentes con plantilla local.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 créditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S1B1 [supuesto hasta confirmación oficial]."
      ]
    },
    "essence": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Convertir planeación semanal en entregas verificables.",
      "Sostener cada actividad en problema, conceptos, producto, análisis propio y conclusión.",
      "Preservar identidad UnADM sin sacrificar postura estudiantil.",
      "Proteger trazabilidad bibliográfica y consistencia LaTeX.",
      "Sincronizar reglas transversales sin copiar contenido temático ajeno."
    ],
    "reason_for_being": [
      "Dar cerebro editorial estable a la materia.",
      "Asegurar coherencia entre consigna, fuentes, análisis y producto final.",
      "Facilitar reportes y presentaciones con formato institucional.",
      "Evitar inferencias no verificadas en materiales jurídicos.",
      "Hacer reutilizables las reglas de calidad en nodos vecinos."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual visible.",
      "Secciones funcionales y trazables.",
      "Citas explícitas y verificables.",
      "Postura argumentada del estudiante.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos.",
      "Metadatos institucionales consistentes.",
      "No transferencia literal entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Plantear problema jurídico o social.",
      "Definir objetivo de la actividad.",
      "Explicar conceptos clave.",
      "Ubicar marco normativo o doctrinal pertinente.",
      "Contrastar evidencia con postura propia.",
      "Evitar resumen aislado.",
      "Conectar desarrollo con pregunta guía.",
      "Cerrar con implicación práctica jurídica.",
      "Ajustar profundidad a rúbrica y producto solicitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Historia del Derecho en Mexico",
        "Licenciatura en Derecho",
        "Semestre 1 bloque 1",
        "Cinco ejes editoriales",
        "Problema jurídico o social",
        "Conceptos, normas, doctrina o datos",
        "Producto solicitado por planeación",
        "Análisis propio",
        "Conclusión transferible",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Coherencia entre consigna y producto",
        "Plantilla LaTeX local",
        "Bibliografía local",
        "Placeholders de Slug",
        "Supuestos explícitos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, producto, análisis y cierre."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria previa bloquea propagación si la salida no es parseable."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos mínimos."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La plantilla conserva portada, metadatos y tabla institucional."
        },
        {
          "source": "Bibliografía local",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "El .bib local contiene entradas institucionales y admite fuentes específicas de actividad."
        },
        {
          "source": "Placeholders de Slug",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens sin resolver pueden romper referencias, rutas o automatización."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Conservadurismo editorial",
          "kind": "supports",
          "justification": "Marcar supuestos evita convertir inferencias en datos verificados."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Historia del Derecho en Mexico",
          "kind": "contrasts",
          "justification": "Son nodos no equivalentes; solo comparten abstracciones editoriales estables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La postura argumentada debe conducir a una aplicación jurídica práctica."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 1, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: unadmSitioWeb.",
        "historia-del-derecho-en-mexico.bib: unadmMallaDerecho2024.",
        "Plantilla reporte local: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
        "Plantilla reporte local: alumno, matrícula, figura docente, semestre/bloque y tipo/créditos.",
        "Memoria previa: alerta por salidas no JSON parseables.",
        "Transferencia actual: solo abstracciones editoriales estables desde Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13 conserva reglas locales verificadas.",
      "Ciclo 13 deduplica reglas repetidas sin recorte semántico.",
      "Ciclo 13 refuerza cinco ejes editoriales como patrón transversal.",
      "Ciclo 13 bloquea transferencia temática no verificable desde Filosofía del Derecho.",
      "Ciclo 13 normaliza relaciones del grafo a tipos permitidos.",
      "Ciclo 13 mantiene alerta de JSON no parseable.",
      "Ciclo 13 marca acentuación de Mexico/México como pendiente.",
      "Ciclo 13 preserva .bib local como fuente bibliográfica canónica."
    ]
  }
}