{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, contexto curricular y pauta editorial de la asignatura.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto: no propagar si no hay JSON parseable y estructura minima completa.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; se conserva plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir explicitamente problema, conceptos, evidencia y analisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar profundidad argumentativa a la rubrica cuando exista.",
    "Supuesto: confirmar producto exacto de Actividad 4 antes de cerrar version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias indefinidas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y deduplicadas.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Conservar reglas utiles previas y agregar solo mejoras comprobables.",
    "Aplicar analogia controlada: transferir patron, no contenido tematico cerrado.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados.",
    "Evitar regresiones de calidad al unificar memoria lateral."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar producto requerido: reporte, presentacion u otro.",
    "Confirmar extension y criterios de evaluacion de la rubrica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del .bib ante token Slug no resuelto en README."
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
        "Normalizacion obligatoria antes de propagar.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Asegurar trazabilidad entre problema, evidencia y conclusion.",
      "Sostener criterio juridico propio con respaldo documental."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explicita para cada afirmacion relevante.",
      "Supuestos marcados cuando falten datos locales.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Fijar postura argumentada.",
      "Concluir con implicacion juridica aplicable."
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
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
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
          "justification": "Los ejes ordenan problema, conceptos, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo y criterio argumentativo."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica, integridad academica y conclusion juridica propia.",
        "Programa analitico: ejes de trabajo reutilizables para cualquier actividad.",
        "Antecedentes: salidas no parseables obligan gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 86: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 86: se preservan reglas utiles previas y se eliminan redundancias no semanticas.",
      "Ciclo 86: se refuerza transferencia lateral por patron reusable, sin copiar contenido especifico de Actividad 1.",
      "Ciclo 86: se mantiene control de supuestos por ausencia de consigna local visible."
    ]
  }
}