{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial institucional verificadas en README y programa analitico.",
    "Se mantienen ejes troncales reutilizables: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se conserva regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantiene separacion entre reglas verificadas y supuestos marcados para datos locales no visibles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear el producto final a la planeacion semanal (reporte, presentacion u otro formato solicitado).",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base de la asignatura.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema delimitado.",
    "Supuesto: si Actividad 6 trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Separar afirmaciones respaldadas de supuestos marcados.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del desarrollo argumentativo.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug visible; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas confiables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a una actividad de interpretacion juridica y no debe asumirse automatico para Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones ni redaccion literal entre hermanos.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Mantener advertencias historicas de salidas no parseables en nodos con herencia dudosa.",
    "No propagar supuestos como hechos confirmados.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna exacta y rubrica de Actividad 6.",
    "Confirmar formato de entrega principal de Actividad 6 (reporte, presentacion u otro).",
    "Confirmar si Actividad 6 exige bloque tematico de interpretacion juridica.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si se reutiliza bibliografia existente o se requiere .bib especifico para Actividad 6.",
    "Supuesto: fuentes heredadas GPT-Pro o Codex siguen en estado provisional hasta validacion local."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en productos academicos claros, sustentados y profesionalmente utiles.",
      "Preservar continuidad editorial entre actividades sin perder trazabilidad ni rigor.",
      "Garantizar memoria reutilizable por patrones y no por copia literal."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Bloques seccionales explicitos.",
      "Citas verificables con postura propia diferenciada.",
      "Cierre con utilidad juridica practica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia argumentada.",
      "Concluir desde el analisis con transferibilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada previa a propagacion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato coherente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada previa a propagacion",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita arrastrar errores de formato y contenido no verificable."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: no propagar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 28: deduplicacion completa de reglas repetidas entre origen y destino.",
      "Ciclo 28: se preservan reglas troncales de calidad, estructura e identidad sin recorte.",
      "Ciclo 28: se evita transferencia de conclusiones especificas del hermano origen.",
      "Ciclo 28: se refuerza manejo de supuestos por falta de consigna local completa."
    ]
  }
}