{
  "summary": [
    "Memoria de actividad para Filosofia del Derecho con identidad UnADM.",
    "Conservar normalizacion estructurada obligatoria antes de propagar.",
    "Ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Aplicar compresion lossless por union y deduplicacion, no por recorte.",
    "Contexto confirmado: Filosofia del Derecho, Licenciatura en Derecho UnADM, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Refuerzo lateral hermano (actividad-1 -> actividad-3): transferir patrones reutilizables sin copiar redaccion ni conclusiones especificas.",
    "Antecedente: ciclos previos con salida no JSON parseable; requiere normalizacion manual.",
    "La materia exige identidad UnADM, integridad academica, citas verificables y cierre juridico propio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente academica.",
    "Registrar origen provisional de incidencias de parseo sin convertirlo en evidencia academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Conservar consistencia con README y programa analitico de la asignatura.",
    "Integrar claridad, fundamento juridico, evidencia y transferencia profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Heredar reglas validas de hermanos sin eliminar ninguna util ni copiar redaccion literal.",
    "Registrar diferencias especificas de actividad-3 como supuestos hasta confirmar guia oficial.",
    "No asumir consigna, semana ni formato de actividad-3 sin evidencia local.",
    "Verificar que el producto corresponda a la consigna de la actividad antes de cerrar."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Confirmar que cada fuente citada exista en bibliografia local o se agregue con datos verificables.",
    "Distinguir fuentes academicas, normativas, jurisprudenciales y antecedentes editoriales.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No renombrar claves bibliograficas ya usadas en documentos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar archivos .tex de reporte o presentacion segun el producto solicitado.",
    "Corregir rutas o nombres de archivo solo con verificacion local.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo entradas realmente citadas por la actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Mantener URLs verificables cuando existan.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No usar memoria editorial como bibliografia academica.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 (interpretacion juridica); confirmar si aplica a actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Usar compresion union-dedupe lossless para consolidar memoria.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar reglas especificas de Filosofia del Derecho solo a actividades laterales de la misma asignatura.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo por antecedente de salida no estructurada.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes."
  ],
  "open_questions": [
    "Falta confirmar consigna exacta de actividad-3.",
    "Falta confirmar formato de entrega requerido en actividad-3 (reporte, presentacion u otro).",
    "Falta confirmar bibliografia obligatoria especifica de actividad-3.",
    "Falta confirmar si actividad-3 corresponde a interpretacion juridica o a otra semana.",
    "Falta confirmar archivo .tex principal de actividad-3.",
    "Falta confirmar si la bibliografia depurada de Semana 7 aplica a actividad-3.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Identidad UnADM e integridad academica.",
      "Bibliografia verificable."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales que integren problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Conservar consistencia con README y programa analitico de la asignatura."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en cada afirmacion relevante.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable a la practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Consistencia entre objetivo, desarrollo y cierre.",
      "Si no hay consigna local, usar estructura base y marcar supuestos.",
      "Heredar reglas validas de hermano sin copiar redaccion literal ni conclusiones especificas."
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
        "Conceptos juridicos fundamentales",
        "Interpretacion juridica (supuesto Semana 7)"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable entre nodos."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte del problema delimitado y evita descripcion vacia."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las fuentes consultables sostienen la pauta de integridad."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica con criterio propio.",
        "Programa analitico: ejes de trabajo y proposito de transformacion del producto.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "bib local: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: refuerzo lateral hermano actividad-1 -> actividad-3 con estrategia progresiva por analogia controlada.",
      "Transferidos patrones reutilizables: identidad institucional, estructura, calidad, conceptos y relaciones recurrentes.",
      "No se copio redaccion literal, conclusiones especificas ni bibliografia exclusiva del hermano.",
      "Deduplicacion lossless aplicada; sin regresion de reglas utiles previas.",
      "Conservada bandera de normalizacion manual por antecedente de salida no JSON parseable."
    ]
  }
}