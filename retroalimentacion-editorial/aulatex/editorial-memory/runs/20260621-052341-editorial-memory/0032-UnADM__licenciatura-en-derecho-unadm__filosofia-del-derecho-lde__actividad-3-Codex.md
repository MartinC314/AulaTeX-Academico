{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales comunes de la asignatura.",
    "Se mantiene regla critica: no propagar sin JSON parseable y sin normalizacion previa.",
    "Se transfiere solo patron reusable, sin copiar conclusiones ni bibliografia exclusiva del hermano.",
    "Se mantiene politica de supuestos para todo dato no confirmado en consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin eliminar reglas utiles previas.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva del hermano.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema especifico de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Distinguir fuentes academicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomales en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a actividad-3 sin confirmacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar lateralmente reglas generales de identidad, estructura y calidad.",
    "No propagar como hecho ningun supuesto no verificado localmente.",
    "Reutilizar union-dedupe lossless para consolidar sin perdida.",
    "Mantener bandera de riesgo cuando existan incidencias de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografia existente o requiere .bib propio."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable.",
      "Sostener claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Preservar consistencia editorial entre actividades hermanas sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion con evidencia y cita.",
      "Supuestos marcados de forma visible.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Politica de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor, cita verificable y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se construye desde un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La trazabilidad de fuentes sostiene la validez del producto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico: proposito y ejes de trabajo estables de la asignatura.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 32: se reforzo ADN comun entre hermanos con transferencia controlada.",
      "Ciclo 32: se deduplicaron reglas repetidas sin recorte semantico.",
      "Ciclo 32: se mantuvo no regresion y politica de supuestos.",
      "Ciclo 32: se evitaron traslados de contenido especifico de actividad-1."
    ]
  }
}