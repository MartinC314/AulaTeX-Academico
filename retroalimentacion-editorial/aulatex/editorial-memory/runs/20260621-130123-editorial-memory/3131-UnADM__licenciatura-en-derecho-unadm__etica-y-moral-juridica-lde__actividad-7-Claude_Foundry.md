```json
{
  "summary": [
    "Memoria de actividad consolidada para Etica y Moral juridica con identidad UnADM.",
    "Se conserva normalizacion estructurada obligatoria antes de propagar reglas.",
    "Ejes editoriales vigentes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se aplica compresion lossless por union y deduplicacion.",
    "Se conserva contexto curricular verificable: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza validacion JSON estricta antes de propagacion recursiva.",
    "Salidas previas sin JSON parseable desde Codex, Auto, Claude Foundry y GPT-Pro requirieron normalizacion.",
    "Refuerzo lateral por analogia controlada desde Filosofia del Derecho sin copiar contenido especifico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de la actividad.",
    "Alinear la actividad con Etica y Moral juridica del semestre 1, bloque 2.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular.",
    "Registrar fuente provisional del ciclo cuando no exista JSON valido del origen. [Supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Preparar salida en JSON parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Mantener integridad academica en citas y referencias.",
    "Evitar asumir fuentes de semanas o materias distintas sin validacion.",
    "Confirmar que el producto corresponda a la consigna de Actividad 7."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Marcar supuestos explicitos cuando falten datos locales.",
    "Aplicar propagacion recursiva solo si pasan las compuertas de calidad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Conservar consistencia entre reporte, presentacion y .bib de la asignatura.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar entradas bibliograficas equivalentes sin perder trazabilidad.",
    "Mantener una clave canonica y mapear aliases cuando existan duplicados de la misma obra. [Supuesto]",
    "No editar ni normalizar entradas si el .bib esta truncado; abrir incidencia primero. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Transferir solo patrones reutilizables en saltos laterales, no contenido especifico de hermanos.",
    "Ciclo 13 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar consigna exacta y tipo de producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Etica y Moral juridica para Actividad 7.",
    "Definir criterio operativo final para duplicados .bib con claves distintas y metadatos iguales.",
    "Confirmar politica local de alias de claves BibTeX para duplicados existentes.",
    "Confirmar si las claves duplicadas actuales del .bib deben mantenerse por retrocompatibilidad. [Supuesto]",
    "Confirmar si el .bib local truncado debe corregirse antes de nuevas propagaciones. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Orientado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad de fuentes y supuestos.",
        "Respeto a la planeacion semanal.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etica y Moral juridica.",
        "Actividad destino: Actividad 7."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Etica",
      "Moral"
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos que integren problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Sostener identidad UnADM e integridad academica en cada entrega.",
      "Aportar conclusion juridica transferible a la practica profesional."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados cuando aplique.",
      "Cierre con utilidad profesional juridica.",
      "Citar malla-curricular-derecho-unadm.pdf para sustento de ubicacion curricular."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste de posturas con evidencia.",
      "Toma de posicion del estudiante.",
      "Conclusion aplicable al ejercicio juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib",
        "ronquilloarmasEticaGeneralProfesional2018",
        "singerCompendioEtica1995",
        "huertaEticaConClasicos2000",
        "prieto2009favor",
        "lopezmartinezTecnicasDidacticas2023",
        "barredaOracionCivica1867",
        "sierraUniversidadNacional1910",
        "constitucionCPEUM2026",
        "casoAyotzinapaCNDH2024",
        "lgv2026",
        "lgmdfp2026"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El desarrollo argumentativo parte del problema para construir postura."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar del razonamiento y evidencia presentados."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es base recurrente para argumentacion en la materia."
        },
        {
          "source": "Moral",
          "target": "Practica juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral incide en criterios de actuacion profesional."
        }
      ],
      "evidence": [
        "README de Etica y Moral juridica: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Archivo etica-y-moral-juridica.bib: base bibliografica local con duplicados observables.",
        "Transferencia lateral desde Filosofia del Derecho con deduplicacion lossless de patrones reutilizables."
      ]
    }
  },
  "reinforcement_log": [
    "Ciclo 13: refuerzo lateral-transversal desde Filosofia del Derecho hacia Etica y Moral juridica.",
    "Se conservaron todas las reglas utiles previas del destino sin eliminacion.",
    "Se transfirieron solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No se copio redaccion literal, conclusiones ni bibliografia exclusiva del nodo hermano.",
    "Se reforzo control de supuestos y validacion JSON estricta previa a propagacion.",
    "Se mantuvo distincion conceptual Etica-Moral como eje argumentativo de la materia."
  ]
}
```