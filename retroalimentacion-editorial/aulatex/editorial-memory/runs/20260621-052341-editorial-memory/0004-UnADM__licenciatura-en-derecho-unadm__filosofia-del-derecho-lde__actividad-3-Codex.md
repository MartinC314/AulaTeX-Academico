{
  "summary": [
    "Se consolida transferencia lateral reusable de Actividad 1 a Actividad 3 sin copiar contenido especifico.",
    "Se preserva ADN UnADM: identidad institucional, integridad academica, citas verificables y cierre juridico propio.",
    "Se mantiene compresion lossless por union y deduplicacion de reglas validas.",
    "Se refuerza bloqueo de propagacion sin JSON parseable ni normalizacion previa.",
    "Se conserva politica de supuestos cuando falte consigna local de Actividad 3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad hermana.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva de otra actividad.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y .bib.",
    "Distinguir fuentes academicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en Actividad 3.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a Semana 7; confirmar aplicabilidad a Actividad 3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir reglas institucionales y de calidad a nodos hermanos compatibles.",
    "Propagar reglas especificas de Filosofia del Derecho solo dentro de la misma asignatura.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Registrar incidencias de parseo como riesgo tecnico persistente."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar archivo .tex principal de Actividad 3.",
    "Confirmar si bibliografia depurada de Semana 7 aplica a Actividad 3."
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
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Asegurar consistencia entre objetivo, evidencia y cierre juridico.",
      "Preservar continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados de forma visible.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo inicial -> desarrollo coherente -> cierre consistente.",
      "Regla general heredada -> ajuste local por consigna -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
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
        "filosofia-del-derecho-clean.bib [supuesto de uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Politica de supuestos",
          "kind": "depends_on",
          "justification": "La propagacion confiable requiere estructura valida y marcas explicitas."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema delimitado y evita descripcion vacia."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico define ejes: problema, conceptos, producto, analisis y cierre.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Contexto local muestra token Slug sin expandir en archivos de referencia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion lossless aplicada sin recorte semantico.",
      "Ciclo 4: reforzada no regresion de reglas utiles previas.",
      "Ciclo 4: mantenida separacion entre memoria editorial y evidencia academica.",
      "Ciclo 4: consolidada transferencia lateral por analogia controlada."
    ]
  }
}