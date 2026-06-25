{
  "summary": [
    "Se refuerza memoria lateral entre asignaturas sin copiar contenido especifico de actividades.",
    "Se conserva identidad UnADM, ejes editoriales y compuertas de calidad parseable.",
    "Se mantiene compresion lossless por deduplicacion y trazabilidad de supuestos.",
    "Se agrega mejora verificable: normalizar token Slug sin expandir en README y programa analitico.",
    "Se agrega mejora verificable: depurar duplicados bibliograficos por clave canonica con alias trazables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sostener integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar que el tipo de producto coincida con la consigna de Actividad 6.",
    "Traducir analisis a implicacion juridica aplicada cuando proceda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar que la fusion no elimine reglas utiles previas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Registrar supuestos de forma explicita cuando falte evidencia local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte y presentacion de la asignatura.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas con caracteres anomales antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar datos sin respaldo.",
    "Conservar metadatos minimos: autor/editor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Deduplicar obras equivalentes con clave canonica y alias trazables.",
    "Marcar entradas truncadas como no operativas hasta su curacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y parseables.",
    "En saltos laterales, transferir patrones institucionales y argumentativos, no conclusiones locales.",
    "Mantener deduplicacion lossless por union de reglas sin recorte.",
    "Aplicar normalizacion manual cuando existan historicos de salida no estructurada.",
    "Usar analogia controlada: mismo esqueleto editorial, contenido disciplinar propio del nodo destino."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato exigido: reporte, presentacion u otro.",
    "Confirmar rubrica para ajustar profundidad argumentativa.",
    "[Supuesto] Confirmar cierre completo de la entrada sierraUniversidadNacional1910 en .bib.",
    "Definir clave canonica oficial para cada par bibliografico duplicado."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible.",
      "Calidad estructural y trazabilidad bibliografica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento, evidencia y aplicacion juridica.",
      "Garantizar consistencia institucional entre actividades y asignaturas afines.",
      "Permitir propagacion segura de memoria editorial reusable."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con criterio juridico propio.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion transferible.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo -> desarrollo -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Deduplicacion bibliografica canonica"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial local exige citas verificables y consistencia institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El programa analitico fija el problema como disparador argumentativo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida debe derivar del razonamiento y evidencia."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce errores de cita y preserva trazabilidad."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Etica y Moral juridica",
          "kind": "develops",
          "justification": "Transferencia lateral controlada de patrones editoriales comunes."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, integridad academica, conclusion juridica con criterio propio.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "README/programa: token Slug sin expandir detectable y normalizable.",
        ".bib local: duplicados verificables y una entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolidan reglas comunes reutilizables entre nodos laterales.",
      "Ciclo 19: se mantiene bloqueo de propagacion ante JSON no parseable.",
      "Ciclo 19: se refuerza deduplicacion bibliografica canonica sin perder trazabilidad.",
      "Ciclo 19: se preserva regla de marcar [Supuesto] ante faltantes de consigna."
    ]
  }
}