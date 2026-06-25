{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 con deduplicacion lossless.",
    "Se preservan reglas utiles previas sin recorte ni regresion.",
    "Se mantiene identidad UnADM y marco curricular verificado en README y programa analitico.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se mantiene bloqueo de propagacion si no hay JSON parseable.",
    "Se conserva politica de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica.",
    "Registrar incidencias de parseo como metadato tecnico, no como evidencia disciplinar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar patrones reutilizables desde actividad-1 sin copiar redaccion literal.",
    "No transferir conclusiones especificas ni bibliografia exclusiva del hermano.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Registrar en .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica y aplica solo si coincide con la consigna de actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validacion JSON y estructura.",
    "Propagar a nodos hermanos solo reglas generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar bandera de riesgo cuando haya historial de salida no estructurada.",
    "Mantener especificidad local sin perder reglas institucionales comunes."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 usa bibliografia propia o reutiliza bibliografia existente.",
    "Confirmar nombre canonico final del .bib en la asignatura."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar transferibilidad profesional del cierre argumentativo.",
      "Conservar coherencia institucional y calidad tecnica en todo nodo de actividad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados de forma visible.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
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
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Politica de supuestos",
          "kind": "depends_on",
          "justification": "La trazabilidad de supuestos requiere estructura parseable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de delimitar el problema y evita descripcion vacia."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico: ejes de trabajo y proposito de transformacion del producto.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza transferencia lateral por patrones, sin copiar contenido especifico del hermano.",
      "Ciclo 15: se mantiene compresion lossless por union y deduplicacion.",
      "Ciclo 15: se consolidan reglas de calidad, LaTeX y bibliografia con supuestos marcados.",
      "Ciclo 15: se preserva ADN editorial institucional y curricular sin regresiones."
    ]
  }
}