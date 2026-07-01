{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial comun de la asignatura.",
    "Se transfieren solo patrones reutilizables desde Actividad 1: estructura, calidad, trazabilidad y argumentacion.",
    "Se mantiene validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se evita copiar conclusiones, redaccion literal y bibliografia exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear cada entrega con UnADM y Licenciatura en Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Sustentar afirmaciones con citas verificables y explicitas.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar aguas abajo.",
    "Validar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar cualquier respuesta no estructurada heredada.",
    "Validar correspondencia del producto con la consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de compilar.",
    "Resolver plantillas sin expandir tipo $(@{...}.Slug) antes de referenciar rutas.",
    "No introducir comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local.",
    "Marcar como supuesto cualquier asignacion bibliografica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reforzar patrones institucionales comunes y no contenido puntual de un hermano.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar union-dedupe para compresion lossless.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion y criterios de profundidad argumentativa.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro artefacto.",
    "Confirmar nombre canonico final del .bib de asignatura por plantilla Slug no resuelta.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o no a Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de asignatura como entrada canonica",
        "Normalizacion estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1",
        "Bloque 2",
        "Obligatoria",
        "8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos, normas, doctrina o datos",
      "Producto solicitado por planeacion",
      "Analisis propio y postura academica",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables con fundamento juridico y evidencia.",
      "Asegurar trazabilidad academica y utilidad profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo puntual al inicio",
      "Secciones funcionales con logica juridica",
      "Citas explicitas y verificables",
      "Supuestos declarados cuando falte dato local"
    ],
    "argumentative_patterns": [
      "Plantear problema inicial",
      "Desarrollar marco conceptual y normativo",
      "Contrastar fuentes con analisis propio",
      "Emitir postura justificada",
      "Cerrar con conclusion juridica aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Normalizacion estructurada",
        "Validacion JSON",
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
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden y contenido minimo de cada entrega."
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
          "justification": "La conclusion valida requiere respaldo y analisis propio."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y criterio de conclusion juridica.",
        "Programa analitico define cinco ejes reutilizables.",
        "Historial reporta salidas no parseables; se justifica gate JSON estricto.",
        "Plantilla Slug sin resolver en README; requiere verificacion de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion de reglas repetidas con conservacion total de contenido util.",
      "Ciclo 2: refuerzo lateral de estructura y calidad comun entre actividades hermanas.",
      "Ciclo 2: mantenimiento de supuestos abiertos donde falta consigna local verificable.",
      "Ciclo 2: bloqueo explicito de transferencia de bibliografia exclusiva no confirmada."
    ]
  }
}