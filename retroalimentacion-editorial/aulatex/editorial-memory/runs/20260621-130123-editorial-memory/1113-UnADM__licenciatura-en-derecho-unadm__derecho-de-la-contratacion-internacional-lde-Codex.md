{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM y ejes editoriales estables sin traslado literal de contenido tematico.",
    "Se mantiene compresion lossless por union y deduplicacion semantica.",
    "Se conserva incidente historico de salidas no JSON parseables como gate activo hasta verificacion local.",
    "Se refuerza contexto local verificado: semestre 6, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho y contexto curricular local verificado.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad del origen transversal: filosofia-del-derecho-lde/actividad-1."
  ],
  "structure_rules": [
    "Aplicar secuencia reusable: problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Separar descripcion de postura argumentativa propia.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; anexar solo mejoras verificables."
  ],
  "activity_rules": [
    "Identificar problema juridico o social que activa la actividad.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Incluir criterio juridico propio y limites del analisis cuando falten datos.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion no verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que nombres y rutas del README coincidan con archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside cuando aplique plantilla local.",
    "Conservar macros institucionales de curso, universidad y metadatos.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders no expandidos tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes a la actividad.",
    "Agregar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "No citar fuentes heredadas del origen si no se consultaron en destino.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales generales.",
    "Mantener incidente JSON historico como alerta hasta cierre verificado.",
    "Aplicar deduplicacion semantica por regla, no por recorte textual.",
    "Corregir rutas o nombres corruptos antes de propagar."
  ],
  "open_questions": [
    "Confirmar si la incidencia JSON no parseable ya quedo resuelta en este ciclo.",
    "Definir formato uniforme local para cita de norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion y visual.",
    "Supuesto: README y programa aun requieren saneamiento de placeholders y saltos corruptos.",
    "Confirmar si existe guia de evaluacion especifica por actividad de la materia."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencia entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico activador.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y trazables.",
      "Asegurar calidad formal, juridica y tecnica en entregables LaTeX.",
      "Sostener continuidad editorial institucional entre nodos."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Estructura fija con secciones funcionales.",
      "Cierre con transferencia profesional.",
      "Sin literalidad heredada entre materias no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema -> norma/doctrina -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna -> producto alineado -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Trazabilidad de herencia",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Bibliografia verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay reutilizacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta local exige respaldo documental y forma institucional."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El argumento juridico se construye desde una cuestion concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento normativo o doctrinal verificable."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo reutilizables.",
        "Bib local: repositorio canonico de referencias.",
        "Registro historico: incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 15: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 15: se evita migrar contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 15: se refuerzan gates tecnicos, estructura reusable e identidad institucional."
    ]
  }
}