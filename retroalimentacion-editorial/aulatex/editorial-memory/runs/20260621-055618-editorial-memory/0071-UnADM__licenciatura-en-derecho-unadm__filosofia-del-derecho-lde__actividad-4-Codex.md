{
  "summary": [
    "Se refuerza memoria lateral de Actividad 4 con union-dedupe lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagar.",
    "Se consolidan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva alerta por salidas no parseables en ciclos previos.",
    "Supuesto: la consigna textual de Actividad 4 no esta visible."
  ],
  "identity_rules": [
    "Mantener tono formal academico de UnADM.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Sostener integridad academica con citas verificables.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Citar malla-curricular-derecho-unadm.pdf para contexto curricular.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema juridico o social explicito.",
    "Integrar conceptos, normas, doctrina o datos pertinentes.",
    "Sustentar afirmaciones con evidencia y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: confirmar producto exacto solicitado en Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos del README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar fuentes especificas de la actividad al .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar URL verificable para fuentes digitales.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna y claves citadas.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 y puede no aplicar a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar union-dedupe lossless en nodos hermanos.",
    "Mantener bandera de normalizacion manual para ciclos con salida no estructurada.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar tipo de producto: reporte, presentacion u otro.",
    "Confirmar rubrica y criterios de evaluacion especificos.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib con token slug resuelto.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o no a Actividad 4."
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
        "Integridad academica y trazabilidad de fuentes.",
        "Normalizacion obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos solidos.",
      "Unir fundamento juridico, evidencia y postura propia con utilidad profesional."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales claras.",
      "Cita explicita en afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Exponer conceptos y normas.",
      "Contrastar fuentes.",
      "Desarrollar postura propia.",
      "Cerrar con conclusion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial institucional lo exige."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Definen el orden logico de redaccion."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia verificable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico fija cinco ejes reutilizables.",
        "Historial reporta salidas no parseables y exige gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: deduplicacion de reglas repetidas con preservacion total de validez.",
      "Ciclo 71: refuerzo lateral de estructura y calidad sin copiar contenido especifico entre hermanos.",
      "Ciclo 71: mantenimiento de supuestos abiertos por falta de consigna local visible."
    ]
  }
}