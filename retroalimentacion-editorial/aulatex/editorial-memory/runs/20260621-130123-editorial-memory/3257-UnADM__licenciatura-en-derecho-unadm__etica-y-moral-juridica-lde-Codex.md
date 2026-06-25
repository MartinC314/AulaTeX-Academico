{
  "summary": [
    "Se consolida memoria transversal minima para Etica y Moral Juridica con identidad UnADM.",
    "Se preservan reglas estables: normalizacion estructurada, JSON parseable y deduplicacion sin perdida.",
    "Se sincronizan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia conservadora: no trasladar literalidad de Filosofia del Derecho al enfoque etico-moral.",
    "Se detectan placeholders y nombres corruptos en README/programa; se marcan para correccion previa a automatizacion.",
    "Se mantiene trazabilidad de fuentes provisionales heredadas hasta verificacion local."
  ],
  "identity_rules": [
    "Mantener tono formal academico alineado a UnADM.",
    "Anclar contexto en Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar herencias Codex o GPT-Pro como provisionales hasta confirmacion.",
    "No transferir contenido tematico especifico de Filosofia del Derecho sin adaptacion etico-moral juridica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos, fundamento normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, reporte y presentacion."
  ],
  "activity_rules": [
    "Verificar correspondencia exacta entre consigna y producto entregable.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Comprobar deduplicacion semantica sin recorte de contenido valido.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Evitar comandos o paquetes no justificados por plantilla local.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir placeholders de slug sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de validaciones automaticas."
  ],
  "bibliography_rules": [
    "Usar etica-y-moral-juridica.bib como archivo canonico local.",
    "No inventar fuentes ni metadatos faltantes.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Unificar duplicados por equivalencia bibliografica verificable.",
    "Completar entradas truncadas antes de citar."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables a nodos laterales no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o ejemplos hiperlocales.",
    "Aplicar normalizacion manual en ciclo 1 ante herencia incompleta.",
    "Mantener regla de no regresion en cada ciclo recursivo.",
    "Registrar supuestos abiertos para validacion local posterior."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de Etica y Moral Juridica en este ciclo.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar criterio definitivo de deduplicacion BibTeX: DOI o titulo+autor+anio.",
    "Confirmar politica de alias para claves historicas fusionadas.",
    "Supuesto: placeholder de slug debe resolverse permanentemente a etica-y-moral-juridica.bib.",
    "Confirmar completitud de la entrada sierraUniversidadNacional1910."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Materia: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social como detonante.",
      "Conceptos y fundamento normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Sostener calidad editorial reproducible en ecosistema LaTeX."
    ],
    "style_markers": [
      "Frases claras y secciones funcionales.",
      "Supuestos marcados de forma explicita.",
      "No afirmaciones sin respaldo.",
      "Cierre con transferencia profesional."
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
        "Problema juridico o social",
        "Fundamento normativo y doctrinal",
        "Etica y moral juridica",
        "Postura argumentada",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Deduplicacion lossless"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Citas verificables",
          "kind": "depends_on",
          "justification": "Sin trazabilidad bibliografica no hay validacion academica."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El problema delimita el alcance argumentativo."
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
          "justification": "La reutilizacion transversal exige formato parseable."
        },
        {
          "source": "Deduplicacion lossless",
          "target": "Memoria persistente",
          "kind": "develops",
          "justification": "Conserva reglas utiles sin inflar ni perder contenido."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Comparten base teorica, pero el nodo destino exige foco etico-moral aplicado."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial UnADM.",
        "Programa analitico con ejes de trabajo y proposito de realizacion.",
        "Bibliografia local con duplicados verificables y una entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Se reforzo regla institucional de JSON parseable antes de propagacion.",
      "Se preservo no regresion y deduplicacion semantica sin recorte.",
      "Se transfirieron ejes editoriales estables de forma transversal.",
      "Se evitaron fuentes inventadas y se mantuvieron supuestos explicitados.",
      "Se creo cerebro editorial minimo del destino con vacios locales abiertos."
    ]
  }
}