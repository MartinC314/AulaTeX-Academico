{
  "summary": [
    "Se consolida transferencia lateral A1->A5 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se preserva identidad UnADM, contexto curricular y ejes troncales de produccion academica.",
    "Se refuerza control de normalizacion JSON parseable antes de propagacion recursiva.",
    "Se mantiene regla de no copiar conclusiones ni bibliografia exclusiva entre nodos hermanos.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte informacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en toda afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revision manual extra en memoria con incidentes historicos de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre .bib canonico esperado filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Agregar solo mejoras verificables por evidencia local.",
    "No propagar fuentes provisionales como bibliografia academica.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion y criterios de ponderacion.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografia existente o requiere .bib propio.",
    "Confirmar nombre canonico final del archivo .bib en la asignatura.",
    "Confirmar pertinencia de fuentes de Semana 7 para Actividad 5."
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
      "Conceptos y marco normativo o doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables academicos solidos.",
      "Garantizar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y trazables.",
      "Supuestos marcados de forma explicita.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib",
        "Bibliografia base",
        "Bibliografia especifica de actividad"
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
          "justification": "Define tono, integridad academica y forma del entregable."
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
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica depende de la consigna local."
        }
      ],
      "evidence": [
        "README: pauta editorial institucional y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de ciclos: incidentes de parseo justifican gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 14: conservadas reglas utiles previas sin eliminacion.",
      "Ciclo 14: reforzada separacion entre patrones reutilizables y contenido especifico de actividad hermana.",
      "Ciclo 14: mantenidos supuestos explicitos por falta de consigna local completa."
    ]
  }
}