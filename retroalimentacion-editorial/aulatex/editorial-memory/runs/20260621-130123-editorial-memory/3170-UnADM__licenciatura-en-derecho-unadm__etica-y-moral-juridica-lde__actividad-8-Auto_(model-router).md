{
  "summary": [
    "Se consolida memoria editorial de Actividad 8 para Ética y Moral jurídica.",
    "Se aplica transferencia lateral desde Filosofía del Derecho solo con patrones reutilizables.",
    "Se preserva identidad UnADM y ubicación curricular común.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización JSON obligatoria antes de propagar.",
    "Se conserva trazabilidad de salidas previas no parseables como fuente provisional.",
    "Se evita copiar bibliografía exclusiva, conclusiones o redacción literal del nodo origen.",
    "Se agregan mejoras verificables desde contexto local: token Slug sin expandir, nombres anómalos y .bib truncado."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en redacción, enfoque académico y cierre jurídico.",
    "Vincular la actividad a la Licenciatura en Derecho.",
    "Usar semestre 1, bloque 2, obligatoria y 8 créditos como ubicación curricular verificada localmente.",
    "Mantener referencia explícita a Ética y Moral jurídica.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Registrar ruta origen y destino en cada fusión editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Conservar como provisionales fusiones previas no parseables de Codex, Auto, Claude Foundry y GPT-Pro.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular cuando aplique."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable.",
    "Usar el esquema canónico completo sin omitir secciones.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Conservar reglas útiles previas durante la fusión.",
    "Marcar supuestos de forma explícita.",
    "Conservar trazabilidad de cambios por ciclo.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Alinear cada entrega al problema jurídico o social de la actividad.",
    "Integrar conceptos, normas, doctrina o datos pertinentes antes de concluir.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir análisis propio y postura académica del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "Ajustar el artefacto al formato solicitado en la actividad.",
    "Seguir los cinco ejes del programa analítico local como lista de verificación.",
    "No asumir fuentes de otras semanas sin validación en la consigna local.",
    "Supuesto: si falta consigna, usar estructura base y abrir preguntas de validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema requerido antes de guardar memoria.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Validar ausencia de duplicados semánticos antes de guardar memoria.",
    "No eliminar reglas útiles previas durante la fusión.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria previa.",
    "Confirmar ausencia de afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar pauta editorial local antes de aplicar reglas transferidas.",
    "Verificar que el producto corresponda a la consigna de Actividad 8.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener compatibilidad con plantilla LaTeX de la asignatura.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Asegurar que citas y referencias compilen sin errores.",
    "Mantener consistencia de nombres de archivos .tex y .bib según slug de la materia.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables en .bib o material institucional.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Evitar claves BibTeX duplicadas para la misma obra cuando se edite.",
    "Citar en texto toda fuente listada que sustente afirmaciones clave.",
    "Registrar duplicados detectados antes de normalizar claves.",
    "Marcar como pendiente la depuración de duplicados históricos sin borrar trazabilidad.",
    "Validar la entrada truncada de etica-y-moral-juridica.bib antes de compilar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo identidad institucional, estructura, calidad y patrones argumentativos reutilizables.",
    "No transferir bibliografía exclusiva de Filosofía del Derecho al nodo de Ética y Moral jurídica.",
    "No copiar redacción literal ni conclusiones específicas entre nodos laterales.",
    "Aplicar analogía controlada entre problema jurídico, ética, moral, evidencia y cierre profesional.",
    "Mantener bandera de normalización manual mientras persistan salidas no estructuradas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 requiere validación manual antes de propagación aguas abajo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8.",
    "Confirmar producto solicitado para Actividad 8.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 8 requiere reporte, presentación, cuadro, mapa u otro formato.",
    "Confirmar lista canónica de claves BibTeX para conservar una por obra.",
    "Confirmar criterio local para resolver duplicados bibliográficos sin perder trazabilidad.",
    "Supuesto: la entrada sierraUniversidadNacional1910 está truncada y requiere corrección previa a compilación.",
    "Confirmar y corregir la entrada truncada en etica-y-moral-juridica.bib.",
    "Confirmar nombres canónicos de archivos afectados por caracteres anómalos en README.",
    "Confirmar si existen contenidos recuperables de intentos no parseables previos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Ético sin perder rigor jurídico.",
        "Breve, accionable y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de fuente, ruta y ciclo.",
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Asignatura destino: Ética y Moral jurídica.",
        "Fuente curricular local: README.md y malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos éticos, morales, normativos y doctrinales pertinentes.",
      "Producto solicitado por la planeación semanal.",
      "Evidencia verificable y citas explícitas.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica profesional.",
      "Integridad académica.",
      "Trazabilidad bibliográfica.",
      "Normalización JSON.",
      "Analogía controlada entre filosofía jurídica y ética jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Unir problema, conceptos, fuentes, análisis y cierre argumentativo.",
      "Formar criterio jurídico con responsabilidad ética.",
      "Evitar productos descriptivos sin postura propia.",
      "Garantizar propagación editorial segura entre nodos.",
      "Preservar memoria útil sin duplicados ni pérdida de reglas."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explícita.",
      "Sin fuentes inventadas.",
      "Sin afirmaciones sin respaldo.",
      "Sin copia literal entre nodos laterales.",
      "Citas verificables y claves BibTeX estables.",
      "Cierre con implicación jurídica práctica.",
      "Diferenciar bibliografía base y específica.",
      "Normalizar antes de propagar.",
      "Conservar especificidad local de Ética y Moral jurídica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Definir conceptos éticos y jurídicos antes del análisis.",
      "Ubicar marco normativo o doctrinal pertinente.",
      "Contrastar postura propia con evidencia verificable.",
      "Distinguir descripción, análisis y valoración.",
      "Relacionar ética, moral y práctica jurídica.",
      "Evitar saltos de conclusión sin premisas.",
      "Cerrar con criterio profesional aplicable.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
      "Usar analogía lateral solo para patrones, no para contenidos exclusivos."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Problema jurídico o social",
        "Conceptos éticos y morales",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica práctica",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Normalización JSON",
        "Compresión lossless por deduplicación",
        "Propagación lateral transversal",
        "Analogía controlada",
        "Producto solicitado por planeación",
        "etica-y-moral-juridica.bib",
        "Token Slug sin expandir",
        "Entrada BibTeX truncada",
        "Duplicados BibTeX históricos"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib",
        "huertaEticaConClasicos2000",
        "huerta2000etica",
        "ronquilloarmasEticaGeneralProfesional2018",
        "ronquillo2018etica",
        "singerCompendioEtica1995",
        "singer1995compendio",
        "lopezmartinezTecnicasDidacticas2023",
        "barredaOracionCivica1867",
        "sierraUniversidadNacional1910",
        "constitucionCPEUM2026",
        "scjnJur37_2016",
        "garciaMaynezEtica",
        "huertaEticaConClasicos2000",
        "scjnTesis2007731"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Licenciatura en Derecho",
          "kind": "supports",
          "justification": "El README local ubica la materia dentro de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "develops",
          "justification": "La asignatura destino pertenece al plan curricular indicado en el README local."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "El programa analítico exige iniciar desde un problema que active la actividad."
        },
        {
          "source": "Conceptos éticos y morales",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos orientan la selección de normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial local exige citas verificables e integridad académica."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las claves estables y metadatos completos permiten verificar fuentes."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación lateral transversal",
          "kind": "depends_on",
          "justification": "La propagación segura requiere salida parseable y esquema completo."
        },
        {
          "source": "Compresión lossless por deduplicación",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "La deduplicación conserva reglas útiles sin recortar información válida."
        },
        {
          "source": "Analogía controlada",
          "target": "Propagación lateral transversal",
          "kind": "supports",
          "justification": "Permite transferir patrones comunes sin copiar contenido exclusivo del origen."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "contrasts",
          "justification": "Son nodos laterales con identidad curricular común, pero contenidos bibliográficos distintos."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Estructura de entrega",
          "kind": "depends_on",
          "justification": "El formato final debe ajustarse a la consigna local de Actividad 8."
        },
        {
          "source": "Token Slug sin expandir",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "El token visible en README y programa analítico puede romper rutas o referencias si no se resuelve."
        },
        {
          "source": "Entrada BibTeX truncada",
          "target": "Compilación LaTeX",
          "kind": "contrasts",
          "justification": "La entrada sierraUniversidadNacional1910 aparece incompleta en el contexto local."
        },
        {
          "source": "Duplicados BibTeX históricos",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "La depuración requiere registrar alias antes de conservar una clave canónica."
        }
      ],
      "evidence": [
        "README.md local: materia de la Licenciatura en Derecho de la UnADM.",
        "README.md local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README.md local: carpeta como punto de entrada canónico.",
        "README.md local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "programa-analitico-etica-y-moral-juridica.md: propósito de transformar planeación en productos académicos.",
        "programa-analitico-etica-y-moral-juridica.md: cinco ejes de trabajo editoriales.",
        "programa-analitico-etica-y-moral-juridica.md: bibliografía específica en archivo .bib de la asignatura.",
        "README.md y programa analítico local: token $(@{...}.Slug) sin expandir.",
        "README.md local: nombres con caracteres anómalos en estructura.",
        "etica-y-moral-juridica.bib: claves duplicadas para Huerta 2000.",
        "etica-y-moral-juridica.bib: claves duplicadas para Ronquillo 2018.",
        "etica-y-moral-juridica.bib: claves duplicadas para Singer 1995.",
        "etica-y-moral-juridica.bib: entrada sierraUniversidadNacional1910 truncada.",
        "Memoria destino previa: Actividad 8 tiene historial de salidas no parseables.",
        "Memoria origen estructurada: patrón común de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se fusiona memoria lateral desde Filosofía del Derecho sin copiar bibliografía exclusiva.",
      "Ciclo 1: se preservan reglas locales de Ética y Moral jurídica.",
      "Ciclo 1: se deduplican reglas equivalentes con acentos y variantes semánticas.",
      "Ciclo 1: se refuerza normalización JSON como puerta de calidad.",
      "Ciclo 1: se mantiene consigna local como pregunta abierta por falta de texto exacto.",
      "Ciclo 1: se agregan incidencias locales verificables de README y .bib.",
      "Ciclo 1: se conserva trazabilidad de intentos previos no parseables.",
      "Ciclo 1: se limita la transferencia a identidad, estructura, calidad y patrones argumentativos."
    ]
  }
}