{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM y marco curricular verificable: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta por antecedentes no parseables.",
    "Se transfieren solo patrones reutilizables desde Actividad 1: identidad, estructura, calidad, conceptos y relaciones.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; no se fijan conclusiones ni fuentes exclusivas."
  ],
  "identity_rules": [
    "Mantener tono formal academico UnADM.",
    "Alinear contenido con Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Anclar ubicacion curricular a README y malla curricular institucional.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear producto final con lo pedido en planeacion semanal.",
    "Distinguir hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con cita explicita verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir redaccion literal ni conclusiones especificas desde Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion sensible.",
    "Validar consistencia entre citas en texto y .bib.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Verificar correspondencia del producto con consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en .bib activo.",
    "No renombrar claves BibTeX usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes de actividad en .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad; validar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar union-dedupe para evitar perdida de reglas utiles.",
    "Preservar reglas institucionales y ajustar solo elementos locales.",
    "No propagar contenido especifico de un hermano a otro.",
    "Mantener bandera de normalizacion manual para ciclos con historial no estructurado.",
    "Escalar solo mejoras verificables por evidencia local."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y rubrica.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib con token Slug resuelto.",
    "Confirmar si se reutiliza bibliografia existente o se crea bloque incremental.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4."
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico util y verificable.",
      "Sostener trazabilidad editorial entre identidad, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Cita explicita para afirmaciones sustantivas.",
      "Marcado de supuestos cuando falta dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Fijar postura justificada.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Ejes del programa analitico",
        "Integridad academica verificable",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere formato parseable."
        },
        {
          "source": "Ejes del programa analitico",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La estructura por ejes conduce al cierre aplicado."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y criterio propio.",
        "Programa analitico define cinco ejes reutilizables.",
        "Historial reporta salidas no parseables; se mantiene gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 3: refuerzo lateral sin copiar redaccion ni bibliografia exclusiva de Actividad 1.",
      "Ciclo 3: mantenimiento de reglas de calidad y propagacion recursiva segura."
    ]
  }
}