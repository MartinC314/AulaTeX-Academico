{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con reglas reutilizables de actividad-1.",
    "Se mantiene identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se preservan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene politica de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no confirmado por fuentes locales.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Registrar incidencias de parseo como metadato tecnico, no como evidencia disciplinar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1, sin copiar redaccion literal.",
    "No transferir conclusiones especificas ni bibliografia exclusiva del nodo hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato ni tema especifico de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Usar reporte o presentacion segun consigna confirmada."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni completar datos sin verificacion.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar al .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar lateralmente reglas institucionales y de calidad por defecto.",
    "Propagar reglas especificas de Filosofia del Derecho solo dentro de la misma asignatura.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresion lossless por union y deduplicacion semantica.",
    "Mantener bandera de riesgo en ciclos con antecedentes de parseo fallido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar si actividad-3 corresponde a interpretacion juridica u otro tema.",
    "Confirmar archivo .tex principal canonico para actividad-3.",
    "Confirmar si la bibliografia depurada de Semana 7 aplica en actividad-3 [supuesto]."
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
      "Problema juridico delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Cumplimiento estricto de consigna."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos utiles y verificables.",
      "Asegurar consistencia metodologica entre actividades hermanas.",
      "Preservar memoria editorial estable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion con evidencia verificable.",
      "Supuestos marcados de forma visible.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre verificable."
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
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        },
        {
          "source": "Politica de supuestos",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "Evita inventar fuentes o aplicar bibliografia no confirmada."
        }
      ],
      "evidence": [
        "README define identidad UnADM, integridad academica y cierre juridico propio.",
        "Programa analitico fija ejes: problema, conceptos/fuentes, analisis y conclusion.",
        "Antecedentes de parseo obligan gate de JSON antes de propagar.",
        "Bibliografia clean indica contexto de Semana 7 y uso condicionado [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 50: deduplicacion lossless aplicada sin eliminar reglas utiles.",
      "Ciclo 50: se reforzo no regresion y validacion JSON como compuerta obligatoria.",
      "Ciclo 50: se mantuvo transferencia lateral por patrones, no por contenido especifico.",
      "Ciclo 50: se conservaron preguntas abiertas donde faltan datos locales."
    ]
  }
}