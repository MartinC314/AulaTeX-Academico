{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta antes de propagar.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar contenido especifico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar conclusiones especificas de Actividad 1 a Actividad 4.",
    "Supuesto: confirmar consigna exacta de Actividad 4 antes de fijar alcance tematico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Verificar que el producto final coincida con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Aplicar union-dedupe para compresion lossless en nodos hermanos.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar nombre canonico final del archivo .bib con slug resuelto.",
    "Confirmar si la bibliografia clean de Semana 7 aplica o no a Actividad 4."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico con rigor juridico.",
      "Asegurar coherencia entre consigna, argumentacion y cierre.",
      "Mantener continuidad editorial entre actividades sin copiar contenido literal."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar hechos, conceptos, argumentos y postura personal.",
      "Marcar supuestos de forma explicita.",
      "Sostener cada afirmacion relevante con cita."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar marco conceptual y normativo.",
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
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
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
          "justification": "Los ejes definen el orden argumentativo reutilizable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere evidencia y postura fundada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica y exigencia de conclusion juridica.",
        "Programa analitico: cinco ejes de trabajo.",
        "Antecedentes de salidas no parseables: gate de JSON obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion de reglas repetidas con preservacion total de validez.",
      "Ciclo 11: refuerzo lateral de patrones estructurales y de calidad desde nodo hermano.",
      "Ciclo 11: se evita transferencia de conclusiones o bibliografia exclusiva de Actividad 1.",
      "Ciclo 11: se mantienen supuestos abiertos donde falta consigna local verificable."
    ]
  }
}