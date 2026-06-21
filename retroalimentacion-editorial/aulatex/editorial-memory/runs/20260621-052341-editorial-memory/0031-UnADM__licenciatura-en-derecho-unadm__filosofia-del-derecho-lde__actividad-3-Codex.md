{
  "summary": [
    "Se consolida memoria lateral reusable de actividad-1 hacia actividad-3 con deduplicacion lossless.",
    "Se preservan reglas nucleares: identidad UnADM, estructura editorial minima, calidad de evidencia y cierre juridico propio.",
    "Se refuerza normalizacion obligatoria: no propagar sin JSON parseable y estructura completa.",
    "Se mantiene politica de supuestos para datos no confirmados de actividad-3.",
    "Se corrige alcance bibliografico: filosofia-del-derecho-clean.bib es contextual a interpretacion juridica (Semana 7) y su uso en actividad-3 queda condicionado."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas del nodo hermano sin copiar redaccion literal ni conclusiones especificas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmacion oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagacion si salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Confirmar respaldo de cada afirmacion o marca explicita de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes academicas y normativas de antecedentes editoriales.",
    "Aplicar no-regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles con citas del .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar al .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con tema y citas reales de actividad-3 [supuesto condicionado]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No propagar conclusiones ni bibliografia exclusiva de un hermano a otro.",
    "Aplicar compresion por union y deduplicacion sin perdida semantica.",
    "Mantener bandera de riesgo cuando existan antecedentes de parseo fallido.",
    "Si faltan datos locales, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar bibliografia obligatoria de la semana correspondiente.",
    "Confirmar si actividad-3 pertenece a interpretacion juridica o a otro bloque tematico.",
    "Confirmar archivo .tex principal y nombre final del artefacto."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundamentados y utiles para practica juridica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas con orden logico.",
      "Afirmacion con evidencia y cita.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo consistente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Estructura editorial minima",
        "Integridad academica",
        "Postura propia",
        "Conclusion juridica transferible",
        "Bibliografia verificable"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor."
        },
        {
          "source": "Estructura editorial minima",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre valido depende de un desarrollo argumentado."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Postura propia",
          "kind": "supports",
          "justification": "La postura se legitima con evidencia rastreable."
        }
      ],
      "evidence": [
        "README: pauta editorial con identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 31: deduplicacion integral aplicada sin eliminar reglas utiles.",
      "Ciclo 31: reforzada separacion entre memoria editorial y evidencia academica.",
      "Ciclo 31: mantenida condicion de uso para bibliografia depurada de Semana 7.",
      "Ciclo 31: consolidadas relaciones argumentativas reutilizables entre nodos hermanos."
    ]
  }
}