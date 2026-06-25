{
  "summary": [
    "Sincronizacion transversal consolidada entre Filosofia del Derecho (actividad) y Etica y Moral juridica (materia).",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, evidencia verificable y conclusion juridica propia.",
    "Se mantiene estrategia conservadora: transferir abstracciones, no literalidad tematica.",
    "Se refuerza gate critico: bloquear propagacion si no hay JSON parseable y normalizar salida no estructurada.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Supuesto: las consignas locales por actividad no estan completas en este salto y deben validarse en origen local."
  ],
  "identity_rules": [
    "Mantener voz formal academica alineada a UnADM.",
    "Anclar todo producto a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Aterrizar el analisis al contexto juridico mexicano cuando aplique.",
    "Incluir postura propia argumentada y sustentada.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales hasta confirmacion local.",
    "No transferir contenido tematico literal de Filosofia del Derecho sin adaptacion al enfoque etico-moral juridico."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, fundamento normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener trazabilidad entre actividad, reporte y presentacion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Verificar correspondencia exacta entre consigna y entregable.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "No asumir que fuentes de otras semanas aplican automaticamente a la actividad actual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en cada consolidacion.",
    "Comprobar deduplicacion semantica sin recorte de contenido valido.",
    "Verificar que toda cita en texto exista en .bib con metadatos minimos.",
    "Validar compilacion o parseo de .tex y .bib sin errores criticos ni referencias rotas.",
    "Confirmar que afirmaciones sin respaldo queden marcadas como supuesto."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad con reporte y presentacion de la materia.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Asegurar consistencia de etiquetas, titulos y nombres de archivo.",
    "Resolver placeholders de slug sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de automatizar validaciones.",
    "Mantener claves BibTeX estables para evitar roturas en recompilacion."
  ],
  "bibliography_rules": [
    "Usar etica-y-moral-juridica.bib como repositorio bibliografico local canonico.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar fuentes ni metadatos faltantes.",
    "Conservar metadatos minimos: autor o editor, titulo, año y fuente editorial o URL.",
    "Depurar duplicados por clave o equivalencia autor-titulo-año.",
    "Mantener alias historicos solo si hay trazabilidad y sin romper citas existentes.",
    "Completar entradas truncadas antes de citarlas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "No propagar literalidad redactada de actividades entre materias no equivalentes.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Etiquetar como provisional toda herencia sin verificacion local.",
    "Si un nodo vecino esta vacio, crear cerebro editorial minimo con vacios abiertos."
  ],
  "open_questions": [
    "Confirmar rubricas de evaluacion por actividad en Etica y Moral juridica.",
    "Confirmar si existe plantilla LaTeX obligatoria adicional para esta materia.",
    "Confirmar criterio final de deduplicacion bibliografica: clave, DOI o autor-titulo-año.",
    "Confirmar politica local para conservar alias BibTeX historicos.",
    "Supuesto: el placeholder de slug debe sustituirse permanentemente por etica-y-moral-juridica.bib en README y programa.",
    "Supuesto: la entrada sierraUniversidadNacional1910 sigue truncada y requiere cierre de metadatos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Etico sin moralismo declarativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Trazabilidad entre fuente, actividad y producto."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos.",
        "Sincronizacion transversal sin fusion tematica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fundamento normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y profesionales.",
      "Sostener coherencia editorial entre actividades, reportes y presentaciones.",
      "Preservar memoria util sin regresiones entre ciclos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "No afirmaciones sin respaldo.",
      "Cierre con implicacion profesional juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Delimitacion conceptual antes de valorar casos.",
      "Contraste entre marco normativo y postura propia.",
      "Sintesis final con transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Integridad academica",
        "Normalizacion estructurada",
        "JSON parseable",
        "Deduplicacion lossless",
        "Trazabilidad bibliografica",
        "Etica y moral juridica",
        "Analisis propio",
        "Conclusion transferible"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Trazabilidad bibliografica",
          "kind": "depends_on",
          "justification": "Sin trazabilidad no hay verificacion academica."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "Estandariza salida para propagacion segura."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Evita reutilizacion defectuosa aguas abajo."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "Exige evaluacion argumentada, no solo descripcion."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional deriva del razonamiento explicito."
        },
        {
          "source": "Deduplicacion lossless",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Reduce ruido sin perder reglas validas."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM y punto de entrada canonico.",
        "Programa analitico define ejes: problema, conceptos, producto, analisis y conclusion.",
        "Bibliografia local muestra duplicados verificables y una entrada truncada.",
        "Memoria heredada confirma necesidad historica de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerza gate de JSON parseable y normalizacion previa.",
      "Ciclo 11: se preservan ejes editoriales comunes sin traslado literal tematico.",
      "Ciclo 11: se fortalece deduplicacion bibliografica con criterio conservador.",
      "Ciclo 11: se mantiene identidad UnADM y trazabilidad curricular verificable."
    ]
  }
}