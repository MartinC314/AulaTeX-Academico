{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se agrega control local verificable: README y programa analitico contienen token Slug sin resolver para .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, articular hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombre canonico.",
    "Marcar como supuesto cualquier nombre de archivo ambiguo hasta confirmarlo."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica automaticamente a Actividad 6 sin validacion de consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener union-dedupe lossless en nodos hermanos.",
    "Etiquetar como provisionales reglas de baja confianza heredadas.",
    "Conservar advertencias historicas de salidas no parseables en ramas con herencia Codex/GPT-Pro.",
    "Propagar identidad curricular y puertas de calidad como nucleo comun lateral."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README/programa.",
    "Confirmar si la bibliografia de interpretacion juridica (Semana 7) aplica total o parcialmente a Actividad 6."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar continuidad editorial entre actividades sin perder trazabilidad ni rigor."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y marco normativo.",
      "Contrastar fuentes pertinentes.",
      "Tomar postura propia fundamentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion estructurada"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sostiene la justificacion argumentativa cuando la consigna lo pide."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no se permite reutilizacion segura."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: bloquear propagacion sin JSON parseable.",
        "clean.bib: corpus util para interpretacion juridica, sujeto a consigna local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 15: preservacion de todas las reglas utiles previas sin recorte.",
      "Ciclo 15: refuerzo lateral de control de supuestos y trazabilidad de fuentes.",
      "Ciclo 15: adicion verificable de riesgo local por token Slug sin resolver."
    ]
  }
}