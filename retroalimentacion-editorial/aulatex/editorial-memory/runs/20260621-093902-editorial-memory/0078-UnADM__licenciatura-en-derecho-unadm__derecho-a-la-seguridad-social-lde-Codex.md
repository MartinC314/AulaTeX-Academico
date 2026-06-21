{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia de Derecho a la Seguridad Social.",
    "Se preservan reglas estables de identidad UnADM, estructura por ejes, control de calidad y normalizacion JSON.",
    "Se mantiene estrategia conservadora: unir y deduplicar sin recorte ni regresion.",
    "Se evita transferir contenido tematico especifico de Filosofia; solo se transfieren abstracciones editoriales reutilizables.",
    "Se refuerza cerebro editorial minimo del destino con foco en trazabilidad, verificabilidad y compilacion LaTeX estable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin regresion.",
    "Conservar trazabilidad de origen cuando una regla sea provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo por ejes, conclusion y referencias.",
    "Registrar en memoria solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Confirmar compresion lossless por union-dedupe, nunca por recorte."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia y personalizar solo campos variables.",
    "Conservar codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y sin claves faltantes.",
    "Mantener metadatos institucionales y curriculares consistentes en todos los .tex.",
    "Normalizar nombres de archivos y rutas con caracteres corruptos o tokens sin expandir antes de compilar.",
    "Mantener clase y opciones de documento por defecto salvo instruccion explicita."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normatividad juridica vigente verificable.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que cada cita usada en LaTeX tenga entrada BibTeX correspondiente.",
    "Marcar faltantes bibliograficos como pendientes o [supuesto] cuando aplique."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas generales estables, no redaccion literal ni contenido tematico local.",
    "Propagar recursivamente solo despues de validar JSON y estructura minima.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos previos.",
    "Aplicar sincronizacion progresiva y conservadora: reforzar sin desplazar reglas locales vigentes.",
    "Reutilizar gates institucionales de calidad en nodos laterales compatibles.",
    "Si falta contexto local, conservar cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida en la materia destino (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o solo etiqueta operativa [supuesto].",
    "Confirmar si todas las plantillas de actividad inicial existen y son canonicas en el destino.",
    "Verificar vigencia de reglas heredadas desde fuentes no juridicas aun marcadas como provisionales [supuesto].",
    "Confirmar rubricas de evaluacion por actividad para ajustar profundidad argumentativa."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco normativo y doctrinal verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Preservar continuidad editorial entre actividades, materia y suite LaTeX.",
      "Garantizar calidad tecnica, academica y de propagacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless exige estructura formal valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El marco institucional orienta el enfoque profesional de cierre."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "El .bib local contiene base institucional y normativa vigente.",
        "Memoria origen confirma regla transversal de normalizacion JSON previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 78: se reforzo identidad UnADM y trazabilidad de supuestos.",
      "Ciclo 78: se integraron patrones argumentativos estables sin mezclar contenido tematico de Filosofia.",
      "Ciclo 78: se consolidaron gates de calidad para JSON, citas y estructura minima.",
      "Ciclo 78: se mantuvo compresion lossless por union-dedupe y sin regresion."
    ]
  }
}