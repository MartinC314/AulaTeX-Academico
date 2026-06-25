{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales troncales de la asignatura.",
    "Se refuerza control estructural: no propagar sin JSON parseable y estructura minima completa.",
    "Se mantiene regla de transferencia: solo patrones reutilizables; no copiar conclusiones ni bibliografia exclusiva entre hermanos.",
    "Supuesto: falta consigna y rubrica local de Actividad 5; se conserva base estructural y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad, fundamento, evidencia y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificacion local.",
    "No usar fuentes de memoria tecnica como fuentes academicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia juridica en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas troncales.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte informacion de alcance."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilizar.",
    "Aplicar revision manual extra en memoria con historial de parseo fallido."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres reales de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematica de otra semana hasta validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin perder especificidad local.",
    "Evitar regresiones: conservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union y deduplicacion como compresion lossless en saltos laterales.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas en lugar de contenido concreto."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografia existente o requiere .bib especifico.",
    "Confirmar nombre canonico final del .bib por presencia de tokens sin expandir en README."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad entre consigna, desarrollo argumentativo y cierre profesional."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Uso explicito de supuestos cuando falte informacion.",
      "Cierre con transferencia a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Consigna -> criterios de evaluacion -> cumplimiento verificable."
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
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, forma y estandar academico del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta o conflicto delimitado."
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
          "justification": "La base orienta la asignatura; la especifica responde a la consigna."
        },
        {
          "source": "Ejes troncales",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "La progresion lateral conserva patron comun sin copiar contenido exclusivo."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico fija ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de parseo fallido justifica gates estrictos de estructura.",
        "README y programa muestran tokens Slug sin expandir; requiere validacion de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion integral aplicada en reglas y ADN editorial.",
      "Ciclo 9: se preservan reglas validas previas sin eliminacion de controles utiles.",
      "Ciclo 9: se refuerza separacion entre bibliografia base y bibliografia por actividad.",
      "Ciclo 9: se mantiene transferencia lateral por analogia controlada y sin copia literal entre hermanos."
    ]
  }
}