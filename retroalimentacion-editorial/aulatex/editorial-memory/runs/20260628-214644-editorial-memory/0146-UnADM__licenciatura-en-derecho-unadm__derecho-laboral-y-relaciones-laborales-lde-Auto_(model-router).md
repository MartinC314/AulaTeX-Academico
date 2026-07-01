{
  "summary": [
    "Memoria de materia consolidada para Derecho laboral y relaciones laborales.",
    "Se conserva identidad UnADM y enfoque juridico-laboral del destino.",
    "Sincronizacion transversal aplicada con estrategia progresiva y conservadora.",
    "Se aplico union-dedupe lossless sobre reglas utiles previas.",
    "Se preservan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Ubicacion curricular local verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Existe antecedente de salida no parseable desde Codex y GPT-Pro.",
    "Normalizar heredados no parseables antes de reutilizacion o propagacion.",
    "No transferir contenido doctrinal especifico de Filosofia del Derecho sin pertinencia laboral verificada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos locales: Derecho laboral y relaciones laborales, LDE-S7B1, semestre 7, bloque 1.",
    "Vincular toda entrega a la Licenciatura en Derecho.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar la malla curricular de Derecho para ubicacion curricular cuando aplique.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Marcar como supuesto cualquier dato personal no confirmado del autor.",
    "Usar el autor de plantilla solo si el alumno lo confirma.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Marcar memoria heredada desde Codex o GPT-Pro como provisional si se reutiliza."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Organizar productos como reporte, presentacion, bibliografia local, programa analitico y carpeta de referencias.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar README de materia como punto de entrada canonico.",
    "Registrar nuevas reglas por union-dedupe sin eliminar reglas vigentes utiles.",
    "Corregir rutas o nombres de archivo mal renderizados antes de canonizarlos.",
    "Resolver marcadores PowerShell sin expandir hacia el slug derecho-laboral-y-relaciones-laborales."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social laboral.",
    "Formular una pregunta guia verificable.",
    "Incluir postura academica propia, no solo resumen descriptivo.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables.",
    "Vincular conceptos laborales con aplicacion profesional comprobable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto corresponda a la consigna de la actividad.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "No asumir fuentes de semanas posteriores como fuentes de la actividad actual.",
    "Marcar como supuesto cualquier inferencia necesaria no confirmada por la consigna."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar o propagar memoria.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Verificar consistencia entre README, programa analitico y plantilla LaTeX.",
    "Verificar que metadatos coincidan con fuentes locales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar trazabilidad de toda cita y ausencia de fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar existencia de archivos y carpetas o marcarlos como supuestos.",
    "Detectar y corregir marcadores de plantilla sin expandir.",
    "Verificar correspondencia del producto con la consigna local.",
    "Preservar reglas utiles previas aunque provengan de memoria institucional."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base por actividad.",
    "Completar metadatos con datos reales de la actividad.",
    "Mantener compatibilidad con compilacion en espanol y letterpaper.",
    "Conservar macros institucionales de universidad, curso, codigo y licenciatura.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Validar cierre de entornos LaTeX antes de compilar.",
    "Completar el entorno authortable truncado antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Evitar rutas o nombres derivados de plantillas no resueltas.",
    "Resolver marcadores PowerShell sin expandir en README, programa analitico y bibliografia."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar fuentes institucionales UnADM ya incluidas.",
    "Conservar claves base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Agregar solo entradas BibTeX verificables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Marcar como supuesto metadatos faltantes como fecha de consulta.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Corregir referencias al marcador PowerShell de bibliografia antes de citar.",
    "No asumir bibliografia de Filosofia del Derecho como bibliografia laboral sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "En ciclo 1, priorizar normalizacion manual de heredados no estructurados.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar solo abstracciones editoriales estables entre materias no equivalentes.",
    "Propagar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido doctrinal especifico del origen.",
    "Propagar solo mejoras verificables y compatibles con contexto juridico-laboral.",
    "Mantener especificidad local del destino al recibir reglas transversales.",
    "Priorizar correccion de artefactos de plantilla en el ciclo actual."
  ],
  "open_questions": [
    "Confirmar consigna textual de cada actividad laboral.",
    "Confirmar producto exacto solicitado por actividad.",
    "Confirmar rubrica oficial para convertirla en checklist.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Definir formato de cita juridica requerido por docente: APA, ISO 690 u otro.",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar si Martin Jonathan de la Cruz es el autor correcto.",
    "Confirmar nombres canonicos finales de reporte, presentacion y carpeta de referencias.",
    "Confirmar si el codigo LDE-S7B1 basta como codigo unico para todas las actividades.",
    "Confirmar fuentes laborales base de la materia antes de ampliar bibliografia.",
    "Confirmar si existen criterios locales sobre legislacion vigente, jurisprudencia y doctrina laboral."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en transferencia transversal.",
        "Explícito al marcar supuestos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Portada y metadatos coherentes con plantilla local.",
        "Normalizacion estructurada antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Codigo local: LDE-S7B1.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema juridico o social laboral.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Trazabilidad de citas.",
      "Bibliografia local verificable.",
      "Normalizacion de salidas no estructuradas.",
      "Union-dedupe sin recorte intencional."
    ],
    "reason_for_being": [
      "Orientar productos academicos laborales con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales pertinentes.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Evitar entregas descriptivas sin criterio juridico propio.",
      "Conservar reglas institucionales utiles en toda actividad de la materia.",
      "Sincronizar transversalmente solo patrones editoriales estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explicitos cuando falte evidencia local.",
      "Sin fuentes inventadas.",
      "Sin redaccion literal heredada entre materias.",
      "Enfoque juridico-laboral verificable.",
      "Citas trazables al .bib local.",
      "Conclusion profesional aplicable.",
      "Rutas y nombres canonicos verificados.",
      "Plantillas no resueltas corregidas antes de canonizar.",
      "Memoria heredada provisional hasta confirmacion."
    ],
    "argumentative_patterns": [
      "Abrir con problema juridico o social laboral.",
      "Convertir el problema en pregunta guia verificable.",
      "Definir objetivo puntual de la actividad.",
      "Delimitar conceptos laborales relevantes.",
      "Vincular conceptos con normas, doctrina o datos.",
      "Contrastar fuentes cuando exista tension interpretativa.",
      "Desarrollar postura propia con soporte verificable.",
      "Evitar resumen sin analisis.",
      "Cerrar con conclusion juridica transferible.",
      "Verificar coherencia entre pregunta, desarrollo y conclusion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho laboral y relaciones laborales",
        "Semestre 7 bloque 1",
        "Problema juridico laboral",
        "Pregunta guia verificable",
        "Conceptos laborales pertinentes",
        "Marco normativo y doctrinal",
        "Datos verificables",
        "Analisis propio",
        "Postura academica",
        "Conclusion transferible",
        "Practica profesional juridica",
        "Producto solicitado por planeacion",
        "Reporte",
        "Presentacion",
        "Bibliografia local",
        "Trazabilidad de citas",
        "Normalizacion estructurada",
        "JSON parseable",
        "Union-dedupe lossless",
        "Marcadores PowerShell sin expandir",
        "Plantilla LaTeX local",
        "Metadatos institucionales",
        "Fuentes provisionales heredadas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos institucionales",
          "kind": "supports",
          "justification": "La plantilla local define universidad, licenciatura, curso y codigo."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derecho laboral y relaciones laborales",
          "kind": "develops",
          "justification": "El README local ubica la materia dentro de la licenciatura."
        },
        {
          "source": "Semestre 7 bloque 1",
          "target": "Derecho laboral y relaciones laborales",
          "kind": "supports",
          "justification": "La ubicacion curricular esta indicada en README y programa analitico."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Pregunta guia verificable",
          "kind": "develops",
          "justification": "Cada actividad debe contextualizar el problema antes del analisis."
        },
        {
          "source": "Pregunta guia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La pregunta ordena el desarrollo argumentativo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Postura academica",
          "kind": "supports",
          "justification": "La postura debe sustentarse en norma, doctrina o datos verificables."
        },
        {
          "source": "Datos verificables",
          "target": "Trazabilidad de citas",
          "kind": "depends_on",
          "justification": "Toda afirmacion relevante requiere cita o marca de supuesto."
        },
        {
          "source": "Bibliografia local",
          "target": "Trazabilidad de citas",
          "kind": "supports",
          "justification": "El archivo .bib de la materia centraliza fuentes verificables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento del estudiante."
        },
        {
          "source": "Conclusion transferible",
          "target": "Practica profesional juridica",
          "kind": "supports",
          "justification": "El programa analitico exige transferencia profesional."
        },
        {
          "source": "Producto solicitado por planeacion",
          "target": "Reporte",
          "kind": "develops",
          "justification": "La planeacion puede materializarse como reporte segun consigna."
        },
        {
          "source": "Producto solicitado por planeacion",
          "target": "Presentacion",
          "kind": "develops",
          "justification": "La planeacion puede materializarse como presentacion segun consigna."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion se bloquea si la memoria no es parseable."
        },
        {
          "source": "Union-dedupe lossless",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "La consolidacion debe preservar reglas utiles sin duplicados."
        },
        {
          "source": "Marcadores PowerShell sin expandir",
          "target": "Plantilla LaTeX local",
          "kind": "contrasts",
          "justification": "Los marcadores no resueltos impiden canonizar rutas y bibliografia."
        },
        {
          "source": "Fuentes provisionales heredadas",
          "target": "Trazabilidad de citas",
          "kind": "depends_on",
          "justification": "Las fuentes heredadas requieren confirmacion local antes de usarse."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 1, obligatoria, 8 creditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico local: claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
        "Programa analitico local: bibliografia especifica en derecho-laboral-y-relaciones-laborales.bib.",
        "Bibliografia local: unadmSitioWeb.",
        "Bibliografia local: unadmMallaDerecho2024.",
        "Plantilla local: coursename Derecho laboral y relaciones laborales.",
        "Plantilla local: coursecode LDE-S7B1.",
        "Plantilla local: documenttitle Plantilla base de Derecho laboral y relaciones laborales.",
        "Contexto local: README contiene marcador PowerShell sin expandir para bibliografia.",
        "Contexto local: README muestra nombres de carpeta o archivo mal renderizados.",
        "Contexto local: plantilla muestra entorno authortable truncado.",
        "Memoria previa: salida no parseable desde Codex y GPT-Pro.",
        "Regla heredada estable: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Transferencia transversal: compartir solo abstracciones editoriales estables.",
        "Transferencia transversal: evitar redaccion literal y fuentes no pertinentes del origen."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura, actividad y calidad.",
      "Se reforzo ubicacion curricular local verificada del destino.",
      "Se conservaron reglas institucionales UnADM del origen por ser transferibles.",
      "Se descartaron como no transferibles los conceptos doctrinales especificos de Filosofia del Derecho.",
      "Se mantuvo alerta sobre fuentes heredadas no verificadas.",
      "Se reforzo bloqueo de propagacion ante JSON no parseable.",
      "Se integro correccion de marcadores PowerShell sin expandir.",
      "Se integro correccion de nombres mal renderizados en README.",
      "Se integro validacion del entorno authortable truncado.",
      "Se reforzo centralizacion bibliografica en el .bib local.",
      "Se mantuvo el patron problema-conceptos-evidencia-analisis-conclusion.",
      "Se preservo enfoque juridico-laboral como identidad disciplinar del destino."
    ]
  }
}