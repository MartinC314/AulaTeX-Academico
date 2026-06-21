{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales transferibles desde Actividad 1.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local verificable.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Citar malla-curricular-derecho-unadm.pdf para sustento curricular.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado en la planeacion semanal.",
    "Diferenciar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otras semanas aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo con caracteres danados antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y puede no aplicar a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y argumentacion.",
    "Evitar copiar redaccion literal o conclusiones especificas entre hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas.",
    "Aplicar union-dedupe sin regresion semantica."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios de evaluacion.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar si existe rubrica docente adicional fuera de README y programa analitico.",
    "Confirmar nombre canonico final del .bib cuando se resuelva el token Slug.",
    "Confirmar fuentes obligatorias especificas de la semana de Actividad 4."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y tecnica para propagacion segura entre nodos."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con logica juridica.",
      "Sostener afirmaciones con cita explicita.",
      "Marcar supuestos ante vacios de informacion local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo y criterio argumentado."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica, citas verificables y conclusion juridica.",
        "Programa analitico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de ciclos: necesidad de gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: deduplicacion integral de reglas repetidas con preservacion semantica.",
      "Ciclo 73: refuerzo lateral de estructura y calidad sin copiar contenido especifico del hermano.",
      "Ciclo 73: mantenimiento de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}