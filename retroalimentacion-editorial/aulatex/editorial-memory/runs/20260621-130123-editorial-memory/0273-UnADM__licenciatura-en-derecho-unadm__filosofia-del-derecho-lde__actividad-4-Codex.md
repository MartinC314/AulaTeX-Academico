{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con union-dedupe lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta antes de propagar.",
    "Se transfieren solo patrones reutilizables desde Actividad 1, sin copiar contenido especifico.",
    "Supuesto: falta consigna textual local de Actividad 4; mantener plantilla base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en cada entrega.",
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica a Actividad 4 sin verificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres reales de archivos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es de Semana 7; validar pertinencia antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 4; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para Actividad 4.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del archivo .bib derivado del Slug.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere .bib incremental propio."
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
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar fundamento juridico, evidencia y transferencia profesional.",
      "Mantener coherencia institucional y trazabilidad editorial."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y ordenadas.",
      "Citas explicitas y verificables.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Concluir con implicacion juridica practica."
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
        "README.md",
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
          "justification": "Los ejes definen secuencia de redaccion y cierre."
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
          "justification": "La conclusion debe derivar de evidencia y analisis."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y entrada canonica.",
        "Programa analitico fija cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 3: refuerzo lateral de patrones reutilizables sin copiar conclusiones de Actividad 1.",
      "Ciclo 3: se mantiene regla de supuestos para datos no visibles.",
      "Ciclo 3: se preserva alerta de token Slug sin resolver en rutas y .bib.",
      "Ciclo 3: se mantiene compatibilidad editorial para reporte y presentacion."
    ]
  }
}