{
  "summary": [
    "Se consolida memoria de Actividad 7 para Ética y Moral jurídica con identidad UnADM.",
    "Se aplica transferencia lateral desde Filosofía del Derecho solo con patrones reutilizables.",
    "Se preservan reglas locales de estructura, calidad, LaTeX y bibliografía.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene validación JSON estricta antes de propagación recursiva.",
    "Se conserva compresión lossless por unión y deduplicación.",
    "Se marca como provisional toda fuente heredada no verificada localmente.",
    "Se agrega control de consistencia entre consigna, producto, citas y archivo .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en cada entrega.",
    "Usar tono académico-jurídico propio de Licenciatura en Derecho.",
    "Alinear la actividad con Ética y Moral jurídica.",
    "Usar semestre 1, bloque 2, obligatoria, 8 créditos según README local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Conservar trazabilidad cuando el origen no sea parseable.",
    "Registrar como provisionales fuentes heredadas no verificadas.",
    "No transferir conclusiones específicas de Filosofía del Derecho."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Integrar el producto solicitado por la planeación semanal.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Alinear estructura con la pauta editorial local de la asignatura.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Preparar salida en JSON parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Confirmar que el producto corresponda a la consigna de Actividad 7.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar afirmaciones sin respaldo documental.",
    "Mantener integridad académica en citas y referencias.",
    "Evitar asumir fuentes de semanas o materias distintas sin validación.",
    "Vincular ética, moral y práctica jurídica cuando la consigna lo permita.",
    "Distinguir análisis conceptual de valoración normativa."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Revisar respuesta no estructurada antes de aplicarla aguas abajo.",
    "Confirmar que no se eliminen reglas útiles previas.",
    "Marcar supuestos explícitos cuando falten datos locales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar propagación recursiva solo si pasan las compuertas de calidad.",
    "Revisar estructura mínima completa antes de reutilizar reglas.",
    "Validar correspondencia del producto con la consigna de Actividad 7."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reporte, presentación y .bib de la materia.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Evitar cambios de formato que rompan compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Conservar consistencia entre archivos .tex y bibliografía local.",
    "Mantener claves BibTeX estables.",
    "Evitar renombres arbitrarios de claves citadas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas y nombres de archivo antes de compilar.",
    "Verificar nombres listados en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de Actividad 7 en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Deduplicar entradas bibliográficas equivalentes sin perder trazabilidad.",
    "Mantener una clave canónica y mapear aliases cuando existan duplicados. [Supuesto]",
    "Verificar integridad sintáctica del .bib antes de propagar cambios. [Supuesto]",
    "No normalizar un .bib truncado sin abrir incidencia. [Supuesto]",
    "No importar bibliografía exclusiva de Filosofía del Derecho sin validación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre asignaturas hermanas.",
    "No copiar redacción literal ni conclusiones específicas de nodos hermanos.",
    "Aplicar analogía controlada entre Filosofía del Derecho y Ética y Moral jurídica.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Normalizar manualmente entradas no estructuradas antes de reutilizarlas.",
    "Ciclos 1 a 11 requieren normalización manual si se reutilizan.",
    "Ciclo 19 refuerza transferencia lateral con deduplicación lossless.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 7.",
    "Confirmar tipo de producto solicitado en Actividad 7.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 7.",
    "Confirmar si Actividad 7 requiere reporte, presentación o producto visual.",
    "Confirmar política local de alias de claves BibTeX para duplicados existentes.",
    "Confirmar si claves duplicadas del .bib deben mantenerse por retrocompatibilidad. [Supuesto]",
    "Confirmar si el .bib local está truncado en el archivo real o solo en la captura. [Supuesto]",
    "Confirmar si el documento local conserva metadatos desactualizados de Actividad 2. [Supuesto]",
    "Definir criterio operativo final para duplicados .bib con claves distintas y metadatos iguales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Respeto a la planeación semanal.",
        "Trazabilidad de fuentes y supuestos.",
        "Validación estructural previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Ética y Moral jurídica.",
        "Actividad destino: Actividad 7.",
        "Semestre 1.",
        "Bloque 2.",
        "Obligatoria.",
        "8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Ética.",
      "Moral.",
      "Práctica jurídica.",
      "Integridad académica.",
      "Criterio profesional verificable."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros y verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con base ética y moral.",
      "Conectar la reflexión ética con la actuación profesional.",
      "Evitar productos meramente descriptivos.",
      "Sostener conclusiones jurídicas con evidencia y postura razonada."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo puntual explícito.",
      "Secciones claras y trazables.",
      "Citas explícitas y verificables.",
      "Supuestos etiquetados cuando aplique.",
      "Contraste conceptual entre ética y moral cuando proceda.",
      "Cierre con utilidad profesional jurídica.",
      "Lenguaje académico sin adornos innecesarios.",
      "Coherencia entre consigna, desarrollo y conclusión."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Definición de conceptos clave.",
      "Marco normativo o doctrinal verificable.",
      "Contraste de posturas con evidencia.",
      "Aplicación al caso o situación jurídica.",
      "Toma de posición del estudiante.",
      "Conclusión aplicable al ejercicio jurídico.",
      "Diferenciar ética, moral y derecho antes de valorarlos.",
      "Vincular deber profesional con responsabilidad social.",
      "Derivar la conclusión del análisis, no de una opinión aislada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Actividad 7",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo",
        "Marco doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Ética",
        "Moral",
        "Derecho",
        "Práctica jurídica",
        "Integridad académica",
        "Planeación semanal",
        "Citas verificables",
        "Bibliografía local",
        "Deduplicación bibliográfica",
        "Supuestos explícitos",
        "Validación JSON",
        "Compilación LaTeX"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib",
        "huertaEticaConClasicos2000",
        "huerta2000etica",
        "ronquilloarmasEticaGeneralProfesional2018",
        "ronquillo2018etica",
        "singerCompendioEtica1995",
        "singer1995compendio",
        "prieto2009favor",
        "lopezmartinezTecnicasDidacticas2023",
        "barredaOracionCivica1867",
        "sierraUniversidadNacional1910",
        "constitucionCPEUM2026",
        "casoAyotzinapaCNDH2024",
        "lgv2026",
        "lgmdfp2026",
        "clave",
        "clave1",
        "clave2"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "La estructura final debe ajustarse al producto pedido por la actividad."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El razonamiento académico parte de un problema delimitado."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco doctrinal",
          "kind": "supports",
          "justification": "Los conceptos ordenan la lectura de fuentes doctrinales."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión debe sostenerse en normas o criterios verificables cuando aplique."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura del estudiante no debe quedar como opinión sin respaldo."
        },
        {
          "source": "Ética",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distinción conceptual es eje recurrente de la asignatura."
        },
        {
          "source": "Moral",
          "target": "Práctica jurídica",
          "kind": "supports",
          "justification": "La valoración moral orienta criterios de actuación profesional."
        },
        {
          "source": "Ética",
          "target": "Práctica jurídica",
          "kind": "supports",
          "justification": "La reflexión ética fundamenta deberes profesionales y responsabilidad social."
        },
        {
          "source": "Derecho",
          "target": "Práctica jurídica",
          "kind": "develops",
          "justification": "El análisis jurídico debe proyectarse a decisiones profesionales concretas."
        },
        {
          "source": "Citas verificables",
          "target": "Bibliografía local",
          "kind": "depends_on",
          "justification": "Toda cita en texto debe corresponder a una entrada válida del .bib."
        },
        {
          "source": "Deduplicación bibliográfica",
          "target": "Bibliografía local",
          "kind": "develops",
          "justification": "El .bib local contiene claves equivalentes que requieren control de trazabilidad."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar datos no confirmados evita afirmaciones inventadas."
        },
        {
          "source": "Validación JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria solo debe propagarse si es parseable y estructurada."
        },
        {
          "source": "Compilación LaTeX",
          "target": "Producto solicitado",
          "kind": "supports",
          "justification": "El archivo final debe compilar sin errores críticos ni referencias rotas."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: conservar identidad UnADM e integridad académica.",
        "README local: usar citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la asignatura.",
        "Archivo etica-y-moral-juridica.bib: contiene entradas locales de ética general, ética clásica y compendios.",
        "Archivo etica-y-moral-juridica.bib: contiene duplicados observables con claves distintas para obras equivalentes.",
        "Memoria destino previa: bloqueo de propagación si no hay JSON parseable.",
        "Memoria destino previa: validación de citas contra archivo .bib.",
        "Memoria origen: patrón reutilizable de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19 consolida transferencia lateral-transversal desde Filosofía del Derecho.",
      "Se transfieren patrones, no contenido específico exclusivo del nodo origen.",
      "Se preserva identidad local de Ética y Moral jurídica.",
      "Se normalizan duplicados editoriales sin eliminar reglas útiles.",
      "Se refuerza analogía controlada entre reflexión filosófica, ética, moral y práctica jurídica.",
      "Se mantiene bloqueo de propagación ante salidas no parseables.",
      "Se agregan preguntas abiertas donde faltan consigna, rúbrica o fuentes obligatorias.",
      "Se evita inventar bibliografía no visible en fuentes locales.",
      "Se conserva trazabilidad de claves BibTeX locales y aliases posibles.",
      "Se refuerza cierre profesional como marca editorial del nodo."
    ]
  }
}