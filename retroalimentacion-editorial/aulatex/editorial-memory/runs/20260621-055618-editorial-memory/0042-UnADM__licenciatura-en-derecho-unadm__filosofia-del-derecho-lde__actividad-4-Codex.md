{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 4 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable de Filosofia del Derecho.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se refuerzan ejes editoriales recurrentes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferencia de conclusiones o redaccion especifica entre nodos hermano.",
    "Supuesto: falta consigna textual completa de actividad 4; se conserva estructura base reusable."
  ],
  "identity_rules": [
    "Mantener tono formal academico con precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Vincular ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte curricular.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Diferenciar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos, fuentes verificables, analisis propio y conclusion.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con cita explicita verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir bibliografia de otra semana sin confirmar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre consigna local y producto entregable.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) en nombres de archivo.",
    "Verificar nombres reales en README antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar aplicacion en actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales reutilizables.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para evitar regresiones y duplicados.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de actividad 4.",
    "Confirmar producto exacto solicitado: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica de actividad 4.",
    "Confirmar fuentes obligatorias de la semana de actividad 4.",
    "Confirmar nombre canonico final del .bib si persiste token sin resolver."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico activa el desarrollo.",
      "Conceptos y normas ordenan el marco.",
      "Evidencia verificable sostiene afirmaciones.",
      "Analisis propio evita descripcion plana.",
      "Conclusion juridica transfiere a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Asegurar coherencia entre identidad institucional y ejecucion tecnica.",
      "Mantener continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Postura personal sustentada.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y marco normativo.",
      "Contrastar evidencia.",
      "Desarrollar postura propia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y coherencia institucional."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay transferencia segura entre nodos."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El flujo problema-conceptos-evidencia-analisis conduce al cierre juridico."
        }
      ],
      "evidence": [
        "README fija identidad, integridad academica y conclusion juridica propia.",
        "Programa analitico fija cinco ejes reutilizables.",
        "Antecedentes de salida no parseable justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 42: deduplicacion de reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 42: refuerzo lateral sin copiar contenido especifico de actividad 1.",
      "Ciclo 42: conservacion de supuestos abiertos por falta de consigna local completa."
    ]
  }
}