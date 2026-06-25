{
  "summary": [
    "Se consolida memoria transversal para Derechos de autor con identidad UnADM.",
    "Se preserva compresion lossless por union y deduplicacion sin recorte.",
    "Se mantiene normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se marca como provisional toda herencia no verificada de Codex y GPT-Pro.",
    "Se corrigen abstracciones reutilizables sin transferir redaccion literal de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar malla-curricular-derecho-unadm.pdf como soporte curricular cuando aplique."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico para tokens sin expandir y nombres corruptos.",
    "Corregir campos pendientes como 'Nombre por definir' antes de version final."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos y paquetes en preambulo valido segun plantilla.",
    "No dejar comandos incompletos como \\usepackage sin argumento.",
    "Compilar sin errores criticos, referencias rotas ni tokens literales.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Normalizar nombres de archivo con slug derechos-de-autor."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo materiales institucionales o verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener derechos-de-autor.bib como contenedor canonico local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo abstracciones editoriales estables.",
    "No propagar datos personales del alumno a otros nodos.",
    "No propagar errores locales de plantilla ni nombres de archivo corruptos.",
    "Mantener etiqueta de herencia provisional para Codex y GPT-Pro hasta verificacion.",
    "Aplicar estrategia progresiva y conservadora: sumar reglas utiles sin regresion."
  ],
  "open_questions": [
    "Supuesto: LDE-S5B1 sigue siendo clave oficial; confirmar.",
    "Confirmar nombre de figura docente para eliminar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer fijo.",
    "Confirmar orden definitivo de paquetes respecto a \\input{template}.",
    "Confirmar limpieza total de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar si existe rubrica local por actividad para ajustar profundidad argumentativa."
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
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicamente solidos.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte dato.",
      "Secciones funcionales y trazables.",
      "Consistencia entre portada, cuerpo y bibliografia."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Desarrollar marco conceptual-normativo.",
      "Sostener postura propia con evidencia.",
      "Cerrar con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada fortalece utilidad profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia editorial de materia",
          "kind": "depends_on",
          "justification": "Define tono, formato y metadatos comunes."
        }
      ],
      "evidence": [
        "README de Derechos de autor con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib con fuentes institucionales base.",
        "Deteccion local de tokens sin expandir y comandos LaTeX incompletos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se preservan reglas utiles previas sin eliminaciones.",
      "Ciclo 19: se deduplican reglas repetidas y se mantienen equivalentes estables.",
      "Ciclo 19: se refuerzan gates de JSON parseable y consistencia bib-citas.",
      "Ciclo 19: se transfiere patron argumentativo estable desde nodo transversal sin contenido literal."
    ]
  }
}