{
  "summary": [
    "Sincronizacion transversal aplicada entre nodos no equivalentes con estrategia conservadora.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza normalizacion obligatoria antes de propagacion recursiva.",
    "Se consolida cerebro editorial minimo de materia con vacios locales abiertos como supuestos."
  ],
  "identity_rules": [
    "Conservar tono academico formal alineado a UnADM.",
    "Anclar el contexto a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Mantener integridad academica con citas verificables y trazabilidad.",
    "Aterrizar el analisis al contexto juridico mexicano cuando aplique.",
    "Incluir postura propia argumentada; evitar neutralidad meramente descriptiva.",
    "Tratar herencias no verificadas de Codex o GPT-Pro como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener secuencia reusable: problema, conceptos, evidencia, analisis, conclusion.",
    "Alinear el formato al producto solicitado por planeacion semanal.",
    "Mantener trazabilidad entre actividad, reporte y presentacion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar correspondencia exacta entre consigna y entregable.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "No trasladar literalidad tematica de Filosofia del Derecho; adaptar al enfoque etico-moral juridico.",
    "No asumir fuentes de otras semanas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Confirmar que no se eliminen reglas utiles previas durante consolidacion.",
    "Comprobar deduplicacion semantica sin recorte de contenido valido.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Verificar correspondencia del producto con la consigna activa."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener consistencia de nombres de archivo, titulos y etiquetas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Resolver placeholders de slug sin expandir en README y programa analitico.",
    "Corregir rutas o nombres corruptos antes de automatizar validaciones.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "Usar etica-y-moral-juridica.bib como contenedor local de materia.",
    "No inventar fuentes ni metadatos faltantes.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Depurar duplicados por clave o equivalencia bibliografica.",
    "Unificar pares duplicados Huerta 2000, Ronquillo 2018 y Singer 1995 con alias historicos controlados.",
    "Completar entradas truncadas antes de citarlas [supuesto: sierraUniversidadNacional1910 incompleta].",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos hiperlocales.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura.",
    "Mantener estrategia progresiva y conservadora sin regresiones.",
    "Marcar ciclos heredados con normalizacion manual cuando venga salida incompleta."
  ],
  "open_questions": [
    "Confirmar plantilla LaTeX obligatoria especifica de la materia.",
    "Confirmar criterio final de deduplicacion bibliografica: clave, DOI o titulo+autor+anio.",
    "Confirmar si se deben conservar aliases BibTeX legacy tras unificacion.",
    "Confirmar consignas semanales no reflejadas en memoria actual.",
    "Confirmar sustitucion permanente del placeholder de slug por etica-y-moral-juridica.bib.",
    "Confirmar cierre de entradas bibliograficas truncadas antes de siguiente ciclo."
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
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Sostener coherencia editorial entre actividades, reportes y presentaciones.",
      "Preservar calidad institucional mediante validacion estructural y bibliografica."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Supuestos marcados explicitamente.",
      "Secciones funcionales y consistentes.",
      "Cierre con transferencia profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Delimitacion conceptual antes de valorar casos.",
      "Contraste entre marco normativo y postura propia.",
      "Sintesis final con implicacion juridica concreta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Integridad academica",
        "Normalizacion estructurada",
        "Deduplicacion lossless",
        "Problema juridico o social",
        "Fundamento normativo y doctrinal",
        "Etica y moral juridica",
        "Postura argumentada",
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
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin respaldo trazable no hay validez academica."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Delimita alcance y pertinencia argumentativa."
        },
        {
          "source": "Fundamento normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere base juridica explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion transversal exige parseo confiable."
        },
        {
          "source": "Deduplicacion lossless",
          "target": "Memoria persistente",
          "kind": "develops",
          "justification": "Conserva reglas validas sin inflacion ni perdida."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Comparten base teorica, pero difieren en foco aplicado."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM e integridad academica.",
        "Programa analitico local define ejes problema-conceptos-evidencia-analisis-cierre.",
        "Bibliografia local muestra duplicados y una entrada truncada [supuesto].",
        "Memoria heredada confirma necesidad historica de normalizacion manual en ciclos tempranos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: consolidacion transversal conservadora aplicada sin regresion.",
      "Ciclo 18: se deduplican reglas repetidas y se preserva contenido util.",
      "Ciclo 18: se refuerzan gates de JSON parseable y estructura minima.",
      "Ciclo 18: se mantiene separacion entre abstraccion estable y contenido tematico local.",
      "Ciclo 18: se dejan abiertos vacios locales para verificacion posterior."
    ]
  }
}