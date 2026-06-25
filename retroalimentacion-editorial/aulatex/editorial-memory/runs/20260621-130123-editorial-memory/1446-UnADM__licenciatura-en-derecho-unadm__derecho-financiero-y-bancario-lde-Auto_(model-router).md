{
  "summary": [
    "Se consolida ADN editorial transversal para Derecho financiero y bancario.",
    "Se preserva identidad UnADM con compresión union-dedupe sin regresión.",
    "La materia destino se ubica en semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva alerta por salidas heredadas no parseables en JSON.",
    "Se detectan artefactos de plantilla en README, programa analítico y portada .tex.",
    "Se transfieren solo abstracciones estables desde Filosofía del Derecho.",
    "No se transfieren fuentes doctrinales específicas del nodo origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar programa académico: Licenciatura en Derecho.",
    "Usar materia destino: Derecho financiero y bancario.",
    "Usar clave local: LDE-S3B2.",
    "Usar ubicación curricular: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Usar la carpeta de materia como entrada canónica.",
    "Conservar autor Martin Jonathan de la Cruz según .tex local.",
    "Conservar matrícula ES2611202040 según .tex local.",
    "Conservar localización Roma Norte, Ciudad de México salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado.",
    "Marcar como supuesto docente, grupo o consigna no visibles.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "No propagar redacción literal entre materias no equivalentes."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, análisis propio y conclusión transferible.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Expandir el token del .bib al slug derecho-financiero-y-bancario.bib.",
    "Corregir nombres de archivos con caracteres faltantes.",
    "No eliminar reglas previas válidas.",
    "Agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Delimitar el problema jurídico o social de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Usar normas, doctrina o datos pertinentes al tema financiero y bancario.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Separar descripción conceptual, análisis propio y conclusión jurídica.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar el producto a la planeación semanal confirmada.",
    "Verificar que el producto corresponda a la consigna local.",
    "No asumir fuentes de otra semana o materia sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear guardado si hay campos obligatorios vacíos sin marca de supuesto.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar deduplicación semántica antes de guardar memoria.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto y consigna de actividad.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener documentclass article en español, letterpaper y oneside salvo instrucción contraria.",
    "Conservar macros de identidad académica en el encabezado.",
    "Mantener título, subtítulo y materia sincronizados con la actividad real.",
    "Reemplazar título y subtítulo de plantilla antes de entregar.",
    "Completar Figura docente con dato real o etiqueta de supuesto.",
    "Revisar que la tabla de identificación compile sin celdas abiertas.",
    "Evitar romper comandos, rutas, portada, tablas y referencias.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliográfico canónico.",
    "Registrar fuentes específicas de actividad en el .bib de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Priorizar materiales jurídicos verificables cuando apliquen.",
    "No inventar fuentes ni metadatos bibliográficos.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Incluir fecha de consulta en referencias web.",
    "Mantener entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir bibliografía de Filosofía del Derecho para esta materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar lateralmente solo reglas independientes de asignatura o actividad específica.",
    "Propagar a nivel materia identidad, estructura, calidad y bibliografía general.",
    "Evitar transferir fuentes o casos específicos del nodo origen.",
    "Mantener compresión union-dedupe con pérdida cero.",
    "Etiquetar reglas heredadas para auditoría de no regresión.",
    "Aplicar normalización manual si reaparece salida no estructurada.",
    "Conservar vacíos de contexto local como preguntas abiertas.",
    "Reforzar grafo conceptual con conceptos transversales verificables.",
    "No reducir especificidad local del destino."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificación.",
    "Confirmar planeación semanal vigente antes de generar actividades.",
    "Confirmar número real de actividad para sustituir Actividad X.",
    "Definir formato obligatorio de citación para la materia.",
    "Supuesto: el formato de citación no está definido aún.",
    "Validar si la localización de portada debe mantenerse.",
    "Verificar si nombres de archivos del README deben corregirse manualmente o regenerarse.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar rúbrica específica de evaluación por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de materia.",
        "Trazabilidad documental entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explícita.",
        "No regresión de reglas útiles previas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Clave local: LDE-S3B2.",
        "Semestre 3, bloque 2.",
        "Materia obligatoria de 8 créditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Evidencia verificable.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Análisis jurídico propio.",
      "Conclusión transferible a la práctica jurídica.",
      "Consistencia entre .tex y .bib.",
      "Normalización estructurada antes de propagar.",
      "Dedupe semántico sin pérdida editorial."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a contextos financieros y bancarios.",
      "Asegurar trazabilidad institucional y bibliográfica.",
      "Evitar entregas descriptivas sin postura jurídica."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos explícitos.",
      "Fuentes no inventadas.",
      "Citas coherentes con .bib.",
      "Estructura visible por secciones.",
      "Conclusión con implicación práctica.",
      "Tono institucional UnADM.",
      "Metadatos sincronizados.",
      "Redacción jurídica precisa.",
      "Transferencia transversal sin literalidad."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual delimitado.",
      "Marco normativo o doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio diferenciado del resumen.",
      "Contraste entre fuente y postura cuando proceda.",
      "Cierre con criterio jurídico aplicable.",
      "Coherencia entre pregunta guía, desarrollo y conclusión.",
      "Ajuste al producto solicitado por planeación."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derecho financiero y bancario",
        "Ubicación curricular",
        "Malla curricular de Derecho",
        "Integridad académica",
        "Evidencia verificable",
        "Fuente institucional",
        "Bibliografía específica de actividad",
        "Archivo .bib canónico",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Normas aplicables",
        "Doctrina pertinente",
        "Análisis jurídico propio",
        "Postura argumentada del estudiante",
        "Conclusión transferible",
        "Planeación semanal",
        "Producto académico",
        "Reporte",
        "Presentación",
        "Normalización estructurada",
        "JSON parseable",
        "Dedupe semántico",
        "Consistencia README-programa-.tex-.bib",
        "Artefactos de plantilla",
        "Supuesto editorial",
        "Propagación transversal conservadora"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica propia."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la declara como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Derecho financiero y bancario",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "El README local define la materia dentro de la Licenciatura en Derecho."
        },
        {
          "source": "Archivo .bib canónico",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El .bib local concentra fuentes institucionales y fuentes específicas de actividad."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Archivo .bib canónico",
          "kind": "depends_on",
          "justification": "El programa analítico indica agregar fuentes específicas al .bib de la materia."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El problema delimita el eje argumentativo del desarrollo."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "Los conceptos permiten distinguir descripción de razonamiento jurídico."
        },
        {
          "source": "Normas aplicables",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión profesional debe derivar de fundamentos jurídicos verificables."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa exige transformar la planeación en reportes, presentaciones o productos visuales."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "La memoria heredada bloquea propagación si la salida no es parseable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Dedupe semántico",
          "kind": "supports",
          "justification": "La normalización permite consolidar reglas sin duplicados ni pérdida útil."
        },
        {
          "source": "Artefactos de plantilla",
          "target": "Consistencia README-programa-.tex-.bib",
          "kind": "contrasts",
          "justification": "Los tokens y caracteres faltantes rompen la coherencia documental esperada."
        },
        {
          "source": "Supuesto editorial",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar incertidumbres evita presentar datos no confirmados como hechos."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la materia.",
        "derecho-financiero-y-bancario.bib: entrada unadmSitioWeb.",
        "derecho-financiero-y-bancario.bib: entrada unadmMallaDerecho2024.",
        "Reporte .tex local: autor Martin Jonathan de la Cruz.",
        "Reporte .tex local: matrícula ES2611202040.",
        "Reporte .tex local: Figura docente pendiente.",
        "README y programa local: token $(@{...}.Slug) sin expandir.",
        "README local: nombres de archivos con caracteres faltantes.",
        "Memoria heredada: revisar salida no estructurada antes de aplicar aguas abajo.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: sustentar afirmaciones con fuentes verificables y cita explícita.",
        "Memoria origen: incluir postura argumentada del estudiante."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10 consolida destino con estrategia progresiva y conservadora.",
      "Se preservan reglas locales verificadas del destino.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se refuerza identidad UnADM como eje transversal.",
      "Se mantiene ubicación curricular local del destino.",
      "Se hereda estructura argumentativa reusable del origen.",
      "Se excluyen citas doctrinales específicas de Filosofía del Derecho.",
      "Se conserva alerta por Codex y GPT-Pro como fuentes provisionales.",
      "Se refuerza bloqueo por JSON no parseable.",
      "Se refuerza normalización previa a propagación recursiva.",
      "Se incorporan artefactos locales de plantilla como riesgos de calidad.",
      "Se mantiene derecho-financiero-y-bancario.bib como .bib canónico.",
      "Se conserva la distinción entre bibliografía base y específica.",
      "Se marcan vacíos locales como preguntas abiertas.",
      "Se evita transferencia literal entre nodos no equivalentes."
    ]
  }
}