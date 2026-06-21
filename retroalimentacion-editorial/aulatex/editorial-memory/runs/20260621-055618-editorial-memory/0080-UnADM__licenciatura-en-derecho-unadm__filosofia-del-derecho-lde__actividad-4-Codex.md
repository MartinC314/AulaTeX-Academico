{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con union-dedupe lossless y sin recorte util.",
    "Se preserva identidad UnADM y contexto curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto de JSON parseable por antecedentes de salidas no estructuradas.",
    "Se evita copiar conclusiones o bibliografia exclusiva de Actividad 1; solo se transfieren patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear cada entrega con UnADM, Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar trazabilidad institucional de ubicacion curricular con malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal para evitar texto descriptivo plano."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 4.",
    "Confirmar el tipo de producto requerido antes de cerrar version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar aguas abajo.",
    "Comprobar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia entre citas en texto y entradas .bib.",
    "Normalizar respuestas no estructuradas heredadas antes de propagacion recursiva.",
    "Evitar regresiones: no eliminar reglas utiles previas ya validadas."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves bibliograficas en uso para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver o documentar tokens tipo $(@{...}.Slug) antes de automatizar referencias."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4 [supuesto pendiente]."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir patrones generales, no redaccion literal ni conclusiones de hermanos.",
    "Mantener bandera de normalizacion manual en ciclos con salidas no estructuradas.",
    "Aplicar union-dedupe semantica para compresion lossless.",
    "Si faltan datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro artefacto.",
    "Confirmar rubrica docente especifica de evaluacion argumentativa.",
    "Confirmar nombre canonico final del .bib cuando el README usa plantilla sin resolver.",
    "Confirmar si bibliografia de interpretacion juridica (Semana 7) aplica o no a Actividad 4 [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico activa el analisis.",
      "Conceptos y normas sostienen el marco.",
      "Evidencia verificable respalda afirmaciones.",
      "Analisis propio distingue el trabajo.",
      "Conclusion juridica transfiere a practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico evaluable.",
      "Asegurar coherencia entre identidad institucional y rigor juridico.",
      "Preservar memoria editorial reutilizable sin perdida semantica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y trazables.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre con postura juridica propia."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y marco normativo.",
      "Contrastar evidencia.",
      "Desarrollar postura propia.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales",
        "Integridad academica",
        "Validacion JSON",
        "Normalizacion estructurada",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Tono formal academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes definen secuencia de redaccion."
        },
        {
          "source": "Validacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige evidencia y argumentacion propia."
        }
      ],
      "evidence": [
        "README fija identidad, entrada canonica e integridad academica.",
        "Programa analitico define proposito y cinco ejes reutilizables.",
        "Existen antecedentes de salida no estructurada; se mantiene gate JSON estricto.",
        "Hay token de slug sin resolver en README; requiere verificacion local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 80: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 80: se reforzo transferencia lateral por patrones, no por contenido especifico.",
      "Ciclo 80: se mantuvieron supuestos abiertos donde falta consigna local verificable."
    ]
  }
}