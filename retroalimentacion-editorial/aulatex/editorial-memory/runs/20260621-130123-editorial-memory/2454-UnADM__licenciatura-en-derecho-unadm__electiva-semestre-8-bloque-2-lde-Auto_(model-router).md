{
  "summary": [
    "Se consolida memoria transversal de materia para Electiva Semestre 8 Bloque 2.",
    "Se conserva identidad UnADM y enfoque de Licenciatura en Derecho.",
    "Se refuerzan ejes estables: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se preserva normalización estructurada antes de propagación recursiva.",
    "Se mantiene estrategia conservadora ante fuentes heredadas no verificadas.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho sin validación local.",
    "Se refuerza corrección de placeholders, tokens sin expandir y nombres truncados.",
    "Se aplica compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos del reporte.",
    "Fijar autor Martin Jonathan de la Cruz en front matter.",
    "Fijar matrícula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta validación manual.",
    "Citar la malla curricular de Derecho como fuente de ubicación curricular local."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la consigna en reporte, presentación o producto visual según corresponda.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y .bib local.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Corregir placeholders de plantilla antes de entrega.",
    "Restaurar nombres truncados en listados de estructura."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir análisis jurídico propio, no solo resumen de fuentes.",
    "Evitar entregas puramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar cada actividad con conclusión aplicable a la práctica jurídica.",
    "No trasladar contenido específico de otra materia sin fuente verificable.",
    "No asumir que fuentes de otra semana corresponden a la actividad vigente.",
    "Confirmar que el producto corresponda a la consigna local."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizar.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Validar correspondencia del producto con la consigna vigente.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Reemplazar Actividad X por el número real de actividad.",
    "Completar figura docente solo con dato confirmado.",
    "Completar créditos solo con dato confirmado.",
    "Mantener codificación y acentos correctos en español.",
    "Mantener nombres de archivos compatibles entre .tex y recursos locales.",
    "Resolver tokens tipo $(@{...}.Slug) antes de compilar.",
    "Corregir caracteres anómalos en rutas o nombres de archivo.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 como base institucional local.",
    "Usar la malla curricular de Derecho para ubicación curricular.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Mantener claves BibTeX estables.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Marcar como [supuesto] cualquier dato bibliográfico no confirmado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y sin ambigüedad.",
    "Compartir abstracciones editoriales estables entre materias no equivalentes.",
    "No propagar contenido temático de Filosofía del Derecho sin validación local.",
    "Propagar reglas transversales de integridad académica en ecosistema UnADM.",
    "Etiquetar normalización estructurada como regla institucional transversal.",
    "Propagar lección de corregir placeholders y nombres truncados.",
    "No propagar datos incompletos de créditos o figura docente.",
    "Mantener etiqueta provisional para herencias Codex y GPT-Pro.",
    "Usar ciclo 1 como etapa de normalización, no como evidencia definitiva.",
    "Mantener compresión por unión-dedupe sin eliminar reglas útiles previas."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto.",
    "[supuesto] Confirmar consignas y productos de cada actividad local.",
    "[supuesto] Confirmar rúbricas de evaluación específicas.",
    "[supuesto] Confirmar fuentes obligatorias por semana.",
    "[supuesto] Verificar si el año 2026 de unadmSitioWeb es dato real o placeholder.",
    "[supuesto] Confirmar política institucional para fecha de consulta en @misc.",
    "[supuesto] Confirmar si se requieren presentaciones además de reportes.",
    "[supuesto] Confirmar limpieza final de README con nombres no truncados."
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
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en entregables concretos.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Evitar propagación de errores editoriales o datos no verificados."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explícito.",
      "Secciones ordenadas.",
      "Marco conceptual o normativo visible.",
      "Postura propia respaldada.",
      "Citas verificables.",
      "Cierre con transferencia profesional.",
      "Marcado explícito de [supuesto].",
      "Metadatos UnADM completos.",
      "Sin placeholders visibles."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual -> evidencia -> postura -> conclusión.",
      "Consigna -> producto solicitado -> estructura -> validación final.",
      "Afirmación jurídica -> fuente verificable -> análisis propio.",
      "Dato no confirmado -> marca [supuesto] -> pregunta abierta.",
      "Planeación semanal -> reporte o presentación -> cierre profesional.",
      "Resumen descriptivo -> contraste crítico -> criterio jurídico razonado.",
      "Fuente heredada -> validación local -> uso controlado."
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
        "Conceptos y fuentes",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Compresión unión-dedupe",
        "Placeholders de plantilla",
        "Nombres de archivo truncados",
        "Bibliografía institucional UnADM",
        "Malla curricular de Derecho",
        "Validación local de contenido temático"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
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
          "justification": "La verificabilidad requiere correspondencia entre texto y bibliografía."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte de un problema delimitado."
        },
        {
          "source": "Conceptos y fuentes",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Las fuentes verificables sostienen la postura del estudiante."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre debe derivarse de fundamentos jurídicos explícitos."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional surge del criterio argumentado."
        },
        {
          "source": "Bibliografía institucional UnADM",
          "target": "Malla curricular de Derecho",
          "kind": "develops",
          "justification": "La malla local documenta la ubicación curricular."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Calidad editorial",
          "kind": "contrasts",
          "justification": "Los tokens visibles contradicen una entrega final limpia."
        },
        {
          "source": "Nombres de archivo truncados",
          "target": "Trazabilidad entre documentos locales",
          "kind": "contrasts",
          "justification": "Los listados truncados rompen coherencia entre README y archivos reales."
        },
        {
          "source": "Validación local de contenido temático",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Impide importar materia ajena como si fuera evidencia del destino."
        },
        {
          "source": "Compresión unión-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles sin duplicación ni recorte."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 2, tipo Electiva.",
        "README local: créditos vacíos pendientes de confirmación.",
        "README local: pauta de identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "README local: presencia de nombre truncado eporte-electiva-semestre-8-bloque-2.tex.",
        "README local: presencia de nombre truncado eferencias-electiva-semestre-8-bloque-2.",
        "README local: presencia de token $(@{...}.Slug) sin expandir.",
        "Programa analítico local: propósito de transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: bibliografía específica debe agregarse en el .bib local.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local: autor Martin Jonathan de la Cruz.",
        "Plantilla .tex local: matrícula ES2611202040.",
        "Plantilla .tex local: código de curso LDE-S8B2.",
        "Herencia institucional: revisar respuestas no estructuradas antes de aplicar aguas abajo.",
        "Origen transversal: bloquear propagación si la salida no es JSON parseable.",
        "Origen transversal: sustentar afirmaciones con fuentes verificables y cita explícita.",
        "Origen transversal: marcar supuestos ante datos no visibles en la consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se deduplican reglas repetidas sin eliminar contenido útil.",
      "Ciclo 20: se preserva identidad local de Electiva Semestre 8 Bloque 2.",
      "Ciclo 20: se incorporan solo abstracciones estables desde Filosofía del Derecho.",
      "Ciclo 20: se evita importar citas y temas filosófico-jurídicos no validados para la electiva.",
      "Ciclo 20: se refuerza normalización JSON como gate transversal.",
      "Ciclo 20: se refuerza trazabilidad entre texto, citas y .bib.",
      "Ciclo 20: se mantiene autor y matrícula confirmados.",
      "Ciclo 20: se mantienen créditos y figura docente como preguntas abiertas.",
      "Ciclo 20: se eleva corrección de placeholders a regla operativa transversal.",
      "Ciclo 20: se conserva compresión lossless por unión-dedupe."
    ]
  }
}