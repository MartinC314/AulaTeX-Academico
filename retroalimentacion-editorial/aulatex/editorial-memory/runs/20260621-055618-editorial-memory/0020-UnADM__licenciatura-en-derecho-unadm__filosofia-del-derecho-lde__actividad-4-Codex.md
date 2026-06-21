{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de Filosofia del Derecho.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se transfiere solo patron reusable; no se copian conclusiones ni bibliografia exclusiva de Actividad 1.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineada a UnADM.",
    "Vincular siempre la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Respetar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el producto final con la planeacion semanal y consigna real.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Explicitar problema, evidencia y postura propia en cada entrega.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar formato (reporte, presentacion u otro) a la consigna de Actividad 4.",
    "No asumir que bibliografia de otra semana aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Verificar correspondencia del producto con la consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Conservar claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Verificar nombres reales de archivos en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar al .bib de asignatura solo fuentes realmente usadas en Actividad 4.",
    "Supuesto: filosofia-del-derecho-clean.bib puede no corresponder a Actividad 4; validar antes de usar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras pasar gates de JSON y estructura.",
    "Aplicar union-dedupe para compresion lossless y evitar regresiones.",
    "Transferir patrones institucionales y de calidad, no contenido tematico especifico hermano.",
    "Mantener trazabilidad de reglas provisionales hasta validacion local.",
    "Si falta consigna, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4 y producto exacto solicitado.",
    "Confirmar rubrica de evaluacion y extension requerida.",
    "Confirmar si el artefacto sigue siendo reporte o cambia de formato.",
    "Confirmar nombre canonico final del .bib (token Slug sin resolver en README).",
    "Confirmar si se usa bibliografia incremental propia para Actividad 4."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y evidencia.",
      "Sostener memoria editorial reutilizable entre actividades hermanas sin contaminar contenido."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con orden juridico.",
      "Postura propia sustentada.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar conceptos y normas relevantes.",
      "Contrastar fuentes con razonamiento propio.",
      "Responder la pregunta guia de forma directa.",
      "Concluir con implicacion juridica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Consigna local como restriccion principal"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de Filosofia del Derecho",
          "kind": "supports",
          "justification": "La identidad define tono, estructura y finalidad formativa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Integridad academica y verificabilidad",
          "kind": "develops",
          "justification": "Los ejes exigen evidencia, analisis y conclusion sustentada."
        },
        {
          "source": "Consigna local como restriccion principal",
          "target": "Ejes editoriales de Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "La plantilla general se ajusta segun requerimientos especificos de actividad."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico define proposito y cinco ejes de trabajo.",
        "Antecedentes de salidas no parseables justifican gate JSON obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: dedupe de reglas repetidas y normalizacion ortografica sin perder contenido util.",
      "Ciclo 20: refuerzo lateral de patrones comunes entre actividades hermanas.",
      "Ciclo 20: se preservan reglas provisionales y se marcan supuestos pendientes de validacion.",
      "Ciclo 20: se evita transferencia de contenido especifico y bibliografia exclusiva de Actividad 1."
    ]
  }
}