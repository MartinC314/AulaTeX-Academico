{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM y contexto curricular verificable: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales recurrentes: problema, conceptos/fuentes, analisis propio, cierre juridico transferible.",
    "Se mantiene gate critico de normalizacion: bloquear propagacion sin JSON parseable y estructura minima completa.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; no se fijan conclusiones ni fuentes exclusivas."
  ],
  "identity_rules": [
    "Mantener tono formal academico UnADM.",
    "Alinear contenido con Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener integridad academica con citas verificables.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Anclar ubicacion curricular en malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar copiar redaccion o conclusiones especificas de Actividad 1.",
    "Transferir solo patrones reutilizables entre hermanos."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Exigir esquema completo antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad entre citas en texto y .bib.",
    "Detectar y normalizar respuestas no estructuradas heredadas.",
    "Bloquear afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar espanol con acentos y codificacion consistente en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Verificar nombres reales de archivos cuando README tenga caracteres danados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar en .bib de asignatura solo fuentes realmente usadas.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra actividad; validar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Aplicar refuerzo lateral por analogia controlada, no por copia literal.",
    "Preservar banderas de normalizacion manual en ciclos con salidas no estructuradas.",
    "Si falta dato local, propagar plantilla base y abrir pregunta."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica de evaluacion.",
    "Confirmar nombre canonico final del .bib cuando el slug no esta resuelto en README.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro artefacto.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica y trazabilidad de fuentes",
        "Entrada canonica en carpeta de asignatura"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos, normas, doctrina o datos",
      "Producto solicitado por planeacion",
      "Analisis propio y postura academica",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos validos",
      "Sostener calidad juridica con evidencia verificable",
      "Asegurar transferencia profesional del aprendizaje"
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales con logica juridica",
      "Cita explicita en afirmaciones clave",
      "Supuestos marcados cuando falte evidencia"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Delimitar marco conceptual y normativo",
      "Contrastar fuentes con analisis propio",
      "Emitir postura justificada",
      "Concluir con aplicacion juridica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica verificable",
        "Ejes editoriales de Filosofia del Derecho"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Validacion JSON estricta",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion confiable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan desarrollo y cierre."
        },
        {
          "source": "Integridad academica verificable",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia y analisis."
        }
      ],
      "evidence": [
        "README fija identidad, integridad y conclusion juridica.",
        "Programa analitico define cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: deduplicacion semantica de reglas repetidas.",
      "Ciclo 38: se mantiene separacion entre patrones transferibles y contenido especifico.",
      "Ciclo 38: se refuerza control de supuestos por falta de consigna local visible."
    ]
  }
}