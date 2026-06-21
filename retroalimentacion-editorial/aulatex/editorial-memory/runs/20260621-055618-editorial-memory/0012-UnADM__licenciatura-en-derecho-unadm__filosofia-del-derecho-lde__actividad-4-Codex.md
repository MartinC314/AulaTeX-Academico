{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless por union.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren patrones reutilizables sin copiar redaccion ni conclusiones de Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 4; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica UnADM.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Sostener integridad academica con citas verificables.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos con fuente institucional."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear forma de entrega al producto pedido en la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, evidencia y analisis propio de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Sustentar cada afirmacion relevante con fuente verificable.",
    "No asumir que bibliografia de Semana 7 aplica automaticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion espanola consistentes en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "No renombrar claves BibTeX activas sin migracion completa.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivo cuando README tenga tokens sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de fijar rutas definitivas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales estables sin perder especificidad local.",
    "Aplicar union-dedupe para evitar regresiones y duplicados.",
    "No transferir conclusiones ni bibliografia exclusiva entre actividades hermanas.",
    "Cuando falte dato local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion especifica y criterios de profundidad argumentativa.",
    "Confirmar si el entregable es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si Actividad 4 requiere bibliografia propia o reutiliza parte de la base existente."
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
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar transferencia profesional mediante cierre argumentativo propio."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con logica juridica.",
      "Sostener afirmaciones con cita explicita.",
      "Marcar supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen secuencia de redaccion y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida exige respaldo documental."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, conclusion juridica propia.",
        "Programa analitico: cinco ejes de trabajo reutilizables.",
        "Historial: salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion ortografica y semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 12: se reforzo gate de JSON parseable por riesgo historico.",
      "Ciclo 12: se preservaron patrones transversales y se excluyo contenido exclusivo de hermano.",
      "Ciclo 12: se mantuvieron supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}