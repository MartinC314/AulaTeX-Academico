{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 5 sin copiar contenido especifico.",
    "Se preserva identidad UnADM y marco curricular de Derecho, semestre 1, bloque 2.",
    "Se mantiene regla de normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se aplico deduplicacion lossless de reglas repetidas y se conservaron reglas utiles vigentes."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda salida con identidad institucional UnADM.",
    "Vincular la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Mantener contexto curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir explicitamente afirmacion, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion a la consigna real de Actividad 5.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1.",
    "No arrastrar bibliografia exclusiva de otra actividad sin validar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responde a la consigna de Actividad 5.",
    "Aplicar revision manual extra si hay antecedentes de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentos y codificacion espanola de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de automatizar rutas.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente usadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Aplicar union y deduplicacion lossless en cada ciclo.",
    "Si falta consigna local, propagar estructura base y abrir preguntas.",
    "No propagar fuentes provisionales como evidencia academica final."
  ],
  "open_questions": [
    "Confirmar enunciado textual de Actividad 5.",
    "Confirmar rubrica especifica de evaluacion de Actividad 5.",
    "Confirmar formato exigido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si bibliografia de Semana 7 aplica total o parcialmente a Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de asignatura como entrada canonica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos",
        "Asignatura: Filosofia del Derecho"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Conceptos y marco normativo pertinentes",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Asegurar coherencia entre consigna, argumentacion y cierre juridico.",
      "Sostener continuidad editorial entre actividades sin copiar resultados especificos."
    ],
    "style_markers": [
      "Encuadre inicial breve",
      "Secciones funcionales",
      "Postura propia sustentada",
      "Uso explicito de supuestos",
      "Cierre con aplicacion profesional"
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Contraste doctrinal breve -> toma de postura"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-.bib"
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
          "justification": "Define tono, forma y criterios de integridad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se deriva de una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna."
        }
      ],
      "evidence": [
        "README establece identidad UnADM e integridad academica.",
        "Programa analitico fija ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial registra incidentes de salida no parseable y exige gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion lossless aplicada a reglas repetidas.",
      "Ciclo 3: se reforzo transferencia por analogia controlada entre nodos hermanos.",
      "Ciclo 3: se preservaron reglas utiles heredadas y se evitaron copias literales de contenido especifico.",
      "Ciclo 3: se mantuvo bandera de riesgo por parseo y normalizacion obligatoria."
    ]
  }
}