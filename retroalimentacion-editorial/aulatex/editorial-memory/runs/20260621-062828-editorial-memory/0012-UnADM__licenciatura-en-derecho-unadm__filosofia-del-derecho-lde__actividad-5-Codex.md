{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria: no propagar sin JSON parseable y estructura minima completa.",
    "Se consolida identidad UnADM y contexto curricular sin copiar conclusiones ni bibliografia exclusiva del nodo hermano.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica con identidad UnADM.",
    "Vincular toda salida a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir explicitamente afirmacion, evidencia e inferencia juridica.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear el formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar presencia de todas las secciones del esquema requerido.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres antes de compilar.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente usadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion estructural completa.",
    "Transferir solo patrones generales reutilizables entre nodos hermanos.",
    "Evitar copiar redaccion literal, conclusiones concretas o bibliografia exclusiva.",
    "Aplicar union y deduplicacion lossless para evitar regresiones.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar tipo de entregable principal: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si las fuentes de Semana 7 aplican total o parcialmente a Actividad 5."
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
      "Problema juridico como detonador del analisis.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable como soporte.",
      "Postura propia del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre.",
      "Sostener continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y claras.",
      "Supuestos explicitados cuando falten datos.",
      "Cierre aplicado a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, formato y criterio de integridad academica."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere conflicto o pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida exige respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia base",
          "target": "Bibliografia especifica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la especifica responde a la consigna."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico define ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de parseo no valido justifica gate estricto de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion completada sin perdida de reglas utiles previas.",
      "Ciclo 12: se reforzo control de parseo JSON como requisito de propagacion.",
      "Ciclo 12: se mantuvo transferencia lateral por patrones, sin copiar contenido especifico del hermano."
    ]
  }
}